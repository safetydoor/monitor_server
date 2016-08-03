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
                "`desc` varchar(300) DEFAULT NULL",
                "`imageUrl` varchar(300) DEFAULT NULL",
                "`adUrl` varchar(300) DEFAULT NULL",
                "`createTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP",
                "`state` int(11) DEFAULT '0'",
                "PRIMARY KEY (`id`)")

if __name__ == "__main__":
    ads = AdModel.mgr().Q()
    for ad in ads:
        ad['imageUrl'] = ad['imageUrl'].replace('http://127.0.0.1:8088', '')
        ad.save()
    pass
