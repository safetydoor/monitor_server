#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'laps'
from handler.base import BaseHandler
import json
import time

class IndexHandler(BaseHandler):
    def get(self, module):
        self.write('hello world')
