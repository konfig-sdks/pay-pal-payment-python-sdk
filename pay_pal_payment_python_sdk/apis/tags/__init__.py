# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from pay_pal_payment_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    AUTHORIZATIONS = "authorizations"
    CAPTURES = "captures"
    REFUNDS = "refunds"
    ASSETS = "assets"
    CANCELPAYMENT = "cancel-payment"
    FINDELIGIBLEMETHODS = "find-eligible-methods"
    PAYMENTRESOURCEOPERATIONS = "payment-resource-operations"
