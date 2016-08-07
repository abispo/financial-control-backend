# -*- coding: utf-8 -*-

from app.resources import AccountResource
from flask import Blueprint

account_view = AccountResource.as_view('account_api')

bp_account = Blueprint('bp_account', __name__, url_prefix='/accounts')

bp_account.add_url_rule(
    '/',
    defaults={'account_id': None},
    view_func=account_view,
    methods=['GET',]
)

bp_account.add_url_rule(
    '/',
    view_func=account_view,
    methods=['POST',]
)

bp_account.add_url_rule(
    '/<int:account_id>/',
    view_func=account_view,
    methods=['GET', 'PUT', 'DELETE',]
)