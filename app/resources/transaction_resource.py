# -*- coding: utf-8 -*-

from flask import jsonify, request
from flask.views import MethodView
from app.models import db, Account, Transaction

class TransactionResource(MethodView):

    def get(self, transaction_id):
        trns = db.session.query(Transaction)
        if (transaction_id):
            trns = db.session.query(Transaction).filter_by(id=transaction_id)

        return jsonify(
            transactions=[trn.serialize for trn in trns.all()])

    def post(self):
        json_trns = request.get_json()
        print(json_trns.keys())

        debited_account = db.session.query(Account).filter_by(
            id=json_trns['debited_account_id']).one()
        credited_account = db.session.query(Account).filter_by(
            id=json_trns['credited_account_id']).one()

        trn = Transaction(
            debited_account_id=json_trns['debited_account_id'],
            credited_account_id=json_trns['credited_account_id'],
            amount=json_trns['amount'],
        )
        if "timestamp" in json_trns.keys():
            trn.timestamp = json_trns['timestamp']

        debited_account.balance += json_trns['amount']
        credited_account.balance -= json_trns['amount']

        db.session.add(debited_account)
        db.session.add(credited_account)
        db.session.add(trn)
        db.session.commit()
        return jsonify({})

    def delete(self, transaction_id):
        return jsonify({})

    def put(self, transaction_id):
        return jsonify({})
