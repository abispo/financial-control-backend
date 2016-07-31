# -*- coding: utf-8 -*-

from flask import jsonify, request
from flask.views import MethodView
from app.models import db, Transaction

class TransactionResource(MethodView):

    def get(self, transaction_id):
        return jsonify({})

    def post(self):
        return jsonify({})

    def delete(self, transaction_id):
        return jsonify({})

    def put(self, transaction_id):
        return jsonify({})
