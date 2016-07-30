#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from lib.database import Model

class AdModel(Model):
    '''
    AdModel
    '''
    _db = 'monitor'
    _table = 'monitor_ad'
    _pk = 'id'
    _fields = set(['id','name','desc','imageUrl','adUrl','createTime','state'])
    _scheme = ("`id` int(11) NOT NULL AUTO_INCREMENT",
                "`name` varchar(50) DEFAULT NULL",
                "`desc` varchar(50) DEFAULT NULL",
                "`imageUrl` varchar(150) DEFAULT NULL",
                "`adUrl` varchar(150) DEFAULT NULL",
                "`createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP",
                "`state` int(11) DEFAULT '0'",
                "PRIMARY KEY (`id`)")

if __name__ == "__main__":
    print AdModel.new().init_table()
    pass
