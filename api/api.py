#-*- coding: utf-8 -*-

from flask import Flask

from .resources import AccountResource
from .resources import TransactionResource

api = Flask(__name__)

AccountResource.register(api, route_base='/accounts/')
TransactionResource.register(api, route_base='/transactions/')