# -*- coding: utf-8 -*-

from app.models import db

class Account(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float)

    transaction = db.relationship(
        'Account',
        backref='transaction',
        lazy='dynamic',
        primaryjoin="and_(Account.id = Transaction.debited_account, Account.id = Transaction.credited_account)"
    )

    def __repr__(self):
        return "<Account(name='%s', balance='%s')>" % (self.name, self.balance)
