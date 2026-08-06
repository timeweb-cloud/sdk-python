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

from timeweb_cloud_api.models.add_certificate import AddCertificate
from timeweb_cloud_api.models.clear_cache import ClearCache
from timeweb_cloud_api.models.create_cdn_resource201_response import CreateCdnResource201Response
from timeweb_cloud_api.models.create_http_resource import CreateHttpResource
from timeweb_cloud_api.models.get_cdn_certificate_tasks200_response import GetCdnCertificateTasks200Response
from timeweb_cloud_api.models.get_cdn_certificates200_response import GetCdnCertificates200Response
from timeweb_cloud_api.models.get_cdn_origin_nodes200_response import GetCdnOriginNodes200Response
from timeweb_cloud_api.models.get_cdn_presets200_response import GetCdnPresets200Response
from timeweb_cloud_api.models.get_cdn_resource_configuration200_response import GetCdnResourceConfiguration200Response
from timeweb_cloud_api.models.get_cdn_resource_nodes200_response import GetCdnResourceNodes200Response
from timeweb_cloud_api.models.get_cdn_resource_statistics200_response import GetCdnResourceStatistics200Response
from timeweb_cloud_api.models.get_cdn_resources200_response import GetCdnResources200Response
from timeweb_cloud_api.models.issue_certificate import IssueCertificate
from timeweb_cloud_api.models.preload_cache import PreloadCache
from timeweb_cloud_api.models.update_http_resource import UpdateHttpResource

from timeweb_cloud_api.api_client import ApiClient
from timeweb_cloud_api.api_response import ApiResponse
from timeweb_cloud_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class CDNApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_cdn_certificate(self, add_certificate : AddCertificate, **kwargs) -> None:  # noqa: E501
        """Загрузка собственного сертификата CDN  # noqa: E501

        Чтобы загрузить собственный SSL-сертификат, отправьте POST-запрос на `/api/v1/cdn/certificates`.  После загрузки сертификат появится в списке `/api/v1/cdn/certificates` — привязать его к ресурсу можно, передав его ID в поле `config.security.certificate_id` PATCH-запроса на `/api/v1/cdn/http-resources/{resource_id}`.  Если сертификат или приватный ключ не проходят проверку — например, истек срок действия или ключ не соответствует сертификату — вернется ошибка `422`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_cdn_certificate(add_certificate, async_req=True)
        >>> result = thread.get()

        :param add_certificate: (required)
        :type add_certificate: AddCertificate
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
            raise ValueError("Error! Please call the add_cdn_certificate_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_cdn_certificate_with_http_info(add_certificate, **kwargs)  # noqa: E501

    @validate_arguments
    def add_cdn_certificate_with_http_info(self, add_certificate : AddCertificate, **kwargs) -> ApiResponse:  # noqa: E501
        """Загрузка собственного сертификата CDN  # noqa: E501

        Чтобы загрузить собственный SSL-сертификат, отправьте POST-запрос на `/api/v1/cdn/certificates`.  После загрузки сертификат появится в списке `/api/v1/cdn/certificates` — привязать его к ресурсу можно, передав его ID в поле `config.security.certificate_id` PATCH-запроса на `/api/v1/cdn/http-resources/{resource_id}`.  Если сертификат или приватный ключ не проходят проверку — например, истек срок действия или ключ не соответствует сертификату — вернется ошибка `422`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_cdn_certificate_with_http_info(add_certificate, async_req=True)
        >>> result = thread.get()

        :param add_certificate: (required)
        :type add_certificate: AddCertificate
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
            'add_certificate'
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
                    " to method add_cdn_certificate" % _key
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
        if _params['add_certificate'] is not None:
            _body_params = _params['add_certificate']

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

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/cdn/certificates', 'POST',
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
    def archive_cdn_certificate_task(self, task_id : Annotated[Any, Field(..., description="ID задачи на выпуск сертификата")], **kwargs) -> None:  # noqa: E501
        """Архивация задачи на выпуск сертификата  # noqa: E501

        Чтобы убрать из списка задачу на выпуск сертификата, отправьте POST-запрос на `/api/v1/cdn/certificates/tasks/{task_id}/archive`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive_cdn_certificate_task(task_id, async_req=True)
        >>> result = thread.get()

        :param task_id: ID задачи на выпуск сертификата (required)
        :type task_id: object
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
            raise ValueError("Error! Please call the archive_cdn_certificate_task_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.archive_cdn_certificate_task_with_http_info(task_id, **kwargs)  # noqa: E501

    @validate_arguments
    def archive_cdn_certificate_task_with_http_info(self, task_id : Annotated[Any, Field(..., description="ID задачи на выпуск сертификата")], **kwargs) -> ApiResponse:  # noqa: E501
        """Архивация задачи на выпуск сертификата  # noqa: E501

        Чтобы убрать из списка задачу на выпуск сертификата, отправьте POST-запрос на `/api/v1/cdn/certificates/tasks/{task_id}/archive`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive_cdn_certificate_task_with_http_info(task_id, async_req=True)
        >>> result = thread.get()

        :param task_id: ID задачи на выпуск сертификата (required)
        :type task_id: object
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
            'task_id'
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
                    " to method archive_cdn_certificate_task" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['task_id']:
            _path_params['task_id'] = _params['task_id']


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
            '/api/v1/cdn/certificates/tasks/{task_id}/archive', 'POST',
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
    def clear_cdn_resource_cache(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], clear_cache : ClearCache, **kwargs) -> None:  # noqa: E501
        """Очистка кэша CDN-ресурса  # noqa: E501

        Чтобы очистить кэш на узлах CDN, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/clear-cache`.  При `purge_type` = `full` очищается весь кэш ресурса, при `purge_type` = `partial` — только файлы из списка `paths`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_cdn_resource_cache(resource_id, clear_cache, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param clear_cache: (required)
        :type clear_cache: ClearCache
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
            raise ValueError("Error! Please call the clear_cdn_resource_cache_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.clear_cdn_resource_cache_with_http_info(resource_id, clear_cache, **kwargs)  # noqa: E501

    @validate_arguments
    def clear_cdn_resource_cache_with_http_info(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], clear_cache : ClearCache, **kwargs) -> ApiResponse:  # noqa: E501
        """Очистка кэша CDN-ресурса  # noqa: E501

        Чтобы очистить кэш на узлах CDN, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/clear-cache`.  При `purge_type` = `full` очищается весь кэш ресурса, при `purge_type` = `partial` — только файлы из списка `paths`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clear_cdn_resource_cache_with_http_info(resource_id, clear_cache, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param clear_cache: (required)
        :type clear_cache: ClearCache
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
            'resource_id',
            'clear_cache'
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
                    " to method clear_cdn_resource_cache" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['clear_cache'] is not None:
            _body_params = _params['clear_cache']

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
            '/api/v1/cdn/http-resources/{resource_id}/clear-cache', 'POST',
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
    def create_cdn_resource(self, create_http_resource : CreateHttpResource, **kwargs) -> CreateCdnResource201Response:  # noqa: E501
        """Создание CDN-ресурса  # noqa: E501

        Чтобы создать CDN-ресурс, отправьте POST-запрос на `/api/v1/cdn/http-resources`.  Источник контента задается ровно одним из полей: `storage_id` для S3-хранилища или `server` для произвольного origin-сервера. Если ни одно из них не передано, вернется ошибка `400`.  Сразу после создания ресурсу выдается технический домен `cdn_domain`, а сам ресурс какое-то время находится в статусе `processing`, пока конфигурация применяется на узлах CDN.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_cdn_resource(create_http_resource, async_req=True)
        >>> result = thread.get()

        :param create_http_resource: (required)
        :type create_http_resource: CreateHttpResource
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateCdnResource201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_cdn_resource_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_cdn_resource_with_http_info(create_http_resource, **kwargs)  # noqa: E501

    @validate_arguments
    def create_cdn_resource_with_http_info(self, create_http_resource : CreateHttpResource, **kwargs) -> ApiResponse:  # noqa: E501
        """Создание CDN-ресурса  # noqa: E501

        Чтобы создать CDN-ресурс, отправьте POST-запрос на `/api/v1/cdn/http-resources`.  Источник контента задается ровно одним из полей: `storage_id` для S3-хранилища или `server` для произвольного origin-сервера. Если ни одно из них не передано, вернется ошибка `400`.  Сразу после создания ресурсу выдается технический домен `cdn_domain`, а сам ресурс какое-то время находится в статусе `processing`, пока конфигурация применяется на узлах CDN.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_cdn_resource_with_http_info(create_http_resource, async_req=True)
        >>> result = thread.get()

        :param create_http_resource: (required)
        :type create_http_resource: CreateHttpResource
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
        :rtype: tuple(CreateCdnResource201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'create_http_resource'
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
                    " to method create_cdn_resource" % _key
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
        if _params['create_http_resource'] is not None:
            _body_params = _params['create_http_resource']

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
            '201': "CreateCdnResource201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/http-resources', 'POST',
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
    def delete_cdn_certificate(self, certificate_id : Annotated[Any, Field(..., description="ID сертификата")], **kwargs) -> None:  # noqa: E501
        """Удаление сертификата CDN  # noqa: E501

        Чтобы удалить SSL-сертификат, отправьте DELETE-запрос на `/api/v1/cdn/certificates/{certificate_id}`.  Если сертификат привязан к CDN-ресурсу, вернется ошибка `409` — сначала отвяжите его, передав `config.security.certificate_id` = `null` в PATCH-запросе на `/api/v1/cdn/http-resources/{resource_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_cdn_certificate(certificate_id, async_req=True)
        >>> result = thread.get()

        :param certificate_id: ID сертификата (required)
        :type certificate_id: object
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
            raise ValueError("Error! Please call the delete_cdn_certificate_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_cdn_certificate_with_http_info(certificate_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_cdn_certificate_with_http_info(self, certificate_id : Annotated[Any, Field(..., description="ID сертификата")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление сертификата CDN  # noqa: E501

        Чтобы удалить SSL-сертификат, отправьте DELETE-запрос на `/api/v1/cdn/certificates/{certificate_id}`.  Если сертификат привязан к CDN-ресурсу, вернется ошибка `409` — сначала отвяжите его, передав `config.security.certificate_id` = `null` в PATCH-запросе на `/api/v1/cdn/http-resources/{resource_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_cdn_certificate_with_http_info(certificate_id, async_req=True)
        >>> result = thread.get()

        :param certificate_id: ID сертификата (required)
        :type certificate_id: object
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
            'certificate_id'
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
                    " to method delete_cdn_certificate" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['certificate_id']:
            _path_params['certificate_id'] = _params['certificate_id']


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

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/cdn/certificates/{certificate_id}', 'DELETE',
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
    def delete_cdn_resource(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], **kwargs) -> None:  # noqa: E501
        """Удаление CDN-ресурса  # noqa: E501

        Чтобы удалить CDN-ресурс, отправьте DELETE-запрос на `/api/v1/cdn/http-resources/{resource_id}`. Вместе с ресурсом освобождается его технический домен, а привязанный сертификат отвязывается.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_cdn_resource(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
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
            raise ValueError("Error! Please call the delete_cdn_resource_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_cdn_resource_with_http_info(resource_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_cdn_resource_with_http_info(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление CDN-ресурса  # noqa: E501

        Чтобы удалить CDN-ресурс, отправьте DELETE-запрос на `/api/v1/cdn/http-resources/{resource_id}`. Вместе с ресурсом освобождается его технический домен, а привязанный сертификат отвязывается.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_cdn_resource_with_http_info(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
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
            'resource_id'
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
                    " to method delete_cdn_resource" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


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
            '/api/v1/cdn/http-resources/{resource_id}', 'DELETE',
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
    def get_cdn_certificate_tasks(self, resource_id : Annotated[Optional[Any], Field(description="Оставить в выдаче только задачи указанного CDN-ресурса.")] = None, **kwargs) -> GetCdnCertificateTasks200Response:  # noqa: E501
        """Получение списка задач на выпуск сертификатов  # noqa: E501

        Чтобы получить список задач на выпуск сертификатов Let's Encrypt, отправьте GET-запрос на `/api/v1/cdn/certificates/tasks`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_certificate_tasks(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: Оставить в выдаче только задачи указанного CDN-ресурса.
        :type resource_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetCdnCertificateTasks200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_cdn_certificate_tasks_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_cdn_certificate_tasks_with_http_info(resource_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_cdn_certificate_tasks_with_http_info(self, resource_id : Annotated[Optional[Any], Field(description="Оставить в выдаче только задачи указанного CDN-ресурса.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка задач на выпуск сертификатов  # noqa: E501

        Чтобы получить список задач на выпуск сертификатов Let's Encrypt, отправьте GET-запрос на `/api/v1/cdn/certificates/tasks`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_certificate_tasks_with_http_info(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: Оставить в выдаче только задачи указанного CDN-ресурса.
        :type resource_id: object
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
        :rtype: tuple(GetCdnCertificateTasks200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id'
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
                    " to method get_cdn_certificate_tasks" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('resource_id') is not None:  # noqa: E501
            _query_params.append(('resource_id', _params['resource_id']))

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
            '200': "GetCdnCertificateTasks200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/certificates/tasks', 'GET',
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
    def get_cdn_certificates(self, resource_id : Annotated[Optional[Any], Field(description="Оставить в выдаче только сертификаты, подходящие для доменов указанного CDN-ресурса.")] = None, **kwargs) -> GetCdnCertificates200Response:  # noqa: E501
        """Получение списка сертификатов CDN  # noqa: E501

        Чтобы получить список SSL-сертификатов, доступных для доменов CDN-ресурсов, отправьте GET-запрос на `/api/v1/cdn/certificates`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_certificates(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: Оставить в выдаче только сертификаты, подходящие для доменов указанного CDN-ресурса.
        :type resource_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetCdnCertificates200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_cdn_certificates_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_cdn_certificates_with_http_info(resource_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_cdn_certificates_with_http_info(self, resource_id : Annotated[Optional[Any], Field(description="Оставить в выдаче только сертификаты, подходящие для доменов указанного CDN-ресурса.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка сертификатов CDN  # noqa: E501

        Чтобы получить список SSL-сертификатов, доступных для доменов CDN-ресурсов, отправьте GET-запрос на `/api/v1/cdn/certificates`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_certificates_with_http_info(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: Оставить в выдаче только сертификаты, подходящие для доменов указанного CDN-ресурса.
        :type resource_id: object
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
        :rtype: tuple(GetCdnCertificates200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id'
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
                    " to method get_cdn_certificates" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('resource_id') is not None:  # noqa: E501
            _query_params.append(('resource_id', _params['resource_id']))

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
            '200': "GetCdnCertificates200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/certificates', 'GET',
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
    def get_cdn_origin_nodes(self, with_extra_zones : Annotated[Optional[Any], Field(description="Добавить в выдачу узлы дополнительных зон раздачи.")] = None, **kwargs) -> GetCdnOriginNodes200Response:  # noqa: E501
        """Получение списка подсетей узлов CDN  # noqa: E501

        Чтобы получить список IP-адресов и подсетей, с которых узлы CDN обращаются к источнику контента, отправьте GET-запрос на `/api/v1/cdn/nodes/origin`. Этот список удобно использовать, чтобы разрешить доступ к origin-серверу только для узлов CDN.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_origin_nodes(with_extra_zones, async_req=True)
        >>> result = thread.get()

        :param with_extra_zones: Добавить в выдачу узлы дополнительных зон раздачи.
        :type with_extra_zones: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetCdnOriginNodes200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_cdn_origin_nodes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_cdn_origin_nodes_with_http_info(with_extra_zones, **kwargs)  # noqa: E501

    @validate_arguments
    def get_cdn_origin_nodes_with_http_info(self, with_extra_zones : Annotated[Optional[Any], Field(description="Добавить в выдачу узлы дополнительных зон раздачи.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка подсетей узлов CDN  # noqa: E501

        Чтобы получить список IP-адресов и подсетей, с которых узлы CDN обращаются к источнику контента, отправьте GET-запрос на `/api/v1/cdn/nodes/origin`. Этот список удобно использовать, чтобы разрешить доступ к origin-серверу только для узлов CDN.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_origin_nodes_with_http_info(with_extra_zones, async_req=True)
        >>> result = thread.get()

        :param with_extra_zones: Добавить в выдачу узлы дополнительных зон раздачи.
        :type with_extra_zones: object
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
        :rtype: tuple(GetCdnOriginNodes200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'with_extra_zones'
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
                    " to method get_cdn_origin_nodes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('with_extra_zones') is not None:  # noqa: E501
            _query_params.append(('with_extra_zones', _params['with_extra_zones']))

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
            '200': "GetCdnOriginNodes200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/nodes/origin', 'GET',
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
    def get_cdn_presets(self, **kwargs) -> GetCdnPresets200Response:  # noqa: E501
        """Получение списка тарифов CDN  # noqa: E501

        Чтобы получить список доступных тарифов CDN, отправьте GET-запрос на `/api/v1/cdn/presets`. ID тарифа из этого списка указывается в поле `preset_id` при создании и изменении ресурса.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_presets(async_req=True)
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
        :rtype: GetCdnPresets200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_cdn_presets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_cdn_presets_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_cdn_presets_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка тарифов CDN  # noqa: E501

        Чтобы получить список доступных тарифов CDN, отправьте GET-запрос на `/api/v1/cdn/presets`. ID тарифа из этого списка указывается в поле `preset_id` при создании и изменении ресурса.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_presets_with_http_info(async_req=True)
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
        :rtype: tuple(GetCdnPresets200Response, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_cdn_presets" % _key
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
            '200': "GetCdnPresets200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/presets', 'GET',
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
    def get_cdn_resource(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], **kwargs) -> CreateCdnResource201Response:  # noqa: E501
        """Получение CDN-ресурса  # noqa: E501

        Чтобы получить информацию об отдельном CDN-ресурсе, отправьте GET-запрос на `/api/v1/cdn/http-resources/{resource_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_resource(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateCdnResource201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_cdn_resource_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_cdn_resource_with_http_info(resource_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_cdn_resource_with_http_info(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение CDN-ресурса  # noqa: E501

        Чтобы получить информацию об отдельном CDN-ресурсе, отправьте GET-запрос на `/api/v1/cdn/http-resources/{resource_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_resource_with_http_info(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
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
        :rtype: tuple(CreateCdnResource201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id'
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
                    " to method get_cdn_resource" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


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
            '200': "CreateCdnResource201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/http-resources/{resource_id}', 'GET',
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
    def get_cdn_resource_configuration(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], **kwargs) -> GetCdnResourceConfiguration200Response:  # noqa: E501
        """Получение конфигурации CDN-ресурса  # noqa: E501

        Чтобы получить текущую конфигурацию CDN-ресурса, отправьте GET-запрос на `/api/v1/cdn/http-resources/{resource_id}/configuration`.  Изменить конфигурацию можно в поле `config` PATCH-запроса на `/api/v1/cdn/http-resources/{resource_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_resource_configuration(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetCdnResourceConfiguration200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_cdn_resource_configuration_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_cdn_resource_configuration_with_http_info(resource_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_cdn_resource_configuration_with_http_info(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение конфигурации CDN-ресурса  # noqa: E501

        Чтобы получить текущую конфигурацию CDN-ресурса, отправьте GET-запрос на `/api/v1/cdn/http-resources/{resource_id}/configuration`.  Изменить конфигурацию можно в поле `config` PATCH-запроса на `/api/v1/cdn/http-resources/{resource_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_resource_configuration_with_http_info(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
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
        :rtype: tuple(GetCdnResourceConfiguration200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id'
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
                    " to method get_cdn_resource_configuration" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


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
            '200': "GetCdnResourceConfiguration200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/http-resources/{resource_id}/configuration', 'GET',
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
    def get_cdn_resource_nodes(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], with_extra_zones : Annotated[Optional[Any], Field(description="Добавить в выдачу узлы дополнительных зон раздачи.")] = None, country : Annotated[Optional[Any], Field(description="Оставить в выдаче только основные зоны раздачи в указанных странах. Коды стран в формате ISO 3166-1 alpha-2.")] = None, **kwargs) -> GetCdnResourceNodes200Response:  # noqa: E501
        """Получение списка раздающих узлов CDN-ресурса  # noqa: E501

        Чтобы получить список узлов, которые раздают контент доменов ресурса, отправьте GET-запрос на `/api/v1/cdn/nodes/http-resources/{resource_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_resource_nodes(resource_id, with_extra_zones, country, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param with_extra_zones: Добавить в выдачу узлы дополнительных зон раздачи.
        :type with_extra_zones: object
        :param country: Оставить в выдаче только основные зоны раздачи в указанных странах. Коды стран в формате ISO 3166-1 alpha-2.
        :type country: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetCdnResourceNodes200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_cdn_resource_nodes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_cdn_resource_nodes_with_http_info(resource_id, with_extra_zones, country, **kwargs)  # noqa: E501

    @validate_arguments
    def get_cdn_resource_nodes_with_http_info(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], with_extra_zones : Annotated[Optional[Any], Field(description="Добавить в выдачу узлы дополнительных зон раздачи.")] = None, country : Annotated[Optional[Any], Field(description="Оставить в выдаче только основные зоны раздачи в указанных странах. Коды стран в формате ISO 3166-1 alpha-2.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка раздающих узлов CDN-ресурса  # noqa: E501

        Чтобы получить список узлов, которые раздают контент доменов ресурса, отправьте GET-запрос на `/api/v1/cdn/nodes/http-resources/{resource_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_resource_nodes_with_http_info(resource_id, with_extra_zones, country, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param with_extra_zones: Добавить в выдачу узлы дополнительных зон раздачи.
        :type with_extra_zones: object
        :param country: Оставить в выдаче только основные зоны раздачи в указанных странах. Коды стран в формате ISO 3166-1 alpha-2.
        :type country: object
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
        :rtype: tuple(GetCdnResourceNodes200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id',
            'with_extra_zones',
            'country'
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
                    " to method get_cdn_resource_nodes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


        # process the query parameters
        _query_params = []
        if _params.get('with_extra_zones') is not None:  # noqa: E501
            _query_params.append(('with_extra_zones', _params['with_extra_zones']))

        if _params.get('country') is not None:  # noqa: E501
            _query_params.append(('country', _params['country']))

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
            '200': "GetCdnResourceNodes200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/nodes/http-resources/{resource_id}', 'GET',
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
    def get_cdn_resource_statistics(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], var_from : Annotated[Optional[Any], Field(description="Начало периода в формате ISO 8601. По умолчанию — 6 часов назад.")] = None, to : Annotated[Optional[Any], Field(description="Конец периода в формате ISO 8601. По умолчанию — текущий момент. Должен быть не раньше `from`.")] = None, **kwargs) -> GetCdnResourceStatistics200Response:  # noqa: E501
        """Получение статистики CDN-ресурса  # noqa: E501

        Чтобы получить статистику трафика и запросов CDN-ресурса, отправьте GET-запрос на `/api/v1/cdn/http-resources/{resource_id}/statistics`.  Данные возвращаются с разбивкой по часовым интервалам. Если период не указан, вернется статистика за последние 6 часов.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_resource_statistics(resource_id, var_from, to, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param var_from: Начало периода в формате ISO 8601. По умолчанию — 6 часов назад.
        :type var_from: object
        :param to: Конец периода в формате ISO 8601. По умолчанию — текущий момент. Должен быть не раньше `from`.
        :type to: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetCdnResourceStatistics200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_cdn_resource_statistics_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_cdn_resource_statistics_with_http_info(resource_id, var_from, to, **kwargs)  # noqa: E501

    @validate_arguments
    def get_cdn_resource_statistics_with_http_info(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], var_from : Annotated[Optional[Any], Field(description="Начало периода в формате ISO 8601. По умолчанию — 6 часов назад.")] = None, to : Annotated[Optional[Any], Field(description="Конец периода в формате ISO 8601. По умолчанию — текущий момент. Должен быть не раньше `from`.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение статистики CDN-ресурса  # noqa: E501

        Чтобы получить статистику трафика и запросов CDN-ресурса, отправьте GET-запрос на `/api/v1/cdn/http-resources/{resource_id}/statistics`.  Данные возвращаются с разбивкой по часовым интервалам. Если период не указан, вернется статистика за последние 6 часов.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_resource_statistics_with_http_info(resource_id, var_from, to, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param var_from: Начало периода в формате ISO 8601. По умолчанию — 6 часов назад.
        :type var_from: object
        :param to: Конец периода в формате ISO 8601. По умолчанию — текущий момент. Должен быть не раньше `from`.
        :type to: object
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
        :rtype: tuple(GetCdnResourceStatistics200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id',
            'var_from',
            'to'
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
                    " to method get_cdn_resource_statistics" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


        # process the query parameters
        _query_params = []
        if _params.get('var_from') is not None:  # noqa: E501
            _query_params.append(('from', _params['var_from']))

        if _params.get('to') is not None:  # noqa: E501
            _query_params.append(('to', _params['to']))

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
            '200': "GetCdnResourceStatistics200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/http-resources/{resource_id}/statistics', 'GET',
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
    def get_cdn_resources(self, bucket_id : Annotated[Optional[Any], Field(description="Оставить в выдаче только ресурсы, источником контента которых является указанное S3-хранилище.")] = None, **kwargs) -> GetCdnResources200Response:  # noqa: E501
        """Получение списка CDN-ресурсов  # noqa: E501

        Чтобы получить список CDN-ресурсов, отправьте GET-запрос на `/api/v1/cdn/http-resources`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_resources(bucket_id, async_req=True)
        >>> result = thread.get()

        :param bucket_id: Оставить в выдаче только ресурсы, источником контента которых является указанное S3-хранилище.
        :type bucket_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetCdnResources200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_cdn_resources_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_cdn_resources_with_http_info(bucket_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_cdn_resources_with_http_info(self, bucket_id : Annotated[Optional[Any], Field(description="Оставить в выдаче только ресурсы, источником контента которых является указанное S3-хранилище.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка CDN-ресурсов  # noqa: E501

        Чтобы получить список CDN-ресурсов, отправьте GET-запрос на `/api/v1/cdn/http-resources`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_cdn_resources_with_http_info(bucket_id, async_req=True)
        >>> result = thread.get()

        :param bucket_id: Оставить в выдаче только ресурсы, источником контента которых является указанное S3-хранилище.
        :type bucket_id: object
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
        :rtype: tuple(GetCdnResources200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'bucket_id'
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
                    " to method get_cdn_resources" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('bucket_id') is not None:  # noqa: E501
            _query_params.append(('bucket_id', _params['bucket_id']))

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
            '200': "GetCdnResources200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/http-resources', 'GET',
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
    def issue_cdn_certificate(self, issue_certificate : IssueCertificate, **kwargs) -> None:  # noqa: E501
        """Выпуск сертификата Let's Encrypt для CDN-ресурса  # noqa: E501

        Чтобы выпустить бесплатный сертификат Let's Encrypt для доменов CDN-ресурса, отправьте POST-запрос на `/api/v1/cdn/certificates/issue`.  Выпуск выполняется асинхронно: в ответ возвращается код `202`, а следить за ходом выпуска можно по списку задач `/api/v1/cdn/certificates/tasks`. Готовый сертификат привязывается к ресурсу автоматически.  Перед выпуском убедитесь, что домены ресурса указывают на его технический домен `cdn_domain` — иначе вернется ошибка `422`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.issue_cdn_certificate(issue_certificate, async_req=True)
        >>> result = thread.get()

        :param issue_certificate: (required)
        :type issue_certificate: IssueCertificate
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
            raise ValueError("Error! Please call the issue_cdn_certificate_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.issue_cdn_certificate_with_http_info(issue_certificate, **kwargs)  # noqa: E501

    @validate_arguments
    def issue_cdn_certificate_with_http_info(self, issue_certificate : IssueCertificate, **kwargs) -> ApiResponse:  # noqa: E501
        """Выпуск сертификата Let's Encrypt для CDN-ресурса  # noqa: E501

        Чтобы выпустить бесплатный сертификат Let's Encrypt для доменов CDN-ресурса, отправьте POST-запрос на `/api/v1/cdn/certificates/issue`.  Выпуск выполняется асинхронно: в ответ возвращается код `202`, а следить за ходом выпуска можно по списку задач `/api/v1/cdn/certificates/tasks`. Готовый сертификат привязывается к ресурсу автоматически.  Перед выпуском убедитесь, что домены ресурса указывают на его технический домен `cdn_domain` — иначе вернется ошибка `422`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.issue_cdn_certificate_with_http_info(issue_certificate, async_req=True)
        >>> result = thread.get()

        :param issue_certificate: (required)
        :type issue_certificate: IssueCertificate
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
            'issue_certificate'
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
                    " to method issue_cdn_certificate" % _key
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
        if _params['issue_certificate'] is not None:
            _body_params = _params['issue_certificate']

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

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/cdn/certificates/issue', 'POST',
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
    def preload_cdn_resource_cache(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], preload_cache : PreloadCache, **kwargs) -> None:  # noqa: E501
        """Предварительная загрузка кэша CDN-ресурса  # noqa: E501

        Чтобы заранее загрузить файлы в кэш узлов CDN, не дожидаясь первого обращения пользователей, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/preload-cache`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.preload_cdn_resource_cache(resource_id, preload_cache, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param preload_cache: (required)
        :type preload_cache: PreloadCache
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
            raise ValueError("Error! Please call the preload_cdn_resource_cache_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.preload_cdn_resource_cache_with_http_info(resource_id, preload_cache, **kwargs)  # noqa: E501

    @validate_arguments
    def preload_cdn_resource_cache_with_http_info(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], preload_cache : PreloadCache, **kwargs) -> ApiResponse:  # noqa: E501
        """Предварительная загрузка кэша CDN-ресурса  # noqa: E501

        Чтобы заранее загрузить файлы в кэш узлов CDN, не дожидаясь первого обращения пользователей, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/preload-cache`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.preload_cdn_resource_cache_with_http_info(resource_id, preload_cache, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param preload_cache: (required)
        :type preload_cache: PreloadCache
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
            'resource_id',
            'preload_cache'
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
                    " to method preload_cdn_resource_cache" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['preload_cache'] is not None:
            _body_params = _params['preload_cache']

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
            '/api/v1/cdn/http-resources/{resource_id}/preload-cache', 'POST',
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
    def resume_cdn_resource(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], **kwargs) -> CreateCdnResource201Response:  # noqa: E501
        """Возобновление раздачи CDN-ресурса  # noqa: E501

        Чтобы возобновить раздачу контента после приостановки, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/resume`.  Если ресурс заблокирован, вернется ошибка `409`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.resume_cdn_resource(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateCdnResource201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the resume_cdn_resource_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.resume_cdn_resource_with_http_info(resource_id, **kwargs)  # noqa: E501

    @validate_arguments
    def resume_cdn_resource_with_http_info(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], **kwargs) -> ApiResponse:  # noqa: E501
        """Возобновление раздачи CDN-ресурса  # noqa: E501

        Чтобы возобновить раздачу контента после приостановки, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/resume`.  Если ресурс заблокирован, вернется ошибка `409`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.resume_cdn_resource_with_http_info(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
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
        :rtype: tuple(CreateCdnResource201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id'
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
                    " to method resume_cdn_resource" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


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
            '201': "CreateCdnResource201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/http-resources/{resource_id}/resume', 'POST',
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
    def suspend_cdn_resource(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], **kwargs) -> CreateCdnResource201Response:  # noqa: E501
        """Приостановка раздачи CDN-ресурса  # noqa: E501

        Чтобы приостановить раздачу контента, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/suspend`. Ресурс перейдет в статус `stopped`, его настройки и домены сохранятся.  Если ресурс заблокирован, вернется ошибка `409`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.suspend_cdn_resource(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateCdnResource201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the suspend_cdn_resource_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.suspend_cdn_resource_with_http_info(resource_id, **kwargs)  # noqa: E501

    @validate_arguments
    def suspend_cdn_resource_with_http_info(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], **kwargs) -> ApiResponse:  # noqa: E501
        """Приостановка раздачи CDN-ресурса  # noqa: E501

        Чтобы приостановить раздачу контента, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/suspend`. Ресурс перейдет в статус `stopped`, его настройки и домены сохранятся.  Если ресурс заблокирован, вернется ошибка `409`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.suspend_cdn_resource_with_http_info(resource_id, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
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
        :rtype: tuple(CreateCdnResource201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id'
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
                    " to method suspend_cdn_resource" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


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
            '201': "CreateCdnResource201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/http-resources/{resource_id}/suspend', 'POST',
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
    def update_cdn_resource(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], update_http_resource : UpdateHttpResource, **kwargs) -> CreateCdnResource201Response:  # noqa: E501
        """Изменение CDN-ресурса  # noqa: E501

        Чтобы изменить CDN-ресурс, отправьте PATCH-запрос на `/api/v1/cdn/http-resources/{resource_id}`.  Передавайте только те поля, которые нужно изменить: переданные значения накладываются на текущую конфигурацию, а непереданные остаются без изменений. Чтобы сбросить настройку, передайте в соответствующем поле `null`.  Поля `storage_id` и `config.origin.servers` нельзя передавать вместе — источник контента может быть только один.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_cdn_resource(resource_id, update_http_resource, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param update_http_resource: (required)
        :type update_http_resource: UpdateHttpResource
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateCdnResource201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_cdn_resource_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_cdn_resource_with_http_info(resource_id, update_http_resource, **kwargs)  # noqa: E501

    @validate_arguments
    def update_cdn_resource_with_http_info(self, resource_id : Annotated[Any, Field(..., description="ID CDN-ресурса")], update_http_resource : UpdateHttpResource, **kwargs) -> ApiResponse:  # noqa: E501
        """Изменение CDN-ресурса  # noqa: E501

        Чтобы изменить CDN-ресурс, отправьте PATCH-запрос на `/api/v1/cdn/http-resources/{resource_id}`.  Передавайте только те поля, которые нужно изменить: переданные значения накладываются на текущую конфигурацию, а непереданные остаются без изменений. Чтобы сбросить настройку, передайте в соответствующем поле `null`.  Поля `storage_id` и `config.origin.servers` нельзя передавать вместе — источник контента может быть только один.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_cdn_resource_with_http_info(resource_id, update_http_resource, async_req=True)
        >>> result = thread.get()

        :param resource_id: ID CDN-ресурса (required)
        :type resource_id: object
        :param update_http_resource: (required)
        :type update_http_resource: UpdateHttpResource
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
        :rtype: tuple(CreateCdnResource201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id',
            'update_http_resource'
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
                    " to method update_cdn_resource" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_http_resource'] is not None:
            _body_params = _params['update_http_resource']

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
            '200': "CreateCdnResource201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cdn/http-resources/{resource_id}', 'PATCH',
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
