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

from timeweb_cloud_api.models.available_networks_response import AvailableNetworksResponse
from timeweb_cloud_api.models.available_static_routes_response import AvailableStaticRoutesResponse
from timeweb_cloud_api.models.dnat_in import DnatIn
from timeweb_cloud_api.models.dnat_rule_response import DnatRuleResponse
from timeweb_cloud_api.models.dnat_rules_response import DnatRulesResponse
from timeweb_cloud_api.models.nat_in import NatIn
from timeweb_cloud_api.models.network_edit import NetworkEdit
from timeweb_cloud_api.models.network_in import NetworkIn
from timeweb_cloud_api.models.network_response import NetworkResponse
from timeweb_cloud_api.models.networks_response import NetworksResponse
from timeweb_cloud_api.models.router_edit import RouterEdit
from timeweb_cloud_api.models.router_in import RouterIn
from timeweb_cloud_api.models.router_presets_response import RouterPresetsResponse
from timeweb_cloud_api.models.router_response import RouterResponse
from timeweb_cloud_api.models.router_statistics_response import RouterStatisticsResponse
from timeweb_cloud_api.models.routers_response import RoutersResponse
from timeweb_cloud_api.models.static_route_in import StaticRouteIn
from timeweb_cloud_api.models.static_route_response import StaticRouteResponse
from timeweb_cloud_api.models.static_routes_response import StaticRoutesResponse

from timeweb_cloud_api.api_client import ApiClient
from timeweb_cloud_api.api_response import ApiResponse
from timeweb_cloud_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class RoutersApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_networks(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_in : NetworkIn, **kwargs) -> NetworksResponse:  # noqa: E501
        """Подключение сетей к роутеру  # noqa: E501

        Чтобы подключить сети к роутеру, отправьте POST-запрос на `/api/v1/routers/{router_id}/networks`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_networks(router_id, network_in, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_in: (required)
        :type network_in: NetworkIn
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NetworksResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the add_networks_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_networks_with_http_info(router_id, network_in, **kwargs)  # noqa: E501

    @validate_arguments
    def add_networks_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_in : NetworkIn, **kwargs) -> ApiResponse:  # noqa: E501
        """Подключение сетей к роутеру  # noqa: E501

        Чтобы подключить сети к роутеру, отправьте POST-запрос на `/api/v1/routers/{router_id}/networks`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_networks_with_http_info(router_id, network_in, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_in: (required)
        :type network_in: NetworkIn
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
        :rtype: tuple(NetworksResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id',
            'network_in'
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
                    " to method add_networks" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['network_in'] is not None:
            _body_params = _params['network_in']

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
            '201': "NetworksResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/networks', 'POST',
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
    def create_router(self, router_in : RouterIn, **kwargs) -> RouterResponse:  # noqa: E501
        """Создание роутера  # noqa: E501

        Чтобы создать роутер, отправьте POST-запрос на `/api/v1/routers`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_router(router_in, async_req=True)
        >>> result = thread.get()

        :param router_in: (required)
        :type router_in: RouterIn
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RouterResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_router_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_router_with_http_info(router_in, **kwargs)  # noqa: E501

    @validate_arguments
    def create_router_with_http_info(self, router_in : RouterIn, **kwargs) -> ApiResponse:  # noqa: E501
        """Создание роутера  # noqa: E501

        Чтобы создать роутер, отправьте POST-запрос на `/api/v1/routers`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_router_with_http_info(router_in, async_req=True)
        >>> result = thread.get()

        :param router_in: (required)
        :type router_in: RouterIn
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
        :rtype: tuple(RouterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_in'
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
                    " to method create_router" % _key
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
        if _params['router_in'] is not None:
            _body_params = _params['router_in']

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
            '201': "RouterResponse",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers', 'POST',
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
    def delete_dnat(self, router_id : Annotated[Any, Field(..., description="ID роутера")], dnat_id : Annotated[Any, Field(..., description="ID правила")], **kwargs) -> None:  # noqa: E501
        """Удаление правила проброса портов  # noqa: E501

        Чтобы удалить правило проброса портов (DNAT), отправьте DELETE-запрос на `/api/v1/routers/{router_id}/dnat-rules/{dnat_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_dnat(router_id, dnat_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param dnat_id: ID правила (required)
        :type dnat_id: object
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
            raise ValueError("Error! Please call the delete_dnat_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_dnat_with_http_info(router_id, dnat_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_dnat_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], dnat_id : Annotated[Any, Field(..., description="ID правила")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление правила проброса портов  # noqa: E501

        Чтобы удалить правило проброса портов (DNAT), отправьте DELETE-запрос на `/api/v1/routers/{router_id}/dnat-rules/{dnat_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_dnat_with_http_info(router_id, dnat_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param dnat_id: ID правила (required)
        :type dnat_id: object
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
            'router_id',
            'dnat_id'
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
                    " to method delete_dnat" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']

        if _params['dnat_id']:
            _path_params['dnat_id'] = _params['dnat_id']


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
            '/api/v1/routers/{router_id}/dnat-rules/{dnat_id}', 'DELETE',
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
    def delete_router(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> None:  # noqa: E501
        """Удаление роутера  # noqa: E501

        Чтобы удалить роутер, отправьте DELETE-запрос на `/api/v1/routers/{router_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_router(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
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
            raise ValueError("Error! Please call the delete_router_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_router_with_http_info(router_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_router_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление роутера  # noqa: E501

        Чтобы удалить роутер, отправьте DELETE-запрос на `/api/v1/routers/{router_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_router_with_http_info(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
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
            'router_id'
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
                    " to method delete_router" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']


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
            '/api/v1/routers/{router_id}', 'DELETE',
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
    def delete_router_nat(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_name : Annotated[Any, Field(..., description="Имя сети")], **kwargs) -> RouterResponse:  # noqa: E501
        """Выключение NAT для сети  # noqa: E501

        Чтобы выключить NAT для сети роутера, отправьте DELETE-запрос на `/api/v1/routers/{router_id}/networks/{network_name}/nat`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_router_nat(router_id, network_name, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_name: Имя сети (required)
        :type network_name: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RouterResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the delete_router_nat_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_router_nat_with_http_info(router_id, network_name, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_router_nat_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_name : Annotated[Any, Field(..., description="Имя сети")], **kwargs) -> ApiResponse:  # noqa: E501
        """Выключение NAT для сети  # noqa: E501

        Чтобы выключить NAT для сети роутера, отправьте DELETE-запрос на `/api/v1/routers/{router_id}/networks/{network_name}/nat`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_router_nat_with_http_info(router_id, network_name, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_name: Имя сети (required)
        :type network_name: object
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
        :rtype: tuple(RouterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id',
            'network_name'
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
                    " to method delete_router_nat" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']

        if _params['network_name']:
            _path_params['network_name'] = _params['network_name']


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
            '200': "RouterResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/networks/{network_name}/nat', 'DELETE',
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
    def delete_router_network(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_name : Annotated[Any, Field(..., description="Имя сети")], **kwargs) -> None:  # noqa: E501
        """Удаление сети из роутера  # noqa: E501

        Чтобы отключить сеть от роутера, отправьте DELETE-запрос на `/api/v1/routers/{router_id}/networks/{network_name}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_router_network(router_id, network_name, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_name: Имя сети (required)
        :type network_name: object
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
            raise ValueError("Error! Please call the delete_router_network_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_router_network_with_http_info(router_id, network_name, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_router_network_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_name : Annotated[Any, Field(..., description="Имя сети")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление сети из роутера  # noqa: E501

        Чтобы отключить сеть от роутера, отправьте DELETE-запрос на `/api/v1/routers/{router_id}/networks/{network_name}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_router_network_with_http_info(router_id, network_name, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_name: Имя сети (required)
        :type network_name: object
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
            'router_id',
            'network_name'
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
                    " to method delete_router_network" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']

        if _params['network_name']:
            _path_params['network_name'] = _params['network_name']


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
            '/api/v1/routers/{router_id}/networks/{network_name}', 'DELETE',
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
    def delete_static_route(self, router_id : Annotated[Any, Field(..., description="ID роутера")], static_route_id : Annotated[Any, Field(..., description="ID статического маршрута")], **kwargs) -> None:  # noqa: E501
        """Удаление статического маршрута  # noqa: E501

        Чтобы удалить статический маршрут, отправьте DELETE-запрос на `/api/v1/routers/{router_id}/static-routes/{static_route_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_static_route(router_id, static_route_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param static_route_id: ID статического маршрута (required)
        :type static_route_id: object
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
            raise ValueError("Error! Please call the delete_static_route_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_static_route_with_http_info(router_id, static_route_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_static_route_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], static_route_id : Annotated[Any, Field(..., description="ID статического маршрута")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление статического маршрута  # noqa: E501

        Чтобы удалить статический маршрут, отправьте DELETE-запрос на `/api/v1/routers/{router_id}/static-routes/{static_route_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_static_route_with_http_info(router_id, static_route_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param static_route_id: ID статического маршрута (required)
        :type static_route_id: object
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
            'router_id',
            'static_route_id'
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
                    " to method delete_static_route" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']

        if _params['static_route_id']:
            _path_params['static_route_id'] = _params['static_route_id']


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
            '/api/v1/routers/{router_id}/static-routes/{static_route_id}', 'DELETE',
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
    def get_available_static_routes(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> AvailableStaticRoutesResponse:  # noqa: E501
        """Получение доступных подсетей для статических маршрутов  # noqa: E501

        Чтобы получить список подсетей, доступных для добавления статических маршрутов, отправьте GET-запрос на `/api/v1/routers/{router_id}/static-routes/available`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_available_static_routes(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AvailableStaticRoutesResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_available_static_routes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_available_static_routes_with_http_info(router_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_available_static_routes_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение доступных подсетей для статических маршрутов  # noqa: E501

        Чтобы получить список подсетей, доступных для добавления статических маршрутов, отправьте GET-запрос на `/api/v1/routers/{router_id}/static-routes/available`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_available_static_routes_with_http_info(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
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
        :rtype: tuple(AvailableStaticRoutesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id'
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
                    " to method get_available_static_routes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']


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
            '200': "AvailableStaticRoutesResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/static-routes/available', 'GET',
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
    def get_dnat(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> DnatRulesResponse:  # noqa: E501
        """Получение списка правил проброса портов  # noqa: E501

        Чтобы получить список правил проброса портов (DNAT), отправьте GET-запрос на `/api/v1/routers/{router_id}/dnat-rules`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dnat(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DnatRulesResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_dnat_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_dnat_with_http_info(router_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dnat_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка правил проброса портов  # noqa: E501

        Чтобы получить список правил проброса портов (DNAT), отправьте GET-запрос на `/api/v1/routers/{router_id}/dnat-rules`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dnat_with_http_info(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
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
        :rtype: tuple(DnatRulesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id'
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
                    " to method get_dnat" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']


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
            '200': "DnatRulesResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/dnat-rules', 'GET',
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
    def get_dnat_rule(self, router_id : Annotated[Any, Field(..., description="ID роутера")], dnat_id : Annotated[Any, Field(..., description="ID правила")], **kwargs) -> DnatRuleResponse:  # noqa: E501
        """Получение правила проброса портов  # noqa: E501

        Чтобы получить информацию о правиле проброса портов (DNAT), отправьте GET-запрос на `/api/v1/routers/{router_id}/dnat-rules/{dnat_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dnat_rule(router_id, dnat_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param dnat_id: ID правила (required)
        :type dnat_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DnatRuleResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_dnat_rule_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_dnat_rule_with_http_info(router_id, dnat_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_dnat_rule_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], dnat_id : Annotated[Any, Field(..., description="ID правила")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение правила проброса портов  # noqa: E501

        Чтобы получить информацию о правиле проброса портов (DNAT), отправьте GET-запрос на `/api/v1/routers/{router_id}/dnat-rules/{dnat_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dnat_rule_with_http_info(router_id, dnat_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param dnat_id: ID правила (required)
        :type dnat_id: object
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
        :rtype: tuple(DnatRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id',
            'dnat_id'
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
                    " to method get_dnat_rule" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']

        if _params['dnat_id']:
            _path_params['dnat_id'] = _params['dnat_id']


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
            '200': "DnatRuleResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/dnat-rules/{dnat_id}', 'GET',
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
    def get_networks(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> NetworksResponse:  # noqa: E501
        """Получение списка сетей роутера  # noqa: E501

        Чтобы получить список сетей роутера, отправьте GET-запрос на `/api/v1/routers/{router_id}/networks`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_networks(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NetworksResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_networks_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_networks_with_http_info(router_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_networks_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка сетей роутера  # noqa: E501

        Чтобы получить список сетей роутера, отправьте GET-запрос на `/api/v1/routers/{router_id}/networks`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_networks_with_http_info(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
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
        :rtype: tuple(NetworksResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id'
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
                    " to method get_networks" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']


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
            '200': "NetworksResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/networks', 'GET',
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
    def get_router(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> RouterResponse:  # noqa: E501
        """Получение информации о роутере  # noqa: E501

        Чтобы получить информацию о роутере, отправьте GET-запрос на `/api/v1/routers/{router_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_router(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RouterResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_router_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_router_with_http_info(router_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_router_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение информации о роутере  # noqa: E501

        Чтобы получить информацию о роутере, отправьте GET-запрос на `/api/v1/routers/{router_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_router_with_http_info(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
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
        :rtype: tuple(RouterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id'
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
                    " to method get_router" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']


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
            '200': "RouterResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}', 'GET',
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
    def get_router_available_networks(self, **kwargs) -> AvailableNetworksResponse:  # noqa: E501
        """Получение списка доступных сетей  # noqa: E501

        Чтобы получить список локальных сетей, доступных для подключения к роутеру, отправьте GET-запрос на `/api/v1/routers/networks/available`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_router_available_networks(async_req=True)
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
        :rtype: AvailableNetworksResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_router_available_networks_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_router_available_networks_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_router_available_networks_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка доступных сетей  # noqa: E501

        Чтобы получить список локальных сетей, доступных для подключения к роутеру, отправьте GET-запрос на `/api/v1/routers/networks/available`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_router_available_networks_with_http_info(async_req=True)
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
        :rtype: tuple(AvailableNetworksResponse, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_router_available_networks" % _key
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
            '200': "AvailableNetworksResponse",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/networks/available', 'GET',
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
    def get_router_presets(self, **kwargs) -> RouterPresetsResponse:  # noqa: E501
        """Получение списка тарифов роутеров  # noqa: E501

        Чтобы получить список доступных тарифов роутеров, отправьте GET-запрос на `/api/v1/presets/routers`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_router_presets(async_req=True)
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
        :rtype: RouterPresetsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_router_presets_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_router_presets_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_router_presets_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка тарифов роутеров  # noqa: E501

        Чтобы получить список доступных тарифов роутеров, отправьте GET-запрос на `/api/v1/presets/routers`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_router_presets_with_http_info(async_req=True)
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
        :rtype: tuple(RouterPresetsResponse, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_router_presets" % _key
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
            '200': "RouterPresetsResponse",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/presets/routers', 'GET',
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
    def get_router_statistics(self, router_id : Annotated[Any, Field(..., description="ID роутера")], time_from : Annotated[Any, Field(..., description="Начало периода")], period : Annotated[Any, Field(..., description="Период агрегации")], keys : Annotated[Any, Field(..., description="Ключи метрик")], node_id : Annotated[Optional[Any], Field(description="ID ноды")] = None, **kwargs) -> RouterStatisticsResponse:  # noqa: E501
        """Получение статистики роутера  # noqa: E501

        Чтобы получить статистику роутера, отправьте GET-запрос на `/api/v1/routers/{router_id}/statistics/{time_from}/{period}/{keys}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_router_statistics(router_id, time_from, period, keys, node_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param time_from: Начало периода (required)
        :type time_from: object
        :param period: Период агрегации (required)
        :type period: object
        :param keys: Ключи метрик (required)
        :type keys: object
        :param node_id: ID ноды
        :type node_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RouterStatisticsResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_router_statistics_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_router_statistics_with_http_info(router_id, time_from, period, keys, node_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_router_statistics_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], time_from : Annotated[Any, Field(..., description="Начало периода")], period : Annotated[Any, Field(..., description="Период агрегации")], keys : Annotated[Any, Field(..., description="Ключи метрик")], node_id : Annotated[Optional[Any], Field(description="ID ноды")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение статистики роутера  # noqa: E501

        Чтобы получить статистику роутера, отправьте GET-запрос на `/api/v1/routers/{router_id}/statistics/{time_from}/{period}/{keys}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_router_statistics_with_http_info(router_id, time_from, period, keys, node_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param time_from: Начало периода (required)
        :type time_from: object
        :param period: Период агрегации (required)
        :type period: object
        :param keys: Ключи метрик (required)
        :type keys: object
        :param node_id: ID ноды
        :type node_id: object
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
        :rtype: tuple(RouterStatisticsResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id',
            'time_from',
            'period',
            'keys',
            'node_id'
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
                    " to method get_router_statistics" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']

        if _params['time_from']:
            _path_params['time_from'] = _params['time_from']

        if _params['period']:
            _path_params['period'] = _params['period']

        if _params['keys']:
            _path_params['keys'] = _params['keys']


        # process the query parameters
        _query_params = []
        if _params.get('node_id') is not None:  # noqa: E501
            _query_params.append(('node_id', _params['node_id']))

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
            '200': "RouterStatisticsResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/statistics/{time_from}/{period}/{keys}', 'GET',
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
    def get_routers(self, **kwargs) -> RoutersResponse:  # noqa: E501
        """Получение списка роутеров  # noqa: E501

        Чтобы получить список роутеров, отправьте GET-запрос на `/api/v1/routers`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_routers(async_req=True)
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
        :rtype: RoutersResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_routers_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_routers_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_routers_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка роутеров  # noqa: E501

        Чтобы получить список роутеров, отправьте GET-запрос на `/api/v1/routers`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_routers_with_http_info(async_req=True)
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
        :rtype: tuple(RoutersResponse, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_routers" % _key
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
            '200': "RoutersResponse",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers', 'GET',
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
    def get_static_routes(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> StaticRoutesResponse:  # noqa: E501
        """Получение списка статических маршрутов  # noqa: E501

        Чтобы получить список статических маршрутов роутера, отправьте GET-запрос на `/api/v1/routers/{router_id}/static-routes`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_static_routes(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StaticRoutesResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_static_routes_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_static_routes_with_http_info(router_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_static_routes_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка статических маршрутов  # noqa: E501

        Чтобы получить список статических маршрутов роутера, отправьте GET-запрос на `/api/v1/routers/{router_id}/static-routes`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_static_routes_with_http_info(router_id, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
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
        :rtype: tuple(StaticRoutesResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id'
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
                    " to method get_static_routes" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']


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
            '200': "StaticRoutesResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/static-routes', 'GET',
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
    def patch_network(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_name : Annotated[Any, Field(..., description="Имя сети")], network_edit : NetworkEdit, **kwargs) -> NetworkResponse:  # noqa: E501
        """Обновление информации о сети  # noqa: E501

        Чтобы включить или выключить DHCP в сети роутера, отправьте PATCH-запрос на `/api/v1/routers/{router_id}/networks/{network_name}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_network(router_id, network_name, network_edit, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_name: Имя сети (required)
        :type network_name: object
        :param network_edit: (required)
        :type network_edit: NetworkEdit
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NetworkResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the patch_network_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.patch_network_with_http_info(router_id, network_name, network_edit, **kwargs)  # noqa: E501

    @validate_arguments
    def patch_network_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_name : Annotated[Any, Field(..., description="Имя сети")], network_edit : NetworkEdit, **kwargs) -> ApiResponse:  # noqa: E501
        """Обновление информации о сети  # noqa: E501

        Чтобы включить или выключить DHCP в сети роутера, отправьте PATCH-запрос на `/api/v1/routers/{router_id}/networks/{network_name}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_network_with_http_info(router_id, network_name, network_edit, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_name: Имя сети (required)
        :type network_name: object
        :param network_edit: (required)
        :type network_edit: NetworkEdit
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
        :rtype: tuple(NetworkResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id',
            'network_name',
            'network_edit'
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
                    " to method patch_network" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']

        if _params['network_name']:
            _path_params['network_name'] = _params['network_name']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['network_edit'] is not None:
            _body_params = _params['network_edit']

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
            '200': "NetworkResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/networks/{network_name}', 'PATCH',
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
    def patch_networks(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_in : NetworkIn, **kwargs) -> NetworksResponse:  # noqa: E501
        """Обновление сетей роутера  # noqa: E501

        Чтобы обновить набор сетей роутера, отправьте PATCH-запрос на `/api/v1/routers/{router_id}/networks`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_networks(router_id, network_in, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_in: (required)
        :type network_in: NetworkIn
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: NetworksResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the patch_networks_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.patch_networks_with_http_info(router_id, network_in, **kwargs)  # noqa: E501

    @validate_arguments
    def patch_networks_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_in : NetworkIn, **kwargs) -> ApiResponse:  # noqa: E501
        """Обновление сетей роутера  # noqa: E501

        Чтобы обновить набор сетей роутера, отправьте PATCH-запрос на `/api/v1/routers/{router_id}/networks`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_networks_with_http_info(router_id, network_in, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_in: (required)
        :type network_in: NetworkIn
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
        :rtype: tuple(NetworksResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id',
            'network_in'
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
                    " to method patch_networks" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['network_in'] is not None:
            _body_params = _params['network_in']

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
            '200': "NetworksResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/networks', 'PATCH',
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
    def post_dnat(self, router_id : Annotated[Any, Field(..., description="ID роутера")], dnat_in : DnatIn, **kwargs) -> DnatRuleResponse:  # noqa: E501
        """Добавление правила проброса портов  # noqa: E501

        Чтобы добавить правило проброса портов (DNAT), отправьте POST-запрос на `/api/v1/routers/{router_id}/dnat-rules`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_dnat(router_id, dnat_in, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param dnat_in: (required)
        :type dnat_in: DnatIn
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: DnatRuleResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the post_dnat_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.post_dnat_with_http_info(router_id, dnat_in, **kwargs)  # noqa: E501

    @validate_arguments
    def post_dnat_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], dnat_in : DnatIn, **kwargs) -> ApiResponse:  # noqa: E501
        """Добавление правила проброса портов  # noqa: E501

        Чтобы добавить правило проброса портов (DNAT), отправьте POST-запрос на `/api/v1/routers/{router_id}/dnat-rules`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_dnat_with_http_info(router_id, dnat_in, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param dnat_in: (required)
        :type dnat_in: DnatIn
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
        :rtype: tuple(DnatRuleResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id',
            'dnat_in'
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
                    " to method post_dnat" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['dnat_in'] is not None:
            _body_params = _params['dnat_in']

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
            '201': "DnatRuleResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/dnat-rules', 'POST',
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
    def post_static_route(self, router_id : Annotated[Any, Field(..., description="ID роутера")], static_route_in : StaticRouteIn, **kwargs) -> StaticRouteResponse:  # noqa: E501
        """Добавление статического маршрута  # noqa: E501

        Чтобы добавить статический маршрут, отправьте POST-запрос на `/api/v1/routers/{router_id}/static-routes`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_static_route(router_id, static_route_in, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param static_route_in: (required)
        :type static_route_in: StaticRouteIn
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: StaticRouteResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the post_static_route_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.post_static_route_with_http_info(router_id, static_route_in, **kwargs)  # noqa: E501

    @validate_arguments
    def post_static_route_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], static_route_in : StaticRouteIn, **kwargs) -> ApiResponse:  # noqa: E501
        """Добавление статического маршрута  # noqa: E501

        Чтобы добавить статический маршрут, отправьте POST-запрос на `/api/v1/routers/{router_id}/static-routes`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post_static_route_with_http_info(router_id, static_route_in, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param static_route_in: (required)
        :type static_route_in: StaticRouteIn
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
        :rtype: tuple(StaticRouteResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id',
            'static_route_in'
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
                    " to method post_static_route" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['static_route_in'] is not None:
            _body_params = _params['static_route_in']

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
            '201': "StaticRouteResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/static-routes', 'POST',
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
    def update_router(self, router_id : Annotated[Any, Field(..., description="ID роутера")], router_edit : RouterEdit, **kwargs) -> RouterResponse:  # noqa: E501
        """Обновление информации о роутере  # noqa: E501

        Чтобы обновить информацию о роутере, отправьте PATCH-запрос на `/api/v1/routers/{router_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_router(router_id, router_edit, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param router_edit: (required)
        :type router_edit: RouterEdit
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RouterResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_router_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_router_with_http_info(router_id, router_edit, **kwargs)  # noqa: E501

    @validate_arguments
    def update_router_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], router_edit : RouterEdit, **kwargs) -> ApiResponse:  # noqa: E501
        """Обновление информации о роутере  # noqa: E501

        Чтобы обновить информацию о роутере, отправьте PATCH-запрос на `/api/v1/routers/{router_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_router_with_http_info(router_id, router_edit, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param router_edit: (required)
        :type router_edit: RouterEdit
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
        :rtype: tuple(RouterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id',
            'router_edit'
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
                    " to method update_router" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['router_edit'] is not None:
            _body_params = _params['router_edit']

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
            '200': "RouterResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}', 'PATCH',
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
    def update_router_nat(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_name : Annotated[Any, Field(..., description="Имя сети")], nat_in : NatIn, **kwargs) -> RouterResponse:  # noqa: E501
        """Включение NAT для сети  # noqa: E501

        Чтобы включить NAT для сети роутера, отправьте PATCH-запрос на `/api/v1/routers/{router_id}/networks/{network_name}/nat`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_router_nat(router_id, network_name, nat_in, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_name: Имя сети (required)
        :type network_name: object
        :param nat_in: (required)
        :type nat_in: NatIn
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RouterResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_router_nat_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_router_nat_with_http_info(router_id, network_name, nat_in, **kwargs)  # noqa: E501

    @validate_arguments
    def update_router_nat_with_http_info(self, router_id : Annotated[Any, Field(..., description="ID роутера")], network_name : Annotated[Any, Field(..., description="Имя сети")], nat_in : NatIn, **kwargs) -> ApiResponse:  # noqa: E501
        """Включение NAT для сети  # noqa: E501

        Чтобы включить NAT для сети роутера, отправьте PATCH-запрос на `/api/v1/routers/{router_id}/networks/{network_name}/nat`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_router_nat_with_http_info(router_id, network_name, nat_in, async_req=True)
        >>> result = thread.get()

        :param router_id: ID роутера (required)
        :type router_id: object
        :param network_name: Имя сети (required)
        :type network_name: object
        :param nat_in: (required)
        :type nat_in: NatIn
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
        :rtype: tuple(RouterResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'router_id',
            'network_name',
            'nat_in'
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
                    " to method update_router_nat" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['router_id']:
            _path_params['router_id'] = _params['router_id']

        if _params['network_name']:
            _path_params['network_name'] = _params['network_name']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['nat_in'] is not None:
            _body_params = _params['nat_in']

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
            '200': "RouterResponse",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/routers/{router_id}/networks/{network_name}/nat', 'PATCH',
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
