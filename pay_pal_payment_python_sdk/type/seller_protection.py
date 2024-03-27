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

from pay_pal_payment_python_sdk.type.seller_protection_dispute_categories import SellerProtectionDisputeCategories

class RequiredSellerProtection(TypedDict):
    pass

class OptionalSellerProtection(TypedDict, total=False):
    # Indicates whether the transaction is eligible for seller protection. For information, see [PayPal Seller Protection for Merchants](https://www.paypal.com/us/webapps/mpp/security/seller-protection).
    status: str

    dispute_categories: SellerProtectionDisputeCategories

class SellerProtection(RequiredSellerProtection, OptionalSellerProtection):
    pass
