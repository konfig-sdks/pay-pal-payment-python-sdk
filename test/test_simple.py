# coding: utf-8

"""
    Payments

    Call the Payments API to authorize payments, capture authorized payments, refund payments that have already been captured, and show payment information. Use the Payments API in conjunction with the <a href=\"/docs/api/orders/v2/\">Orders API</a>. For more information, see the <a href=\"/docs/checkout/\">PayPal Checkout Overview</a>.

    The version of the OpenAPI document: 2.5
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from pay_pal_payment_python_sdk import PayPalPayment

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        paypalpayment = PayPalPayment(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(paypalpayment)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()