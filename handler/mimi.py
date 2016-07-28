#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'
from model.user import MiUserModel
from model.mimi import MiMiModel
from handler.base import BaseHandler
import json
import Image
from model.photo import PhotoModel

class MiMiHandler(BaseHandler):
    def add(self):
        content = self.get_argument('content','').encode('utf-8')
        photoid = self.get_argument('photo','')
        userid = self.get_argument('userid','0')
        schoolid = self.get_argument('schoolid','2')
        praisecount = int(self.get_argument('praisecount','1'))
        mimi = MiMiModel.new()
        mimi.content = content
        mimi.photoid = photoid
        mimi.userid = userid
        mimi.schoolid = schoolid
        mimi.praisecount = praisecount
        res = mimi.save();
        print res
        return self.write('发布成功')
    def uploadpage(self):
        self.render('index.html')
    def uploadphoto(self):
        try:
            file_dict_list = self.request.files['file']
            file_dict = file_dict_list[0]
            filename = file_dict["filename"]
            filepath = "static/%s" % filename
            f = open(filepath, "wb")
            f.write(file_dict["body"])
            f.close()
            img = Image.open(filepath)
            width,height = img.size
            photo = PhotoModel.new()
            photo['address'] = filepath
            photo['width'] = width
            photo['height'] = height
            res = photo.save()
            print res
            self.write(str(res['id']));
        except BaseException as e:
            print e
            self.write(e.message);

    def praise(self):
        mimiid = self.get_argument('mimiid','')
        mimis = MiMiModel.mgr().Q().filter(id=mimiid);
        res = {}
        res['code'] = 0
        res['result'] = 0
        if len(mimis)>0:
            mimi = mimis[0]
            mimi['praisecount'] = mimi['praisecount'] +1
            ret = mimi.save();
            res['msg'] ='点赞成功'
            res['result'] = ret['praisecount']
        else:
            res['msg'] ='点赞失败'
        jsondata = json.dumps(res);
        self.write(jsondata);
    def list(self):
        userid = self.get_argument('userid','')
        schoolid = self.get_argument('schoolid','2')
        size = self.get_argument('size','10')
        type = int(self.get_argument('type','1'))
        id = self.get_argument('id','0')
        if type > 0:
            sql = 'select id,content,photoid,praisecount,commentcount from mimi where schoolid = %s and stat = 0 and id > %s order by id desc limit %s'
        else:
            sql = 'select id,content,photoid,praisecount,commentcount from mimi where schoolid = %s and stat = 0 and id < %s limit %s'
        sql = sql % (schoolid,id,size)
        print sql;
        mimis = MiMiModel.mgr().raw(sql)
        for mimi in mimis:
            photo = PhotoModel.mgr().Q().filter(id=mimi['photoid'])[0]
            mimi['photourl'] = '/'+photo['address']
            mimi['width'] = photo['width']
            mimi['height'] = photo['height']
        res = {}
        res['result'] = mimis
        res['code'] = 0
        res['msg'] =''
        #dthandler = lambda obj: obj.isoformat();
        jsondata = json.dumps(res);# default=dthandler
        self.write(jsondata);
