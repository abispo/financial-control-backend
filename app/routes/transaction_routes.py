# -*- coding: utf-8 -*-

from app.resources import TransactionResource
from flask import Blueprint

transaction_view = TransactionResource.as_view('transaction_api')

bp_transaction = Blueprint(
    'bp_transaction',
    __name__,
    url_prefix='/transactions'
)

bp_transaction.add_url_rule(
    '/',
    defaults={'transaction_id': None},
    view_func=transaction_view,
    methods=['GET',]
)

bp_transaction.add_url_rule(
    '/',
    view_func=transaction_view,
    methods=['POST',]
)

bp_transaction.add_url_rule(
    '/<int:transaction_id>/',
    view_func=transaction_view,
    methods=['GET', 'PUT', 'DELETE',]
)