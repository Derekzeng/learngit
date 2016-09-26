#!/usr/bin/ev python
#coding=utf-8

import tornado
import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")


class LoginHandler(BaseHandler):
    def post(self, *args, **kwargs):
        username = self.get_argument("username")
        if username:
            self.set_secure_cookie("user",username)

        self.redirect(self.reverse_url("derk_index"))

    def get(self, *args, **kwargs):
        self.render("login.html")

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render("index.html")

class WelcomeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write('''
            <html>
              <h1>欢迎你光临本系统,please login:</h1>
              <a href='/login'><strong>Login to system</strong></a>
            </html>
        ''')