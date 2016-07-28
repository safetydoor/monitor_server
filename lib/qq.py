#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Python client SDK for QQ API using OAuth 2.0
'''

try:
	import json
except ImportError:
	import simplejson as json
import time
import urllib
import urllib2
import urlparse
import logging

def _obj_hook(pairs):
	'''
	convert json object to python object.
	'''
	o = JsonObject()
	for k, v in pairs.iteritems():
		o[str(k)] = v
	return o

def parse_uriqs(content):
	'''
	convert uri query sting to python object.
	'''
	o = JsonObject()
	pairs = urlparse.parse_qs(content)
	for k, v in pairs.iteritems():
		o[str(k)] = v[0]
	return o

class APIError(StandardError):
	'''
	raise APIError if got failed json message.
	'''
	def __init__(self, error_code, error, request):
		self.error_code = error_code
		self.error = error
		self.request = request
		StandardError.__init__(self, error)

	def __str__(self):
		return 'APIError: %s: %s, request: %s' % (self.error_code, self.error, self.request)

class JsonObject(dict):
	'''
	general json object that can bind any fields but also act as a dict.
	'''
	def __getattr__(self, attr):
		return self[attr]

	def __setattr__(self, attr, value):
		self[attr] = value

def _encode_params(**kw):
	'''
	Encode parameters.
	'''
	args = []
	for k, v in kw.iteritems():
		qv = v.encode('utf-8') if isinstance(v, unicode) else str(v)
		args.append('%s=%s' % (k, urllib.quote(qv)))
	return '&'.join(args)

def _encode_multipart(**kw):
	'''
	Build a multipart/form-data body with generated random boundary.
	'''
	boundary = '----------%s' % hex(int(time.time() * 1000))
	data = []
	for k, v in kw.iteritems():
		data.append('--%s' % boundary)
		if hasattr(v, 'read'):
			# file-like object:
			ext = ''
			filename = getattr(v, 'name', '')
			n = filename.rfind('.')
			if n != (-1):
				ext = filename[n:].lower()
			content = v.read()
			data.append('Content-Disposition: form-data; name="%s"; filename="hidden"' % k)
			data.append('Content-Length: %d' % len(content))
			data.append('Content-Type: %s\r\n' % _guess_content_type(ext))
			data.append(content)
		else:
			data.append('Content-Disposition: form-data; name="%s"\r\n' % k)
			data.append(v.encode('utf-8') if isinstance(v, unicode) else v)
	data.append('--%s--\r\n' % boundary)
	return '\r\n'.join(data), boundary

_CONTENT_TYPES = { '.png': 'image/png', '.gif': 'image/gif', '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.jpe': 'image/jpeg' }

def _guess_content_type(ext):
	return _CONTENT_TYPES.get(ext, 'application/octet-stream')

_HTTP_GET = 0
_HTTP_POST = 1
_HTTP_UPLOAD = 2

def _http_get(url, resp_format='json', **kw):
	logging.info('GET %s' % url)
	return _http_call(url, _HTTP_GET, resp_format, **kw)

def _http_post(url, resp_format='json', **kw):
	logging.info('POST %s' % url)
	return _http_call(url, _HTTP_POST, resp_format, **kw)

def _http_upload(url, resp_format='json', **kw):
	logging.info('MULTIPART POST %s' % url)
	return _http_call(url, _HTTP_UPLOAD, resp_format, **kw)

def _http_call(url, method, resp_format='json', **kw):
	'''
	send an http request and expect to return a json object if no error.
	'''
	params = None
	boundary = None
	if method==_HTTP_UPLOAD:
		params, boundary = _encode_multipart(**kw)
	else:
		params = _encode_params(**kw)
	http_url = '%s?%s' % (url, params) if method==_HTTP_GET else url
	http_body = None if method==_HTTP_GET else params
	req = urllib2.Request(http_url, data=http_body)
	if boundary:
		req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
	resp = urllib2.urlopen(req)
	body = resp.read()
	resp.close()
	if resp_format == 'json' or resp_format == 'jsonp':
		if resp_format == 'jsonp':
			body = body[body.index('{'):body.rindex('}')+1]	
		r = json.loads(body, object_hook=_obj_hook)
	elif resp_format == 'uriqs':
		r = parse_uriqs(body)
	if hasattr(r, 'error_code'):
		raise APIError(r.error_code, getattr(r, 'error', ''), getattr(r, 'request', ''))
	return r

class HttpObject(object):
	def __init__(self, client, method):
		self.client = client
		self.method = method

	def __getattr__(self, attr):
		def wrap(**kw):
			if self.client.is_expires():
				raise APIError('21327', 'expired_token', attr)
			kw["access_token"] = self.client.access_token
			kw["oauth_consumer_key"] = self.client.client_id
			kw["openid"] = self.client.openid
			kw["format"] = 'json'
			return _http_call('%s%s'%(self.client.api_url,attr.replace('__', '/')),self.method,**kw)
		return wrap

class APIClient(object):
	'''
	API client using synchronized invocation.
	'''
	def __init__(self, app_key, app_secret, redirect_uri=None, response_type='code', site_type='pc'):
		self.client_id = app_key
		self.client_secret = app_secret
		self.redirect_uri = redirect_uri
		self.response_type = response_type
		self.site_type= site_type
		self.auth_url = 'https://graph.qq.com/oauth2.0/'
		self.api_url = 'https://graph.qq.com/'
		self.access_token = None
		self.expires = 0.0
		self.openid = 0
		self.get = HttpObject(self, _HTTP_GET)
		self.post = HttpObject(self, _HTTP_POST)
		self.upload = HttpObject(self, _HTTP_UPLOAD)

	def set_access_token(self, access_token, expires, openid):
		self.access_token = str(access_token)
		self.expires = expires
		self.openid = openid 

	def get_authorize_url(self, redirect_uri=None):
		'''
		return the authroize url that should be redirect.
		'''
		redirect = redirect_uri if redirect_uri else self.redirect_uri
		if not redirect:
			raise APIError('21305', 'Parameter absent: redirect_uri', 'OAuth2 request')
		display = 'mobile' if self.site_type=='mobile' else 'default'
		return '%s%s?%s' % (self.auth_url, 'authorize', \
				_encode_params(client_id = self.client_id, \
						response_type = 'code', \
						display = display, \
						state = 'shupeng', \
						redirect_uri = redirect))

	def get_access_token(self, code, redirect_uri=None):
		'''
		return access token as object: {"access_token":"your-access-token","expires_in":12345678}, expires_in is standard unix-epoch-time
		'''
		redirect = redirect_uri if redirect_uri else self.redirect_uri
		if not redirect:
			raise APIError('21305', 'Parameter absent: redirect_uri', 'OAuth2 request')
		r = _http_get('%s%s' % (self.auth_url, 'token'), 'uriqs', \
				client_id = self.client_id, \
				client_secret = self.client_secret, \
				redirect_uri = redirect, \
				state = 'shupeng', \
				code = code, grant_type = 'authorization_code')
		r.expires = int(time.time()) + int(r.expires_in)
		r.openid = self.get_openid(r.access_token)
		self.set_access_token(r.access_token,r.expires,r.openid)
		return r

	def get_openid(self, access_token=None):
		'''
		return openid as object: {"client_id":"your-appid","openid":12345678}
		'''
		access_token = access_token if access_token else self.access_token
		if not access_token:
			raise APIError('21305', 'Parameter absent: access_token', 'openid request')
		resp_format = 'jsonp'
		r = _http_get('%s%s' % (self.auth_url, 'me'), resp_format, access_token = access_token)
		return r.openid

	def is_expires(self):
		return not self.access_token or time.time() > self.expires

	def __getattr__(self, attr):
		return getattr(self.get, attr)

