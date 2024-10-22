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

from pay_pal_payment_python_sdk.pydantic.exchange_rate import ExchangeRate
from pay_pal_payment_python_sdk.pydantic.money import Money
from pay_pal_payment_python_sdk.pydantic.platform_fee import PlatformFee

class SellerReceivableBreakdown(BaseModel):
    gross_amount: Money = Field(alias='gross_amount')

    paypal_fee: typing.Optional[Money] = Field(None, alias='paypal_fee')

    paypal_fee_in_receivable_currency: typing.Optional[Money] = Field(None, alias='paypal_fee_in_receivable_currency')

    net_amount: typing.Optional[Money] = Field(None, alias='net_amount')

    receivable_amount: typing.Optional[Money] = Field(None, alias='receivable_amount')

    exchange_rate: typing.Optional[ExchangeRate] = Field(None, alias='exchange_rate')

    # An array of platform or partner fees, commissions, or brokerage fees that associated with the captured payment.
    platform_fees: typing.Optional[typing.List[PlatformFee]] = Field(None, alias='platform_fees')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
