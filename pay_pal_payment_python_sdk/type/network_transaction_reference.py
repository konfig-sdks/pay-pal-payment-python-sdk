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

from pay_pal_payment_python_sdk.type.card_brand import CardBrand

class RequiredNetworkTransactionReference(TypedDict):
    # Transaction reference id returned by the scheme. For Visa and Amex, this is the \"Tran id\" field in response. For MasterCard, this is the \"BankNet reference id\" field in response. For Discover, this is the \"NRID\" field in response. The pattern we expect for this field from Visa/Amex/CB/Discover is numeric, Mastercard/BNPP is alphanumeric and Paysecure is alphanumeric with special character -.
    id: str

class OptionalNetworkTransactionReference(TypedDict, total=False):
    # The date that the transaction was authorized by the scheme. This field may not be returned for all networks. MasterCard refers to this field as \"BankNet reference date.
    date: str

    network: CardBrand

    # Reference ID issued for the card transaction. This ID can be used to track the transaction across processors, card brands and issuing banks.
    acquirer_reference_number: str

class NetworkTransactionReference(RequiredNetworkTransactionReference, OptionalNetworkTransactionReference):
    pass