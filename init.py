#!/usr/bin/env python
# -*- coding: utf-8 -*-

# sys
import os
import sys
import logging
# tornado
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from conf.settings import COOKIE_NAME,COOKIE_SECRET,PORT

define("port", default=PORT, help="run on this port", type=int)
define("debug", default=True, help="enable debug mode")
define("online", default=False, help="enable online mode")
define("project_path", default=sys.path[0], help="deploy_path" )
if options.debug:
    import tornado.autoreload
from lib import uimodules, uimethods
from handler.user import UserHandler
from handler.admin import AdminHandler
from handler.ad import AdHandler
from handler.live import LiveHandler
from handler.lump import LumpHandler
from handler.category import CategoryHandler
from lib.membackend import MemBackend
from lib.session import TornadoSessionManager

class Application(tornado.web.Application):
    def __init__(self):
        settings = {
            "ui_modules": uimodules,
            "ui_methods": uimethods,
            "static_path": os.path.join(options.project_path, "static"),
            "template_path": os.path.join(options.project_path, "tpl"),
            "xsrf_cookies": False,
            "site_title": "img",
            "session_mgr": TornadoSessionManager(COOKIE_NAME, COOKIE_SECRET, MemBackend()),
            "debug": options.debug,
            "online": options.online,
        }
        handlers = [
            (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "static"}),
            (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": "static/css"}),
            (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": "static/js"}),
            (r"/admin/js/(.*)", tornado.web.StaticFileHandler, {"path": "static/admin/js"}),
            (r"/admin/img/(.*)", tornado.web.StaticFileHandler, {"path": "static/admin/img"}),
            (r"/admin/uploadify/(.*)", tornado.web.StaticFileHandler, {"path": "static/admin/uploadify"}),
            (r"/admin/xheditor/(.*)", tornado.web.StaticFileHandler, {"path": "static/admin/xheditor"}),
            (r"/admin/chart/(.*)", tornado.web.StaticFileHandler, {"path": "static/admin/chart"}),
            (r"/admin/themes/(.*)", tornado.web.StaticFileHandler, {"path": "static/admin/themes"}),
            (r"/admin/bin/(.*)", tornado.web.StaticFileHandler, {"path": "static/admin/bin"}),

            (r"/ad(/[a-zA-Z/]*)?", AdHandler),
            (r"/live(/[a-zA-Z/]*)?", LiveHandler),
            (r"/lump(/[a-zA-Z/]*)?", LumpHandler),
            (r"/category(/[a-zA-Z/]*)?", CategoryHandler),
            (r"/user(/[a-zA-Z/]*)?", UserHandler),
            (r"/admin(/[a-zA-Z/]*)?", AdminHandler),
            (r"/(/[a-zA-Z/]*)?", AdminHandler),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)

    def log_request(self, handler):
        status = handler.get_status()
        url = handler.request.uri
        print '%s : %s' % (status, url);
        if status < 400:
            if handler.request.uri[0:7] == '/static':
                return
            log_method = logging.info
        elif status < 500:
            log_method = logging.warning
        else:
            log_method = logging.error
        request_time = 1000.0 * handler.request.request_time()
        if request_time > 30.0 or options.debug or status >= 400:
            pass
            log_method("%d %s %.2fms", status, handler._request_summary(), request_time)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    print  "start service:%s"%options.port
    tornado.ioloop.IOLoop.instance().start()