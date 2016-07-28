#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'
from model.user import MiUserModel
from handler.base import BaseHandler
from model.photo import PhotoModel
import json
class MiUserHandler(BaseHandler):
    def autoreg(self):
        schoolid = self.get_argument('schoolid','2')
        miuser = MiUserModel.new()
        miuser['schoolid'] = schoolid
        user = miuser.save()
        self.write(str(user['id']));
    def login(self):
        pass;