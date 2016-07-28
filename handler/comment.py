#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'
from handler.base import BaseHandler
import json
import time
from model.comment import CommentModel
from model.mimi import MiMiModel

class CommentHandler(BaseHandler):
    def list(self):
        mimiid = self.get_argument('mimiid',0)
        sql = 'select id,userid,content from comment where mimiid = %s and stat = 0'%mimiid
        comments = CommentModel.mgr().raw(sql)
        res = {}
        for comment in comments:
            comment['headphoto'] ='/static/photo/%s.png'%(1+ int(comment['userid'])%40)
        res['result'] = comments
        res['code'] = 0
        res['msg'] =''
        res['type'] =0
        jsondata = json.dumps(res);
        self.write(jsondata);

    def add(self):
        userid = self.get_argument('userid',0)
        content = self.get_argument('content','').encode('utf-8')
        mimiid = self.get_argument('mimiid',0)
        comment = CommentModel.new()
        comment.userid = userid
        comment.content = content
        comment.mimiid = mimiid
        ret = comment.save()
        mimi = MiMiModel.mgr().Q().filter(id = mimiid)[0]
        mimi['commentcount'] =  mimi['commentcount'] +1
        mimi.save()
        res = {}
        comments = []
        rComment = {}
        rComment['id'] = ret['id']
        rComment['userid'] = ret['userid']
        rComment['content'] = ret['content']
        rComment['headphoto'] ='/static/photo/%s.png'%((1+ int(userid))%40)
        comments.append(rComment)
        res['result'] = comments
        res['code'] = 0
        res['msg'] ='发表成功'
        res['type'] =0
        jsondata = json.dumps(res);
        self.write(jsondata);