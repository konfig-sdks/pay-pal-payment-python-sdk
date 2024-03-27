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


class CapturesRefund422(BaseModel):
    details: typing.Optional[typing.List[typing.Union[typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]], typing.List[typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]]] = Field(None, alias='details')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
