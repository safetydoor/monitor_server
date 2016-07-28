#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Abstract: membackend for windows

import os
import time
import hashlib
import logging
import datetime 
import uuid
import cPickle as pickle

class MemBackend(dict):  
    '''
    membackend for session
    ''' 
    def set(self, key, data, expires):
        if not expires:
            expires = 360000
        now = time.time()
        self[key] = {"value":data, "expire":now+expires}
        
    def get(self, key):
        now = time.time()
        value = super(MemBackend,self).get(key,None)
        if self._valid(key,value,now):
            return value['value']
        else:
            return None

    def _valid(self, key, value, now):
        if value:
            if value["expire"] > now:
                return True
            else:
                del self[key]
                return False
        else:
            return False

