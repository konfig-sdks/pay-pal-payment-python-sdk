# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pay_pal_payment_python_sdk.paths.v2_payments_authorizations_authorization_id_void import Api

from pay_pal_payment_python_sdk.paths import PathValues

path = PathValues.V2_PAYMENTS_AUTHORIZATIONS_AUTHORIZATION_ID_VOID