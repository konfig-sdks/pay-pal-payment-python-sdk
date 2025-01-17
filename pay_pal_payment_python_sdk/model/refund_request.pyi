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


class RefundRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Refunds a captured payment, by ID. For a full refund, include an empty request body. For a partial refund, include an <code>amount</code> object in the request body.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def amount() -> typing.Type['Money']:
                return Money
            
            
            class custom_id(
                schemas.StrSchema
            ):
                pass
            
            
            class invoice_id(
                schemas.StrSchema
            ):
                pass
            
            
            class note_to_payer(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def payment_instruction() -> typing.Type['PaymentInstruction2']:
                return PaymentInstruction2
            __annotations__ = {
                "amount": amount,
                "custom_id": custom_id,
                "invoice_id": invoice_id,
                "note_to_payer": note_to_payer,
                "payment_instruction": payment_instruction,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> 'Money': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_id"]) -> MetaOapg.properties.custom_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invoice_id"]) -> MetaOapg.properties.invoice_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["note_to_payer"]) -> MetaOapg.properties.note_to_payer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_instruction"]) -> 'PaymentInstruction2': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["amount", "custom_id", "invoice_id", "note_to_payer", "payment_instruction", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union['Money', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_id"]) -> typing.Union[MetaOapg.properties.custom_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invoice_id"]) -> typing.Union[MetaOapg.properties.invoice_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["note_to_payer"]) -> typing.Union[MetaOapg.properties.note_to_payer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_instruction"]) -> typing.Union['PaymentInstruction2', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["amount", "custom_id", "invoice_id", "note_to_payer", "payment_instruction", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union['Money', schemas.Unset] = schemas.unset,
        custom_id: typing.Union[MetaOapg.properties.custom_id, str, schemas.Unset] = schemas.unset,
        invoice_id: typing.Union[MetaOapg.properties.invoice_id, str, schemas.Unset] = schemas.unset,
        note_to_payer: typing.Union[MetaOapg.properties.note_to_payer, str, schemas.Unset] = schemas.unset,
        payment_instruction: typing.Union['PaymentInstruction2', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RefundRequest':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            custom_id=custom_id,
            invoice_id=invoice_id,
            note_to_payer=note_to_payer,
            payment_instruction=payment_instruction,
            _configuration=_configuration,
            **kwargs,
        )

from pay_pal_payment_python_sdk.model.money import Money
from pay_pal_payment_python_sdk.model.payment_instruction2 import PaymentInstruction2
