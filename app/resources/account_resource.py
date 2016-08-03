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
        )

    def post(self):
        json_acc = request.get_json()
        acc = Account(name=json_acc['name'], balance=json_acc['balance'])
        db.session.add(acc)
        db.session.commit()
        return jsonify({})

    def delete(self, account_id):
        n_rows_affected = db.session.query(Account).filter_by(id=account_id).delete()
        db.session.commit()
        return jsonify(rows_affected=n_rows_affected)

    def put(self, account_id):
        json_acc = request.get_json()
        n_rows_affected = db.session.query(Account).filter_by(id=account_id).update(json_acc)
        db.session.commit()

        return jsonify(rows_affected=n_rows_affected)
