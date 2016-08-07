# -*- coding: utf-8 -*-

from flask import Flask
from app.models import db
from app.routes import bp_account, bp_transaction

api = Flask(__name__)

api.register_blueprint(bp_account)
api.register_blueprint(bp_transaction)

with api.app_context():
    api.config.from_pyfile('../config.py', silent=True)
    db.init_app(api)
    db.create_all()
