#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]))

from lib.database import Model

class LumpCategoryModel(Model):
    '''
    LumpCategoryModel
    '''
    _db = 'monitor'
    _table = 'monitor_lumpCategory'
    _pk = 'id'
    _fields = set(['id', 'name', 'desc', 'sort', 'createTime','state'])
    _scheme = ("`id` int(11) NOT NULL AUTO_INCREMENT",
                "`name` varchar(50) DEFAULT NULL",
                "`desc` varchar(300) DEFAULT NULL",
                "`sort` int(11) DEFAULT '0'",
                "`createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP",
                "`state` int(11) DEFAULT '0'",
                "PRIMARY KEY (`id`)")

if __name__ == "__main__":
    print LumpCategoryModel.new().init_table()
    pass
