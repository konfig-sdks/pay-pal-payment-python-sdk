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

from pay_pal_payment_python_sdk.pydantic.platform_fee import PlatformFee

class PaymentInstruction2(BaseModel):
    # Specifies the amount that the API caller will contribute to the refund being processed. The amount needs to be lower than platform_fees amount originally captured or the amount that is remaining if multiple refunds have been processed. This field is only applicable to merchants that have been enabled for PayPal Commerce Platform for Marketplaces and Platforms capability. Please speak to your account manager if you want to use this capability.
    platform_fees: typing.Optional[typing.List[PlatformFee]] = Field(None, alias='platform_fees')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
