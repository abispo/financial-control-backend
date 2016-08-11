# -*- coding: utf-8 -*-

from flask import jsonify, request
from flask.views import MethodView
from app.models import db, Account

class AccountResource(MethodView):

    def get(self, account_id):
        accs = db.session.query(Account)
        if (account_id):
            accs = db.session.query(Account).filter_by(id=account_id)

        return jsonify(
            accounts=[acc.serialize for acc in accs.all()]
        ), 200

    def post(self):
        json_acc = request.get_json()
        acc = Account(name=json_acc['name'], balance=json_acc['balance'])
        db.session.add(acc)
        db.session.commit()
        db.session.refresh(acc)

        return jsonify(
            accounts=[acc.serialize]
        ), 201

    def delete(self, account_id):
        db.session.query(Account).filter_by(id=account_id).delete()
        db.session.commit()

        return '', 204

    def put(self, account_id):
        json_acc = request.get_json()
        acc = db.session.query(Account).filter_by(id=account_id).first()
        acc.name = json_acc['name']
        acc.balance = json_acc['balance']
        db.session.commit()

        return jsonify(accounts=[acc.serialize]), 200
