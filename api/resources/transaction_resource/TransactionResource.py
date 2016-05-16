#-*- coding: utf-8 -*-

from flask.ext.classy import FlaskView

class TransactionResource(FlaskView):
    def index(self):
        return "transaction"