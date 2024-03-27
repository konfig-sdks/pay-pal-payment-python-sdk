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

from pay_pal_payment_python_sdk.pydantic.error_details import ErrorDetails
from pay_pal_payment_python_sdk.pydantic.error_link_description import ErrorLinkDescription

class Error404(BaseModel):
    name: typing.Optional[Literal["RESOURCE_NOT_FOUND"]] = Field(None, alias='name')

    message: typing.Optional[Literal["The specified resource does not exist."]] = Field(None, alias='message')

    details: typing.Optional[typing.List[ErrorDetails]] = Field(None, alias='details')

    # The PayPal internal ID. Used for correlation purposes.
    debug_id: typing.Optional[str] = Field(None, alias='debug_id')

    # An array of request-related [HATEOAS links](https://en.wikipedia.org/wiki/HATEOAS).
    links: typing.Optional[typing.List[ErrorLinkDescription]] = Field(None, alias='links')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
