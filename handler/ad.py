#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'

import json
from model.ad import AdModel
from lib.jsonencoder import CJsonEncoder
from handler.base import BaseHandler
from conf.settings import SERVER_ADDRESS

class AdHandler(BaseHandler):
    def list(self):
        size = int(self.get_argument('size', '10'))
        page = int(self.get_argument('page', '0'))
        if page < 0:
            page = 0
        if size <= 0:
            size = 10
        sql = 'select `id`,`name`,`imageUrl`,`adUrl` from monitor_ad limit %d,%d' % (page * size, size);
        ads = AdModel.mgr().raw(sql)
        for ad in ads:
            imageUrl = ad['imageUrl']
            if imageUrl.startswith('/static/images/'):
                ad['imageUrl'] = SERVER_ADDRESS + imageUrl
        self.send_json(ads, 0 ,'成功')

    def add(self):
        aid = self.get_argument('id', '')
        name = self.get_argument('name', '').encode('utf-8')
        desc = self.get_argument('desc', '').encode('utf-8')
        imageUrl = self.get_argument('imageUrl', '').encode('utf-8')
        adUrl = self.get_argument('adUrl', '').encode('utf-8')
        state = self.get_argument('state', '0')

        ad = AdModel.new()
        if aid != '':
            ad.id = aid
        ad.name = name
        ad.desc = desc
        ad.imageUrl = imageUrl
        ad.adUrl = adUrl
        ad.state = state
        resAd = ad.save()
        res = dict()
        res['result'] = resAd
        res['code'] = 0
        res['msg'] = '成功'
        jsondata = json.dumps(res, cls=CJsonEncoder)
        self.write(jsondata)

    def delete(self):
        aid = int(self.get_argument('id'))
        ads = AdModel.mgr(ismaster=1).Q().filter(id=aid)
        if ads:
            for ad in ads:
                ad.delete()
        res = dict()
        res['result'] = {}
        res['code'] = 0
        res['msg'] = '成功'
        jsondata = json.dumps(res)
        self.write(jsondata)

    def edit(self):
        self.add();


if __name__ == "__main__":
    for i in range(0, 50):
        ad = AdModel.new()
        u = '%d%d%d%d' % (i, i, i, i)
        ad.name = u
        ad.desc = u
        ad.imageUrl = u
        ad.adUrl = u
        res = ad.save()
        print res
    pass
