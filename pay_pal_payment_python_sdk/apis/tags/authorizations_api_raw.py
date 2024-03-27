# coding: utf-8

"""
    Payments

    Call the Payments API to authorize payments, capture authorized payments, refund payments that have already been captured, and show payment information. Use the Payments API in conjunction with the <a href=\"/docs/api/orders/v2/\">Orders API</a>. For more information, see the <a href=\"/docs/checkout/\">PayPal Checkout Overview</a>.

    The version of the OpenAPI document: 2.5
    Generated by: https://konfigthis.com
"""

from pay_pal_payment_python_sdk.paths.v2_payments_authorizations_authorization_id_capture.post import CapturePaymentRaw
from pay_pal_payment_python_sdk.paths.v2_payments_authorizations_authorization_id_reauthorize.post import ReauthorizePaymentRaw
from pay_pal_payment_python_sdk.paths.v2_payments_authorizations_authorization_id.get import ShowDetailsRaw
from pay_pal_payment_python_sdk.paths.v2_payments_authorizations_authorization_id_void.post import VoidPaymentRaw


class AuthorizationsApiRaw(
    CapturePaymentRaw,
    ReauthorizePaymentRaw,
    ShowDetailsRaw,
    VoidPaymentRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
