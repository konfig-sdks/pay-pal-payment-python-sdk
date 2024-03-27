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


class RelatedIds(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Identifiers related to a specific resource.
    """


    class MetaOapg:
        
        class properties:
            
            
            class order_id(
                schemas.StrSchema
            ):
                pass
            
            
            class authorization_id(
                schemas.StrSchema
            ):
                pass
            
            
            class capture_id(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "order_id": order_id,
                "authorization_id": authorization_id,
                "capture_id": capture_id,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_id"]) -> MetaOapg.properties.order_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authorization_id"]) -> MetaOapg.properties.authorization_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["capture_id"]) -> MetaOapg.properties.capture_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["order_id", "authorization_id", "capture_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_id"]) -> typing.Union[MetaOapg.properties.order_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authorization_id"]) -> typing.Union[MetaOapg.properties.authorization_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["capture_id"]) -> typing.Union[MetaOapg.properties.capture_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["order_id", "authorization_id", "capture_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        order_id: typing.Union[MetaOapg.properties.order_id, str, schemas.Unset] = schemas.unset,
        authorization_id: typing.Union[MetaOapg.properties.authorization_id, str, schemas.Unset] = schemas.unset,
        capture_id: typing.Union[MetaOapg.properties.capture_id, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RelatedIds':
        return super().__new__(
            cls,
            *args,
            order_id=order_id,
            authorization_id=authorization_id,
            capture_id=capture_id,
            _configuration=_configuration,
            **kwargs,
        )
