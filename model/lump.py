#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from lib.database import Model

class LumpModel(Model):
    '''
    LumpModel
    '''
    _db = 'monitor'
    _table = 'monitor_lump'
    _pk = 'id'
    _fields = set(['id','name','desc','iconUrl','url', 'categoryId','createTime','state'])
    _scheme = ("`id` int(11) NOT NULL AUTO_INCREMENT",
                "`name` varchar(50) DEFAULT NULL",
                "`desc` varchar(50) DEFAULT NULL",
                "`iconUrl` varchar(150) DEFAULT NULL",
                "`url` varchar(150) DEFAULT NULL",
                "`categoryId` int(11) DEFAULT '0'",
                "`createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP",
                "`state` int(11) DEFAULT '0'",
                "PRIMARY KEY (`id`)")

if __name__ == "__main__":
    print LumpModel.new().init_table()
    pass
