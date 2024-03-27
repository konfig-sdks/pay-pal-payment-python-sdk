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


class AuthorizationsVoid422(
    schemas.AnyTypeSchema,
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            
            
            class details(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.ComposedSchema,
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class any_of_0(
                                schemas.AnyTypeSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                        
                                        
                                        class description(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                enum_value_to_name = {
                                                    "Authorization has been previously captured and hence cannot be voided.": "AUTHORIZATION_HAS_BEEN_PREVIOUSLY_CAPTURED_AND_HENCE_CANNOT_BE_VOIDED_",
                                                }
                                            
                                            @schemas.classproperty
                                            def AUTHORIZATION_HAS_BEEN_PREVIOUSLY_CAPTURED_AND_HENCE_CANNOT_BE_VOIDED_(cls):
                                                return cls("Authorization has been previously captured and hence cannot be voided.")
                                        
                                        
                                        class issue(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                enum_value_to_name = {
                                                    "PREVIOUSLY_CAPTURED": "PREVIOUSLY_CAPTURED",
                                                }
                                            
                                            @schemas.classproperty
                                            def PREVIOUSLY_CAPTURED(cls):
                                                return cls("PREVIOUSLY_CAPTURED")
                                        __annotations__ = {
                                            "description": description,
                                            "issue": issue,
                                        }
                            
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["issue"]) -> MetaOapg.properties.issue: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "issue", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["issue"]) -> typing.Union[MetaOapg.properties.issue, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "issue", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                                    issue: typing.Union[MetaOapg.properties.issue, str, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_0':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        description=description,
                                        issue=issue,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            
                            class any_of_1(
                                schemas.AnyTypeSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                        
                                        
                                        class description(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                enum_value_to_name = {
                                                    "Authorization has been previously voided and hence cannot be voided again.": "AUTHORIZATION_HAS_BEEN_PREVIOUSLY_VOIDED_AND_HENCE_CANNOT_BE_VOIDED_AGAIN_",
                                                }
                                            
                                            @schemas.classproperty
                                            def AUTHORIZATION_HAS_BEEN_PREVIOUSLY_VOIDED_AND_HENCE_CANNOT_BE_VOIDED_AGAIN_(cls):
                                                return cls("Authorization has been previously voided and hence cannot be voided again.")
                                        
                                        
                                        class issue(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                enum_value_to_name = {
                                                    "PREVIOUSLY_VOIDED": "PREVIOUSLY_VOIDED",
                                                }
                                            
                                            @schemas.classproperty
                                            def PREVIOUSLY_VOIDED(cls):
                                                return cls("PREVIOUSLY_VOIDED")
                                        __annotations__ = {
                                            "description": description,
                                            "issue": issue,
                                        }
                            
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["issue"]) -> MetaOapg.properties.issue: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "issue", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["issue"]) -> typing.Union[MetaOapg.properties.issue, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "issue", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                                    issue: typing.Union[MetaOapg.properties.issue, str, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_1':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        description=description,
                                        issue=issue,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            
                            class any_of_2(
                                schemas.AnyTypeSchema,
                            ):
                            
                            
                                class MetaOapg:
                                    
                                    class properties:
                                        
                                        
                                        class description(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                enum_value_to_name = {
                                                    "A reauthorization cannot be voided. Please void the original parent authorization.": "A_REAUTHORIZATION_CANNOT_BE_VOIDED__PLEASE_VOID_THE_ORIGINAL_PARENT_AUTHORIZATION_",
                                                }
                                            
                                            @schemas.classproperty
                                            def A_REAUTHORIZATION_CANNOT_BE_VOIDED__PLEASE_VOID_THE_ORIGINAL_PARENT_AUTHORIZATION_(cls):
                                                return cls("A reauthorization cannot be voided. Please void the original parent authorization.")
                                        
                                        
                                        class issue(
                                            schemas.EnumBase,
                                            schemas.StrSchema
                                        ):
                                        
                                        
                                            class MetaOapg:
                                                enum_value_to_name = {
                                                    "CANNOT_BE_VOIDED": "CANNOT_BE_VOIDED",
                                                }
                                            
                                            @schemas.classproperty
                                            def CANNOT_BE_VOIDED(cls):
                                                return cls("CANNOT_BE_VOIDED")
                                        __annotations__ = {
                                            "description": description,
                                            "issue": issue,
                                        }
                            
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
                                
                                @typing.overload
                                def __getitem__(self, name: typing_extensions.Literal["issue"]) -> MetaOapg.properties.issue: ...
                                
                                @typing.overload
                                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                                
                                def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "issue", ], str]):
                                    # dict_instance[name] accessor
                                    return super().__getitem__(name)
                                
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: typing_extensions.Literal["issue"]) -> typing.Union[MetaOapg.properties.issue, schemas.Unset]: ...
                                
                                @typing.overload
                                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                                
                                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "issue", ], str]):
                                    return super().get_item_oapg(name)
                                
                            
                                def __new__(
                                    cls,
                                    *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                    description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
                                    issue: typing.Union[MetaOapg.properties.issue, str, schemas.Unset] = schemas.unset,
                                    _configuration: typing.Optional[schemas.Configuration] = None,
                                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                ) -> 'any_of_2':
                                    return super().__new__(
                                        cls,
                                        *args,
                                        description=description,
                                        issue=issue,
                                        _configuration=_configuration,
                                        **kwargs,
                                    )
                            
                            @classmethod
                            @functools.lru_cache()
                            def any_of(cls):
                                # we need this here to make our import statements work
                                # we must store _composed_schemas in here so the code is only run
                                # when we invoke this method. If we kept this at the class
                                # level we would get an error because the class level
                                # code would be run when this module is imported, and these composed
                                # classes don't exist yet because their module has not finished
                                # loading
                                return [
                                    cls.any_of_0,
                                    cls.any_of_1,
                                    cls.any_of_2,
                                ]
                    
                    
                        def __new__(
                            cls,
                            *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'details':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "details": details,
            }

    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["details"]) -> MetaOapg.properties.details: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["details", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["details"]) -> typing.Union[MetaOapg.properties.details, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["details", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        details: typing.Union[MetaOapg.properties.details, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AuthorizationsVoid422':
        return super().__new__(
            cls,
            *args,
            details=details,
            _configuration=_configuration,
            **kwargs,
        )
