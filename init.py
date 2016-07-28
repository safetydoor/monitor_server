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
from handler.school import SchoolHandler
from handler.mimi import MiMiHandler
from handler.location import LocationHandler
from handler.index import IndexHandler
from handler.comment import CommentHandler
from handler.miuser import MiUserHandler
define("port", default=80, help="run on this port", type=int)
define("debug", default=True, help="enable debug mode")
define("online", default=False, help="enable online mode")
define("project_path", default=sys.path[0], help="deploy_path" )
if options.debug:
    import tornado.autoreload
from lib import uimodules, uimethods


class Application(tornado.web.Application):
    def __init__(self):
        settings = {
            "ui_modules": uimodules,
            "ui_methods": uimethods,
            "static_path": os.path.join(options.project_path, "static"),
            "template_path": os.path.join(options.project_path, "tpl"),
            "xsrf_cookies": False,
            "site_title": "img",
            "debug": options.debug,
            "online": options.online,
        }
        handlers = [
            (r"/location(/[a-zA-Z/]*)?", LocationHandler),
            (r"/school(/[a-zA-Z/]*)?", SchoolHandler),
            (r"/mimi(/[a-zA-Z/]*)?", MiMiHandler),
            (r"/index(/[a-zA-Z/]*)?", IndexHandler),
            (r"/comment(/[a-zA-Z/]*)?", CommentHandler),
            (r"/miuser(/[a-zA-Z/]*)?", MiUserHandler),
            (r"/(/[a-zA-Z/]*)?", IndexHandler),
        ]
        tornado.web.Application.__init__(self, handlers, **settings)

    def log_request(self, handler):
        status = handler.get_status()
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
            log_method("%d %s %.2fms", status, handler._request_summary(), request_time)

if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    http_server.listen(options.port)
    print  "start service:%s"%options.port
    tornado.ioloop.IOLoop.instance().start()