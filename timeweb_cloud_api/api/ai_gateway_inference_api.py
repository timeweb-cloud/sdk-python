# coding: utf-8

"""
    Timeweb Cloud API

    # Введение API Timeweb Cloud позволяет вам управлять ресурсами в облаке программным способом с использованием обычных HTTP-запросов.  Множество функций, которые доступны в панели управления Timeweb Cloud, также доступны через API, что позволяет вам автоматизировать ваши собственные сценарии.  В этой документации сперва будет описан общий дизайн и принципы работы API, а после этого конкретные конечные точки. Также будут приведены примеры запросов к ним.   ## Запросы Запросы должны выполняться по протоколу `HTTPS`, чтобы гарантировать шифрование транзакций. Поддерживаются следующие методы запроса: |Метод|Применение| |--- |--- | |GET|Извлекает данные о коллекциях и отдельных ресурсах.| |POST|Для коллекций создает новый ресурс этого типа. Также используется для выполнения действий с конкретным ресурсом.| |PUT|Обновляет существующий ресурс.| |PATCH|Некоторые ресурсы поддерживают частичное обновление, то есть обновление только части атрибутов ресурса, в этом случае вместо метода PUT будет использован PATCH.| |DELETE|Удаляет ресурс.|  Методы `POST`, `PUT` и `PATCH` могут включать объект в тело запроса с типом содержимого `application/json`.  ### Параметры в запросах Некоторые коллекции поддерживают пагинацию, поиск или сортировку в запросах. В параметрах запроса требуется передать: - `limit` — обозначает количество записей, которое необходимо вернуть  - `offset` — указывает на смещение, относительно начала списка  - `search` — позволяет указать набор символов для поиска  - `sort` — можно задать правило сортировки коллекции  ## Ответы Запросы вернут один из следующих кодов состояния ответа HTTP:  |Статус|Описание| |--- |--- | |200 OK|Действие с ресурсом было выполнено успешно.| |201 Created|Ресурс был успешно создан. При этом ресурс может быть как уже готовым к использованию, так и находиться в процессе запуска.| |204 No Content|Действие с ресурсом было выполнено успешно, и ответ не содержит дополнительной информации в теле.| |400 Bad Request|Был отправлен неверный запрос, например, в нем отсутствуют обязательные параметры и т. д. Тело ответа будет содержать дополнительную информацию об ошибке.| |401 Unauthorized|Ошибка аутентификации.| |403 Forbidden|Аутентификация прошла успешно, но недостаточно прав для выполнения действия.| |404 Not Found|Запрашиваемый ресурс не найден.| |409 Conflict|Запрос конфликтует с текущим состоянием.| |423 Locked|Ресурс из запроса заблокирован от применения к нему указанного метода.| |429 Too Many Requests|Был достигнут лимит по количеству запросов в единицу времени.| |500 Internal Server Error|При выполнении запроса произошла какая-то внутренняя ошибка. Чтобы решить эту проблему, лучше всего создать тикет в панели управления.|  ### Структура успешного ответа Все конечные точки будут возвращать данные в формате `JSON`. Ответы на `GET`-запросы будут иметь на верхнем уровне следующую структуру атрибутов:  |Название поля|Тип|Описание| |--- |--- |--- | |[entity_name]|object, object[], string[], number[], boolean|Динамическое поле, которое будет меняться в зависимости от запрашиваемого ресурса и будет содержать все атрибуты, необходимые для описания этого ресурса. Например, при запросе списка баз данных будет возвращаться поле `dbs`, а при запросе конкретного облачного сервера `server`. Для некоторых конечных точек в ответе может возвращаться сразу несколько ресурсов.| |meta|object|Опционально. Объект, который содержит вспомогательную информацию о ресурсе. Чаще всего будет встречаться при запросе коллекций и содержать поле `total`, которое будет указывать на количество элементов в коллекции.| |response_id|string|Опционально. В большинстве случаев в ответе будет содержаться ID ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот ID— так мы сможем найти ответ на него намного быстрее. Также вы можете использовать этот ID, чтобы убедиться, что это новый ответ на запрос и результат не был получен из кэша.|  Пример запроса на получение списка SSH-ключей: ```     HTTP/2.0 200 OK     {       \"ssh_keys\":[           {             \"body\":\"ssh-rsa AAAAB3NzaC1sdfghjkOAsBwWhs= example@device.local\",             \"created_at\":\"2021-09-15T19:52:27Z\",             \"expired_at\":null,             \"id\":5297,             \"is_default\":false,             \"name\":\"example@device.local\",             \"used_at\":null,             \"used_by\":[]           }       ],       \"meta\":{           \"total\":1       },       \"response_id\":\"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ### Структура ответа с ошибкой |Название поля|Тип|Описание| |--- |--- |--- | |status_code|number|Короткий числовой идентификатор ошибки.| |error_code|string|Короткий текстовый идентификатор ошибки, который уточняет числовой идентификатор и удобен для программной обработки. Самый простой пример — это код `not_found` для ошибки 404.| |message|string, string[]|Опционально. В большинстве случаев в ответе будет содержаться человекочитаемое подробное описание ошибки или ошибок, которые помогут понять, что нужно исправить.| |response_id|string|Опционально. В большинстве случае в ответе будет содержаться ID ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот ID — так мы сможем найти ответ на него намного быстрее.|  Пример: ```     HTTP/2.0 403 Forbidden     {       \"status_code\": 403,       \"error_code\":  \"forbidden\",       \"message\":     \"You do not have access for the attempted action\",       \"response_id\": \"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ## Статусы ресурсов Важно учесть, что при создании большинства ресурсов внутри платформы вам будет сразу возвращен ответ от сервера со статусом `200 OK` или `201 Created` и ID созданного ресурса в теле ответа, но при этом этот ресурс может быть ещё в *состоянии запуска*.  Для того чтобы понять, в каком состоянии сейчас находится ваш ресурс, мы добавили поле `status` в ответ на получение информации о ресурсе.  Список статусов будет отличаться в зависимости от типа ресурса. Увидеть поддерживаемый список статусов вы сможете в описании каждого конкретного ресурса.     ## Ограничение скорости запросов (Rate Limiting) Чтобы обеспечить стабильность для всех пользователей, Timeweb Cloud защищает API от всплесков входящего трафика, анализируя количество запросов c каждого аккаунта к каждой конечной точке.  Если ваше приложение отправляет более 20 запросов в секунду на одну конечную точку, то для этого запроса API может вернуть код состояния HTTP `429 Too Many Requests`.   ## Аутентификация Доступ к API осуществляется с помощью JWT-токена. Токенами можно управлять внутри панели управления Timeweb Cloud в разделе *API и Terraform*.  Токен необходимо передавать в заголовке каждого запроса в формате: ```   Authorization: Bearer $TIMEWEB_CLOUD_TOKEN ```  ## Формат примеров API Примеры в этой документации описаны с помощью `curl`, HTTP-клиента командной строки. На компьютерах `Linux` и `macOS` обычно по умолчанию установлен `curl`, и он доступен для загрузки на всех популярных платформах, включая `Windows`.  Каждый пример разделен на несколько строк символом `\\`, который совместим с `bash`. Типичный пример выглядит так: ```   curl -X PATCH      -H \"Content-Type: application/json\"      -H \"Authorization: Bearer $TIMEWEB_CLOUD_TOKEN\"      -d '{\"name\":\"Cute Corvus\",\"comment\":\"Development Server\"}'      \"https://api.timeweb.cloud/api/v1/dedicated/1051\" ``` - Параметр `-X` задает метод запроса. Для согласованности метод будет указан во всех примерах, даже если он явно не требуется для методов `GET`. - Строки `-H` задают требуемые HTTP-заголовки. - Примеры, для которых требуется объект JSON в теле запроса, передают требуемые данные через параметр `-d`.  Чтобы использовать приведенные примеры, не подставляя каждый раз в них свой токен, вы можете добавить токен один раз в переменные окружения в вашей консоли. Например, на `Linux` это можно сделать с помощью команды:  ``` TIMEWEB_CLOUD_TOKEN=\"token\" ```  После этого токен будет автоматически подставляться в ваши запросы.  Обратите внимание, что все значения в этой документации являются примерами. Не полагайтесь на IDы операционных систем, тарифов и т.д., используемые в примерах. Используйте соответствующую конечную точку для получения значений перед созданием ресурсов.   ## Версионирование API построено согласно принципам [семантического версионирования](https://semver.org/lang/ru). Это значит, что мы гарантируем обратную совместимость всех изменений в пределах одной мажорной версии.  Мажорная версия каждой конечной точки обозначается в пути запроса, например, запрос `/api/v1/servers` указывает, что этот метод имеет версию 1.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@timeweb.cloud
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field

from typing import Any, Dict, Optional

from timeweb_cloud_api.models.ai_gateway_batch import AiGatewayBatch
from timeweb_cloud_api.models.ai_gateway_batch_create_request import AiGatewayBatchCreateRequest
from timeweb_cloud_api.models.ai_gateway_batch_list import AiGatewayBatchList
from timeweb_cloud_api.models.ai_gateway_chat_completion import AiGatewayChatCompletion
from timeweb_cloud_api.models.ai_gateway_completion import AiGatewayCompletion
from timeweb_cloud_api.models.ai_gateway_embedding_list import AiGatewayEmbeddingList
from timeweb_cloud_api.models.ai_gateway_file import AiGatewayFile
from timeweb_cloud_api.models.ai_gateway_file_deleted import AiGatewayFileDeleted
from timeweb_cloud_api.models.ai_gateway_images_response import AiGatewayImagesResponse
from timeweb_cloud_api.models.ai_gateway_model_list import AiGatewayModelList
from timeweb_cloud_api.models.ai_gateway_response import AiGatewayResponse
from timeweb_cloud_api.models.ai_gateway_response_deleted import AiGatewayResponseDeleted
from timeweb_cloud_api.models.ai_gateway_transcription import AiGatewayTranscription

from timeweb_cloud_api.api_client import ApiClient
from timeweb_cloud_api.api_response import ApiResponse
from timeweb_cloud_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AIGatewayInferenceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def cancel_ai_gateway_batch(self, batch_id : Annotated[Any, Field(..., description="ID батча")], **kwargs) -> AiGatewayBatch:  # noqa: E501
        """Отмена батча  # noqa: E501

        Чтобы отменить батч, отправьте POST-запрос на `/v1/batches/{batch_id}/cancel`.  Батч переходит в статус `cancelling`, отмена выполняется асинхронно и может занять несколько минут; итоговый статус `cancelled` проверяйте через `GET /v1/batches/{batch_id}`. Пока отмена не завершилась, входной файл батча удалить нельзя.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_ai_gateway_batch(batch_id, async_req=True)
        >>> result = thread.get()

        :param batch_id: ID батча (required)
        :type batch_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayBatch
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the cancel_ai_gateway_batch_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.cancel_ai_gateway_batch_with_http_info(batch_id, **kwargs)  # noqa: E501

    @validate_arguments
    def cancel_ai_gateway_batch_with_http_info(self, batch_id : Annotated[Any, Field(..., description="ID батча")], **kwargs) -> ApiResponse:  # noqa: E501
        """Отмена батча  # noqa: E501

        Чтобы отменить батч, отправьте POST-запрос на `/v1/batches/{batch_id}/cancel`.  Батч переходит в статус `cancelling`, отмена выполняется асинхронно и может занять несколько минут; итоговый статус `cancelled` проверяйте через `GET /v1/batches/{batch_id}`. Пока отмена не завершилась, входной файл батча удалить нельзя.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_ai_gateway_batch_with_http_info(batch_id, async_req=True)
        >>> result = thread.get()

        :param batch_id: ID батча (required)
        :type batch_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayBatch, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'batch_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_ai_gateway_batch" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['batch_id']:
            _path_params['batch_id'] = _params['batch_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayBatch",
            '401': "AiGatewayError",
            '403': "AiGatewayError",
            '404': "AiGatewayError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/batches/{batch_id}/cancel', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def cancel_ai_gateway_response(self, response_id : Annotated[Any, Field(..., description="ID ответа Responses API")], **kwargs) -> AiGatewayResponse:  # noqa: E501
        """Отмена фонового ответа (Responses API)  # noqa: E501

        Чтобы отменить ответ, запущенный с `\"background\": true`, отправьте POST-запрос на `/v1/responses/{response_id}/cancel`.  Отмена может завершиться не сразу: итоговый статус `cancelled` проверяйте через `GET /v1/responses/{response_id}`. Ответ, созданный без `background`, отменить нельзя — вернётся ошибка 400. Неизвестный `response_id` также возвращает 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_ai_gateway_response(response_id, async_req=True)
        >>> result = thread.get()

        :param response_id: ID ответа Responses API (required)
        :type response_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the cancel_ai_gateway_response_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.cancel_ai_gateway_response_with_http_info(response_id, **kwargs)  # noqa: E501

    @validate_arguments
    def cancel_ai_gateway_response_with_http_info(self, response_id : Annotated[Any, Field(..., description="ID ответа Responses API")], **kwargs) -> ApiResponse:  # noqa: E501
        """Отмена фонового ответа (Responses API)  # noqa: E501

        Чтобы отменить ответ, запущенный с `\"background\": true`, отправьте POST-запрос на `/v1/responses/{response_id}/cancel`.  Отмена может завершиться не сразу: итоговый статус `cancelled` проверяйте через `GET /v1/responses/{response_id}`. Ответ, созданный без `background`, отменить нельзя — вернётся ошибка 400. Неизвестный `response_id` также возвращает 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.cancel_ai_gateway_response_with_http_info(response_id, async_req=True)
        >>> result = thread.get()

        :param response_id: ID ответа Responses API (required)
        :type response_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'response_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_ai_gateway_response" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['response_id']:
            _path_params['response_id'] = _params['response_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayResponse",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '403': "AiGatewayError",
            '500': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/responses/{response_id}/cancel', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def create_ai_gateway_batch(self, ai_gateway_batch_create_request : AiGatewayBatchCreateRequest, **kwargs) -> AiGatewayBatch:  # noqa: E501
        """Создание батча  # noqa: E501

        Чтобы запустить асинхронную обработку входного файла, загруженного с `purpose=batch`, отправьте POST-запрос на `/v1/batches`.  При создании батча его оценочная стоимость резервируется на балансе, фактическая стоимость списывается по цене Batch API после выполнения. Модели, эндпоинты и коэффициенты цены Batch API — в поле `batch` каталога моделей (`GET https://api.timeweb.cloud/api/v3/cloud-ai/models`). Batch API доступен только для ключей AI Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_batch(ai_gateway_batch_create_request, async_req=True)
        >>> result = thread.get()

        :param ai_gateway_batch_create_request: (required)
        :type ai_gateway_batch_create_request: AiGatewayBatchCreateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayBatch
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_gateway_batch_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_gateway_batch_with_http_info(ai_gateway_batch_create_request, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_gateway_batch_with_http_info(self, ai_gateway_batch_create_request : AiGatewayBatchCreateRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Создание батча  # noqa: E501

        Чтобы запустить асинхронную обработку входного файла, загруженного с `purpose=batch`, отправьте POST-запрос на `/v1/batches`.  При создании батча его оценочная стоимость резервируется на балансе, фактическая стоимость списывается по цене Batch API после выполнения. Модели, эндпоинты и коэффициенты цены Batch API — в поле `batch` каталога моделей (`GET https://api.timeweb.cloud/api/v3/cloud-ai/models`). Batch API доступен только для ключей AI Gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_batch_with_http_info(ai_gateway_batch_create_request, async_req=True)
        >>> result = thread.get()

        :param ai_gateway_batch_create_request: (required)
        :type ai_gateway_batch_create_request: AiGatewayBatchCreateRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayBatch, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'ai_gateway_batch_create_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ai_gateway_batch" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['ai_gateway_batch_create_request'] is not None:
            _body_params = _params['ai_gateway_batch_create_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayBatch",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '402': "AiGatewayError",
            '403': "AiGatewayError",
            '404': "AiGatewayError",
            '405': "AiGatewayError",
            '410': "AiGatewayError",
            '422': "AiGatewayError",
            '429': "AiGatewayError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/batches', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def create_ai_gateway_chat_completion(self, request_body : Optional[Dict[str, Any]], **kwargs) -> AiGatewayChatCompletion:  # noqa: E501
        """Генерация ответа в диалоге (Chat Completions)  # noqa: E501

        Чтобы получить следующий ответ модели в диалоге, отправьте POST-запрос на `/v1/chat/completions`.  Запрос не хранит состояние: передавайте всю историю диалога в `messages`. Поддерживаются вызов функций (`tools`), структурированный ответ (`response_format`) и изображения во входных сообщениях (для моделей с поддержкой зрения).  С `\"stream\": true` ответ приходит потоком Server-Sent Events: события `chat.completion.chunk` в строках `data:`, в конце — `data: [DONE]`. С `\"stream_options\": {\"include_usage\": true}` последний чанк содержит расход токенов.  Если у ключа настроены запасные модели и запрошенная модель не ответила, запрос повторяется на запасных. Заголовок ответа `x-timeweb-attempted-fallbacks` показывает, сколько запасных моделей было опробовано.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_chat_completion(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayChatCompletion
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_gateway_chat_completion_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_gateway_chat_completion_with_http_info(request_body, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_gateway_chat_completion_with_http_info(self, request_body : Optional[Dict[str, Any]], **kwargs) -> ApiResponse:  # noqa: E501
        """Генерация ответа в диалоге (Chat Completions)  # noqa: E501

        Чтобы получить следующий ответ модели в диалоге, отправьте POST-запрос на `/v1/chat/completions`.  Запрос не хранит состояние: передавайте всю историю диалога в `messages`. Поддерживаются вызов функций (`tools`), структурированный ответ (`response_format`) и изображения во входных сообщениях (для моделей с поддержкой зрения).  С `\"stream\": true` ответ приходит потоком Server-Sent Events: события `chat.completion.chunk` в строках `data:`, в конце — `data: [DONE]`. С `\"stream_options\": {\"include_usage\": true}` последний чанк содержит расход токенов.  Если у ключа настроены запасные модели и запрошенная модель не ответила, запрос повторяется на запасных. Заголовок ответа `x-timeweb-attempted-fallbacks` показывает, сколько запасных моделей было опробовано.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_chat_completion_with_http_info(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayChatCompletion, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'request_body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ai_gateway_chat_completion" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['request_body'] is not None:
            _body_params = _params['request_body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/event-stream'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayChatCompletion",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '402': "AiGatewayError",
            '403': "AiGatewayError",
            '404': "AiGatewayError",
            '410': "AiGatewayError",
            '422': "AiGatewayError",
            '429': "AiGatewayError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/chat/completions', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def create_ai_gateway_completion(self, request_body : Optional[Dict[str, Any]], **kwargs) -> AiGatewayCompletion:  # noqa: E501
        """Продолжение текста (Completions)  # noqa: E501

        Чтобы получить продолжение текста `prompt`, отправьте POST-запрос на `/v1/completions`.  Это устаревший API OpenAI — для новых интеграций используйте `/v1/chat/completions`. С `\"stream\": true` ответ приходит потоком Server-Sent Events и заканчивается `data: [DONE]`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_completion(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayCompletion
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_gateway_completion_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_gateway_completion_with_http_info(request_body, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_gateway_completion_with_http_info(self, request_body : Optional[Dict[str, Any]], **kwargs) -> ApiResponse:  # noqa: E501
        """Продолжение текста (Completions)  # noqa: E501

        Чтобы получить продолжение текста `prompt`, отправьте POST-запрос на `/v1/completions`.  Это устаревший API OpenAI — для новых интеграций используйте `/v1/chat/completions`. С `\"stream\": true` ответ приходит потоком Server-Sent Events и заканчивается `data: [DONE]`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_completion_with_http_info(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayCompletion, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'request_body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ai_gateway_completion" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['request_body'] is not None:
            _body_params = _params['request_body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/event-stream'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayCompletion",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '402': "AiGatewayError",
            '403': "AiGatewayError",
            '404': "AiGatewayError",
            '422': "AiGatewayError",
            '429': "AiGatewayError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/completions', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def create_ai_gateway_embedding(self, request_body : Optional[Dict[str, Any]], **kwargs) -> AiGatewayEmbeddingList:  # noqa: E501
        """Получение эмбеддингов  # noqa: E501

        Чтобы получить векторные представления текстов, отправьте POST-запрос на `/v1/embeddings`.  Используйте модель с `mode: embedding` из `GET /v1/models`. Эмбеддинги возвращаются в порядке входных текстов.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_embedding(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayEmbeddingList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_gateway_embedding_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_gateway_embedding_with_http_info(request_body, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_gateway_embedding_with_http_info(self, request_body : Optional[Dict[str, Any]], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение эмбеддингов  # noqa: E501

        Чтобы получить векторные представления текстов, отправьте POST-запрос на `/v1/embeddings`.  Используйте модель с `mode: embedding` из `GET /v1/models`. Эмбеддинги возвращаются в порядке входных текстов.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_embedding_with_http_info(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayEmbeddingList, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'request_body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ai_gateway_embedding" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['request_body'] is not None:
            _body_params = _params['request_body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayEmbeddingList",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '402': "AiGatewayError",
            '403': "AiGatewayError",
            '404': "AiGatewayError",
            '410': "AiGatewayError",
            '422': "AiGatewayError",
            '429': "AiGatewayError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/embeddings', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def create_ai_gateway_image(self, request_body : Optional[Dict[str, Any]], **kwargs) -> AiGatewayImagesResponse:  # noqa: E501
        """Генерация изображений  # noqa: E501

        Чтобы сгенерировать изображения по текстовому описанию, отправьте POST-запрос на `/v1/images/generations`.  Используйте модель с `mode: image_generation` из `GET /v1/models`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_image(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayImagesResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_gateway_image_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_gateway_image_with_http_info(request_body, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_gateway_image_with_http_info(self, request_body : Optional[Dict[str, Any]], **kwargs) -> ApiResponse:  # noqa: E501
        """Генерация изображений  # noqa: E501

        Чтобы сгенерировать изображения по текстовому описанию, отправьте POST-запрос на `/v1/images/generations`.  Используйте модель с `mode: image_generation` из `GET /v1/models`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_image_with_http_info(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayImagesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'request_body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ai_gateway_image" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['request_body'] is not None:
            _body_params = _params['request_body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayImagesResponse",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '402': "AiGatewayError",
            '403': "AiGatewayError",
            '404': "AiGatewayError",
            '410': "AiGatewayError",
            '422': "AiGatewayError",
            '429': "AiGatewayError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/images/generations', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def create_ai_gateway_image_edit(self, model : Annotated[Optional[Any], Field(..., description="ID модели: GPT Image (`openai/gpt-image-*`) или FLUX.2 (`black_forest_labs/flux-2-*`)")], image : Annotated[Optional[Any], Field(..., description="Исходное изображение или несколько файлов в поле `image[]`")], prompt : Annotated[Optional[Any], Field(..., description="Что изменить")], mask : Annotated[Optional[Any], Field(description="Маска: прозрачные области будут изменены")] = None, n : Annotated[Optional[Any], Field(description="Количество изображений")] = None, size : Annotated[Optional[Any], Field(description="Размер изображения")] = None, quality : Annotated[Optional[Any], Field(description="Качество изображения")] = None, **kwargs) -> AiGatewayImagesResponse:  # noqa: E501
        """Редактирование изображений  # noqa: E501

        Чтобы изменить или дополнить изображения по описанию, отправьте POST-запрос на `/v1/images/edits` (multipart/form-data).  Доступно для моделей GPT Image (`openai/gpt-image-*`) и FLUX.2 (`black_forest_labs/flux-2-*`). Для других моделей, в том числе неизвестных, возвращается ошибка 405.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_image_edit(model, image, prompt, mask, n, size, quality, async_req=True)
        >>> result = thread.get()

        :param model: ID модели: GPT Image (`openai/gpt-image-*`) или FLUX.2 (`black_forest_labs/flux-2-*`) (required)
        :type model: object
        :param image: Исходное изображение или несколько файлов в поле `image[]` (required)
        :type image: object
        :param prompt: Что изменить (required)
        :type prompt: object
        :param mask: Маска: прозрачные области будут изменены
        :type mask: object
        :param n: Количество изображений
        :type n: object
        :param size: Размер изображения
        :type size: object
        :param quality: Качество изображения
        :type quality: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayImagesResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_gateway_image_edit_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_gateway_image_edit_with_http_info(model, image, prompt, mask, n, size, quality, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_gateway_image_edit_with_http_info(self, model : Annotated[Optional[Any], Field(..., description="ID модели: GPT Image (`openai/gpt-image-*`) или FLUX.2 (`black_forest_labs/flux-2-*`)")], image : Annotated[Optional[Any], Field(..., description="Исходное изображение или несколько файлов в поле `image[]`")], prompt : Annotated[Optional[Any], Field(..., description="Что изменить")], mask : Annotated[Optional[Any], Field(description="Маска: прозрачные области будут изменены")] = None, n : Annotated[Optional[Any], Field(description="Количество изображений")] = None, size : Annotated[Optional[Any], Field(description="Размер изображения")] = None, quality : Annotated[Optional[Any], Field(description="Качество изображения")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Редактирование изображений  # noqa: E501

        Чтобы изменить или дополнить изображения по описанию, отправьте POST-запрос на `/v1/images/edits` (multipart/form-data).  Доступно для моделей GPT Image (`openai/gpt-image-*`) и FLUX.2 (`black_forest_labs/flux-2-*`). Для других моделей, в том числе неизвестных, возвращается ошибка 405.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_image_edit_with_http_info(model, image, prompt, mask, n, size, quality, async_req=True)
        >>> result = thread.get()

        :param model: ID модели: GPT Image (`openai/gpt-image-*`) или FLUX.2 (`black_forest_labs/flux-2-*`) (required)
        :type model: object
        :param image: Исходное изображение или несколько файлов в поле `image[]` (required)
        :type image: object
        :param prompt: Что изменить (required)
        :type prompt: object
        :param mask: Маска: прозрачные области будут изменены
        :type mask: object
        :param n: Количество изображений
        :type n: object
        :param size: Размер изображения
        :type size: object
        :param quality: Качество изображения
        :type quality: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayImagesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'model',
            'image',
            'prompt',
            'mask',
            'n',
            'size',
            'quality'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ai_gateway_image_edit" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['model']:
            _form_params.append(('model', _params['model']))

        if _params['image']:
            _form_params.append(('image', _params['image']))

        if _params['mask']:
            _form_params.append(('mask', _params['mask']))

        if _params['prompt']:
            _form_params.append(('prompt', _params['prompt']))

        if _params['n']:
            _form_params.append(('n', _params['n']))

        if _params['size']:
            _form_params.append(('size', _params['size']))

        if _params['quality']:
            _form_params.append(('quality', _params['quality']))

        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayImagesResponse",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '402': "AiGatewayError",
            '403': "AiGatewayError",
            '405': "AiGatewayError",
            '410': "AiGatewayError",
            '422': "AiGatewayError",
            '429': "AiGatewayError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/images/edits', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def create_ai_gateway_response(self, request_body : Optional[Dict[str, Any]], **kwargs) -> AiGatewayResponse:  # noqa: E501
        """Создание ответа (Responses API)  # noqa: E501

        Чтобы получить ответ модели через OpenAI Responses API, отправьте POST-запрос на `/v1/responses`.  Диалог можно продолжить по `previous_response_id`, долгие запросы — выполнить в фоне с `\"background\": true` и получать результат через `GET /v1/responses/{response_id}`.  С `\"stream\": true` ответ приходит потоком типизированных событий Server-Sent Events (`response.created`, `response.output_text.delta`, `response.completed` и др.), в конце потока — `data: [DONE]`.  Если у ключа настроены запасные модели и запрошенная модель не ответила, запрос повторяется на запасных (заголовок `x-timeweb-attempted-fallbacks`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_response(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_gateway_response_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_gateway_response_with_http_info(request_body, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_gateway_response_with_http_info(self, request_body : Optional[Dict[str, Any]], **kwargs) -> ApiResponse:  # noqa: E501
        """Создание ответа (Responses API)  # noqa: E501

        Чтобы получить ответ модели через OpenAI Responses API, отправьте POST-запрос на `/v1/responses`.  Диалог можно продолжить по `previous_response_id`, долгие запросы — выполнить в фоне с `\"background\": true` и получать результат через `GET /v1/responses/{response_id}`.  С `\"stream\": true` ответ приходит потоком типизированных событий Server-Sent Events (`response.created`, `response.output_text.delta`, `response.completed` и др.), в конце потока — `data: [DONE]`.  Если у ключа настроены запасные модели и запрошенная модель не ответила, запрос повторяется на запасных (заголовок `x-timeweb-attempted-fallbacks`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_response_with_http_info(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'request_body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ai_gateway_response" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['request_body'] is not None:
            _body_params = _params['request_body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/event-stream'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayResponse",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '402': "AiGatewayError",
            '403': "AiGatewayError",
            '404': "AiGatewayError",
            '410': "AiGatewayError",
            '422': "AiGatewayError",
            '429': "AiGatewayError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/responses', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def create_ai_gateway_speech(self, request_body : Optional[Dict[str, Any]], **kwargs) -> object:  # noqa: E501
        """Синтез речи  # noqa: E501

        Чтобы озвучить текст, отправьте POST-запрос на `/v1/audio/speech`.  Используйте модель с `mode: audio_speech` из `GET /v1/models`. Ответ — аудиофайл в формате `response_format` (по умолчанию `mp3`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_speech(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_gateway_speech_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_gateway_speech_with_http_info(request_body, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_gateway_speech_with_http_info(self, request_body : Optional[Dict[str, Any]], **kwargs) -> ApiResponse:  # noqa: E501
        """Синтез речи  # noqa: E501

        Чтобы озвучить текст, отправьте POST-запрос на `/v1/audio/speech`.  Используйте модель с `mode: audio_speech` из `GET /v1/models`. Ответ — аудиофайл в формате `response_format` (по умолчанию `mp3`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_speech_with_http_info(request_body, async_req=True)
        >>> result = thread.get()

        :param request_body: (required)
        :type request_body: Dict[str, object]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'request_body'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ai_gateway_speech" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['request_body'] is not None:
            _body_params = _params['request_body']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['audio/mpeg', 'audio/wav', 'application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "object",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '402': "AiGatewayError",
            '403': "AiGatewayError",
            '410': "AiGatewayError",
            '422': "AiGatewayError",
            '429': "AiGatewayError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/audio/speech', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def create_ai_gateway_transcription(self, file : Annotated[Optional[Any], Field(..., description="Аудиофайл")], model : Annotated[Optional[Any], Field(..., description="ID модели распознавания речи (`*-transcribe`)")], language : Annotated[Optional[Any], Field(description="Язык аудио в формате ISO-639-1")] = None, prompt : Annotated[Optional[Any], Field(description="Подсказка для распознавания: термины, имена, стиль")] = None, response_format : Annotated[Optional[Any], Field(description="Формат ответа")] = None, temperature : Annotated[Optional[Any], Field(description="Температура выборки")] = None, **kwargs) -> AiGatewayTranscription:  # noqa: E501
        """Распознавание речи  # noqa: E501

        Чтобы распознать речь в аудиофайле, отправьте POST-запрос на `/v1/audio/transcriptions` (multipart/form-data).  Доступно для моделей распознавания речи `*-transcribe` (например, `openai/gpt-4o-mini-transcribe`). Для других моделей, в том числе неизвестных, возвращается ошибка 405. Ответ возвращается в JSON.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_transcription(file, model, language, prompt, response_format, temperature, async_req=True)
        >>> result = thread.get()

        :param file: Аудиофайл (required)
        :type file: object
        :param model: ID модели распознавания речи (`*-transcribe`) (required)
        :type model: object
        :param language: Язык аудио в формате ISO-639-1
        :type language: object
        :param prompt: Подсказка для распознавания: термины, имена, стиль
        :type prompt: object
        :param response_format: Формат ответа
        :type response_format: object
        :param temperature: Температура выборки
        :type temperature: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayTranscription
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_gateway_transcription_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_gateway_transcription_with_http_info(file, model, language, prompt, response_format, temperature, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_gateway_transcription_with_http_info(self, file : Annotated[Optional[Any], Field(..., description="Аудиофайл")], model : Annotated[Optional[Any], Field(..., description="ID модели распознавания речи (`*-transcribe`)")], language : Annotated[Optional[Any], Field(description="Язык аудио в формате ISO-639-1")] = None, prompt : Annotated[Optional[Any], Field(description="Подсказка для распознавания: термины, имена, стиль")] = None, response_format : Annotated[Optional[Any], Field(description="Формат ответа")] = None, temperature : Annotated[Optional[Any], Field(description="Температура выборки")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Распознавание речи  # noqa: E501

        Чтобы распознать речь в аудиофайле, отправьте POST-запрос на `/v1/audio/transcriptions` (multipart/form-data).  Доступно для моделей распознавания речи `*-transcribe` (например, `openai/gpt-4o-mini-transcribe`). Для других моделей, в том числе неизвестных, возвращается ошибка 405. Ответ возвращается в JSON.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_gateway_transcription_with_http_info(file, model, language, prompt, response_format, temperature, async_req=True)
        >>> result = thread.get()

        :param file: Аудиофайл (required)
        :type file: object
        :param model: ID модели распознавания речи (`*-transcribe`) (required)
        :type model: object
        :param language: Язык аудио в формате ISO-639-1
        :type language: object
        :param prompt: Подсказка для распознавания: термины, имена, стиль
        :type prompt: object
        :param response_format: Формат ответа
        :type response_format: object
        :param temperature: Температура выборки
        :type temperature: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayTranscription, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'file',
            'model',
            'language',
            'prompt',
            'response_format',
            'temperature'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_ai_gateway_transcription" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['file']:
            _form_params.append(('file', _params['file']))

        if _params['model']:
            _form_params.append(('model', _params['model']))

        if _params['language']:
            _form_params.append(('language', _params['language']))

        if _params['prompt']:
            _form_params.append(('prompt', _params['prompt']))

        if _params['response_format']:
            _form_params.append(('response_format', _params['response_format']))

        if _params['temperature']:
            _form_params.append(('temperature', _params['temperature']))

        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayTranscription",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '402': "AiGatewayError",
            '403': "AiGatewayError",
            '405': "AiGatewayError",
            '410': "AiGatewayError",
            '422': "AiGatewayError",
            '429': "AiGatewayError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/audio/transcriptions', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_ai_gateway_file(self, file_id : Annotated[Any, Field(..., description="ID файла")], **kwargs) -> AiGatewayFileDeleted:  # noqa: E501
        """Удаление файла  # noqa: E501

        Чтобы удалить файл, отправьте DELETE-запрос на `/v1/files/{file_id}`.  Входной файл батча, который ещё выполняется или отменяется, и результаты батча, расход которого ещё не списан, удалить нельзя — вернётся ошибка 409.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_ai_gateway_file(file_id, async_req=True)
        >>> result = thread.get()

        :param file_id: ID файла (required)
        :type file_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayFileDeleted
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_ai_gateway_file_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_ai_gateway_file_with_http_info(file_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_ai_gateway_file_with_http_info(self, file_id : Annotated[Any, Field(..., description="ID файла")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление файла  # noqa: E501

        Чтобы удалить файл, отправьте DELETE-запрос на `/v1/files/{file_id}`.  Входной файл батча, который ещё выполняется или отменяется, и результаты батча, расход которого ещё не списан, удалить нельзя — вернётся ошибка 409.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_ai_gateway_file_with_http_info(file_id, async_req=True)
        >>> result = thread.get()

        :param file_id: ID файла (required)
        :type file_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayFileDeleted, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'file_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_ai_gateway_file" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['file_id']:
            _path_params['file_id'] = _params['file_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayFileDeleted",
            '401': "AiGatewayError",
            '403': "AiGatewayError",
            '404': "AiGatewayError",
            '409': "AiGatewayError",
            '500': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/files/{file_id}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_ai_gateway_response(self, response_id : Annotated[Any, Field(..., description="ID ответа Responses API")], **kwargs) -> AiGatewayResponseDeleted:  # noqa: E501
        """Удаление ответа (Responses API)  # noqa: E501

        Чтобы удалить сохранённый ответ, отправьте DELETE-запрос на `/v1/responses/{response_id}`.  Неизвестный или уже удалённый `response_id` возвращает ошибку 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_ai_gateway_response(response_id, async_req=True)
        >>> result = thread.get()

        :param response_id: ID ответа Responses API (required)
        :type response_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayResponseDeleted
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_ai_gateway_response_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_ai_gateway_response_with_http_info(response_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_ai_gateway_response_with_http_info(self, response_id : Annotated[Any, Field(..., description="ID ответа Responses API")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление ответа (Responses API)  # noqa: E501

        Чтобы удалить сохранённый ответ, отправьте DELETE-запрос на `/v1/responses/{response_id}`.  Неизвестный или уже удалённый `response_id` возвращает ошибку 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_ai_gateway_response_with_http_info(response_id, async_req=True)
        >>> result = thread.get()

        :param response_id: ID ответа Responses API (required)
        :type response_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayResponseDeleted, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'response_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_ai_gateway_response" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['response_id']:
            _path_params['response_id'] = _params['response_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayResponseDeleted",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '403': "AiGatewayError",
            '500': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/responses/{response_id}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def download_ai_gateway_file_content(self, file_id : Annotated[Any, Field(..., description="ID файла")], **kwargs) -> object:  # noqa: E501
        """Скачивание файла  # noqa: E501

        Чтобы скачать содержимое файла — например, результаты выполненного батча (`output_file_id`), — отправьте GET-запрос на `/v1/files/{file_id}/content`.  Перед скачиванием результатов получите батч через `GET /v1/batches/{batch_id}` и убедитесь, что он в статусе `completed`. Файлы с `purpose=user_data` скачать нельзя — вернётся ошибка 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_ai_gateway_file_content(file_id, async_req=True)
        >>> result = thread.get()

        :param file_id: ID файла (required)
        :type file_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: object
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the download_ai_gateway_file_content_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.download_ai_gateway_file_content_with_http_info(file_id, **kwargs)  # noqa: E501

    @validate_arguments
    def download_ai_gateway_file_content_with_http_info(self, file_id : Annotated[Any, Field(..., description="ID файла")], **kwargs) -> ApiResponse:  # noqa: E501
        """Скачивание файла  # noqa: E501

        Чтобы скачать содержимое файла — например, результаты выполненного батча (`output_file_id`), — отправьте GET-запрос на `/v1/files/{file_id}/content`.  Перед скачиванием результатов получите батч через `GET /v1/batches/{batch_id}` и убедитесь, что он в статусе `completed`. Файлы с `purpose=user_data` скачать нельзя — вернётся ошибка 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_ai_gateway_file_content_with_http_info(file_id, async_req=True)
        >>> result = thread.get()

        :param file_id: ID файла (required)
        :type file_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(object, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'file_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_ai_gateway_file_content" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['file_id']:
            _path_params['file_id'] = _params['file_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream', 'application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "object",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '403': "AiGatewayError",
            '404': "AiGatewayError",
            '500': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/files/{file_id}/content', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_ai_gateway_batch(self, batch_id : Annotated[Any, Field(..., description="ID батча")], **kwargs) -> AiGatewayBatch:  # noqa: E501
        """Получение батча  # noqa: E501

        Чтобы получить статус батча, отправьте GET-запрос на `/v1/batches/{batch_id}`.  Когда статус станет `completed`, скачайте результаты по `output_file_id` через `GET /v1/files/{file_id}/content`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_gateway_batch(batch_id, async_req=True)
        >>> result = thread.get()

        :param batch_id: ID батча (required)
        :type batch_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayBatch
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_gateway_batch_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_gateway_batch_with_http_info(batch_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_gateway_batch_with_http_info(self, batch_id : Annotated[Any, Field(..., description="ID батча")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение батча  # noqa: E501

        Чтобы получить статус батча, отправьте GET-запрос на `/v1/batches/{batch_id}`.  Когда статус станет `completed`, скачайте результаты по `output_file_id` через `GET /v1/files/{file_id}/content`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_gateway_batch_with_http_info(batch_id, async_req=True)
        >>> result = thread.get()

        :param batch_id: ID батча (required)
        :type batch_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayBatch, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'batch_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ai_gateway_batch" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['batch_id']:
            _path_params['batch_id'] = _params['batch_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayBatch",
            '401': "AiGatewayError",
            '403': "AiGatewayError",
            '404': "AiGatewayError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/batches/{batch_id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_ai_gateway_batches(self, limit : Annotated[Optional[Any], Field(description="Количество батчей на странице")] = None, after : Annotated[Optional[Any], Field(description="Вернуть батчи после батча с этим ID (значение `last_id` предыдущей страницы)")] = None, **kwargs) -> AiGatewayBatchList:  # noqa: E501
        """Получение списка батчей  # noqa: E501

        Чтобы получить список батчей, отправьте GET-запрос на `/v1/batches`.  Для следующей страницы передайте в `after` значение `last_id`, пока `has_more` равно `true`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_gateway_batches(limit, after, async_req=True)
        >>> result = thread.get()

        :param limit: Количество батчей на странице
        :type limit: object
        :param after: Вернуть батчи после батча с этим ID (значение `last_id` предыдущей страницы)
        :type after: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayBatchList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_gateway_batches_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_gateway_batches_with_http_info(limit, after, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_gateway_batches_with_http_info(self, limit : Annotated[Optional[Any], Field(description="Количество батчей на странице")] = None, after : Annotated[Optional[Any], Field(description="Вернуть батчи после батча с этим ID (значение `last_id` предыдущей страницы)")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка батчей  # noqa: E501

        Чтобы получить список батчей, отправьте GET-запрос на `/v1/batches`.  Для следующей страницы передайте в `after` значение `last_id`, пока `has_more` равно `true`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_gateway_batches_with_http_info(limit, after, async_req=True)
        >>> result = thread.get()

        :param limit: Количество батчей на странице
        :type limit: object
        :param after: Вернуть батчи после батча с этим ID (значение `last_id` предыдущей страницы)
        :type after: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayBatchList, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'limit',
            'after'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ai_gateway_batches" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('after') is not None:  # noqa: E501
            _query_params.append(('after', _params['after']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayBatchList",
            '401': "AiGatewayError",
            '403': "AiGatewayError",
            '422': "AiGatewayValidationError",
            '500': "AiGatewayError",
            '503': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/batches', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_ai_gateway_file(self, file_id : Annotated[Any, Field(..., description="ID файла")], **kwargs) -> AiGatewayFile:  # noqa: E501
        """Получение информации о файле  # noqa: E501

        Чтобы получить информацию о загруженном файле, отправьте GET-запрос на `/v1/files/{file_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_gateway_file(file_id, async_req=True)
        >>> result = thread.get()

        :param file_id: ID файла (required)
        :type file_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayFile
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_gateway_file_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_gateway_file_with_http_info(file_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_gateway_file_with_http_info(self, file_id : Annotated[Any, Field(..., description="ID файла")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение информации о файле  # noqa: E501

        Чтобы получить информацию о загруженном файле, отправьте GET-запрос на `/v1/files/{file_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_gateway_file_with_http_info(file_id, async_req=True)
        >>> result = thread.get()

        :param file_id: ID файла (required)
        :type file_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayFile, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'file_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ai_gateway_file" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['file_id']:
            _path_params['file_id'] = _params['file_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayFile",
            '401': "AiGatewayError",
            '403': "AiGatewayError",
            '404': "AiGatewayError",
            '500': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/files/{file_id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_ai_gateway_models(self, **kwargs) -> AiGatewayModelList:  # noqa: E501
        """Получение списка моделей AI Gateway  # noqa: E501

        Чтобы получить список моделей, доступных ключу, отправьте GET-запрос на `/v1/models`.  Поле `mode` показывает назначение модели. В списке могут оставаться модели, снятые с обслуживания: запросы к ним возвращают ошибку 410. Актуальный статус, цены и возможности моделей — в каталоге `GET https://api.timeweb.cloud/api/v3/cloud-ai/models` (снятые модели — `is_stopped: true`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_gateway_models(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayModelList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_gateway_models_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_gateway_models_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_gateway_models_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка моделей AI Gateway  # noqa: E501

        Чтобы получить список моделей, доступных ключу, отправьте GET-запрос на `/v1/models`.  Поле `mode` показывает назначение модели. В списке могут оставаться модели, снятые с обслуживания: запросы к ним возвращают ошибку 410. Актуальный статус, цены и возможности моделей — в каталоге `GET https://api.timeweb.cloud/api/v3/cloud-ai/models` (снятые модели — `is_stopped: true`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_gateway_models_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayModelList, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ai_gateway_models" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayModelList",
            '401': "AiGatewayError",
            '403': "AiGatewayError",
            '500': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/models', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_ai_gateway_response(self, response_id : Annotated[Any, Field(..., description="ID ответа Responses API")], **kwargs) -> AiGatewayResponse:  # noqa: E501
        """Получение ответа (Responses API)  # noqa: E501

        Чтобы получить сохранённый ответ — например, дождаться завершения фонового ответа, — отправьте GET-запрос на `/v1/responses/{response_id}`.  Неизвестный или удалённый `response_id` возвращает ошибку 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_gateway_response(response_id, async_req=True)
        >>> result = thread.get()

        :param response_id: ID ответа Responses API (required)
        :type response_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_gateway_response_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_gateway_response_with_http_info(response_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_gateway_response_with_http_info(self, response_id : Annotated[Any, Field(..., description="ID ответа Responses API")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение ответа (Responses API)  # noqa: E501

        Чтобы получить сохранённый ответ — например, дождаться завершения фонового ответа, — отправьте GET-запрос на `/v1/responses/{response_id}`.  Неизвестный или удалённый `response_id` возвращает ошибку 400.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_gateway_response_with_http_info(response_id, async_req=True)
        >>> result = thread.get()

        :param response_id: ID ответа Responses API (required)
        :type response_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'response_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ai_gateway_response" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['response_id']:
            _path_params['response_id'] = _params['response_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayResponse",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '403': "AiGatewayError",
            '500': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/responses/{response_id}', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def upload_ai_gateway_file(self, file : Annotated[Optional[Any], Field(..., description="Файл. Для Batch API — JSONL, по одному запросу в строке")], purpose : Annotated[Optional[Any], Field(..., description="Назначение: `batch` — входной файл Batch API, `user_data` и другие назначения OpenAI — файлы для передачи модели")], model : Annotated[Optional[Any], Field(description="Модель, для которой загружается файл. Обязателен, если не передан `target_model_names`")] = None, target_model_names : Annotated[Optional[Any], Field(description="Список моделей через запятую — вместо `model`")] = None, **kwargs) -> AiGatewayFile:  # noqa: E501
        """Загрузка файла  # noqa: E501

        Чтобы загрузить файл, отправьте POST-запрос на `/v1/files` (multipart/form-data).  Файл загружается для конкретной модели, поэтому `model` (или `target_model_names`) обязателен: - `purpose=batch` — входной JSONL-файл Batch API. Все строки должны обращаться к одной модели — той, что указана в `model`, иначе вернётся 400. Размер — до 50 МБ и до 50 000 запросов; - `user_data` и другие назначения OpenAI — файлы, на которые можно сослаться по `file_id` в сообщениях.  Загрузка бесплатна. Сохраняйте `id` загруженных файлов: получить список файлов нельзя (`GET /v1/files` возвращает 405).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_ai_gateway_file(file, purpose, model, target_model_names, async_req=True)
        >>> result = thread.get()

        :param file: Файл. Для Batch API — JSONL, по одному запросу в строке (required)
        :type file: object
        :param purpose: Назначение: `batch` — входной файл Batch API, `user_data` и другие назначения OpenAI — файлы для передачи модели (required)
        :type purpose: object
        :param model: Модель, для которой загружается файл. Обязателен, если не передан `target_model_names`
        :type model: object
        :param target_model_names: Список моделей через запятую — вместо `model`
        :type target_model_names: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AiGatewayFile
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the upload_ai_gateway_file_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.upload_ai_gateway_file_with_http_info(file, purpose, model, target_model_names, **kwargs)  # noqa: E501

    @validate_arguments
    def upload_ai_gateway_file_with_http_info(self, file : Annotated[Optional[Any], Field(..., description="Файл. Для Batch API — JSONL, по одному запросу в строке")], purpose : Annotated[Optional[Any], Field(..., description="Назначение: `batch` — входной файл Batch API, `user_data` и другие назначения OpenAI — файлы для передачи модели")], model : Annotated[Optional[Any], Field(description="Модель, для которой загружается файл. Обязателен, если не передан `target_model_names`")] = None, target_model_names : Annotated[Optional[Any], Field(description="Список моделей через запятую — вместо `model`")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Загрузка файла  # noqa: E501

        Чтобы загрузить файл, отправьте POST-запрос на `/v1/files` (multipart/form-data).  Файл загружается для конкретной модели, поэтому `model` (или `target_model_names`) обязателен: - `purpose=batch` — входной JSONL-файл Batch API. Все строки должны обращаться к одной модели — той, что указана в `model`, иначе вернётся 400. Размер — до 50 МБ и до 50 000 запросов; - `user_data` и другие назначения OpenAI — файлы, на которые можно сослаться по `file_id` в сообщениях.  Загрузка бесплатна. Сохраняйте `id` загруженных файлов: получить список файлов нельзя (`GET /v1/files` возвращает 405).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_ai_gateway_file_with_http_info(file, purpose, model, target_model_names, async_req=True)
        >>> result = thread.get()

        :param file: Файл. Для Batch API — JSONL, по одному запросу в строке (required)
        :type file: object
        :param purpose: Назначение: `batch` — входной файл Batch API, `user_data` и другие назначения OpenAI — файлы для передачи модели (required)
        :type purpose: object
        :param model: Модель, для которой загружается файл. Обязателен, если не передан `target_model_names`
        :type model: object
        :param target_model_names: Список моделей через запятую — вместо `model`
        :type target_model_names: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AiGatewayFile, status_code(int), headers(HTTPHeaderDict))
        """

        _hosts = [
            'https://api.timeweb.ai'
        ]
        _host = _hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(_host)
                )
            _host = _hosts[_host_index]
        _params = locals()

        _all_params = [
            'file',
            'purpose',
            'model',
            'target_model_names'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params and _key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_ai_gateway_file" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['file']:
            _form_params.append(('file', _params['file']))

        if _params['purpose']:
            _form_params.append(('purpose', _params['purpose']))

        if _params['model']:
            _form_params.append(('model', _params['model']))

        if _params['target_model_names']:
            _form_params.append(('target_model_names', _params['target_model_names']))

        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['AiGatewayKey']  # noqa: E501

        _response_types_map = {
            '200': "AiGatewayFile",
            '400': "AiGatewayError",
            '401': "AiGatewayError",
            '403': "AiGatewayError",
            '422': "AiGatewayValidationError",
            '500': "AiGatewayError",
        }

        return self.api_client.call_api(
            '/v1/files', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            _host=_host,
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
