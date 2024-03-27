# coding: utf-8

"""
    Payments

    Call the Payments API to authorize payments, capture authorized payments, refund payments that have already been captured, and show payment information. Use the Payments API in conjunction with the <a href=\"/docs/api/orders/v2/\">Orders API</a>. For more information, see the <a href=\"/docs/checkout/\">PayPal Checkout Overview</a>.

    The version of the OpenAPI document: 2.5
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from pay_pal_payment_python_sdk import schemas  # noqa: F401


class PaymentInstruction(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Any additional payment instructions to be consider during payment processing. This processing instruction is applicable for Capturing an order or Authorizing an Order.
    """


    class MetaOapg:
        
        class properties:
            
            
            class platform_fees(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PlatformFee']:
                        return PlatformFee
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PlatformFee'], typing.List['PlatformFee']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'platform_fees':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PlatformFee':
                    return super().__getitem__(i)
        
            @staticmethod
            def disbursement_mode() -> typing.Type['DisbursementMode']:
                return DisbursementMode
            
            
            class payee_pricing_tier_id(
                schemas.StrSchema
            ):
                pass
            
            
            class payee_receivable_fx_rate_id(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "platform_fees": platform_fees,
                "disbursement_mode": disbursement_mode,
                "payee_pricing_tier_id": payee_pricing_tier_id,
                "payee_receivable_fx_rate_id": payee_receivable_fx_rate_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platform_fees"]) -> MetaOapg.properties.platform_fees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disbursement_mode"]) -> 'DisbursementMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payee_pricing_tier_id"]) -> MetaOapg.properties.payee_pricing_tier_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payee_receivable_fx_rate_id"]) -> MetaOapg.properties.payee_receivable_fx_rate_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["platform_fees", "disbursement_mode", "payee_pricing_tier_id", "payee_receivable_fx_rate_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform_fees"]) -> typing.Union[MetaOapg.properties.platform_fees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disbursement_mode"]) -> typing.Union['DisbursementMode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payee_pricing_tier_id"]) -> typing.Union[MetaOapg.properties.payee_pricing_tier_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payee_receivable_fx_rate_id"]) -> typing.Union[MetaOapg.properties.payee_receivable_fx_rate_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["platform_fees", "disbursement_mode", "payee_pricing_tier_id", "payee_receivable_fx_rate_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        platform_fees: typing.Union[MetaOapg.properties.platform_fees, list, tuple, schemas.Unset] = schemas.unset,
        disbursement_mode: typing.Union['DisbursementMode', schemas.Unset] = schemas.unset,
        payee_pricing_tier_id: typing.Union[MetaOapg.properties.payee_pricing_tier_id, str, schemas.Unset] = schemas.unset,
        payee_receivable_fx_rate_id: typing.Union[MetaOapg.properties.payee_receivable_fx_rate_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentInstruction':
        return super().__new__(
            cls,
            *args,
            platform_fees=platform_fees,
            disbursement_mode=disbursement_mode,
            payee_pricing_tier_id=payee_pricing_tier_id,
            payee_receivable_fx_rate_id=payee_receivable_fx_rate_id,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_payment_python_sdk.model.disbursement_mode import DisbursementMode
from pay_pal_payment_python_sdk.model.platform_fee import PlatformFee
