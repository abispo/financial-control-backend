#-*- coding: utf-8 -*-

from flask import Flask

from .resources import AccountResource

api = Flask(__name__)
