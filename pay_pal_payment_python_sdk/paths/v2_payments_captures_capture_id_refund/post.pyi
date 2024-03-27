# coding: utf-8

"""
    Payments

    Call the Payments API to authorize payments, capture authorized payments, refund payments that have already been captured, and show payment information. Use the Payments API in conjunction with the <a href=\"/docs/api/orders/v2/\">Orders API</a>. For more information, see the <a href=\"/docs/checkout/\">PayPal Checkout Overview</a>.

    The version of the OpenAPI document: 2.5
    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from pay_pal_payment_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from pay_pal_payment_python_sdk.api_response import AsyncGeneratorResponse
from pay_pal_payment_python_sdk import api_client, exceptions
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

from pay_pal_payment_python_sdk.model.refund import Refund as RefundSchema
from pay_pal_payment_python_sdk.model.captures_refund_payment403_response import CapturesRefundPayment403Response as CapturesRefundPayment403ResponseSchema
from pay_pal_payment_python_sdk.model.money import Money as MoneySchema
from pay_pal_payment_python_sdk.model.error_default import ErrorDefault as ErrorDefaultSchema
from pay_pal_payment_python_sdk.model.captures_refund_payment409_response import CapturesRefundPayment409Response as CapturesRefundPayment409ResponseSchema
from pay_pal_payment_python_sdk.model.payment_instruction2 import PaymentInstruction2 as PaymentInstruction2Schema
from pay_pal_payment_python_sdk.model.captures_refund_payment401_response import CapturesRefundPayment401Response as CapturesRefundPayment401ResponseSchema
from pay_pal_payment_python_sdk.model.refund_request import RefundRequest as RefundRequestSchema
from pay_pal_payment_python_sdk.model.captures_refund_payment422_response import CapturesRefundPayment422Response as CapturesRefundPayment422ResponseSchema
from pay_pal_payment_python_sdk.model.captures_refund_payment_response import CapturesRefundPaymentResponse as CapturesRefundPaymentResponseSchema
from pay_pal_payment_python_sdk.model.captures_refund_payment404_response import CapturesRefundPayment404Response as CapturesRefundPayment404ResponseSchema

from pay_pal_payment_python_sdk.type.money import Money
from pay_pal_payment_python_sdk.type.captures_refund_payment401_response import CapturesRefundPayment401Response
from pay_pal_payment_python_sdk.type.captures_refund_payment409_response import CapturesRefundPayment409Response
from pay_pal_payment_python_sdk.type.refund import Refund
from pay_pal_payment_python_sdk.type.error_default import ErrorDefault
from pay_pal_payment_python_sdk.type.captures_refund_payment404_response import CapturesRefundPayment404Response
from pay_pal_payment_python_sdk.type.captures_refund_payment403_response import CapturesRefundPayment403Response
from pay_pal_payment_python_sdk.type.payment_instruction2 import PaymentInstruction2
from pay_pal_payment_python_sdk.type.captures_refund_payment422_response import CapturesRefundPayment422Response
from pay_pal_payment_python_sdk.type.refund_request import RefundRequest
from pay_pal_payment_python_sdk.type.captures_refund_payment_response import CapturesRefundPaymentResponse

from ...api_client import Dictionary
from pay_pal_payment_python_sdk.pydantic.captures_refund_payment404_response import CapturesRefundPayment404Response as CapturesRefundPayment404ResponsePydantic
from pay_pal_payment_python_sdk.pydantic.captures_refund_payment422_response import CapturesRefundPayment422Response as CapturesRefundPayment422ResponsePydantic
from pay_pal_payment_python_sdk.pydantic.captures_refund_payment401_response import CapturesRefundPayment401Response as CapturesRefundPayment401ResponsePydantic
from pay_pal_payment_python_sdk.pydantic.captures_refund_payment403_response import CapturesRefundPayment403Response as CapturesRefundPayment403ResponsePydantic
from pay_pal_payment_python_sdk.pydantic.money import Money as MoneyPydantic
from pay_pal_payment_python_sdk.pydantic.captures_refund_payment_response import CapturesRefundPaymentResponse as CapturesRefundPaymentResponsePydantic
from pay_pal_payment_python_sdk.pydantic.payment_instruction2 import PaymentInstruction2 as PaymentInstruction2Pydantic
from pay_pal_payment_python_sdk.pydantic.captures_refund_payment409_response import CapturesRefundPayment409Response as CapturesRefundPayment409ResponsePydantic
from pay_pal_payment_python_sdk.pydantic.refund import Refund as RefundPydantic
from pay_pal_payment_python_sdk.pydantic.refund_request import RefundRequest as RefundRequestPydantic
from pay_pal_payment_python_sdk.pydantic.error_default import ErrorDefault as ErrorDefaultPydantic

# Header params
PayPalRequestIdSchema = schemas.StrSchema
PreferSchema = schemas.StrSchema
PayPalAuthAssertionSchema = schemas.StrSchema
RequestRequiredHeaderParams = typing_extensions.TypedDict(
    'RequestRequiredHeaderParams',
    {
    }
)
RequestOptionalHeaderParams = typing_extensions.TypedDict(
    'RequestOptionalHeaderParams',
    {
        'PayPal-Request-Id': typing.Union[PayPalRequestIdSchema, str, ],
        'Prefer': typing.Union[PreferSchema, str, ],
        'PayPal-Auth-Assertion': typing.Union[PayPalAuthAssertionSchema, str, ],
    },
    total=False
)


class RequestHeaderParams(RequestRequiredHeaderParams, RequestOptionalHeaderParams):
    pass


request_header_pay_pal_request_id = api_client.HeaderParameter(
    name="PayPal-Request-Id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PayPalRequestIdSchema,
)
request_header_prefer = api_client.HeaderParameter(
    name="Prefer",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PreferSchema,
)
request_header_pay_pal_auth_assertion = api_client.HeaderParameter(
    name="PayPal-Auth-Assertion",
    style=api_client.ParameterStyle.SIMPLE,
    schema=PayPalAuthAssertionSchema,
)
# Path params
CaptureIdSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'capture_id': typing.Union[CaptureIdSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_capture_id = api_client.PathParameter(
    name="capture_id",
    style=api_client.ParameterStyle.SIMPLE,
    schema=CaptureIdSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = RefundRequestSchema


request_body_refund_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor201ResponseBodyApplicationJson = RefundSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: Refund


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: Refund


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = CapturesRefundPaymentResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: CapturesRefundPaymentResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: CapturesRefundPaymentResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = CapturesRefundPayment401ResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: CapturesRefundPayment401Response


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: CapturesRefundPayment401Response


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = CapturesRefundPayment403ResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: CapturesRefundPayment403Response


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: CapturesRefundPayment403Response


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = CapturesRefundPayment404ResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: CapturesRefundPayment404Response


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: CapturesRefundPayment404Response


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor409ResponseBodyApplicationJson = CapturesRefundPayment409ResponseSchema


@dataclass
class ApiResponseFor409(api_client.ApiResponse):
    body: CapturesRefundPayment409Response


@dataclass
class ApiResponseFor409Async(api_client.AsyncApiResponse):
    body: CapturesRefundPayment409Response


_response_for_409 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor409,
    response_cls_async=ApiResponseFor409Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor409ResponseBodyApplicationJson),
    },
)
SchemaFor422ResponseBodyApplicationJson = CapturesRefundPayment422ResponseSchema


@dataclass
class ApiResponseFor422(api_client.ApiResponse):
    body: CapturesRefundPayment422Response


@dataclass
class ApiResponseFor422Async(api_client.AsyncApiResponse):
    body: CapturesRefundPayment422Response


_response_for_422 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor422,
    response_cls_async=ApiResponseFor422Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor422ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    body: schemas.Unset = schemas.unset


@dataclass
class ApiResponseFor500Async(api_client.AsyncApiResponse):
    body: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    response_cls_async=ApiResponseFor500Async,
)
SchemaFor0ResponseBodyApplicationJson = ErrorDefaultSchema


@dataclass
class ApiResponseForDefault(api_client.ApiResponse):
    body: ErrorDefault


@dataclass
class ApiResponseForDefaultAsync(api_client.AsyncApiResponse):
    body: ErrorDefault


_response_for_default = api_client.OpenApiResponse(
    response_cls=ApiResponseForDefault,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor0ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _refund_payment_mapped_args(
        self,
        capture_id: str,
        amount: typing.Optional[Money] = None,
        custom_id: typing.Optional[str] = None,
        invoice_id: typing.Optional[str] = None,
        note_to_payer: typing.Optional[str] = None,
        payment_instruction: typing.Optional[PaymentInstruction2] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _header_params = {}
        _path_params = {}
        _body = {}
        if amount is not None:
            _body["amount"] = amount
        if custom_id is not None:
            _body["custom_id"] = custom_id
        if invoice_id is not None:
            _body["invoice_id"] = invoice_id
        if note_to_payer is not None:
            _body["note_to_payer"] = note_to_payer
        if payment_instruction is not None:
            _body["payment_instruction"] = payment_instruction
        args.body = _body
        if pay_pal_request_id is not None:
            _header_params["PayPal-Request-Id"] = pay_pal_request_id
        if prefer is not None:
            _header_params["Prefer"] = prefer
        if pay_pal_auth_assertion is not None:
            _header_params["PayPal-Auth-Assertion"] = pay_pal_auth_assertion
        if capture_id is not None:
            _path_params["capture_id"] = capture_id
        args.header = _header_params
        args.path = _path_params
        return args

    async def _arefund_payment_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Refund captured payment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_capture_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_pay_pal_request_id,
            request_header_prefer,
            request_header_pay_pal_auth_assertion,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/payments/captures/{capture_id}/refund',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_refund_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserializationAsync(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _refund_payment_oapg(
        self,
        body: typing.Any = None,
            header_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Refund captured payment
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestHeaderParams, header_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_capture_id,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        for parameter in (
            request_header_pay_pal_request_id,
            request_header_prefer,
            request_header_pay_pal_auth_assertion,
        ):
            parameter_data = header_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _headers.extend(serialized_data)
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/v2/payments/captures/{capture_id}/refund',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_refund_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            default_response = _status_code_to_response.get('default')
            if default_response:
                api_response = default_response.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(
                    response=response.http_response,
                    round_trip_time=response.round_trip_time,
                    status=response.http_response.status,
                    headers=response.http_response.headers,
                )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class RefundPaymentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def arefund_payment(
        self,
        capture_id: str,
        amount: typing.Optional[Money] = None,
        custom_id: typing.Optional[str] = None,
        invoice_id: typing.Optional[str] = None,
        note_to_payer: typing.Optional[str] = None,
        payment_instruction: typing.Optional[PaymentInstruction2] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._refund_payment_mapped_args(
            capture_id=capture_id,
            amount=amount,
            custom_id=custom_id,
            invoice_id=invoice_id,
            note_to_payer=note_to_payer,
            payment_instruction=payment_instruction,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
        )
        return await self._arefund_payment_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def refund_payment(
        self,
        capture_id: str,
        amount: typing.Optional[Money] = None,
        custom_id: typing.Optional[str] = None,
        invoice_id: typing.Optional[str] = None,
        note_to_payer: typing.Optional[str] = None,
        payment_instruction: typing.Optional[PaymentInstruction2] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._refund_payment_mapped_args(
            capture_id=capture_id,
            amount=amount,
            custom_id=custom_id,
            invoice_id=invoice_id,
            note_to_payer=note_to_payer,
            payment_instruction=payment_instruction,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
        )
        return self._refund_payment_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

class RefundPayment(BaseApi):

    async def arefund_payment(
        self,
        capture_id: str,
        amount: typing.Optional[Money] = None,
        custom_id: typing.Optional[str] = None,
        invoice_id: typing.Optional[str] = None,
        note_to_payer: typing.Optional[str] = None,
        payment_instruction: typing.Optional[PaymentInstruction2] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> RefundPydantic:
        raw_response = await self.raw.arefund_payment(
            capture_id=capture_id,
            amount=amount,
            custom_id=custom_id,
            invoice_id=invoice_id,
            note_to_payer=note_to_payer,
            payment_instruction=payment_instruction,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
            **kwargs,
        )
        if validate:
            return RootModel[RefundPydantic](raw_response.body).root
        return api_client.construct_model_instance(RefundPydantic, raw_response.body)
    
    
    def refund_payment(
        self,
        capture_id: str,
        amount: typing.Optional[Money] = None,
        custom_id: typing.Optional[str] = None,
        invoice_id: typing.Optional[str] = None,
        note_to_payer: typing.Optional[str] = None,
        payment_instruction: typing.Optional[PaymentInstruction2] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
        validate: bool = False,
    ) -> RefundPydantic:
        raw_response = self.raw.refund_payment(
            capture_id=capture_id,
            amount=amount,
            custom_id=custom_id,
            invoice_id=invoice_id,
            note_to_payer=note_to_payer,
            payment_instruction=payment_instruction,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
        )
        if validate:
            return RootModel[RefundPydantic](raw_response.body).root
        return api_client.construct_model_instance(RefundPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        capture_id: str,
        amount: typing.Optional[Money] = None,
        custom_id: typing.Optional[str] = None,
        invoice_id: typing.Optional[str] = None,
        note_to_payer: typing.Optional[str] = None,
        payment_instruction: typing.Optional[PaymentInstruction2] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        ApiResponseForDefaultAsync,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._refund_payment_mapped_args(
            capture_id=capture_id,
            amount=amount,
            custom_id=custom_id,
            invoice_id=invoice_id,
            note_to_payer=note_to_payer,
            payment_instruction=payment_instruction,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
        )
        return await self._arefund_payment_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        capture_id: str,
        amount: typing.Optional[Money] = None,
        custom_id: typing.Optional[str] = None,
        invoice_id: typing.Optional[str] = None,
        note_to_payer: typing.Optional[str] = None,
        payment_instruction: typing.Optional[PaymentInstruction2] = None,
        pay_pal_request_id: typing.Optional[str] = None,
        prefer: typing.Optional[str] = None,
        pay_pal_auth_assertion: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        ApiResponseForDefault,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._refund_payment_mapped_args(
            capture_id=capture_id,
            amount=amount,
            custom_id=custom_id,
            invoice_id=invoice_id,
            note_to_payer=note_to_payer,
            payment_instruction=payment_instruction,
            pay_pal_request_id=pay_pal_request_id,
            prefer=prefer,
            pay_pal_auth_assertion=pay_pal_auth_assertion,
        )
        return self._refund_payment_oapg(
            body=args.body,
            header_params=args.header,
            path_params=args.path,
        )

