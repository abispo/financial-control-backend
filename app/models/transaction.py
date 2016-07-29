# -*- coding: utf-8 -*-

from app.models import db

class Transaction(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, default=db.func.now())
    amount = db.Column(db.Float, nullable=False)
    
    debited_account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    credited_account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    debited_account = db.relationship("Account", foreign_keys=[debited_account_id])
    credited_account = db.relationship("Account", foreign_keys=[credited_account_id])

    def __init__(self, timestamp, amount):
        self.timestamp = timestamp
        self.amount = amount

    def __repr__(self):
        return "<Transaction(timestamp='%s', amount='%s')>" % (self.timestamp, self.amount)
