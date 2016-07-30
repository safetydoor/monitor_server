#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'
from handler.base import BaseHandler
import json
from model.live import LiveModel
from lib.jsonencoder import CJsonEncoder


class LiveHandler(BaseHandler):
    def list(self):
        size = int(self.get_argument('size', '10'))
        page = int(self.get_argument('page', '0'))
        if page < 0:
            page = 0
        if size <= 0:
            size = 10
        sql = 'select * from monitor_live limit %d,%d' % (page * size, size);
        lives = LiveModel.mgr().raw(sql)
        res = {}
        res['result'] = lives
        res['code'] = 0
        res['msg'] = '成功'
        jsondata = json.dumps(res, cls=CJsonEncoder)
        self.write(jsondata)

    def add(self):
        lid = self.get_argument('id', '')
        name = self.get_argument('name', '').encode('utf-8')
        desc = self.get_argument('desc', '').encode('utf-8')
        iconUrl = self.get_argument('iconUrl', '').encode('utf-8')
        address = self.get_argument('address', '').encode('utf-8')
        state = self.get_argument('state', '0')

        live = LiveModel.new()
        if lid != '':
            live.id = lid
        live.name = name
        live.desc = desc
        live.iconUrl = iconUrl
        live.address = address
        live.state = state
        resLive = live.save()
        res = dict()
        res['result'] = resLive
        res['code'] = 0
        res['msg'] = '成功'
        jsondata = json.dumps(res, cls=CJsonEncoder)
        self.write(jsondata)

    def delete(self):
        lid = int(self.get_argument('id'))
        lives = LiveModel.mgr(ismaster=1).Q().filter(id=lid)
        if lives:
            for live in lives:
                live.delete()
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
        live = LiveModel.new()
        u = '%d%d%d%d' % (i, i, i, i)
        live.name = u
        live.desc = u
        live.imageUrl = u
        live.address = u
        res = live.save()
        print res
    pass
