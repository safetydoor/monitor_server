#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'
import json
import os
import time
import hashlib
from handler.base import BaseHandler
from model.admin import AdminModel
from model.user import UserModel
from model.ad import AdModel
from model.category import LumpCategoryModel
from model.lump import LumpModel
from model.live import LiveModel

class AdminHandler(BaseHandler):
    def get(self, module):
        print 'admin get:%s' % module
        if not self.get_current_user() and module != '/login':
            self.redirect('/admin/login')
        else:
            BaseHandler.get(self, module)

    def post(self, module):
        print 'admin post:%s' % module
        if not self.get_current_user() and module != '/check':
            self.write(json.dumps({'statusCode': "200",
                                   'callbackType': "",
                                   'message': "login",
                                   'forwardUrl': "/admin/login"}))
        else:
            BaseHandler.post(self, module)

    #################### main ####################

    def index(self):
        user = self.get_current_user()
        userName = user['userName']
        admin = AdminModel.mgr().Q().filter(userName=userName)[0]
        self.render('index.html',
                    admin=admin)

    def login(self):
        self.render('login.html')

    def logout(self):
        self._logout()
        self.send_json({}, 0, '成功');

    def check(self):
        userName = self.get_argument('userName', '').encode('utf-8')
        passWord = self.get_argument('passWord', '')
        sql = "select * from monitor_admin where userName='%s' and passWord='%s' and `group` in ('root','admin')" % (
            userName, passWord)
        admins = AdminModel.mgr().raw(sql)
        if len(admins) > 0:
            self._login(admins[0]['userName'])
            self.send_json({}, 0, '登陆成功')
        else:
            self.send_json({}, 1, '用户名或密码错误,登陆失败')

    #################### admin ####################

    def adminlist(self):
        # 列表的当前页，默认在第一页
        currentPage = int(self.get_argument('pageNum', 1))
        # 列表中每页显示多少条，默认每页显示20条
        numPerPage = int(self.get_argument('numPerPage', 20))
        print 'numPerPage : %s' % numPerPage;
        # 计算User的总数
        all = AdminModel.mgr().Q()
        totalCount = len(all)
        admins = all[(currentPage - 1) * numPerPage: currentPage * numPerPage]
        self.render('admin/list.html',
                    admins=admins,
                    currentPage=currentPage,
                    numPerPage=numPerPage,
                    totalCount=totalCount);

    def adminadd(self):
        self.render('admin/add.html');

    def adminedit(self):
        id = self.get_argument('id', '0')
        admin = AdminModel.mgr().Q().filter(id=id)[0];
        self.render('admin/edit.html',
                    admin=admin);

    def adminsave(self):
        id = self.get_argument('id', '')
        state = self.get_argument('state', '0')
        passWord = self.get_argument('passWord', '')
        userName = self.get_argument('userName', '')
        group = self.get_argument('group', 'admin')
        admin = AdminModel.new()
        if id != '':
            admin.id = id
        if userName != '':
            admin.userName = userName
        if passWord != '':
            admin.passWord = self.md5(passWord)
        admin.state = state
        admin.group = group
        admin.save()
        self.write(json.dumps({'statusCode': "200",
                               'callbackType': "closeCurrent",
                               'navTabId': "admin",
                               'forwardUrl': "/admin/adminlist"}))

    def adminpwd(self):
        id = self.get_argument('id', '')
        passWord = self.get_argument('passWord', '')
        admin = AdminModel.new()
        admin.id = id
        admin.passWord = self.md5(passWord);
        admin.save()
        self._logout()
        self.redirect('/admin/login')

    def admindelete(self):
        ids = str(self.get_argument('ids')).split(",")
        for id in ids:
            admins = AdminModel.mgr().Q().filter(id=id)
            if admins:
                for admin in admins:
                    if admin['userName'] != 'admin':
                        admin.delete()
        self.write(json.dumps({'statusCode': "200",
                               'callbackType': "forward",
                               'navTabId': "admin",
                               'forwardUrl': "/admin/adminlist"}))

    #################### user ####################

    def userlist(self):
        # 列表的当前页，默认在第一页
        currentPage = int(self.get_argument('pageNum', 1))
        # 列表中每页显示多少条，默认每页显示20条
        numPerPage = int(self.get_argument('numPerPage', 20))
        searchWord = self.get_argument('searchWord', '')
        # 计算User的总数
        if searchWord != '':
            sql = "select * from monitor_user where userName like '%%%%%s%%%%'" % searchWord
            all = UserModel.mgr().raw(sql)
        else:
            all = UserModel.mgr().Q()
        totalCount = len(all)
        users = all[(currentPage - 1) * numPerPage: currentPage * numPerPage]
        self.render('user/list.html',
                    users=users,
                    currentPage=currentPage,
                    numPerPage=numPerPage,
                    totalCount=totalCount,
                    searchWord=searchWord);

    def useradd(self):
        self.render('user/add.html');

    def usersave(self):
        id = self.get_argument('id', '')
        passWord = self.get_argument('passWord', '')
        userName = self.get_argument('userName', '')
        imei = self.get_argument('imei', '')
        phoneNumber = self.get_argument('phoneNumber', '')
        user = UserModel.new()
        if id != '':
            user.id = id
        user.userName = userName
        user.phoneNumber = phoneNumber
        user.imei = imei
        user.passWord = self.md5(passWord)
        user.save()
        self.write(json.dumps({'statusCode': "200",
                               'callbackType': "closeCurrent",
                               'navTabId': "user",
                               'forwardUrl': "/admin/userlist"}))

    #################### ad ####################

    def adlist(self):
        # 列表的当前页，默认在第一页
        currentPage = int(self.get_argument('pageNum', 1))
        # 列表中每页显示多少条，默认每页显示20条
        numPerPage = int(self.get_argument('numPerPage', 20))
        # 计算User的总数
        all = AdModel.mgr().Q()
        totalCount = len(all)
        ads = all[(currentPage - 1) * numPerPage: currentPage * numPerPage]
        self.render('ad/list.html',
                    ads=ads,
                    currentPage=currentPage,
                    numPerPage=numPerPage,
                    totalCount=totalCount);

    def addelete(self):
        ids = str(self.get_argument('ids')).split(",")
        for id in ids:
            ads = AdModel.mgr().Q().filter(id=id)
            if ads:
                for ad in ads:
                    ad.delete()
        self.write(json.dumps({'statusCode': "200",
                               'callbackType': "forward",
                               'navTabId': "admin",
                               'forwardUrl': "/admin/adlist"}))

    def adadd(self):
        self.render('ad/add.html');

    def adedit(self):
        id = self.get_argument('id', '0')
        ad = AdModel.mgr().Q().filter(id=id)[0];
        self.render('ad/edit.html',
                    ad=ad);

    def adsave(self):
        id = self.get_argument('id', '')
        name = self.get_argument('name', '')
        desc = self.get_argument('desc', '')
        imageUrl = self.get_argument('imageUrl', '')
        adUrl = self.get_argument('adUrl', '')
        state = self.get_argument('state', '0')

        ad = AdModel.new()
        if id != '':
            ad.id = id
        ad.name = name
        ad.desc = desc
        ad.imageUrl = imageUrl
        ad.adUrl = adUrl
        ad.state = state
        ad.save()
        self.write(json.dumps({'statusCode': "200",
                               'callbackType': "closeCurrent",
                               'navTabId': "ad",
                               'forwardUrl': "/admin/adlist"}))

    #################### category ####################

    def categorylist(self):
        # 列表的当前页，默认在第一页
        currentPage = int(self.get_argument('pageNum', 1))
        # 列表中每页显示多少条，默认每页显示20条
        numPerPage = int(self.get_argument('numPerPage', 20))
        # 计算User的总数
        all = LumpCategoryModel.mgr().Q().orderby('sort', 'desc')
        totalCount = len(all)
        categorys = all[(currentPage - 1) * numPerPage: currentPage * numPerPage]
        self.render('category/list.html',
                    categorys=categorys,
                    currentPage=currentPage,
                    numPerPage=numPerPage,
                    totalCount=totalCount);

    def categorydelete(self):
        ids = str(self.get_argument('ids')).split(",")
        for id in ids:
            categorys = LumpCategoryModel.mgr().Q().filter(id=id)
            if categorys:
                for category in categorys:
                    category.delete()
        self.write(json.dumps({'statusCode': "200",
                               'callbackType': "forward",
                               'navTabId': "category",
                               'forwardUrl': "/admin/categorylist"}))

    def categoryadd(self):
        self.render('category/add.html');

    def categoryedit(self):
        id = self.get_argument('id', '0')
        category = LumpCategoryModel.mgr().Q().filter(id=id)[0];
        self.render('category/edit.html',
                    category=category);

    def categorysave(self):
        id = self.get_argument('id', '')
        name = self.get_argument('name', '')
        desc = self.get_argument('desc', '')
        sort = self.get_argument('sort', '0')
        category = LumpCategoryModel.new()
        if id != '':
            category.id = id
        category.name = name
        category.desc = desc
        category.sort = sort
        category.save()
        self.write(json.dumps({'statusCode': "200",
                               'callbackType': "closeCurrent",
                               'navTabId': "category",
                               'forwardUrl': "/admin/categorylist"}))

    #################### lump ####################

    def lumplist(self):
        # 列表的当前页，默认在第一页
        currentPage = int(self.get_argument('pageNum', 1))
        # 列表中每页显示多少条，默认每页显示20条
        numPerPage = int(self.get_argument('numPerPage', 20))
        # 计算User的总数
        all = LumpModel.mgr().Q().orderby('sort', 'desc')
        totalCount = len(all)
        lumps = all[(currentPage - 1) * numPerPage: currentPage * numPerPage]
        categorys = LumpCategoryModel.mgr().Q()
        print 'lumplist numPerPage:%d' % numPerPage
        self.render('lump/list.html',
                    lumps=lumps,
                    categorys=categorys,
                    currentPage=currentPage,
                    numPerPage=numPerPage,
                    totalCount=totalCount);

    def lumpdelete(self):
        ids = str(self.get_argument('ids')).split(",")
        for id in ids:
            lumps = LumpModel.mgr().Q().filter(id=id)
            if lumps:
                for lump in lumps:
                    lump.delete()
        self.write(json.dumps({'statusCode': "200",
                               'callbackType': "forward",
                               'navTabId': "lump",
                               'forwardUrl': "/admin/lumplist"}))

    def lumpadd(self):
        categorys = LumpCategoryModel.mgr().Q()
        print 'categorys'
        print categorys
        self.render('lump/add.html',
                    categorys=categorys);

    def lumpedit(self):
        id = self.get_argument('id', '0')
        lump = LumpModel.mgr().Q().filter(id=id)[0];
        categorys = LumpCategoryModel.mgr().Q()
        self.render('lump/edit.html',
                    lump=lump,
                    categorys=categorys);

    def lumpsave(self):
        id = self.get_argument('id', '')
        name = self.get_argument('name', '')
        desc = self.get_argument('desc', '')
        iconUrl = self.get_argument('iconUrl', '')
        url = self.get_argument('url', '')
        categoryId = self.get_argument('categoryId', '0')
        sort = self.get_argument('sort', '0')
        lump = LumpModel.new()
        if id != '':
            lump.id = id
        lump.name = name
        lump.desc = desc
        lump.iconUrl = iconUrl
        lump.url = url
        lump.categoryId = categoryId
        lump.sort = sort
        lump.save()
        self.write(json.dumps({'statusCode': "200",
                               'callbackType': "closeCurrent",
                               'navTabId': "lump",
                               'forwardUrl': "/admin/lumplist"}))

    #################### live ####################

    def livelist(self):
        # 列表的当前页，默认在第一页
        currentPage = int(self.get_argument('pageNum', 1))
        # 列表中每页显示多少条，默认每页显示20条
        numPerPage = int(self.get_argument('numPerPage', 20))
        # 计算User的总数
        all = LiveModel.mgr().Q().orderby('sort', 'desc')
        totalCount = len(all)
        lives = all[(currentPage - 1) * numPerPage: currentPage * numPerPage]
        self.render('live/list.html',
                    lives=lives,
                    currentPage=currentPage,
                    numPerPage=numPerPage,
                    totalCount=totalCount);

    def livedelete(self):
        ids = str(self.get_argument('ids')).split(",")
        for id in ids:
            lives = LiveModel.mgr().Q().filter(id=id)
            if lives:
                for live in lives:
                    live.delete()
        self.write(json.dumps({'statusCode': "200",
                               'callbackType': "forward",
                               'navTabId': "live",
                               'forwardUrl': "/admin/livelist"}))

    def liveadd(self):
        self.render('live/add.html');

    def liveedit(self):
        id = self.get_argument('id', '0')
        live = LiveModel.mgr().Q().filter(id=id)[0];
        self.render('live/edit.html',
                    live=live);

    def livesave(self):
        id = self.get_argument('id', '')
        name = self.get_argument('name', '')
        desc = self.get_argument('desc', '')
        address = self.get_argument('address', '')
        sort = self.get_argument('sort', '0')
        live = LiveModel.new()
        if id != '':
            live.id = id
        live.name = name
        live.desc = desc
        live.address = address
        live.sort = sort
        live.save()
        self.write(json.dumps({'statusCode': "200",
                               'callbackType': "closeCurrent",
                               'navTabId': "live",
                               'forwardUrl': "/admin/livelist"}))

    #################### lump ####################
    def upload(self):
        # 文件的暂存路径
        upload_path = os.path.join(os.path.dirname(__file__), '../static/images')
        # 提取表单中‘name’为‘file’的文件元数据
        print self.request.files
        file_metas = self.request.files['Filedata']
        meta = file_metas[0]
        filename = '%d.png' % int(time.time()*100)
        filepath = os.path.join(upload_path, filename)
        with open(filepath, 'wb') as up:
            up.write(meta['body'])

        url = '/static/images/%s' % filename
        self.send_json({'url': url}, 0, '成功');

    def md5(self, str):
        m2 = hashlib.md5()
        m2.update(str)
        return m2.hexdigest()


if __name__ == '__main__':
    print os.path.join(os.path.dirname(__file__), '../static/images')
    print int(time.time()*100)
    # sql = "select * from monitor_user where userName like '%%%%%s%%%%'" % '1111'
    # print sql
    # print UserModel.mgr().raw(sql)
    # for i in range(50, 100):
    #     admin = AdminModel.new()
    #     u = '%d%d%d%d' % (i, i, i, i)
    #     admin.userName = u
    #     admin.passWord = u
    #     admin.group = 'admin'
    #     res = admin.save()
    #     print res
    pass
