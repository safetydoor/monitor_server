#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'
from handler.base import BaseHandler
import json
from model.live import LiveModel
from lib.jsonencoder import CJsonEncoder

class LiveHandler(BaseHandler):
    def list(self):
        size = int(self.get_argument('size', '20'))
        page = int(self.get_argument('page', '0'))
        if page < 0:
            page = 0
        if size <= 0:
            size = 10
        sql = 'select id,name,address from monitor_live order by sort desc limit %d,%d' % (page * size, size);
        lives = LiveModel.mgr().raw(sql)
        self.send_json(lives, 0, '成功')

    def add(self):
        lid = self.get_argument('id', '')
        name = self.get_argument('name', '').encode('utf-8')
        desc = self.get_argument('desc', '').encode('utf-8')
        iconUrl = self.get_argument('iconUrl', '').encode('utf-8')
        address = self.get_argument('address', '').encode('utf-8')
        sort = self.get_argument('sort', '0')
        state = self.get_argument('state', '0')

        live = LiveModel.new()
        if lid != '':
            live.id = lid
        live.name = name
        live.desc = desc
        live.iconUrl = iconUrl
        live.address = address
        live.sort = sort
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
    lives = LiveModel.mgr().Q()
    for live in lives:
        live['iconUrl'] = ''
        live.save()
    pass
