# -*- coding: utf-8 -*-

from app.models import db

class Account(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    balance = db.Column(db.Float)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __repr__(self):
        return "<Account(name='%s', balance='%s')>" % (self.name, self.balance)

    @property
    def serialize(self):
        return {
            'id':       self.id,
            'name':     self.name,
            'balance':  self.balance
        }
