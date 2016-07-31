# -*- coding: utf-8 -*-

from app.models import db
from datetime import datetime

class Transaction(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime, default=db.func.now())
    amount = db.Column(db.Float, nullable=False)
    
    debited_account_id = db.Column(db.Integer, db.ForeignKey('account.id'))
    credited_account_id = db.Column(db.Integer, db.ForeignKey('account.id'))

    debited_account = db.relationship("Account", foreign_keys=[debited_account_id])
    credited_account = db.relationship("Account", foreign_keys=[credited_account_id])

    def __init__(self, debited_account_id, credited_account_id, amount, timestamp=datetime.today()):
        self.debited_account_id = debited_account_id
        self.credited_account_id = credited_account_id
        self.amount = amount
        self.timestamp = timestamp

    @property
    def serialize(self):
        return {
            'id': self.id,
            'debited_account_id': self.debited_account_id,
            'credited_account_id': self.credited_account_id,
            'amount': self.amount,
            'timestamp': self.timestamp
        }
