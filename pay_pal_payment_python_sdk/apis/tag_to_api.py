import typing_extensions

from pay_pal_payment_python_sdk.apis.tags import TagValues
from pay_pal_payment_python_sdk.apis.tags.authorizations_api import AuthorizationsApi
from pay_pal_payment_python_sdk.apis.tags.captures_api import CapturesApi
from pay_pal_payment_python_sdk.apis.tags.refunds_api import RefundsApi
from pay_pal_payment_python_sdk.apis.tags.assets_api import AssetsApi
from pay_pal_payment_python_sdk.apis.tags.cancel_payment_api import CancelPaymentApi
from pay_pal_payment_python_sdk.apis.tags.find_eligible_methods_api import FindEligibleMethodsApi
from pay_pal_payment_python_sdk.apis.tags.payment_resource_operations_api import PaymentResourceOperationsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHORIZATIONS: AuthorizationsApi,
        TagValues.CAPTURES: CapturesApi,
        TagValues.REFUNDS: RefundsApi,
        TagValues.ASSETS: AssetsApi,
        TagValues.CANCELPAYMENT: CancelPaymentApi,
        TagValues.FINDELIGIBLEMETHODS: FindEligibleMethodsApi,
        TagValues.PAYMENTRESOURCEOPERATIONS: PaymentResourceOperationsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHORIZATIONS: AuthorizationsApi,
        TagValues.CAPTURES: CapturesApi,
        TagValues.REFUNDS: RefundsApi,
        TagValues.ASSETS: AssetsApi,
        TagValues.CANCELPAYMENT: CancelPaymentApi,
        TagValues.FINDELIGIBLEMETHODS: FindEligibleMethodsApi,
        TagValues.PAYMENTRESOURCEOPERATIONS: PaymentResourceOperationsApi,
    }
)
