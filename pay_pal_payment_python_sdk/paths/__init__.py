# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pay_pal_payment_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID = "/v2/payments/authorizations/{authorization_id}"
    V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID_CAPTURE = "/v2/payments/authorizations/{authorization_id}/capture"
    V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID_REAUTHORIZE = "/v2/payments/authorizations/{authorization_id}/reauthorize"
    V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID_VOID = "/v2/payments/authorizations/{authorization_id}/void"
    V2_PAYMENTS_CAPTURES_CAPTURE_ID = "/v2/payments/captures/{capture_id}"
    V2_PAYMENTS_CAPTURES_CAPTURE_ID_REFUND = "/v2/payments/captures/{capture_id}/refund"
    V2_PAYMENTS_REFUNDS_REFUND_ID = "/v2/payments/refunds/{refund_id}"
