#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'
from handler.base import BaseHandler
import json
from model.category import LumpCategoryModel
from lib.jsonencoder import CJsonEncoder


class CategoryHandler(BaseHandler):
    def list(self):
        size = int(self.get_argument('size', '10'))
        page = int(self.get_argument('page', '0'))
        if page == 0:
            page = 0
        if size == 0:
            size = 10
        sql = 'select * from monitor_lumpCategory limit %d,%d' % (page * size, size);
        categorys = LumpCategoryModel.mgr().raw(sql)
        res = {}
        res['result'] = categorys
        res['code'] = 0
        res['msg'] = '成功'
        jsondata = json.dumps(res, cls=CJsonEncoder)
        self.write(jsondata)

    def add(self):
        cid = self.get_argument('id', '')
        name = self.get_argument('name', '').encode('utf-8')
        desc = self.get_argument('desc', '').encode('utf-8')
        state = self.get_argument('state', '0')
        category = LumpCategoryModel.new()
        if cid != '':
            category.id = cid
        category.name = name
        category.desc = desc
        category.state = state
        resCat = category.save()
        res = dict()
        res['result'] = resCat
        res['code'] = 0
        res['msg'] = '成功'
        jsondata = json.dumps(res, cls=CJsonEncoder)
        self.write(jsondata)

    def delete(self):
        cid = int(self.get_argument('id'))
        categorys = LumpCategoryModel.mgr(ismaster=1).Q().filter(id=cid)
        if categorys:
            for category in categorys:
                category.delete()
        res = dict()
        res['result'] = {}
        res['code'] = 0
        res['msg'] = '成功'
        jsondata = json.dumps(res)
        self.write(jsondata)

    def edit(self):
        self.add();


if __name__ == "__main__":
    category = LumpCategoryModel.new()
    u = '便民服务'
    category.name = u
    category.desc = u
    res = category.save()
    print res
    pass
