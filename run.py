#-*- coding: utf-8 -*-

from api import api
from api.resources import AccountResource

AccountResource.register(api, route_base='/accounts/')

api.run()
