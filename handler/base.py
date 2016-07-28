#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import urllib
import datetime
import logging
import json
import time
import base64

import tornado.web
from conf.settings import SESSION_USER
#from model.user import User

class BaseHandler(tornado.web.RequestHandler):
    @property
    def session(self):
        if not hasattr(self,'_session'):
            self._session = self.application.settings['session_mgr'].load_session(self)
        return self._session

    def send_json(self, res, code, msg='', callback=None):
        r = {'status':{'code':code,'msg':msg},'result':res}
        r = json.dumps(r)
        if callback:
            r = '%s(%s);'%(callback,r)
            self.set_header('Content-Type', 'application/json')
        self.write(r)

    def parse_module(self, module):
        mod,sub = "",""
        if module:
            arr = module.split("/")
            if len(arr)>=3:
                mod,sub = arr[1],arr[2]
            elif len(arr)>=2:
                mod = arr[1]
        return '%s__%s'%(mod,sub) if sub else mod

    def get(self, module):
        module = self.parse_module(module)
        method = getattr(self,module or 'index')
        # if not self.current_user:
        #     self.redirect('/login')
        #     return;
        if method and module not in ('get','post'):
            method()
        else:
            raise tornado.web.HTTPError(404)

    def post(self, module):
        module = self.parse_module(module)
        method = getattr(self,module or 'index')
        # if not self.current_user:
        #     self.redirect('/login')
        #     return;
        if method and module not in ('get','post'):
            method()
        else:
            raise tornado.web.HTTPError(404)

    # def get_current_user(self):
    #     uInfo = self.session[SESSION_USER];
    #     if uInfo:
    #         user = User.mgr().Q().filter(userName=uInfo['userName'])[0]
    #         if not user:
    #             self._logout()
    #     print 'get_current_user:%s'%uInfo
    #     return uInfo;

    def _login(self, userName):
        self.session[SESSION_USER] = {'userName':userName}
        self.session.save()

    def _logout(self):
        self.session[SESSION_USER] = None
        self.session.save()