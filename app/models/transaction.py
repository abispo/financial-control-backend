# -*- coding: utf-8 -*-

from app.models import db

class Transaction(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, default=db.func.now())
    amount = db.Column(db.Float, nullable=False)
    
    debited_account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    credited_account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    def __repr__(self):
        return "<Transaction(timestamp='%s', amount='%s')>" % (self.timestamp, self.amount)
