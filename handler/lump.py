#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'
from handler.base import BaseHandler
import json
from model.lump import LumpModel
from lib.jsonencoder import CJsonEncoder


class LumpHandler(BaseHandler):
    def list(self):
        size = int(self.get_argument('size', '10'))
        page = int(self.get_argument('page', '0'))
        if page < 0:
            page = 0
        if size <= 0:
            size = 10
        sql = 'select * from monitor_lump limit %d,%d' % (page * size, size);
        lumps = LumpModel.mgr().raw(sql)
        res = {}
        res['result'] = lumps
        res['code'] = 0
        res['msg'] = '成功'
        jsondata = json.dumps(res, cls=CJsonEncoder)
        self.write(jsondata)

    def add(self):
        lid = self.get_argument('id', '')
        name = self.get_argument('name', '').encode('utf-8')
        desc = self.get_argument('desc', '').encode('utf-8')
        iconUrl = self.get_argument('iconUrl', '').encode('utf-8')
        url = self.get_argument('url', '').encode('utf-8')
        categoryId = self.get_argument('categoryId', '0')
        state = self.get_argument('state', '0')

        lump = LumpModel.new()
        if lid != '':
            lump.id = lid
        lump.name = name
        lump.desc = desc
        lump.iconUrl = iconUrl
        lump.url = url
        lump.categoryId = categoryId
        lump.state = state
        resLump = lump.save()
        res = dict()
        res['result'] = resLump
        res['code'] = 0
        res['msg'] = '成功'
        jsondata = json.dumps(res, cls=CJsonEncoder)
        self.write(jsondata)

    def delete(self):
        lid = int(self.get_argument('id'))
        lumps = LumpModel.mgr(ismaster=1).Q().filter(id=lid)
        if lumps:
            for lump in lumps:
                lump.delete()
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
        lump = LumpModel.new()
        u = '%d%d%d%d' % (i, i, i, i)
        lump.name = u
        lump.desc = u
        lump.iconUrl = u
        lump.url = u
        lump.categoryId = 1
        res = lump.save()
        print res
    pass
