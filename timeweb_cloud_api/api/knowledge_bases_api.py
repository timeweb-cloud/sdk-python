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

from typing import Any, Optional

from timeweb_cloud_api.models.add_token_package import AddTokenPackage
from timeweb_cloud_api.models.create_knowledgebase import CreateKnowledgebase
from timeweb_cloud_api.models.create_knowledgebase201_response import CreateKnowledgebase201Response
from timeweb_cloud_api.models.get_knowledgebase_statistics200_response import GetKnowledgebaseStatistics200Response
from timeweb_cloud_api.models.get_knowledgebases200_response import GetKnowledgebases200Response
from timeweb_cloud_api.models.update_knowledgebase import UpdateKnowledgebase
from timeweb_cloud_api.models.upload_files_to_knowledgebase200_response import UploadFilesToKnowledgebase200Response

from timeweb_cloud_api.api_client import ApiClient
from timeweb_cloud_api.api_response import ApiResponse
from timeweb_cloud_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class KnowledgeBasesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_additional_token_package_to_knowledgebase(self, id : Annotated[Any, Field(..., description="ID базы знаний")], add_token_package : Optional[AddTokenPackage] = None, **kwargs) -> None:  # noqa: E501
        """Добавление дополнительного пакета токенов  # noqa: E501

        Чтобы добавить дополнительный пакет токенов для базы знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/add-additional-token-package`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_additional_token_package_to_knowledgebase(id, add_token_package, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param add_token_package:
        :type add_token_package: AddTokenPackage
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the add_additional_token_package_to_knowledgebase_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_additional_token_package_to_knowledgebase_with_http_info(id, add_token_package, **kwargs)  # noqa: E501

    @validate_arguments
    def add_additional_token_package_to_knowledgebase_with_http_info(self, id : Annotated[Any, Field(..., description="ID базы знаний")], add_token_package : Optional[AddTokenPackage] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Добавление дополнительного пакета токенов  # noqa: E501

        Чтобы добавить дополнительный пакет токенов для базы знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/add-additional-token-package`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_additional_token_package_to_knowledgebase_with_http_info(id, add_token_package, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param add_token_package:
        :type add_token_package: AddTokenPackage
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'id',
            'add_token_package'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_additional_token_package_to_knowledgebase" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['add_token_package'] is not None:
            _body_params = _params['add_token_package']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases/{id}/add-additional-token-package', 'POST',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def create_knowledgebase(self, create_knowledgebase : CreateKnowledgebase, **kwargs) -> CreateKnowledgebase201Response:  # noqa: E501
        """Создание базы знаний  # noqa: E501

        Чтобы создать базу знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases`, задав необходимые атрибуты.  База знаний будет создана с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданной базе знаний.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_knowledgebase(create_knowledgebase, async_req=True)
        >>> result = thread.get()

        :param create_knowledgebase: (required)
        :type create_knowledgebase: CreateKnowledgebase
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateKnowledgebase201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_knowledgebase_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_knowledgebase_with_http_info(create_knowledgebase, **kwargs)  # noqa: E501

    @validate_arguments
    def create_knowledgebase_with_http_info(self, create_knowledgebase : CreateKnowledgebase, **kwargs) -> ApiResponse:  # noqa: E501
        """Создание базы знаний  # noqa: E501

        Чтобы создать базу знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases`, задав необходимые атрибуты.  База знаний будет создана с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданной базе знаний.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_knowledgebase_with_http_info(create_knowledgebase, async_req=True)
        >>> result = thread.get()

        :param create_knowledgebase: (required)
        :type create_knowledgebase: CreateKnowledgebase
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
        :rtype: tuple(CreateKnowledgebase201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'create_knowledgebase'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_knowledgebase" % _key
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
        if _params['create_knowledgebase'] is not None:
            _body_params = _params['create_knowledgebase']

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
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '201': "CreateKnowledgebase201Response",
            '400': None,
            '401': None,
            '403': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases', 'POST',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_document(self, id : Annotated[Any, Field(..., description="ID базы знаний")], document_id : Annotated[Any, Field(..., description="ID документа")], **kwargs) -> None:  # noqa: E501
        """Удаление документа из базы знаний  # noqa: E501

        Чтобы удалить документ из базы знаний, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_document(id, document_id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param document_id: ID документа (required)
        :type document_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_document_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_document_with_http_info(id, document_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_document_with_http_info(self, id : Annotated[Any, Field(..., description="ID базы знаний")], document_id : Annotated[Any, Field(..., description="ID документа")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление документа из базы знаний  # noqa: E501

        Чтобы удалить документ из базы знаний, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_document_with_http_info(id, document_id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param document_id: ID документа (required)
        :type document_id: object
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'id',
            'document_id'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_document" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        if _params['document_id']:
            _path_params['document_id'] = _params['document_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}', 'DELETE',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def delete_knowledgebase(self, id : Annotated[Any, Field(..., description="ID базы знаний")], **kwargs) -> None:  # noqa: E501
        """Удаление базы знаний  # noqa: E501

        Чтобы удалить базу знаний, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_knowledgebase(id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_knowledgebase_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_knowledgebase_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_knowledgebase_with_http_info(self, id : Annotated[Any, Field(..., description="ID базы знаний")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление базы знаний  # noqa: E501

        Чтобы удалить базу знаний, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_knowledgebase_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'id'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_knowledgebase" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases/{id}', 'DELETE',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def download_document(self, id : Annotated[Any, Field(..., description="ID базы знаний")], document_id : Annotated[Any, Field(..., description="ID документа")], **kwargs) -> object:  # noqa: E501
        """Скачивание документа из базы знаний  # noqa: E501

        Чтобы скачать документ из базы знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/download`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_document(id, document_id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param document_id: ID документа (required)
        :type document_id: object
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
            raise ValueError("Error! Please call the download_document_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.download_document_with_http_info(id, document_id, **kwargs)  # noqa: E501

    @validate_arguments
    def download_document_with_http_info(self, id : Annotated[Any, Field(..., description="ID базы знаний")], document_id : Annotated[Any, Field(..., description="ID документа")], **kwargs) -> ApiResponse:  # noqa: E501
        """Скачивание документа из базы знаний  # noqa: E501

        Чтобы скачать документ из базы знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/download`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download_document_with_http_info(id, document_id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param document_id: ID документа (required)
        :type document_id: object
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

        _params = locals()

        _all_params = [
            'id',
            'document_id'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method download_document" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        if _params['document_id']:
            _path_params['document_id'] = _params['document_id']


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
            ['application/octet-stream'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "object",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/download', 'GET',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_knowledgebase(self, id : Annotated[Any, Field(..., description="ID базы знаний")], **kwargs) -> CreateKnowledgebase201Response:  # noqa: E501
        """Получение базы знаний  # noqa: E501

        Чтобы получить информацию о базе знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_knowledgebase(id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateKnowledgebase201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_knowledgebase_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_knowledgebase_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_knowledgebase_with_http_info(self, id : Annotated[Any, Field(..., description="ID базы знаний")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение базы знаний  # noqa: E501

        Чтобы получить информацию о базе знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_knowledgebase_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
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
        :rtype: tuple(CreateKnowledgebase201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledgebase" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


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
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "CreateKnowledgebase201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases/{id}', 'GET',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_knowledgebase_statistics(self, id : Annotated[Any, Field(..., description="ID базы знаний")], start_time : Annotated[Optional[Any], Field(description="Начало временного диапазона (ISO 8601)")] = None, end_time : Annotated[Optional[Any], Field(description="Конец временного диапазона (ISO 8601)")] = None, interval : Annotated[Optional[Any], Field(description="Интервал в минутах (по умолчанию 60)")] = None, **kwargs) -> GetKnowledgebaseStatistics200Response:  # noqa: E501
        """Получение статистики использования токенов базы знаний  # noqa: E501

        Чтобы получить статистику использования токенов базы знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/statistic`.  Можно указать временной диапазон и интервал агрегации.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_knowledgebase_statistics(id, start_time, end_time, interval, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param start_time: Начало временного диапазона (ISO 8601)
        :type start_time: object
        :param end_time: Конец временного диапазона (ISO 8601)
        :type end_time: object
        :param interval: Интервал в минутах (по умолчанию 60)
        :type interval: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetKnowledgebaseStatistics200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_knowledgebase_statistics_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_knowledgebase_statistics_with_http_info(id, start_time, end_time, interval, **kwargs)  # noqa: E501

    @validate_arguments
    def get_knowledgebase_statistics_with_http_info(self, id : Annotated[Any, Field(..., description="ID базы знаний")], start_time : Annotated[Optional[Any], Field(description="Начало временного диапазона (ISO 8601)")] = None, end_time : Annotated[Optional[Any], Field(description="Конец временного диапазона (ISO 8601)")] = None, interval : Annotated[Optional[Any], Field(description="Интервал в минутах (по умолчанию 60)")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение статистики использования токенов базы знаний  # noqa: E501

        Чтобы получить статистику использования токенов базы знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/statistic`.  Можно указать временной диапазон и интервал агрегации.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_knowledgebase_statistics_with_http_info(id, start_time, end_time, interval, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param start_time: Начало временного диапазона (ISO 8601)
        :type start_time: object
        :param end_time: Конец временного диапазона (ISO 8601)
        :type end_time: object
        :param interval: Интервал в минутах (по умолчанию 60)
        :type interval: object
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
        :rtype: tuple(GetKnowledgebaseStatistics200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'start_time',
            'end_time',
            'interval'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledgebase_statistics" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        if _params.get('start_time') is not None:  # noqa: E501
            _query_params.append(('startTime', _params['start_time']))

        if _params.get('end_time') is not None:  # noqa: E501
            _query_params.append(('endTime', _params['end_time']))

        if _params.get('interval') is not None:  # noqa: E501
            _query_params.append(('interval', _params['interval']))

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
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "GetKnowledgebaseStatistics200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases/{id}/statistic', 'GET',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_knowledgebases(self, **kwargs) -> GetKnowledgebases200Response:  # noqa: E501
        """Получение списка баз знаний  # noqa: E501

        Чтобы получить список баз знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases`.  Тело ответа будет представлять собой объект JSON с ключом `knowledgebases`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_knowledgebases(async_req=True)
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
        :rtype: GetKnowledgebases200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_knowledgebases_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_knowledgebases_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_knowledgebases_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка баз знаний  # noqa: E501

        Чтобы получить список баз знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases`.  Тело ответа будет представлять собой объект JSON с ключом `knowledgebases`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_knowledgebases_with_http_info(async_req=True)
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
        :rtype: tuple(GetKnowledgebases200Response, status_code(int), headers(HTTPHeaderDict))
        """

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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_knowledgebases" % _key
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
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "GetKnowledgebases200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases', 'GET',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def link_knowledgebase_to_agent(self, id : Annotated[Any, Field(..., description="ID базы знаний")], agent_id : Annotated[Any, Field(..., description="ID агента")], **kwargs) -> None:  # noqa: E501
        """Привязка базы знаний к агенту  # noqa: E501

        Чтобы привязать базу знаний к AI агенту, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.link_knowledgebase_to_agent(id, agent_id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param agent_id: ID агента (required)
        :type agent_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the link_knowledgebase_to_agent_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.link_knowledgebase_to_agent_with_http_info(id, agent_id, **kwargs)  # noqa: E501

    @validate_arguments
    def link_knowledgebase_to_agent_with_http_info(self, id : Annotated[Any, Field(..., description="ID базы знаний")], agent_id : Annotated[Any, Field(..., description="ID агента")], **kwargs) -> ApiResponse:  # noqa: E501
        """Привязка базы знаний к агенту  # noqa: E501

        Чтобы привязать базу знаний к AI агенту, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.link_knowledgebase_to_agent_with_http_info(id, agent_id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param agent_id: ID агента (required)
        :type agent_id: object
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'id',
            'agent_id'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method link_knowledgebase_to_agent" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        if _params['agent_id']:
            _path_params['agent_id'] = _params['agent_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id}', 'POST',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def reindex_document(self, id : Annotated[Any, Field(..., description="ID базы знаний")], document_id : Annotated[Any, Field(..., description="ID документа")], **kwargs) -> None:  # noqa: E501
        """Переиндексация документа  # noqa: E501

        Чтобы переиндексировать документ в базе знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/reindex`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reindex_document(id, document_id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param document_id: ID документа (required)
        :type document_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the reindex_document_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.reindex_document_with_http_info(id, document_id, **kwargs)  # noqa: E501

    @validate_arguments
    def reindex_document_with_http_info(self, id : Annotated[Any, Field(..., description="ID базы знаний")], document_id : Annotated[Any, Field(..., description="ID документа")], **kwargs) -> ApiResponse:  # noqa: E501
        """Переиндексация документа  # noqa: E501

        Чтобы переиндексировать документ в базе знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/reindex`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reindex_document_with_http_info(id, document_id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param document_id: ID документа (required)
        :type document_id: object
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'id',
            'document_id'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reindex_document" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        if _params['document_id']:
            _path_params['document_id'] = _params['document_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/reindex', 'POST',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def unlink_knowledgebase_from_agent(self, id : Annotated[Any, Field(..., description="ID базы знаний")], agent_id : Annotated[Any, Field(..., description="ID агента")], **kwargs) -> None:  # noqa: E501
        """Отвязка базы знаний от агента  # noqa: E501

        Чтобы отвязать базу знаний от AI агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.unlink_knowledgebase_from_agent(id, agent_id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param agent_id: ID агента (required)
        :type agent_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the unlink_knowledgebase_from_agent_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.unlink_knowledgebase_from_agent_with_http_info(id, agent_id, **kwargs)  # noqa: E501

    @validate_arguments
    def unlink_knowledgebase_from_agent_with_http_info(self, id : Annotated[Any, Field(..., description="ID базы знаний")], agent_id : Annotated[Any, Field(..., description="ID агента")], **kwargs) -> ApiResponse:  # noqa: E501
        """Отвязка базы знаний от агента  # noqa: E501

        Чтобы отвязать базу знаний от AI агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.unlink_knowledgebase_from_agent_with_http_info(id, agent_id, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param agent_id: ID агента (required)
        :type agent_id: object
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
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'id',
            'agent_id'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method unlink_knowledgebase_from_agent" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']

        if _params['agent_id']:
            _path_params['agent_id'] = _params['agent_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id}', 'DELETE',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def update_knowledgebase(self, id : Annotated[Any, Field(..., description="ID базы знаний")], update_knowledgebase : UpdateKnowledgebase, **kwargs) -> CreateKnowledgebase201Response:  # noqa: E501
        """Обновление базы знаний  # noqa: E501

        Чтобы обновить базу знаний, отправьте PATCH-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_knowledgebase(id, update_knowledgebase, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param update_knowledgebase: (required)
        :type update_knowledgebase: UpdateKnowledgebase
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateKnowledgebase201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_knowledgebase_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_knowledgebase_with_http_info(id, update_knowledgebase, **kwargs)  # noqa: E501

    @validate_arguments
    def update_knowledgebase_with_http_info(self, id : Annotated[Any, Field(..., description="ID базы знаний")], update_knowledgebase : UpdateKnowledgebase, **kwargs) -> ApiResponse:  # noqa: E501
        """Обновление базы знаний  # noqa: E501

        Чтобы обновить базу знаний, отправьте PATCH-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_knowledgebase_with_http_info(id, update_knowledgebase, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param update_knowledgebase: (required)
        :type update_knowledgebase: UpdateKnowledgebase
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
        :rtype: tuple(CreateKnowledgebase201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'update_knowledgebase'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_knowledgebase" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_knowledgebase'] is not None:
            _body_params = _params['update_knowledgebase']

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
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "CreateKnowledgebase201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases/{id}', 'PATCH',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def upload_files_to_knowledgebase(self, id : Annotated[Any, Field(..., description="ID базы знаний")], files : Annotated[Optional[Any], Field(..., description="Файлы для загрузки (максимум 10 файлов, 10 МБ каждый)")], **kwargs) -> UploadFilesToKnowledgebase200Response:  # noqa: E501
        """Загрузка файлов в базу знаний  # noqa: E501

        Чтобы загрузить файлы в базу знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/upload` с файлами в формате multipart/form-data.  Поддерживаемые форматы: CSV, XML, Markdown (md), HTML, TXT. JSON не поддерживается. Максимум 10 файлов, до 10 МБ каждый.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_files_to_knowledgebase(id, files, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param files: Файлы для загрузки (максимум 10 файлов, 10 МБ каждый) (required)
        :type files: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UploadFilesToKnowledgebase200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the upload_files_to_knowledgebase_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.upload_files_to_knowledgebase_with_http_info(id, files, **kwargs)  # noqa: E501

    @validate_arguments
    def upload_files_to_knowledgebase_with_http_info(self, id : Annotated[Any, Field(..., description="ID базы знаний")], files : Annotated[Optional[Any], Field(..., description="Файлы для загрузки (максимум 10 файлов, 10 МБ каждый)")], **kwargs) -> ApiResponse:  # noqa: E501
        """Загрузка файлов в базу знаний  # noqa: E501

        Чтобы загрузить файлы в базу знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/upload` с файлами в формате multipart/form-data.  Поддерживаемые форматы: CSV, XML, Markdown (md), HTML, TXT. JSON не поддерживается. Максимум 10 файлов, до 10 МБ каждый.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_files_to_knowledgebase_with_http_info(id, files, async_req=True)
        >>> result = thread.get()

        :param id: ID базы знаний (required)
        :type id: object
        :param files: Файлы для загрузки (максимум 10 файлов, 10 МБ каждый) (required)
        :type files: object
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
        :rtype: tuple(UploadFilesToKnowledgebase200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'files'
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
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upload_files_to_knowledgebase" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['files']:
            _form_params.append(('files', _params['files']))

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
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "UploadFilesToKnowledgebase200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/knowledge-bases/{id}/upload', 'POST',
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
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
