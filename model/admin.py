#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from lib.database import Model

class AdminModel(Model):
    '''
    AdminModel
    '''
    _db = 'monitor'
    _table = 'monitor_admin'
    _pk = 'id'
    _fields = set(['id','userName','passWord','group','createTime','state'])
    _scheme = ("`id` int(11) NOT NULL AUTO_INCREMENT",
                "`userName` varchar(50) DEFAULT NULL",
                "`passWord` varchar(50) DEFAULT NULL",
                "`group` varchar(50) DEFAULT 'root'",
                "`createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP",
                "`state` int(11) DEFAULT '0'",
                "PRIMARY KEY (`id`)")

if __name__ == "__main__":
    print AdminModel.new().init_table()
    pass
