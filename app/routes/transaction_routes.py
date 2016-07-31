# -*- coding: utf-8 -*-

from app.resources import TransactionResource

transaction_view = TransactionResource.as_view('transaction_api')