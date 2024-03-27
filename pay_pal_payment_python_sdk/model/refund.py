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


class Refund(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The refund information.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.AnyTypeSchema,
        ):
        
        
            class MetaOapg:
                
                class properties:
                    id = schemas.StrSchema
                
                    @staticmethod
                    def amount() -> typing.Type['Money']:
                        return Money
                    invoice_id = schemas.StrSchema
                    
                    
                    class custom_id(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 127
                            min_length = 1
                            regex=[{
                                'pattern': r'^[A-Za-z0-9-_.,]*$',
                            }]
                    
                    
                    class acquirer_reference_number(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 36
                            min_length = 1
                            regex=[{
                                'pattern': r'^[a-zA-Z0-9]+$',
                            }]
                    note_to_payer = schemas.StrSchema
                    
                    
                    class seller_payable_breakdown(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
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
                                def net_amount_in_receivable_currency() -> typing.Type['Money']:
                                    return Money
                                
                                
                                class platform_fees(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        max_items = 1
                                        min_items = 0
                                        
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
                                
                                
                                class net_amount_breakdown(
                                    schemas.ListSchema
                                ):
                                
                                
                                    class MetaOapg:
                                        
                                        @staticmethod
                                        def items() -> typing.Type['NetAmountBreakdownItem']:
                                            return NetAmountBreakdownItem
                                
                                    def __new__(
                                        cls,
                                        arg: typing.Union[typing.Tuple['NetAmountBreakdownItem'], typing.List['NetAmountBreakdownItem']],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                    ) -> 'net_amount_breakdown':
                                        return super().__new__(
                                            cls,
                                            arg,
                                            _configuration=_configuration,
                                        )
                                
                                    def __getitem__(self, i: int) -> 'NetAmountBreakdownItem':
                                        return super().__getitem__(i)
                            
                                @staticmethod
                                def total_refunded_amount() -> typing.Type['Money']:
                                    return Money
                                __annotations__ = {
                                    "gross_amount": gross_amount,
                                    "paypal_fee": paypal_fee,
                                    "paypal_fee_in_receivable_currency": paypal_fee_in_receivable_currency,
                                    "net_amount": net_amount,
                                    "net_amount_in_receivable_currency": net_amount_in_receivable_currency,
                                    "platform_fees": platform_fees,
                                    "net_amount_breakdown": net_amount_breakdown,
                                    "total_refunded_amount": total_refunded_amount,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["gross_amount"]) -> 'Money': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["paypal_fee"]) -> 'Money': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["paypal_fee_in_receivable_currency"]) -> 'Money': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["net_amount"]) -> 'Money': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["net_amount_in_receivable_currency"]) -> 'Money': ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["platform_fees"]) -> MetaOapg.properties.platform_fees: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["net_amount_breakdown"]) -> MetaOapg.properties.net_amount_breakdown: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["total_refunded_amount"]) -> 'Money': ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["gross_amount", "paypal_fee", "paypal_fee_in_receivable_currency", "net_amount", "net_amount_in_receivable_currency", "platform_fees", "net_amount_breakdown", "total_refunded_amount", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["gross_amount"]) -> typing.Union['Money', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["paypal_fee"]) -> typing.Union['Money', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["paypal_fee_in_receivable_currency"]) -> typing.Union['Money', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["net_amount"]) -> typing.Union['Money', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["net_amount_in_receivable_currency"]) -> typing.Union['Money', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["platform_fees"]) -> typing.Union[MetaOapg.properties.platform_fees, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["net_amount_breakdown"]) -> typing.Union[MetaOapg.properties.net_amount_breakdown, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["total_refunded_amount"]) -> typing.Union['Money', schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gross_amount", "paypal_fee", "paypal_fee_in_receivable_currency", "net_amount", "net_amount_in_receivable_currency", "platform_fees", "net_amount_breakdown", "total_refunded_amount", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, ],
                            gross_amount: typing.Union['Money', schemas.Unset] = schemas.unset,
                            paypal_fee: typing.Union['Money', schemas.Unset] = schemas.unset,
                            paypal_fee_in_receivable_currency: typing.Union['Money', schemas.Unset] = schemas.unset,
                            net_amount: typing.Union['Money', schemas.Unset] = schemas.unset,
                            net_amount_in_receivable_currency: typing.Union['Money', schemas.Unset] = schemas.unset,
                            platform_fees: typing.Union[MetaOapg.properties.platform_fees, list, tuple, schemas.Unset] = schemas.unset,
                            net_amount_breakdown: typing.Union[MetaOapg.properties.net_amount_breakdown, list, tuple, schemas.Unset] = schemas.unset,
                            total_refunded_amount: typing.Union['Money', schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'seller_payable_breakdown':
                            return super().__new__(
                                cls,
                                *args,
                                gross_amount=gross_amount,
                                paypal_fee=paypal_fee,
                                paypal_fee_in_receivable_currency=paypal_fee_in_receivable_currency,
                                net_amount=net_amount,
                                net_amount_in_receivable_currency=net_amount_in_receivable_currency,
                                platform_fees=platform_fees,
                                net_amount_breakdown=net_amount_breakdown,
                                total_refunded_amount=total_refunded_amount,
                                _configuration=_configuration,
                                **kwargs,
                            )
                
                    @staticmethod
                    def payer() -> typing.Type['PayeeBase']:
                        return PayeeBase
                    
                    
                    class links(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['LinkDescription']:
                                return LinkDescription
                    
                        def __new__(
                            cls,
                            arg: typing.Union[typing.Tuple['LinkDescription'], typing.List['LinkDescription']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'links':
                            return super().__new__(
                                cls,
                                arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'LinkDescription':
                            return super().__getitem__(i)
                    __annotations__ = {
                        "id": id,
                        "amount": amount,
                        "invoice_id": invoice_id,
                        "custom_id": custom_id,
                        "acquirer_reference_number": acquirer_reference_number,
                        "note_to_payer": note_to_payer,
                        "seller_payable_breakdown": seller_payable_breakdown,
                        "payer": payer,
                        "links": links,
                    }
        
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["amount"]) -> 'Money': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["invoice_id"]) -> MetaOapg.properties.invoice_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["custom_id"]) -> MetaOapg.properties.custom_id: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["acquirer_reference_number"]) -> MetaOapg.properties.acquirer_reference_number: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["note_to_payer"]) -> MetaOapg.properties.note_to_payer: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["seller_payable_breakdown"]) -> MetaOapg.properties.seller_payable_breakdown: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["payer"]) -> 'PayeeBase': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "amount", "invoice_id", "custom_id", "acquirer_reference_number", "note_to_payer", "seller_payable_breakdown", "payer", "links", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union['Money', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["invoice_id"]) -> typing.Union[MetaOapg.properties.invoice_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["custom_id"]) -> typing.Union[MetaOapg.properties.custom_id, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["acquirer_reference_number"]) -> typing.Union[MetaOapg.properties.acquirer_reference_number, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["note_to_payer"]) -> typing.Union[MetaOapg.properties.note_to_payer, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["seller_payable_breakdown"]) -> typing.Union[MetaOapg.properties.seller_payable_breakdown, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["payer"]) -> typing.Union['PayeeBase', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "amount", "invoice_id", "custom_id", "acquirer_reference_number", "note_to_payer", "seller_payable_breakdown", "payer", "links", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                amount: typing.Union['Money', schemas.Unset] = schemas.unset,
                invoice_id: typing.Union[MetaOapg.properties.invoice_id, str, schemas.Unset] = schemas.unset,
                custom_id: typing.Union[MetaOapg.properties.custom_id, str, schemas.Unset] = schemas.unset,
                acquirer_reference_number: typing.Union[MetaOapg.properties.acquirer_reference_number, str, schemas.Unset] = schemas.unset,
                note_to_payer: typing.Union[MetaOapg.properties.note_to_payer, str, schemas.Unset] = schemas.unset,
                seller_payable_breakdown: typing.Union[MetaOapg.properties.seller_payable_breakdown, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                payer: typing.Union['PayeeBase', schemas.Unset] = schemas.unset,
                links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    id=id,
                    amount=amount,
                    invoice_id=invoice_id,
                    custom_id=custom_id,
                    acquirer_reference_number=acquirer_reference_number,
                    note_to_payer=note_to_payer,
                    seller_payable_breakdown=seller_payable_breakdown,
                    payer=payer,
                    links=links,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                RefundStatus,
                cls.all_of_1,
                ActivityTimestamps,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Refund':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_payment_python_sdk.model.activity_timestamps import ActivityTimestamps
from pay_pal_payment_python_sdk.model.link_description import LinkDescription
from pay_pal_payment_python_sdk.model.money import Money
from pay_pal_payment_python_sdk.model.net_amount_breakdown_item import NetAmountBreakdownItem
from pay_pal_payment_python_sdk.model.payee_base import PayeeBase
from pay_pal_payment_python_sdk.model.platform_fee import PlatformFee
from pay_pal_payment_python_sdk.model.refund_status import RefundStatus