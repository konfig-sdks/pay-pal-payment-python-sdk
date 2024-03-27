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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from pay_pal_payment_python_sdk.pydantic.disbursement_mode import DisbursementMode
from pay_pal_payment_python_sdk.pydantic.platform_fee import PlatformFee

class PaymentInstruction(BaseModel):
    # An array of various fees, commissions, tips, or donations. This field is only applicable to merchants that been enabled for PayPal Commerce Platform for Marketplaces and Platforms capability.
    platform_fees: typing.Optional[typing.List[PlatformFee]] = Field(None, alias='platform_fees')

    disbursement_mode: typing.Optional[DisbursementMode] = Field(None, alias='disbursement_mode')

    # This field is only enabled for selected merchants/partners to use and provides the ability to trigger a specific pricing rate/plan for a payment transaction. The list of eligible 'payee_pricing_tier_id' would be provided to you by your Account Manager. Specifying values other than the one provided to you by your account manager would result in an error.
    payee_pricing_tier_id: typing.Optional[str] = Field(None, alias='payee_pricing_tier_id')

    # FX identifier generated returned by PayPal to be used for payment processing in order to honor FX rate (for eligible integrations) to be used when amount is settled/received into the payee account.
    payee_receivable_fx_rate_id: typing.Optional[str] = Field(None, alias='payee_receivable_fx_rate_id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
