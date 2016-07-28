#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'

import json
import cmath
from handler.base import BaseHandler
from model.school import SchoolModel
from model.lump import AreaModel
class SchoolHandler(BaseHandler):
    schools = None;
    def getschools(self):
        if self.schools is None:
            self.schools = SchoolModel.mgr().Q();
        return self.schools;
    def trimprov(self,prov):
        if prov.endswith('市') or prov.endswith('省'):
            prov = prov[0:len(prov)-3];
        return prov
    def near(self):
        prov = self.get_argument('prov','').encode('utf-8')
        prov = self.trimprov(prov)
        lng = float(self.get_argument('lng','0'))
        lat = float(self.get_argument('lat','0'))
        areaid = AreaModel.mgr().Q().filter(aname = prov)[0].id
        schools = SchoolModel.mgr().Q().filter(sareaid = areaid)
        neardis = [10000.0,10000.0,10000.0]
        nearschools = [None,None,None]
        #all = list()
        for school in schools:
            one = dict()
            one['id'] = school.idt
            one['name'] = school.sname
            #all.append(one)
            if school.slng is None or school.slat is None:
                continue
            distance = cmath.sqrt(pow(abs(lng-float(school.slng)),2)+pow(abs(lat-float(school.slat)),2)).real
            if distance<neardis[2]:
                if distance <neardis[1]:
                    if distance <neardis[0]:
                        neardis[2] = neardis[1]
                        neardis[1] = neardis[0]
                        neardis[0] = distance
                        nearschools[2] = nearschools[1]
                        nearschools[1] = nearschools[0]
                        nearschools[0] = school
                    else:
                        neardis[2] = neardis[1]
                        neardis[1] = distance
                        nearschools[2] = nearschools[1]
                        nearschools[1] = school
                else:
                    neardis[2] = distance
                    nearschools[2]  = school
            #print '%s%s'%(school.sname,distance)
        #print near
        #print nearschools

        near = list()
        for s in nearschools:
            one = dict()
            one['id'] = s.id
            one['name'] = s.sname
            near.append(one)
        res = {}
        res['result'] = near
        res['type'] = 'near'
        res['code'] = 0
        res['msg'] =''
        #res['all'] = all
        #dthandler = lambda obj: obj.isoformat();
        #jsondata = json.dumps(res, default=dthandler);
        jsondata = json.dumps(res)
        self.write(jsondata);
    def search(self):
        print 'search'
        key = self.get_argument('key','').encode('utf-8')
        temps = self.getschools()
        searchlist = list();
        for s in temps:
            if key in s.sname:
                model = dict()
                model['id'] = s.id;
                model['name'] = s.sname
                searchlist.append(model)
        res = {}
        res['type'] = 'search'
        res['result'] = searchlist
        res['code'] = 0
        res['msg'] =''
        jsondata = json.dumps(res)
        self.write(jsondata);

if __name__ =='__main__':
    prov = '湖北省';
    len = len(prov);
    print len
    if prov.endswith('市') or prov.endswith('省'):
        prov = prov[0:len-3]
    print prov