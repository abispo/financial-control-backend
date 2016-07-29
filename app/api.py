# -*- coding: utf-8 -*-

from flask import Flask
from app.models import db
from app.models import Account

api = Flask(__name__)

with api.app_context():
    api.config.from_pyfile('../config.py', silent=True)
    db.init_app(api)
    db.create_all()
