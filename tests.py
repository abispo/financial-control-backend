# -*- coding: utf-8 -*-

from api import api
import unittest

class AccountResourceTest(unittest.TestCase):

    def test_index(self):
        tester = api.test_client(self)
        response = tester.get('/accounts/', content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'account index')

if __name__ == '__main__':
    unittest.main()