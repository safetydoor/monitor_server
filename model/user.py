#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from lib.database import Model

class UserModel(Model):
    '''
    UserModel
    '''
    _db = 'monitor'
    _table = 'monitor_user'
    _pk = 'id'
    _fields = set(['id','imei','userName','passWord','phoneNumber','createTime','stat'])
    _scheme = ("`id` int(11) NOT NULL AUTO_INCREMENT",
                "`imei` varchar(50) DEFAULT NULL",
                "`userName` varchar(50) DEFAULT NULL",
                "`passWord` varchar(50) DEFAULT NULL",
                "`phoneNumber` varchar(50) DEFAULT NULL",
                "`createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP",
                "`state` int(11) DEFAULT '0'",
                "PRIMARY KEY (`id`)")

if __name__ == "__main__":
    print UserModel.mgr().Q()
    pass
