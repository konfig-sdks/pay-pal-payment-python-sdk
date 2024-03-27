import typing_extensions

from pay_pal_payment_python_sdk.paths import PathValues
from pay_pal_payment_python_sdk.apis.paths.v2_payments_authorizations_authorization_id import V2PaymentsAuthorizationsAuthorizationId
from pay_pal_payment_python_sdk.apis.paths.v2_payments_authorizations_authorization_id_capture import V2PaymentsAuthorizationsAuthorizationIdCapture
from pay_pal_payment_python_sdk.apis.paths.v2_payments_authorizations_authorization_id_reauthorize import V2PaymentsAuthorizationsAuthorizationIdReauthorize
from pay_pal_payment_python_sdk.apis.paths.v2_payments_authorizations_authorization_id_void import V2PaymentsAuthorizationsAuthorizationIdVoid
from pay_pal_payment_python_sdk.apis.paths.v2_payments_captures_capture_id import V2PaymentsCapturesCaptureId
from pay_pal_payment_python_sdk.apis.paths.v2_payments_captures_capture_id_refund import V2PaymentsCapturesCaptureIdRefund
from pay_pal_payment_python_sdk.apis.paths.v2_payments_refunds_refund_id import V2PaymentsRefundsRefundId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID: V2PaymentsAuthorizationsAuthorizationId,
        PathValues.V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID_CAPTURE: V2PaymentsAuthorizationsAuthorizationIdCapture,
        PathValues.V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID_REAUTHORIZE: V2PaymentsAuthorizationsAuthorizationIdReauthorize,
        PathValues.V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID_VOID: V2PaymentsAuthorizationsAuthorizationIdVoid,
        PathValues.V2_PAYMENTS_CAPTURES_CAPTURE_ID: V2PaymentsCapturesCaptureId,
        PathValues.V2_PAYMENTS_CAPTURES_CAPTURE_ID_REFUND: V2PaymentsCapturesCaptureIdRefund,
        PathValues.V2_PAYMENTS_REFUNDS_REFUND_ID: V2PaymentsRefundsRefundId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID: V2PaymentsAuthorizationsAuthorizationId,
        PathValues.V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID_CAPTURE: V2PaymentsAuthorizationsAuthorizationIdCapture,
        PathValues.V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID_REAUTHORIZE: V2PaymentsAuthorizationsAuthorizationIdReauthorize,
        PathValues.V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID_VOID: V2PaymentsAuthorizationsAuthorizationIdVoid,
        PathValues.V2_PAYMENTS_CAPTURES_CAPTURE_ID: V2PaymentsCapturesCaptureId,
        PathValues.V2_PAYMENTS_CAPTURES_CAPTURE_ID_REFUND: V2PaymentsCapturesCaptureIdRefund,
        PathValues.V2_PAYMENTS_REFUNDS_REFUND_ID: V2PaymentsRefundsRefundId,
    }
)
