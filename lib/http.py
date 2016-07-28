__author__ = 'safetydoor'

import urllib
import urllib2
import socket
from lib.logger import Logger

class Http(object):
    def __init__(self):
        self.errortimes = 0
        self.errorlimit = 3
        self.timeout = 10
        socket.setdefaulttimeout(self.timeout)

    def getRequest(self,url):
        try:
            request=urllib2.Request(url)
            f =urllib2.urlopen(request)
            response=f.read()
            self.errortimes = 0
            return response;
        except BaseException as e:
            Logger.error('getRequest:%s   %s '%(url,e))
            self.errortimes = self.errortimes + 1
            if self.errortimes >= self.errorlimit:
                return None;
            return self.getRequest(url)
    def postRequest(self,url,data):
        try:
            request=urllib2.Request(url)
            f =urllib2.urlopen(request,data,10000)
            response=f.read()
            self.errortimes = 0
            return response;
        except BaseException as e:
            Logger.error('postRequest:%s   %s'%(url,e))
            self.errortimes = self.errortimes + 1
            if self.errortimes >= self.errorlimit:
                return None;
            return self.postRequest(url,data)

    def down(self,url,savepath):
        try:
            urllib.urlretrieve(url, savepath)
            self.errortimes = 0
            return True
        except BaseException as e:
            Logger.error('down:%s , %s  %s'%(url,savepath,e))
            self.errortimes = self.errortimes + 1
            if self.errortimes >= self.errorlimit:
                return False;
            return self.down(url,savepath)