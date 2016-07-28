#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib
import datetime
import tornado.web
uibase = tornado.web.UIModule

class UserMod(uibase):
	def render(self, name, title=None):
		return self.render_string("ui-mod/channel-col.html",
			name = name,
			title = title,
		)

