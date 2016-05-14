#-*- coding: utf-8 -*-

from flask.ext.classy import FlaskView, route

class AccountResource(FlaskView):
    def index(self):
        return "index"
