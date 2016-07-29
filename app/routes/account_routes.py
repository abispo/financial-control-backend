# -*- coding: utf-8 -*-

from app.resources import AccountResource

account_view = AccountResource.as_view('account_api')