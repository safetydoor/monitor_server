#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'
from handler.base import BaseHandler
import json
import time
class LocationHandler(BaseHandler):
    def publish(self):
        lat = self.get_argument('lat','0')
        lng = self.get_argument('lng','0')
        type = self.get_argument('type','0')
        prov = self.get_argument('prov','')#.encode('utf-8')
        address = self.get_argument('address','')#.encode('utf-8')
        print address;
        t = time.strftime('%Y-%m-%d:%H:%M:%S',time.localtime(time.time()))
        str = "time:%s,lat=%s,lng=%s,type=%s,prov=%s,address=%s"%(t,lat,lng,type,prov,address)
        print str;
        res = {}
        res['msg'] = ''
        res['interval'] = 300
        jsondata = json.dumps(res);
        self.write(jsondata);