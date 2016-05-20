#-*- coding: utf-8 -*-

from flask.ext.classy import FlaskView

class AccountResource(FlaskView):
    def index(self):
        return "account index"
