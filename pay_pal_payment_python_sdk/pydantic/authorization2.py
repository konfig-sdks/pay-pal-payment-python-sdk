# coding: utf-8

"""
    Payments

    Call the Payments API to authorize payments, capture authorized payments, refund payments that have already been captured, and show payment information. Use the Payments API in conjunction with the <a href=\"/docs/api/orders/v2/\">Orders API</a>. For more information, see the <a href=\"/docs/checkout/\">PayPal Checkout Overview</a>.

    The version of the OpenAPI document: 2.5
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from pay_pal_payment_python_sdk.pydantic.authorization import Authorization
from pay_pal_payment_python_sdk.pydantic.payee_base import PayeeBase
from pay_pal_payment_python_sdk.pydantic.supplementary_data import SupplementaryData

Authorization2 = typing.Union[Authorization,typing.Union[bool, date, datetime, dict, float, int, list, str, None]]
Authorization2 = object
