# coding: utf-8

"""
    Payments

    Call the Payments API to authorize payments, capture authorized payments, refund payments that have already been captured, and show payment information. Use the Payments API in conjunction with the <a href=\"/docs/api/orders/v2/\">Orders API</a>. For more information, see the <a href=\"/docs/checkout/\">PayPal Checkout Overview</a>.

    The version of the OpenAPI document: 2.5
    Generated by: https://konfigthis.com
"""

from pay_pal_payment_python_sdk.paths.v2_payments_authorizations_authorization_id_capture.post import CapturePayment
from pay_pal_payment_python_sdk.paths.v2_payments_authorizations_authorization_id_reauthorize.post import ReauthorizePayment
from pay_pal_payment_python_sdk.paths.v2_payments_authorizations_authorization_id.get import ShowDetails
from pay_pal_payment_python_sdk.paths.v2_payments_authorizations_authorization_id_void.post import VoidPayment
from pay_pal_payment_python_sdk.apis.tags.authorizations_api_raw import AuthorizationsApiRaw


class AuthorizationsApi(
    CapturePayment,
    ReauthorizePayment,
    ShowDetails,
    VoidPayment,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: AuthorizationsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = AuthorizationsApiRaw(api_client)