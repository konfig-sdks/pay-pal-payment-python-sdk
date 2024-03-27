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


class SellerReceivableBreakdown(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The detailed breakdown of the capture activity. This is not available for transactions that are in pending state.
    """


    class MetaOapg:
        required = {
            "gross_amount",
        }
        
        class properties:
        
            @staticmethod
            def gross_amount() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def paypal_fee() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def paypal_fee_in_receivable_currency() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def net_amount() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def receivable_amount() -> typing.Type['Money']:
                return Money
        
            @staticmethod
            def exchange_rate() -> typing.Type['ExchangeRate']:
                return ExchangeRate
            
            
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
            __annotations__ = {
                "gross_amount": gross_amount,
                "paypal_fee": paypal_fee,
                "paypal_fee_in_receivable_currency": paypal_fee_in_receivable_currency,
                "net_amount": net_amount,
                "receivable_amount": receivable_amount,
                "exchange_rate": exchange_rate,
                "platform_fees": platform_fees,
            }
    
    gross_amount: 'Money'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gross_amount"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paypal_fee"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paypal_fee_in_receivable_currency"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["net_amount"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receivable_amount"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exchange_rate"]) -> 'ExchangeRate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["platform_fees"]) -> MetaOapg.properties.platform_fees: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gross_amount", "paypal_fee", "paypal_fee_in_receivable_currency", "net_amount", "receivable_amount", "exchange_rate", "platform_fees", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gross_amount"]) -> 'Money': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paypal_fee"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paypal_fee_in_receivable_currency"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["net_amount"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receivable_amount"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exchange_rate"]) -> typing.Union['ExchangeRate', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["platform_fees"]) -> typing.Union[MetaOapg.properties.platform_fees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gross_amount", "paypal_fee", "paypal_fee_in_receivable_currency", "net_amount", "receivable_amount", "exchange_rate", "platform_fees", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        gross_amount: 'Money',
        paypal_fee: typing.Union['Money', schemas.Unset] = schemas.unset,
        paypal_fee_in_receivable_currency: typing.Union['Money', schemas.Unset] = schemas.unset,
        net_amount: typing.Union['Money', schemas.Unset] = schemas.unset,
        receivable_amount: typing.Union['Money', schemas.Unset] = schemas.unset,
        exchange_rate: typing.Union['ExchangeRate', schemas.Unset] = schemas.unset,
        platform_fees: typing.Union[MetaOapg.properties.platform_fees, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SellerReceivableBreakdown':
        return super().__new__(
            cls,
            *args,
            gross_amount=gross_amount,
            paypal_fee=paypal_fee,
            paypal_fee_in_receivable_currency=paypal_fee_in_receivable_currency,
            net_amount=net_amount,
            receivable_amount=receivable_amount,
            exchange_rate=exchange_rate,
            platform_fees=platform_fees,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_payment_python_sdk.model.exchange_rate import ExchangeRate
from pay_pal_payment_python_sdk.model.money import Money
from pay_pal_payment_python_sdk.model.platform_fee import PlatformFee