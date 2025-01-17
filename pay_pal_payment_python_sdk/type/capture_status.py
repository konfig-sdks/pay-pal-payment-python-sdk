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

from pay_pal_payment_python_sdk.type.capture_status_details import CaptureStatusDetails

class RequiredCaptureStatus(TypedDict):
    pass

class OptionalCaptureStatus(TypedDict, total=False):
    # The status of the captured payment.
    status: str

    status_details: CaptureStatusDetails

class CaptureStatus(RequiredCaptureStatus, OptionalCaptureStatus):
    pass
