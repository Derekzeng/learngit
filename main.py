<<<<<<< HEAD
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
=======
#!/usr/bin/ev python
#coding=utf-8

import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
import os
from handlers import WelcomeHandler,LoginHandler,IndexHandler




urls =[
    (r'/',WelcomeHandler,None,'derk_welcome'),
    (r'/login',LoginHandler,None,'derk_login'),
    (r'/index',IndexHandler,None,'derk_index')
       ]


settings={
    'template_path':os.path.join(os.path.dirname(__file__),'templates'),
    'static_path':os.path.join(os.path.dirname(__file__),'statics'),
    'debug':True,
    'cookie_secret': "HeavyMetalWillNeverDie",
    'login_url':'/login'
}

application = tornado.web.Application(urls,**settings)

if __name__ == "__main__":
    httpd = tornado.httpserver.HTTPServer(application)
    httpd.listen(8089)

    tornado.ioloop.IOLoop.instance().start()


>>>>>>> 9f11dcdc329da99c27366e914410c53e04fa521c
