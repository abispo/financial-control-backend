# -*- coding: utf-8 -*-

from flask import Flask
from app.models import db
from app.routes import account_view, transaction_view

api = Flask(__name__)

api.add_url_rule('/accounts/', defaults={'account_id': None}, view_func=account_view, methods=['GET',])
api.add_url_rule('/accounts/', view_func=account_view, methods=['POST',])
api.add_url_rule('/accounts/<int:account_id>/', view_func=account_view, methods=['GET', 'PUT', 'DELETE',])

api.add_url_rule('/transactions/', defaults={'transaction_id': None}, view_func=transaction_view, methods=['GET',])
api.add_url_rule('/transactions/', view_func=transaction_view, methods=['POST',])
api.add_url_rule('/transactions/<int:transaction_id>/', view_func=transaction_view, methods=['GET', 'PUT', 'DELETE',])

with api.app_context():
    api.config.from_pyfile('../config.py', silent=True)
    db.init_app(api)
    db.create_all()
