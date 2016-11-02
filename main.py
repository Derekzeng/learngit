#coding=utf-8
import tornado
import tornado.web



class GenericHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("rime/hello.html")

import os

TEMPLATE_DIR=os.path.join(os.path.dirname(__file__),'templates')
setting = dict(debug=True,template_path=TEMPLATE_DIR)


application = tornado.web.Application

# kiss something