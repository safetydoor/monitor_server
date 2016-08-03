#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from handler.base import BaseHandler
import json
from model.user import UserModel

class UserHandler(BaseHandler):
    def list(self):
        size = int(self.get_argument('size', '10'))
        page = int(self.get_argument('page', '0'))
        if page == 0:
            page = 0
        if size == 0:
            size = 10
        sql = 'select * from monitor_user limit %d,%d' % (page * size, size);
        users = UserModel.mgr().raw(sql)
        self.send_json(users, 0 , '成功')

    def save(self):
        uid = self.get_argument('id', '')
        imei = self.get_argument('imei', '')
        userName = self.get_argument('userName', '').encode('utf-8')
        passWord = self.get_argument('passWord', '')
        phoneNumber = self.get_argument('phoneNumber', '')

        user = UserModel.new()
        if uid != '':
            user.id = uid
        user.imei = imei
        user.userName = userName
        user.passWord = passWord
        user.phoneNumber = phoneNumber
        resUser = user.save()
        self.send_json(resUser, 0, '成功')

    def delete(self):
        uid = int(self.get_argument('id'))
        users = UserModel.mgr(ismaster=1).Q().filter(id=uid)
        if users:
            for user in users:
                user.delete()
        self.send_json({}, 0, '成功')

    def check(self):
        userName = self.get_argument('userName', '').encode('utf-8')
        passWord = self.get_argument('passWord', '')
        sql = "select * from monitor_user where userName='%s' and passWord='%s'" % (userName, passWord)
        users = UserModel.mgr().raw(sql)
        res = dict()
        if len(res) > 0:
            self.send_json(users[0], 0, '登陆成功')
        else:
            self.send_json({}, 1, '用户名或密码错误,登陆失败')

    def edit(self):
        self.save()


if __name__ == "__main__":
    # for i in range(1, 49):
    #     user = UserModel.new()
    #     u = '%d%d%d%d' % (i, i, i, i)
    #     user.imei = u
    #     user.userName = u
    #     user.passWord = u
    #     user.phoneNumber = u
    #     res = user.save()
    #     print res
    pass
