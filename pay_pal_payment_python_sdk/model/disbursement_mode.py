# coding: utf-8

"""
    Payments

    Call the Payments API to authorize payments, capture authorized payments, refund payments that have already been captured, and show payment information. Use the Payments API in conjunction with the <a href=\"/docs/api/orders/v2/\">Orders API</a>. For more information, see the <a href=\"/docs/checkout/\">PayPal Checkout Overview</a>.

    The version of the OpenAPI document: 2.5
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from pay_pal_payment_python_sdk import schemas  # noqa: F401


class DisbursementMode(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The funds that are held on behalf of the merchant.
    """


    class MetaOapg:
        max_length = 16
        min_length = 1
        regex=[{
            'pattern': r'^[A-Z_]+$',
        }]
        enum_value_to_name = {
            "INSTANT": "INSTANT",
            "DELAYED": "DELAYED",
        }
    
    @schemas.classproperty
    def INSTANT(cls):
        return cls("INSTANT")
    
    @schemas.classproperty
    def DELAYED(cls):
        return cls("DELAYED")
