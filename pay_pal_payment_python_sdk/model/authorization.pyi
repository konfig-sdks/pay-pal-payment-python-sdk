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


class Authorization(
    schemas.ComposedBase,
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The authorized payment transaction.
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
                        pass
                
                    @staticmethod
                    def network_transaction_reference() -> typing.Type['NetworkTransactionReference']:
                        return NetworkTransactionReference
                
                    @staticmethod
                    def seller_protection() -> typing.Type['SellerProtection']:
                        return SellerProtection
                
                    @staticmethod
                    def expiration_time() -> typing.Type['DateTime']:
                        return DateTime
                    
                    
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
                        "network_transaction_reference": network_transaction_reference,
                        "seller_protection": seller_protection,
                        "expiration_time": expiration_time,
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
            def __getitem__(self, name: typing_extensions.Literal["network_transaction_reference"]) -> 'NetworkTransactionReference': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["seller_protection"]) -> 'SellerProtection': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["expiration_time"]) -> 'DateTime': ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "amount", "invoice_id", "custom_id", "network_transaction_reference", "seller_protection", "expiration_time", "links", ], str]):
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
            def get_item_oapg(self, name: typing_extensions.Literal["network_transaction_reference"]) -> typing.Union['NetworkTransactionReference', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["seller_protection"]) -> typing.Union['SellerProtection', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["expiration_time"]) -> typing.Union['DateTime', schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "amount", "invoice_id", "custom_id", "network_transaction_reference", "seller_protection", "expiration_time", "links", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
                amount: typing.Union['Money', schemas.Unset] = schemas.unset,
                invoice_id: typing.Union[MetaOapg.properties.invoice_id, str, schemas.Unset] = schemas.unset,
                custom_id: typing.Union[MetaOapg.properties.custom_id, str, schemas.Unset] = schemas.unset,
                network_transaction_reference: typing.Union['NetworkTransactionReference', schemas.Unset] = schemas.unset,
                seller_protection: typing.Union['SellerProtection', schemas.Unset] = schemas.unset,
                expiration_time: typing.Union['DateTime', schemas.Unset] = schemas.unset,
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
                    network_transaction_reference=network_transaction_reference,
                    seller_protection=seller_protection,
                    expiration_time=expiration_time,
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
                AuthorizationStatus,
                cls.all_of_1,
                ActivityTimestamps,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Authorization':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_payment_python_sdk.model.activity_timestamps import ActivityTimestamps
from pay_pal_payment_python_sdk.model.authorization_status import AuthorizationStatus
from pay_pal_payment_python_sdk.model.date_time import DateTime
from pay_pal_payment_python_sdk.model.link_description import LinkDescription
from pay_pal_payment_python_sdk.model.money import Money
from pay_pal_payment_python_sdk.model.network_transaction_reference import NetworkTransactionReference
from pay_pal_payment_python_sdk.model.seller_protection import SellerProtection
