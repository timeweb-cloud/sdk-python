# coding: utf-8

"""
    Timeweb Cloud API

    # Введение API Timeweb Cloud позволяет вам управлять ресурсами в облаке программным способом с использованием обычных HTTP-запросов.  Множество функций, которые доступны в панели управления Timeweb Cloud, также доступны через API, что позволяет вам автоматизировать ваши собственные сценарии.  В этой документации сперва будет описан общий дизайн и принципы работы API, а после этого конкретные конечные точки. Также будут приведены примеры запросов к ним.   ## Запросы Запросы должны выполняться по протоколу `HTTPS`, чтобы гарантировать шифрование транзакций. Поддерживаются следующие методы запроса: |Метод|Применение| |--- |--- | |GET|Извлекает данные о коллекциях и отдельных ресурсах.| |POST|Для коллекций создает новый ресурс этого типа. Также используется для выполнения действий с конкретным ресурсом.| |PUT|Обновляет существующий ресурс.| |PATCH|Некоторые ресурсы поддерживают частичное обновление, то есть обновление только части атрибутов ресурса, в этом случае вместо метода PUT будет использован PATCH.| |DELETE|Удаляет ресурс.|  Методы `POST`, `PUT` и `PATCH` могут включать объект в тело запроса с типом содержимого `application/json`.  ### Параметры в запросах Некоторые коллекции поддерживают пагинацию, поиск или сортировку в запросах. В параметрах запроса требуется передать: - `limit` — обозначает количество записей, которое необходимо вернуть  - `offset` — указывает на смещение, относительно начала списка  - `search` — позволяет указать набор символов для поиска  - `sort` — можно задать правило сортировки коллекции  ## Ответы Запросы вернут один из следующих кодов состояния ответа HTTP:  |Статус|Описание| |--- |--- | |200 OK|Действие с ресурсом было выполнено успешно.| |201 Created|Ресурс был успешно создан. При этом ресурс может быть как уже готовым к использованию, так и находиться в процессе запуска.| |204 No Content|Действие с ресурсом было выполнено успешно, и ответ не содержит дополнительной информации в теле.| |400 Bad Request|Был отправлен неверный запрос, например, в нем отсутствуют обязательные параметры и т. д. Тело ответа будет содержать дополнительную информацию об ошибке.| |401 Unauthorized|Ошибка аутентификации.| |403 Forbidden|Аутентификация прошла успешно, но недостаточно прав для выполнения действия.| |404 Not Found|Запрашиваемый ресурс не найден.| |409 Conflict|Запрос конфликтует с текущим состоянием.| |423 Locked|Ресурс из запроса заблокирован от применения к нему указанного метода.| |429 Too Many Requests|Был достигнут лимит по количеству запросов в единицу времени.| |500 Internal Server Error|При выполнении запроса произошла какая-то внутренняя ошибка. Чтобы решить эту проблему, лучше всего создать тикет в панели управления.|  ### Структура успешного ответа Все конечные точки будут возвращать данные в формате `JSON`. Ответы на `GET`-запросы будут иметь на верхнем уровне следующую структуру атрибутов:  |Название поля|Тип|Описание| |--- |--- |--- | |[entity_name]|object, object[], string[], number[], boolean|Динамическое поле, которое будет меняться в зависимости от запрашиваемого ресурса и будет содержать все атрибуты, необходимые для описания этого ресурса. Например, при запросе списка баз данных будет возвращаться поле `dbs`, а при запросе конкретного облачного сервера `server`. Для некоторых конечных точек в ответе может возвращаться сразу несколько ресурсов.| |meta|object|Опционально. Объект, который содержит вспомогательную информацию о ресурсе. Чаще всего будет встречаться при запросе коллекций и содержать поле `total`, которое будет указывать на количество элементов в коллекции.| |response_id|string|Опционально. В большинстве случаев в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее. Также вы можете использовать этот идентификатор, чтобы убедиться, что это новый ответ на запрос и результат не был получен из кэша.|  Пример запроса на получение списка SSH-ключей: ```     HTTP/2.0 200 OK     {       \"ssh_keys\":[           {             \"body\":\"ssh-rsa AAAAB3NzaC1sdfghjkOAsBwWhs= example@device.local\",             \"created_at\":\"2021-09-15T19:52:27Z\",             \"expired_at\":null,             \"id\":5297,             \"is_default\":false,             \"name\":\"example@device.local\",             \"used_at\":null,             \"used_by\":[]           }       ],       \"meta\":{           \"total\":1       },       \"response_id\":\"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ### Структура ответа с ошибкой |Название поля|Тип|Описание| |--- |--- |--- | |status_code|number|Короткий числовой идентификатор ошибки.| |error_code|string|Короткий текстовый идентификатор ошибки, который уточняет числовой идентификатор и удобен для программной обработки. Самый простой пример — это код `not_found` для ошибки 404.| |message|string, string[]|Опционально. В большинстве случаев в ответе будет содержаться человекочитаемое подробное описание ошибки или ошибок, которые помогут понять, что нужно исправить.| |response_id|string|Опционально. В большинстве случае в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее.|  Пример: ```     HTTP/2.0 403 Forbidden     {       \"status_code\": 403,       \"error_code\":  \"forbidden\",       \"message\":     \"You do not have access for the attempted action\",       \"response_id\": \"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"     } ```  ## Статусы ресурсов Важно учесть, что при создании большинства ресурсов внутри платформы вам будет сразу возвращен ответ от сервера со статусом `200 OK` или `201 Created` и идентификатором созданного ресурса в теле ответа, но при этом этот ресурс может быть ещё в *состоянии запуска*.  Для того чтобы понять, в каком состоянии сейчас находится ваш ресурс, мы добавили поле `status` в ответ на получение информации о ресурсе.  Список статусов будет отличаться в зависимости от типа ресурса. Увидеть поддерживаемый список статусов вы сможете в описании каждого конкретного ресурса.     ## Ограничение скорости запросов (Rate Limiting) Чтобы обеспечить стабильность для всех пользователей, Timeweb Cloud защищает API от всплесков входящего трафика, анализируя количество запросов c каждого аккаунта к каждой конечной точке.  Если ваше приложение отправляет более 20 запросов в секунду на одну конечную точку, то для этого запроса API может вернуть код состояния HTTP `429 Too Many Requests`.   ## Аутентификация Доступ к API осуществляется с помощью JWT-токена. Токенами можно управлять внутри панели управления Timeweb Cloud в разделе *API и Terraform*.  Токен необходимо передавать в заголовке каждого запроса в формате: ```   Authorization: Bearer $TIMEWEB_CLOUD_TOKEN ```  ## Формат примеров API Примеры в этой документации описаны с помощью `curl`, HTTP-клиента командной строки. На компьютерах `Linux` и `macOS` обычно по умолчанию установлен `curl`, и он доступен для загрузки на всех популярных платформах, включая `Windows`.  Каждый пример разделен на несколько строк символом `\\`, который совместим с `bash`. Типичный пример выглядит так: ```   curl -X PATCH      -H \"Content-Type: application/json\"      -H \"Authorization: Bearer $TIMEWEB_CLOUD_TOKEN\"      -d '{\"name\":\"Cute Corvus\",\"comment\":\"Development Server\"}'      \"https://api.timeweb.cloud/api/v1/dedicated/1051\" ``` - Параметр `-X` задает метод запроса. Для согласованности метод будет указан во всех примерах, даже если он явно не требуется для методов `GET`. - Строки `-H` задают требуемые HTTP-заголовки. - Примеры, для которых требуется объект JSON в теле запроса, передают требуемые данные через параметр `-d`.  Чтобы использовать приведенные примеры, не подставляя каждый раз в них свой токен, вы можете добавить токен один раз в переменные окружения в вашей консоли. Например, на `Linux` это можно сделать с помощью команды:  ``` TIMEWEB_CLOUD_TOKEN=\"token\" ```  После этого токен будет автоматически подставляться в ваши запросы.  Обратите внимание, что все значения в этой документации являются примерами. Не полагайтесь на идентификаторы операционных систем, тарифов и т.д., используемые в примерах. Используйте соответствующую конечную точку для получения значений перед созданием ресурсов.   ## Версионирование API построено согласно принципам [семантического версионирования](https://semver.org/lang/ru). Это значит, что мы гарантируем обратную совместимость всех изменений в пределах одной мажорной версии.  Мажорная версия каждой конечной точки обозначается в пути запроса, например, запрос `/api/v1/servers` указывает, что этот метод имеет версию 1.  # noqa: E501

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

from openapi_client.models.firewall_group_in_api import FirewallGroupInAPI
from openapi_client.models.firewall_group_out_response import FirewallGroupOutResponse
from openapi_client.models.firewall_group_resource_out_response import FirewallGroupResourceOutResponse
from openapi_client.models.firewall_group_resources_out_response import FirewallGroupResourcesOutResponse
from openapi_client.models.firewall_groups_out_response import FirewallGroupsOutResponse
from openapi_client.models.firewall_rule_in_api import FirewallRuleInAPI
from openapi_client.models.firewall_rule_out_response import FirewallRuleOutResponse
from openapi_client.models.firewall_rules_out_response import FirewallRulesOutResponse
from openapi_client.models.resource_type import ResourceType

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class FirewallApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_resource_to_group(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], resource_id : Annotated[Any, Field(..., description="Идентификатор ресурса")], resource_type : Optional[ResourceType] = None, **kwargs) -> FirewallGroupResourceOutResponse:  # noqa: E501
        """Линковка ресурса в firewall group  # noqa: E501

        Чтобы слинковать ресурс с группой правил, отправьте POST запрос на `/api/v1/firewall/groups/{group_id}/resources/{resource_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_resource_to_group(group_id, resource_id, resource_type, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param resource_id: Идентификатор ресурса (required)
        :type resource_id: object
        :param resource_type:
        :type resource_type: ResourceType
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FirewallGroupResourceOutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the add_resource_to_group_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_resource_to_group_with_http_info(group_id, resource_id, resource_type, **kwargs)  # noqa: E501

    @validate_arguments
    def add_resource_to_group_with_http_info(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], resource_id : Annotated[Any, Field(..., description="Идентификатор ресурса")], resource_type : Optional[ResourceType] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Линковка ресурса в firewall group  # noqa: E501

        Чтобы слинковать ресурс с группой правил, отправьте POST запрос на `/api/v1/firewall/groups/{group_id}/resources/{resource_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_resource_to_group_with_http_info(group_id, resource_id, resource_type, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param resource_id: Идентификатор ресурса (required)
        :type resource_id: object
        :param resource_type:
        :type resource_type: ResourceType
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
        :rtype: tuple(FirewallGroupResourceOutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'group_id',
            'resource_id',
            'resource_type'
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
                    " to method add_resource_to_group" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['group_id']:
            _path_params['group_id'] = _params['group_id']

        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


        # process the query parameters
        _query_params = []
        if _params.get('resource_type') is not None:  # noqa: E501
            _query_params.append(('resource_type', _params['resource_type'].value))

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
            '201': "FirewallGroupResourceOutResponse",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/firewall/groups/{group_id}/resources/{resource_id}', 'POST',
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
    def create_group(self, firewall_group_in_api : FirewallGroupInAPI, **kwargs) -> FirewallGroupOutResponse:  # noqa: E501
        """Создание группы правил  # noqa: E501

        Чтобы создать группу правил, отправьте POST запрос на `/api/v1/firewall/groups`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_group(firewall_group_in_api, async_req=True)
        >>> result = thread.get()

        :param firewall_group_in_api: (required)
        :type firewall_group_in_api: FirewallGroupInAPI
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FirewallGroupOutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_group_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_group_with_http_info(firewall_group_in_api, **kwargs)  # noqa: E501

    @validate_arguments
    def create_group_with_http_info(self, firewall_group_in_api : FirewallGroupInAPI, **kwargs) -> ApiResponse:  # noqa: E501
        """Создание группы правил  # noqa: E501

        Чтобы создать группу правил, отправьте POST запрос на `/api/v1/firewall/groups`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_group_with_http_info(firewall_group_in_api, async_req=True)
        >>> result = thread.get()

        :param firewall_group_in_api: (required)
        :type firewall_group_in_api: FirewallGroupInAPI
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
        :rtype: tuple(FirewallGroupOutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'firewall_group_in_api'
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
                    " to method create_group" % _key
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
        if _params['firewall_group_in_api'] is not None:
            _body_params = _params['firewall_group_in_api']

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
            '201': "FirewallGroupOutResponse",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/firewall/groups', 'POST',
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
    def create_group_rule(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], firewall_rule_in_api : FirewallRuleInAPI, **kwargs) -> FirewallRuleOutResponse:  # noqa: E501
        """Создание firewall правила  # noqa: E501

        Чтобы создать правило в группе, отправьте POST запрос на `/api/v1/firewall/groups/{group_id}/rules`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_group_rule(group_id, firewall_rule_in_api, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param firewall_rule_in_api: (required)
        :type firewall_rule_in_api: FirewallRuleInAPI
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FirewallRuleOutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_group_rule_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_group_rule_with_http_info(group_id, firewall_rule_in_api, **kwargs)  # noqa: E501

    @validate_arguments
    def create_group_rule_with_http_info(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], firewall_rule_in_api : FirewallRuleInAPI, **kwargs) -> ApiResponse:  # noqa: E501
        """Создание firewall правила  # noqa: E501

        Чтобы создать правило в группе, отправьте POST запрос на `/api/v1/firewall/groups/{group_id}/rules`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_group_rule_with_http_info(group_id, firewall_rule_in_api, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param firewall_rule_in_api: (required)
        :type firewall_rule_in_api: FirewallRuleInAPI
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
        :rtype: tuple(FirewallRuleOutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'group_id',
            'firewall_rule_in_api'
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
                    " to method create_group_rule" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['group_id']:
            _path_params['group_id'] = _params['group_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['firewall_rule_in_api'] is not None:
            _body_params = _params['firewall_rule_in_api']

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
            '201': "FirewallRuleOutResponse",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/firewall/groups/{group_id}/rules', 'POST',
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
    def delete_group(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], **kwargs) -> None:  # noqa: E501
        """Удаление группы правил  # noqa: E501

        Чтобы удалить группу правил, отправьте DELETE запрос на `/api/v1/firewall/groups/{group_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_group(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
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
            raise ValueError("Error! Please call the delete_group_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_group_with_http_info(group_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_group_with_http_info(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление группы правил  # noqa: E501

        Чтобы удалить группу правил, отправьте DELETE запрос на `/api/v1/firewall/groups/{group_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_group_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
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
            'group_id'
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
                    " to method delete_group" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['group_id']:
            _path_params['group_id'] = _params['group_id']


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
            '/api/v1/firewall/groups/{group_id}', 'DELETE',
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
    def delete_group_rule(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], rule_id : Annotated[Any, Field(..., description="Идентификатор правила")], **kwargs) -> None:  # noqa: E501
        """Удаление firewall правила  # noqa: E501

        Чтобы удалить правило, отправьте DELETE запрос на `/api/v1/firewall/groups/{group_id}/rules/{rule_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_group_rule(group_id, rule_id, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param rule_id: Идентификатор правила (required)
        :type rule_id: object
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
            raise ValueError("Error! Please call the delete_group_rule_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_group_rule_with_http_info(group_id, rule_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_group_rule_with_http_info(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], rule_id : Annotated[Any, Field(..., description="Идентификатор правила")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление firewall правила  # noqa: E501

        Чтобы удалить правило, отправьте DELETE запрос на `/api/v1/firewall/groups/{group_id}/rules/{rule_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_group_rule_with_http_info(group_id, rule_id, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param rule_id: Идентификатор правила (required)
        :type rule_id: object
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
            'group_id',
            'rule_id'
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
                    " to method delete_group_rule" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['group_id']:
            _path_params['group_id'] = _params['group_id']

        if _params['rule_id']:
            _path_params['rule_id'] = _params['rule_id']


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
            '/api/v1/firewall/groups/{group_id}/rules/{rule_id}', 'DELETE',
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
    def delete_resource_from_group(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], resource_id : Annotated[Any, Field(..., description="Идентификатор ресурса")], resource_type : Optional[ResourceType] = None, **kwargs) -> None:  # noqa: E501
        """Отлинковка ресурса из firewall group  # noqa: E501

        Чтобы отлинковать ресурс от группы правил, отправьте DELETE запрос на `/api/v1/firewall/groups/{group_id}/resources/{resource_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_resource_from_group(group_id, resource_id, resource_type, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param resource_id: Идентификатор ресурса (required)
        :type resource_id: object
        :param resource_type:
        :type resource_type: ResourceType
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
            raise ValueError("Error! Please call the delete_resource_from_group_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_resource_from_group_with_http_info(group_id, resource_id, resource_type, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_resource_from_group_with_http_info(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], resource_id : Annotated[Any, Field(..., description="Идентификатор ресурса")], resource_type : Optional[ResourceType] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Отлинковка ресурса из firewall group  # noqa: E501

        Чтобы отлинковать ресурс от группы правил, отправьте DELETE запрос на `/api/v1/firewall/groups/{group_id}/resources/{resource_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_resource_from_group_with_http_info(group_id, resource_id, resource_type, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param resource_id: Идентификатор ресурса (required)
        :type resource_id: object
        :param resource_type:
        :type resource_type: ResourceType
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
            'group_id',
            'resource_id',
            'resource_type'
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
                    " to method delete_resource_from_group" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['group_id']:
            _path_params['group_id'] = _params['group_id']

        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']


        # process the query parameters
        _query_params = []
        if _params.get('resource_type') is not None:  # noqa: E501
            _query_params.append(('resource_type', _params['resource_type'].value))

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
            '/api/v1/firewall/groups/{group_id}/resources/{resource_id}', 'DELETE',
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
    def get_group(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], **kwargs) -> FirewallGroupOutResponse:  # noqa: E501
        """Получение информации о группе правил  # noqa: E501

        Чтобы получить информацию о группе правил, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FirewallGroupOutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_group_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_group_with_http_info(group_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_group_with_http_info(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение информации о группе правил  # noqa: E501

        Чтобы получить информацию о группе правил, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group_with_http_info(group_id, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
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
        :rtype: tuple(FirewallGroupOutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'group_id'
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
                    " to method get_group" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['group_id']:
            _path_params['group_id'] = _params['group_id']


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
            '200': "FirewallGroupOutResponse",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/firewall/groups/{group_id}', 'GET',
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
    def get_group_resources(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> FirewallGroupResourcesOutResponse:  # noqa: E501
        """Получение слинкованных ресурсов  # noqa: E501

        Чтобы получить слинкованных ресурсов для группы правил, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}/resources`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group_resources(group_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param limit: Обозначает количество записей, которое необходимо вернуть.
        :type limit: object
        :param offset: Указывает на смещение относительно начала списка.
        :type offset: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FirewallGroupResourcesOutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_group_resources_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_group_resources_with_http_info(group_id, limit, offset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_group_resources_with_http_info(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение слинкованных ресурсов  # noqa: E501

        Чтобы получить слинкованных ресурсов для группы правил, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}/resources`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group_resources_with_http_info(group_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param limit: Обозначает количество записей, которое необходимо вернуть.
        :type limit: object
        :param offset: Указывает на смещение относительно начала списка.
        :type offset: object
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
        :rtype: tuple(FirewallGroupResourcesOutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'group_id',
            'limit',
            'offset'
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
                    " to method get_group_resources" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['group_id']:
            _path_params['group_id'] = _params['group_id']


        # process the query parameters
        _query_params = []
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

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
            '200': "FirewallGroupResourcesOutResponse",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/firewall/groups/{group_id}/resources', 'GET',
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
    def get_group_rule(self, rule_id : Annotated[Any, Field(..., description="Идентификатор правила")], group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], **kwargs) -> FirewallRuleOutResponse:  # noqa: E501
        """Получение информации о правиле  # noqa: E501

        Чтобы получить инфомрацию о правиле, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}/rules/{rule_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group_rule(rule_id, group_id, async_req=True)
        >>> result = thread.get()

        :param rule_id: Идентификатор правила (required)
        :type rule_id: object
        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FirewallRuleOutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_group_rule_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_group_rule_with_http_info(rule_id, group_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_group_rule_with_http_info(self, rule_id : Annotated[Any, Field(..., description="Идентификатор правила")], group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение информации о правиле  # noqa: E501

        Чтобы получить инфомрацию о правиле, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}/rules/{rule_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group_rule_with_http_info(rule_id, group_id, async_req=True)
        >>> result = thread.get()

        :param rule_id: Идентификатор правила (required)
        :type rule_id: object
        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
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
        :rtype: tuple(FirewallRuleOutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'rule_id',
            'group_id'
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
                    " to method get_group_rule" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['rule_id']:
            _path_params['rule_id'] = _params['rule_id']

        if _params['group_id']:
            _path_params['group_id'] = _params['group_id']


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
            '200': "FirewallRuleOutResponse",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/firewall/groups/{group_id}/rules/{rule_id}', 'GET',
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
    def get_group_rules(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> FirewallRulesOutResponse:  # noqa: E501
        """Получение списка правил  # noqa: E501

        Чтобы получить список правил в группе, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}/rules`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group_rules(group_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param limit: Обозначает количество записей, которое необходимо вернуть.
        :type limit: object
        :param offset: Указывает на смещение относительно начала списка.
        :type offset: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FirewallRulesOutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_group_rules_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_group_rules_with_http_info(group_id, limit, offset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_group_rules_with_http_info(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка правил  # noqa: E501

        Чтобы получить список правил в группе, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}/rules`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_group_rules_with_http_info(group_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param limit: Обозначает количество записей, которое необходимо вернуть.
        :type limit: object
        :param offset: Указывает на смещение относительно начала списка.
        :type offset: object
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
        :rtype: tuple(FirewallRulesOutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'group_id',
            'limit',
            'offset'
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
                    " to method get_group_rules" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['group_id']:
            _path_params['group_id'] = _params['group_id']


        # process the query parameters
        _query_params = []
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

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
            '200': "FirewallRulesOutResponse",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/firewall/groups/{group_id}/rules', 'GET',
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
    def get_groups(self, limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> FirewallGroupsOutResponse:  # noqa: E501
        """Получение групп правил  # noqa: E501

        Чтобы получить групп правил для аккаунта, отправьте GET запрос на `/api/v1/firewall/groups`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_groups(limit, offset, async_req=True)
        >>> result = thread.get()

        :param limit: Обозначает количество записей, которое необходимо вернуть.
        :type limit: object
        :param offset: Указывает на смещение относительно начала списка.
        :type offset: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FirewallGroupsOutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_groups_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_groups_with_http_info(limit, offset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_groups_with_http_info(self, limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение групп правил  # noqa: E501

        Чтобы получить групп правил для аккаунта, отправьте GET запрос на `/api/v1/firewall/groups`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_groups_with_http_info(limit, offset, async_req=True)
        >>> result = thread.get()

        :param limit: Обозначает количество записей, которое необходимо вернуть.
        :type limit: object
        :param offset: Указывает на смещение относительно начала списка.
        :type offset: object
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
        :rtype: tuple(FirewallGroupsOutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'limit',
            'offset'
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
                    " to method get_groups" % _key
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

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

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
            '200': "FirewallGroupsOutResponse",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/firewall/groups', 'GET',
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
    def get_rules_for_resource(self, resource_id : Annotated[Any, Field(..., description="Идентификатор ресурса")], resource_type : ResourceType, limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> FirewallGroupsOutResponse:  # noqa: E501
        """Получение групп правил для ресурса  # noqa: E501

        Чтобы получить список групп правил, с которыми слинкован ресурс, отправьте GET запрос на `/api/v1/firewall/service/{resource_type}/{resource_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_rules_for_resource(resource_id, resource_type, limit, offset, async_req=True)
        >>> result = thread.get()

        :param resource_id: Идентификатор ресурса (required)
        :type resource_id: object
        :param resource_type: (required)
        :type resource_type: ResourceType
        :param limit: Обозначает количество записей, которое необходимо вернуть.
        :type limit: object
        :param offset: Указывает на смещение относительно начала списка.
        :type offset: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FirewallGroupsOutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_rules_for_resource_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_rules_for_resource_with_http_info(resource_id, resource_type, limit, offset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_rules_for_resource_with_http_info(self, resource_id : Annotated[Any, Field(..., description="Идентификатор ресурса")], resource_type : ResourceType, limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение групп правил для ресурса  # noqa: E501

        Чтобы получить список групп правил, с которыми слинкован ресурс, отправьте GET запрос на `/api/v1/firewall/service/{resource_type}/{resource_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_rules_for_resource_with_http_info(resource_id, resource_type, limit, offset, async_req=True)
        >>> result = thread.get()

        :param resource_id: Идентификатор ресурса (required)
        :type resource_id: object
        :param resource_type: (required)
        :type resource_type: ResourceType
        :param limit: Обозначает количество записей, которое необходимо вернуть.
        :type limit: object
        :param offset: Указывает на смещение относительно начала списка.
        :type offset: object
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
        :rtype: tuple(FirewallGroupsOutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'resource_id',
            'resource_type',
            'limit',
            'offset'
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
                    " to method get_rules_for_resource" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['resource_id']:
            _path_params['resource_id'] = _params['resource_id']

        if _params['resource_type']:
            _path_params['resource_type'] = _params['resource_type']


        # process the query parameters
        _query_params = []
        if _params.get('limit') is not None:  # noqa: E501
            _query_params.append(('limit', _params['limit']))

        if _params.get('offset') is not None:  # noqa: E501
            _query_params.append(('offset', _params['offset']))

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
            '200': "FirewallGroupsOutResponse",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/firewall/service/{resource_type}/{resource_id}', 'GET',
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
    def update_group(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], firewall_group_in_api : FirewallGroupInAPI, **kwargs) -> FirewallGroupOutResponse:  # noqa: E501
        """Обновление группы правил  # noqa: E501

        Чтобы изменить группу правил, отправьте PATCH запрос на `/api/v1/firewall/groups/{group_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_group(group_id, firewall_group_in_api, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param firewall_group_in_api: (required)
        :type firewall_group_in_api: FirewallGroupInAPI
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FirewallGroupOutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_group_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_group_with_http_info(group_id, firewall_group_in_api, **kwargs)  # noqa: E501

    @validate_arguments
    def update_group_with_http_info(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], firewall_group_in_api : FirewallGroupInAPI, **kwargs) -> ApiResponse:  # noqa: E501
        """Обновление группы правил  # noqa: E501

        Чтобы изменить группу правил, отправьте PATCH запрос на `/api/v1/firewall/groups/{group_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_group_with_http_info(group_id, firewall_group_in_api, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param firewall_group_in_api: (required)
        :type firewall_group_in_api: FirewallGroupInAPI
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
        :rtype: tuple(FirewallGroupOutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'group_id',
            'firewall_group_in_api'
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
                    " to method update_group" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['group_id']:
            _path_params['group_id'] = _params['group_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['firewall_group_in_api'] is not None:
            _body_params = _params['firewall_group_in_api']

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
            '201': "FirewallGroupOutResponse",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/firewall/groups/{group_id}', 'PATCH',
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
    def update_group_rule(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], rule_id : Annotated[Any, Field(..., description="Идентификатор правила")], firewall_rule_in_api : FirewallRuleInAPI, **kwargs) -> FirewallRuleOutResponse:  # noqa: E501
        """Обновление firewall правила  # noqa: E501

        Чтобы изменить правило, отправьте PATCH запрос на `/api/v1/firewall/groups/{group_id}/rules/{rule_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_group_rule(group_id, rule_id, firewall_rule_in_api, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param rule_id: Идентификатор правила (required)
        :type rule_id: object
        :param firewall_rule_in_api: (required)
        :type firewall_rule_in_api: FirewallRuleInAPI
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: FirewallRuleOutResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_group_rule_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_group_rule_with_http_info(group_id, rule_id, firewall_rule_in_api, **kwargs)  # noqa: E501

    @validate_arguments
    def update_group_rule_with_http_info(self, group_id : Annotated[Any, Field(..., description="Идентификатор группы правил")], rule_id : Annotated[Any, Field(..., description="Идентификатор правила")], firewall_rule_in_api : FirewallRuleInAPI, **kwargs) -> ApiResponse:  # noqa: E501
        """Обновление firewall правила  # noqa: E501

        Чтобы изменить правило, отправьте PATCH запрос на `/api/v1/firewall/groups/{group_id}/rules/{rule_id}`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_group_rule_with_http_info(group_id, rule_id, firewall_rule_in_api, async_req=True)
        >>> result = thread.get()

        :param group_id: Идентификатор группы правил (required)
        :type group_id: object
        :param rule_id: Идентификатор правила (required)
        :type rule_id: object
        :param firewall_rule_in_api: (required)
        :type firewall_rule_in_api: FirewallRuleInAPI
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
        :rtype: tuple(FirewallRuleOutResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'group_id',
            'rule_id',
            'firewall_rule_in_api'
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
                    " to method update_group_rule" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['group_id']:
            _path_params['group_id'] = _params['group_id']

        if _params['rule_id']:
            _path_params['rule_id'] = _params['rule_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['firewall_rule_in_api'] is not None:
            _body_params = _params['firewall_rule_in_api']

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
            '201': "FirewallRuleOutResponse",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/firewall/groups/{group_id}/rules/{rule_id}', 'PATCH',
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
