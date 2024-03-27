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


class AuthorizationStatus(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    The status fields for an authorized payment.
    """


    class MetaOapg:
        
        class properties:
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def CREATED(cls):
                    return cls("CREATED")
                
                @schemas.classproperty
                def CAPTURED(cls):
                    return cls("CAPTURED")
                
                @schemas.classproperty
                def DENIED(cls):
                    return cls("DENIED")
                
                @schemas.classproperty
                def PARTIALLY_CAPTURED(cls):
                    return cls("PARTIALLY_CAPTURED")
                
                @schemas.classproperty
                def VOIDED(cls):
                    return cls("VOIDED")
                
                @schemas.classproperty
                def PENDING(cls):
                    return cls("PENDING")
        
            @staticmethod
            def status_details() -> typing.Type['AuthorizationStatusDetails']:
                return AuthorizationStatusDetails
            __annotations__ = {
                "status": status,
                "status_details": status_details,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status_details"]) -> 'AuthorizationStatusDetails': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["status", "status_details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status_details"]) -> typing.Union['AuthorizationStatusDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["status", "status_details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        status_details: typing.Union['AuthorizationStatusDetails', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuthorizationStatus':
        return super().__new__(
            cls,
            *args,
            status=status,
            status_details=status_details,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_payment_python_sdk.model.authorization_status_details import AuthorizationStatusDetails
