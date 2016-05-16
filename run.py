#-*- coding: utf-8 -*-

from api import api
from api.resources import AccountResource
from api.resources import TransactionResource

AccountResource.register(api, route_base='/accounts/')
TransactionResource.register(api, route_base='transactions')

api.run()
