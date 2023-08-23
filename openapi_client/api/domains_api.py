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

from openapi_client.models.add_subdomain201_response import AddSubdomain201Response
from openapi_client.models.check_domain200_response import CheckDomain200Response
from openapi_client.models.create_dns import CreateDns
from openapi_client.models.create_domain_dns_record201_response import CreateDomainDNSRecord201Response
from openapi_client.models.create_domain_request201_response import CreateDomainRequest201Response
from openapi_client.models.domain_register import DomainRegister
from openapi_client.models.get_domain200_response import GetDomain200Response
from openapi_client.models.get_domain_dns_records200_response import GetDomainDNSRecords200Response
from openapi_client.models.get_domain_name_servers200_response import GetDomainNameServers200Response
from openapi_client.models.get_domain_requests200_response import GetDomainRequests200Response
from openapi_client.models.get_domains200_response import GetDomains200Response
from openapi_client.models.get_tld200_response import GetTLD200Response
from openapi_client.models.get_tlds200_response import GetTLDs200Response
from openapi_client.models.update_domain import UpdateDomain
from openapi_client.models.update_domain_auto_prolongation200_response import UpdateDomainAutoProlongation200Response
from openapi_client.models.update_domain_name_servers import UpdateDomainNameServers
from openapi_client.models.use import Use

from openapi_client.api_client import ApiClient
from openapi_client.api_response import ApiResponse
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DomainsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_domain(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], **kwargs) -> None:  # noqa: E501
        """Добавление домена на аккаунт  # noqa: E501

        Чтобы добавить домен на свой аккаунт, отправьте запрос POST на `/api/v1/add-domain/{fqdn}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_domain(fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
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
            raise ValueError("Error! Please call the add_domain_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_domain_with_http_info(fqdn, **kwargs)  # noqa: E501

    @validate_arguments
    def add_domain_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Добавление домена на аккаунт  # noqa: E501

        Чтобы добавить домен на свой аккаунт, отправьте запрос POST на `/api/v1/add-domain/{fqdn}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_domain_with_http_info(fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
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
            'fqdn'
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
                    " to method add_domain" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']


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
            '/api/v1/add-domain/{fqdn}', 'POST',
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
    def add_subdomain(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], subdomain_fqdn : Annotated[Any, Field(..., description="Полное имя поддомена.")], **kwargs) -> AddSubdomain201Response:  # noqa: E501
        """Добавление поддомена  # noqa: E501

        Чтобы добавить поддомен, отправьте запрос POST на `/api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn}`, задав необходимые атрибуты.  Поддомен будет добавлен с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о добавленном поддомене.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_subdomain(fqdn, subdomain_fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
        :param subdomain_fqdn: Полное имя поддомена. (required)
        :type subdomain_fqdn: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddSubdomain201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the add_subdomain_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_subdomain_with_http_info(fqdn, subdomain_fqdn, **kwargs)  # noqa: E501

    @validate_arguments
    def add_subdomain_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], subdomain_fqdn : Annotated[Any, Field(..., description="Полное имя поддомена.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Добавление поддомена  # noqa: E501

        Чтобы добавить поддомен, отправьте запрос POST на `/api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn}`, задав необходимые атрибуты.  Поддомен будет добавлен с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о добавленном поддомене.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_subdomain_with_http_info(fqdn, subdomain_fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
        :param subdomain_fqdn: Полное имя поддомена. (required)
        :type subdomain_fqdn: object
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
        :rtype: tuple(AddSubdomain201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'fqdn',
            'subdomain_fqdn'
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
                    " to method add_subdomain" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']

        if _params['subdomain_fqdn']:
            _path_params['subdomain_fqdn'] = _params['subdomain_fqdn']


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
            '201': "AddSubdomain201Response",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn}', 'POST',
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
    def check_domain(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], **kwargs) -> CheckDomain200Response:  # noqa: E501
        """Проверить, доступен ли домен для регистрации  # noqa: E501

        Чтобы проверить, доступен ли домен для регистрации, отправьте запрос GET на `/api/v1/check-domain/{fqdn}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_domain(fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CheckDomain200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the check_domain_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.check_domain_with_http_info(fqdn, **kwargs)  # noqa: E501

    @validate_arguments
    def check_domain_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Проверить, доступен ли домен для регистрации  # noqa: E501

        Чтобы проверить, доступен ли домен для регистрации, отправьте запрос GET на `/api/v1/check-domain/{fqdn}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_domain_with_http_info(fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
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
        :rtype: tuple(CheckDomain200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'fqdn'
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
                    " to method check_domain" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']


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
            '200': "CheckDomain200Response",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/check-domain/{fqdn}', 'GET',
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
    def create_domain_dns_record(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена или поддомена.")], create_dns : CreateDns, **kwargs) -> CreateDomainDNSRecord201Response:  # noqa: E501
        """Добавить информацию о DNS-записи для домена или поддомена  # noqa: E501

        Чтобы добавить информацию о DNS-записи для домена или поддомена, отправьте запрос POST на `/api/v1/domains/{fqdn}/dns-records`, задав необходимые атрибуты.  DNS-запись будет добавлена с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о добавленной DNS-записи.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_domain_dns_record(fqdn, create_dns, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена или поддомена. (required)
        :type fqdn: object
        :param create_dns: (required)
        :type create_dns: CreateDns
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateDomainDNSRecord201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_domain_dns_record_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_domain_dns_record_with_http_info(fqdn, create_dns, **kwargs)  # noqa: E501

    @validate_arguments
    def create_domain_dns_record_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена или поддомена.")], create_dns : CreateDns, **kwargs) -> ApiResponse:  # noqa: E501
        """Добавить информацию о DNS-записи для домена или поддомена  # noqa: E501

        Чтобы добавить информацию о DNS-записи для домена или поддомена, отправьте запрос POST на `/api/v1/domains/{fqdn}/dns-records`, задав необходимые атрибуты.  DNS-запись будет добавлена с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о добавленной DNS-записи.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_domain_dns_record_with_http_info(fqdn, create_dns, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена или поддомена. (required)
        :type fqdn: object
        :param create_dns: (required)
        :type create_dns: CreateDns
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
        :rtype: tuple(CreateDomainDNSRecord201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'fqdn',
            'create_dns'
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
                    " to method create_domain_dns_record" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_dns'] is not None:
            _body_params = _params['create_dns']

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
            '201': "CreateDomainDNSRecord201Response",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains/{fqdn}/dns-records', 'POST',
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
    def create_domain_request(self, domain_register : DomainRegister, **kwargs) -> CreateDomainRequest201Response:  # noqa: E501
        """Создание заявки на регистрацию/продление/трансфер домена  # noqa: E501

        Чтобы создать заявку на регистрацию/продление/трансфер домена, отправьте POST-запрос в `api/v1/domains-requests`, задав необходимые атрибуты.  Заявка будет создана с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданной заявке.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_domain_request(domain_register, async_req=True)
        >>> result = thread.get()

        :param domain_register: (required)
        :type domain_register: DomainRegister
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateDomainRequest201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_domain_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_domain_request_with_http_info(domain_register, **kwargs)  # noqa: E501

    @validate_arguments
    def create_domain_request_with_http_info(self, domain_register : DomainRegister, **kwargs) -> ApiResponse:  # noqa: E501
        """Создание заявки на регистрацию/продление/трансфер домена  # noqa: E501

        Чтобы создать заявку на регистрацию/продление/трансфер домена, отправьте POST-запрос в `api/v1/domains-requests`, задав необходимые атрибуты.  Заявка будет создана с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданной заявке.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_domain_request_with_http_info(domain_register, async_req=True)
        >>> result = thread.get()

        :param domain_register: (required)
        :type domain_register: DomainRegister
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
        :rtype: tuple(CreateDomainRequest201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'domain_register'
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
                    " to method create_domain_request" % _key
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
        if _params['domain_register'] is not None:
            _body_params = _params['domain_register']

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
            '201': "CreateDomainRequest201Response",
            '400': None,
            '401': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains-requests', 'POST',
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
    def delete_domain(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], **kwargs) -> None:  # noqa: E501
        """Удаление домена  # noqa: E501

        Чтобы удалить домен, отправьте запрос DELETE на `/api/v1/domains/{fqdn}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_domain(fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
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
            raise ValueError("Error! Please call the delete_domain_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_domain_with_http_info(fqdn, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_domain_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление домена  # noqa: E501

        Чтобы удалить домен, отправьте запрос DELETE на `/api/v1/domains/{fqdn}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_domain_with_http_info(fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
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
            'fqdn'
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
                    " to method delete_domain" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']


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
            '/api/v1/domains/{fqdn}', 'DELETE',
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
    def delete_domain_dns_record(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена или поддомена.")], record_id : Annotated[Any, Field(..., description="Идентификатор DNS-записи домена или поддомена.")], **kwargs) -> None:  # noqa: E501
        """Удалить информацию о DNS-записи для домена или поддомена  # noqa: E501

        Чтобы удалить информацию о DNS-записи для домена или поддомена, отправьте запрос DELETE на `/api/v1/domains/{fqdn}/dns-records/{record_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_domain_dns_record(fqdn, record_id, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена или поддомена. (required)
        :type fqdn: object
        :param record_id: Идентификатор DNS-записи домена или поддомена. (required)
        :type record_id: object
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
            raise ValueError("Error! Please call the delete_domain_dns_record_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_domain_dns_record_with_http_info(fqdn, record_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_domain_dns_record_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена или поддомена.")], record_id : Annotated[Any, Field(..., description="Идентификатор DNS-записи домена или поддомена.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удалить информацию о DNS-записи для домена или поддомена  # noqa: E501

        Чтобы удалить информацию о DNS-записи для домена или поддомена, отправьте запрос DELETE на `/api/v1/domains/{fqdn}/dns-records/{record_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_domain_dns_record_with_http_info(fqdn, record_id, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена или поддомена. (required)
        :type fqdn: object
        :param record_id: Идентификатор DNS-записи домена или поддомена. (required)
        :type record_id: object
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
            'fqdn',
            'record_id'
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
                    " to method delete_domain_dns_record" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']

        if _params['record_id']:
            _path_params['record_id'] = _params['record_id']


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
            '/api/v1/domains/{fqdn}/dns-records/{record_id}', 'DELETE',
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
    def delete_subdomain(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], subdomain_fqdn : Annotated[Any, Field(..., description="Полное имя поддомена.")], **kwargs) -> None:  # noqa: E501
        """Удаление поддомена  # noqa: E501

        Чтобы удалить поддомен, отправьте запрос DELETE на `/api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_subdomain(fqdn, subdomain_fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
        :param subdomain_fqdn: Полное имя поддомена. (required)
        :type subdomain_fqdn: object
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
            raise ValueError("Error! Please call the delete_subdomain_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_subdomain_with_http_info(fqdn, subdomain_fqdn, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_subdomain_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], subdomain_fqdn : Annotated[Any, Field(..., description="Полное имя поддомена.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление поддомена  # noqa: E501

        Чтобы удалить поддомен, отправьте запрос DELETE на `/api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_subdomain_with_http_info(fqdn, subdomain_fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
        :param subdomain_fqdn: Полное имя поддомена. (required)
        :type subdomain_fqdn: object
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
            'fqdn',
            'subdomain_fqdn'
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
                    " to method delete_subdomain" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']

        if _params['subdomain_fqdn']:
            _path_params['subdomain_fqdn'] = _params['subdomain_fqdn']


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
            '/api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn}', 'DELETE',
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
    def get_domain(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], **kwargs) -> GetDomain200Response:  # noqa: E501
        """Получение информации о домене  # noqa: E501

        Чтобы отобразить информацию об отдельном домене, отправьте запрос GET на `/api/v1/domains/{fqdn}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain(fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetDomain200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_domain_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_domain_with_http_info(fqdn, **kwargs)  # noqa: E501

    @validate_arguments
    def get_domain_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение информации о домене  # noqa: E501

        Чтобы отобразить информацию об отдельном домене, отправьте запрос GET на `/api/v1/domains/{fqdn}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_with_http_info(fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
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
        :rtype: tuple(GetDomain200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'fqdn'
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
                    " to method get_domain" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']


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
            '200': "GetDomain200Response",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains/{fqdn}', 'GET',
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
    def get_domain_default_dns_records(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена или поддомена.")], limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> GetDomainDNSRecords200Response:  # noqa: E501
        """Получить информацию обо всех DNS-записях по умолчанию домена или поддомена  # noqa: E501

        Чтобы получить информацию обо всех DNS-записях по умолчанию домена или поддомена, отправьте запрос GET на `/api/v1/domains/{fqdn}/default-dns-records`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_default_dns_records(fqdn, limit, offset, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена или поддомена. (required)
        :type fqdn: object
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
        :rtype: GetDomainDNSRecords200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_domain_default_dns_records_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_domain_default_dns_records_with_http_info(fqdn, limit, offset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_domain_default_dns_records_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена или поддомена.")], limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получить информацию обо всех DNS-записях по умолчанию домена или поддомена  # noqa: E501

        Чтобы получить информацию обо всех DNS-записях по умолчанию домена или поддомена, отправьте запрос GET на `/api/v1/domains/{fqdn}/default-dns-records`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_default_dns_records_with_http_info(fqdn, limit, offset, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена или поддомена. (required)
        :type fqdn: object
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
        :rtype: tuple(GetDomainDNSRecords200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'fqdn',
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
                    " to method get_domain_default_dns_records" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']


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
            '200': "GetDomainDNSRecords200Response",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains/{fqdn}/default-dns-records', 'GET',
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
    def get_domain_dns_records(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена или поддомена.")], limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> GetDomainDNSRecords200Response:  # noqa: E501
        """Получить информацию обо всех пользовательских DNS-записях домена или поддомена  # noqa: E501

        Чтобы получить информацию обо всех пользовательских DNS-записях домена или поддомена, отправьте запрос GET на `/api/v1/domains/{fqdn}/dns-records`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_dns_records(fqdn, limit, offset, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена или поддомена. (required)
        :type fqdn: object
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
        :rtype: GetDomainDNSRecords200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_domain_dns_records_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_domain_dns_records_with_http_info(fqdn, limit, offset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_domain_dns_records_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена или поддомена.")], limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получить информацию обо всех пользовательских DNS-записях домена или поддомена  # noqa: E501

        Чтобы получить информацию обо всех пользовательских DNS-записях домена или поддомена, отправьте запрос GET на `/api/v1/domains/{fqdn}/dns-records`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_dns_records_with_http_info(fqdn, limit, offset, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена или поддомена. (required)
        :type fqdn: object
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
        :rtype: tuple(GetDomainDNSRecords200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'fqdn',
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
                    " to method get_domain_dns_records" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']


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
            '200': "GetDomainDNSRecords200Response",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains/{fqdn}/dns-records', 'GET',
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
    def get_domain_name_servers(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], **kwargs) -> GetDomainNameServers200Response:  # noqa: E501
        """Получение списка name-серверов домена  # noqa: E501

        Чтобы получить список name-серверов домена, отправьте запрос GET на `/api/v1/domains/{fqdn}/name-servers`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_name_servers(fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetDomainNameServers200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_domain_name_servers_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_domain_name_servers_with_http_info(fqdn, **kwargs)  # noqa: E501

    @validate_arguments
    def get_domain_name_servers_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка name-серверов домена  # noqa: E501

        Чтобы получить список name-серверов домена, отправьте запрос GET на `/api/v1/domains/{fqdn}/name-servers`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_name_servers_with_http_info(fqdn, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
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
        :rtype: tuple(GetDomainNameServers200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'fqdn'
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
                    " to method get_domain_name_servers" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']


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
            '200': "GetDomainNameServers200Response",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains/{fqdn}/name-servers', 'GET',
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
    def get_domain_request(self, request_id : Annotated[Any, Field(..., description="Идентификатор заявки на регистрацию/продление/трансфер домена.")], **kwargs) -> CreateDomainRequest201Response:  # noqa: E501
        """Получение заявки на регистрацию/продление/трансфер домена  # noqa: E501

        Чтобы получить заявку на регистрацию/продление/трансфер домена, отправьте запрос GET на `/api/v1/domains-requests/{request_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_request(request_id, async_req=True)
        >>> result = thread.get()

        :param request_id: Идентификатор заявки на регистрацию/продление/трансфер домена. (required)
        :type request_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateDomainRequest201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_domain_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_domain_request_with_http_info(request_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_domain_request_with_http_info(self, request_id : Annotated[Any, Field(..., description="Идентификатор заявки на регистрацию/продление/трансфер домена.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение заявки на регистрацию/продление/трансфер домена  # noqa: E501

        Чтобы получить заявку на регистрацию/продление/трансфер домена, отправьте запрос GET на `/api/v1/domains-requests/{request_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_request_with_http_info(request_id, async_req=True)
        >>> result = thread.get()

        :param request_id: Идентификатор заявки на регистрацию/продление/трансфер домена. (required)
        :type request_id: object
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
        :rtype: tuple(CreateDomainRequest201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'request_id'
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
                    " to method get_domain_request" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['request_id']:
            _path_params['request_id'] = _params['request_id']


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
            '200': "CreateDomainRequest201Response",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains-requests/{request_id}', 'GET',
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
    def get_domain_requests(self, person_id : Annotated[Optional[Any], Field(description="Идентификатор администратора, на которого зарегистрирован домен.")] = None, **kwargs) -> GetDomainRequests200Response:  # noqa: E501
        """Получение списка заявок на регистрацию/продление/трансфер домена  # noqa: E501

        Чтобы получить список заявок на регистрацию/продление/трансфер домена, отправьте запрос GET на `/api/v1/domains-requests`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_requests(person_id, async_req=True)
        >>> result = thread.get()

        :param person_id: Идентификатор администратора, на которого зарегистрирован домен.
        :type person_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetDomainRequests200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_domain_requests_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_domain_requests_with_http_info(person_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_domain_requests_with_http_info(self, person_id : Annotated[Optional[Any], Field(description="Идентификатор администратора, на которого зарегистрирован домен.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка заявок на регистрацию/продление/трансфер домена  # noqa: E501

        Чтобы получить список заявок на регистрацию/продление/трансфер домена, отправьте запрос GET на `/api/v1/domains-requests`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_requests_with_http_info(person_id, async_req=True)
        >>> result = thread.get()

        :param person_id: Идентификатор администратора, на которого зарегистрирован домен.
        :type person_id: object
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
        :rtype: tuple(GetDomainRequests200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'person_id'
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
                    " to method get_domain_requests" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('person_id') is not None:  # noqa: E501
            _query_params.append(('person_id', _params['person_id']))

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
            '200': "GetDomainRequests200Response",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains-requests', 'GET',
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
    def get_domains(self, limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, idn_name : Annotated[Optional[Any], Field(description="Интернационализированное доменное имя.")] = None, linked_ip : Annotated[Optional[Any], Field(description="Привязанный к домену IP-адрес.")] = None, order : Annotated[Optional[Any], Field(description="Порядок доменов.")] = None, sort : Annotated[Optional[Any], Field(description="Сортировка доменов.")] = None, **kwargs) -> GetDomains200Response:  # noqa: E501
        """Получение списка всех доменов  # noqa: E501

        Чтобы получить список всех доменов на вашем аккаунте, отправьте GET-запрос на `/api/v1/domains`.   Тело ответа будет представлять собой объект JSON с ключом `domains`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domains(limit, offset, idn_name, linked_ip, order, sort, async_req=True)
        >>> result = thread.get()

        :param limit: Обозначает количество записей, которое необходимо вернуть.
        :type limit: object
        :param offset: Указывает на смещение относительно начала списка.
        :type offset: object
        :param idn_name: Интернационализированное доменное имя.
        :type idn_name: object
        :param linked_ip: Привязанный к домену IP-адрес.
        :type linked_ip: object
        :param order: Порядок доменов.
        :type order: object
        :param sort: Сортировка доменов.
        :type sort: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetDomains200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_domains_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_domains_with_http_info(limit, offset, idn_name, linked_ip, order, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def get_domains_with_http_info(self, limit : Annotated[Optional[Any], Field(description="Обозначает количество записей, которое необходимо вернуть.")] = None, offset : Annotated[Optional[Any], Field(description="Указывает на смещение относительно начала списка.")] = None, idn_name : Annotated[Optional[Any], Field(description="Интернационализированное доменное имя.")] = None, linked_ip : Annotated[Optional[Any], Field(description="Привязанный к домену IP-адрес.")] = None, order : Annotated[Optional[Any], Field(description="Порядок доменов.")] = None, sort : Annotated[Optional[Any], Field(description="Сортировка доменов.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка всех доменов  # noqa: E501

        Чтобы получить список всех доменов на вашем аккаунте, отправьте GET-запрос на `/api/v1/domains`.   Тело ответа будет представлять собой объект JSON с ключом `domains`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domains_with_http_info(limit, offset, idn_name, linked_ip, order, sort, async_req=True)
        >>> result = thread.get()

        :param limit: Обозначает количество записей, которое необходимо вернуть.
        :type limit: object
        :param offset: Указывает на смещение относительно начала списка.
        :type offset: object
        :param idn_name: Интернационализированное доменное имя.
        :type idn_name: object
        :param linked_ip: Привязанный к домену IP-адрес.
        :type linked_ip: object
        :param order: Порядок доменов.
        :type order: object
        :param sort: Сортировка доменов.
        :type sort: object
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
        :rtype: tuple(GetDomains200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'limit',
            'offset',
            'idn_name',
            'linked_ip',
            'order',
            'sort'
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
                    " to method get_domains" % _key
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

        if _params.get('idn_name') is not None:  # noqa: E501
            _query_params.append(('idn_name', _params['idn_name']))

        if _params.get('linked_ip') is not None:  # noqa: E501
            _query_params.append(('linked_ip', _params['linked_ip']))

        if _params.get('order') is not None:  # noqa: E501
            _query_params.append(('order', _params['order'].value))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort'].value))

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
            '200': "GetDomains200Response",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains', 'GET',
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
    def get_tld(self, tld_id : Annotated[Any, Field(..., description="Идентификатор доменной зоны.")], **kwargs) -> GetTLD200Response:  # noqa: E501
        """Получить информацию о доменной зоне по идентификатору  # noqa: E501

        Чтобы получить информацию о доменной зоне по идентификатору, отправьте запрос GET на `/api/v1/tlds/{tld_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_tld(tld_id, async_req=True)
        >>> result = thread.get()

        :param tld_id: Идентификатор доменной зоны. (required)
        :type tld_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetTLD200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_tld_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_tld_with_http_info(tld_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_tld_with_http_info(self, tld_id : Annotated[Any, Field(..., description="Идентификатор доменной зоны.")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получить информацию о доменной зоне по идентификатору  # noqa: E501

        Чтобы получить информацию о доменной зоне по идентификатору, отправьте запрос GET на `/api/v1/tlds/{tld_id}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_tld_with_http_info(tld_id, async_req=True)
        >>> result = thread.get()

        :param tld_id: Идентификатор доменной зоны. (required)
        :type tld_id: object
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
        :rtype: tuple(GetTLD200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'tld_id'
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
                    " to method get_tld" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['tld_id']:
            _path_params['tld_id'] = _params['tld_id']


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
            '200': "GetTLD200Response",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/tlds/{tld_id}', 'GET',
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
    def get_tlds(self, is_published : Annotated[Optional[Any], Field(description="Это логическое значение, которое показывает, опубликована ли доменная зона.")] = None, is_registered : Annotated[Optional[Any], Field(description="Это логическое значение, которое показывает, зарегистрирована ли доменная зона.")] = None, **kwargs) -> GetTLDs200Response:  # noqa: E501
        """Получить информацию о доменных зонах  # noqa: E501

        Чтобы получить информацию о доменных зонах, отправьте запрос GET на `/api/v1/tlds`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_tlds(is_published, is_registered, async_req=True)
        >>> result = thread.get()

        :param is_published: Это логическое значение, которое показывает, опубликована ли доменная зона.
        :type is_published: object
        :param is_registered: Это логическое значение, которое показывает, зарегистрирована ли доменная зона.
        :type is_registered: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetTLDs200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_tlds_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_tlds_with_http_info(is_published, is_registered, **kwargs)  # noqa: E501

    @validate_arguments
    def get_tlds_with_http_info(self, is_published : Annotated[Optional[Any], Field(description="Это логическое значение, которое показывает, опубликована ли доменная зона.")] = None, is_registered : Annotated[Optional[Any], Field(description="Это логическое значение, которое показывает, зарегистрирована ли доменная зона.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получить информацию о доменных зонах  # noqa: E501

        Чтобы получить информацию о доменных зонах, отправьте запрос GET на `/api/v1/tlds`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_tlds_with_http_info(is_published, is_registered, async_req=True)
        >>> result = thread.get()

        :param is_published: Это логическое значение, которое показывает, опубликована ли доменная зона.
        :type is_published: object
        :param is_registered: Это логическое значение, которое показывает, зарегистрирована ли доменная зона.
        :type is_registered: object
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
        :rtype: tuple(GetTLDs200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'is_published',
            'is_registered'
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
                    " to method get_tlds" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('is_published') is not None:  # noqa: E501
            _query_params.append(('is_published', _params['is_published']))

        if _params.get('is_registered') is not None:  # noqa: E501
            _query_params.append(('is_registered', _params['is_registered']))

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
            '200': "GetTLDs200Response",
            '400': None,
            '401': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/tlds', 'GET',
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
    def update_domain_auto_prolongation(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], update_domain : UpdateDomain, **kwargs) -> UpdateDomainAutoProlongation200Response:  # noqa: E501
        """Включение/выключение автопродления домена  # noqa: E501

        Чтобы включить/выключить автопродление домена, отправьте запрос PATCH на `/api/v1/domains/{fqdn}`, передав в теле запроса параметр `is_autoprolong_enabled`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_domain_auto_prolongation(fqdn, update_domain, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
        :param update_domain: (required)
        :type update_domain: UpdateDomain
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UpdateDomainAutoProlongation200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_domain_auto_prolongation_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_domain_auto_prolongation_with_http_info(fqdn, update_domain, **kwargs)  # noqa: E501

    @validate_arguments
    def update_domain_auto_prolongation_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], update_domain : UpdateDomain, **kwargs) -> ApiResponse:  # noqa: E501
        """Включение/выключение автопродления домена  # noqa: E501

        Чтобы включить/выключить автопродление домена, отправьте запрос PATCH на `/api/v1/domains/{fqdn}`, передав в теле запроса параметр `is_autoprolong_enabled`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_domain_auto_prolongation_with_http_info(fqdn, update_domain, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
        :param update_domain: (required)
        :type update_domain: UpdateDomain
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
        :rtype: tuple(UpdateDomainAutoProlongation200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'fqdn',
            'update_domain'
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
                    " to method update_domain_auto_prolongation" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_domain'] is not None:
            _body_params = _params['update_domain']

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
            '200': "UpdateDomainAutoProlongation200Response",
            '400': None,
            '401': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains/{fqdn}', 'PATCH',
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
    def update_domain_dns_record(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена или поддомена.")], record_id : Annotated[Any, Field(..., description="Идентификатор DNS-записи домена или поддомена.")], create_dns : CreateDns, **kwargs) -> CreateDomainDNSRecord201Response:  # noqa: E501
        """Обновить информацию о DNS-записи домена или поддомена  # noqa: E501

        Чтобы обновить информацию о DNS-записи для домена или поддомена, отправьте запрос PATCH на `/api/v1/domains/{fqdn}/dns-records/{record_id}`, задав необходимые атрибуты.  DNS-запись будет обновлена с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией об добавленной DNS-записи.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_domain_dns_record(fqdn, record_id, create_dns, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена или поддомена. (required)
        :type fqdn: object
        :param record_id: Идентификатор DNS-записи домена или поддомена. (required)
        :type record_id: object
        :param create_dns: (required)
        :type create_dns: CreateDns
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateDomainDNSRecord201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_domain_dns_record_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_domain_dns_record_with_http_info(fqdn, record_id, create_dns, **kwargs)  # noqa: E501

    @validate_arguments
    def update_domain_dns_record_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена или поддомена.")], record_id : Annotated[Any, Field(..., description="Идентификатор DNS-записи домена или поддомена.")], create_dns : CreateDns, **kwargs) -> ApiResponse:  # noqa: E501
        """Обновить информацию о DNS-записи домена или поддомена  # noqa: E501

        Чтобы обновить информацию о DNS-записи для домена или поддомена, отправьте запрос PATCH на `/api/v1/domains/{fqdn}/dns-records/{record_id}`, задав необходимые атрибуты.  DNS-запись будет обновлена с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией об добавленной DNS-записи.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_domain_dns_record_with_http_info(fqdn, record_id, create_dns, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена или поддомена. (required)
        :type fqdn: object
        :param record_id: Идентификатор DNS-записи домена или поддомена. (required)
        :type record_id: object
        :param create_dns: (required)
        :type create_dns: CreateDns
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
        :rtype: tuple(CreateDomainDNSRecord201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'fqdn',
            'record_id',
            'create_dns'
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
                    " to method update_domain_dns_record" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']

        if _params['record_id']:
            _path_params['record_id'] = _params['record_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_dns'] is not None:
            _body_params = _params['create_dns']

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
            '200': "CreateDomainDNSRecord201Response",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains/{fqdn}/dns-records/{record_id}', 'PATCH',
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
    def update_domain_name_servers(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], update_domain_name_servers : UpdateDomainNameServers, **kwargs) -> GetDomainNameServers200Response:  # noqa: E501
        """Изменение name-серверов домена  # noqa: E501

        Чтобы изменить name-серверы домена, отправьте запрос PUT на `/api/v1/domains/{fqdn}/name-servers`, задав необходимые атрибуты.  Name-серверы будут изменены с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о name-серверах домена.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_domain_name_servers(fqdn, update_domain_name_servers, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
        :param update_domain_name_servers: (required)
        :type update_domain_name_servers: UpdateDomainNameServers
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetDomainNameServers200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_domain_name_servers_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_domain_name_servers_with_http_info(fqdn, update_domain_name_servers, **kwargs)  # noqa: E501

    @validate_arguments
    def update_domain_name_servers_with_http_info(self, fqdn : Annotated[Any, Field(..., description="Полное имя домена.")], update_domain_name_servers : UpdateDomainNameServers, **kwargs) -> ApiResponse:  # noqa: E501
        """Изменение name-серверов домена  # noqa: E501

        Чтобы изменить name-серверы домена, отправьте запрос PUT на `/api/v1/domains/{fqdn}/name-servers`, задав необходимые атрибуты.  Name-серверы будут изменены с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о name-серверах домена.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_domain_name_servers_with_http_info(fqdn, update_domain_name_servers, async_req=True)
        >>> result = thread.get()

        :param fqdn: Полное имя домена. (required)
        :type fqdn: object
        :param update_domain_name_servers: (required)
        :type update_domain_name_servers: UpdateDomainNameServers
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
        :rtype: tuple(GetDomainNameServers200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'fqdn',
            'update_domain_name_servers'
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
                    " to method update_domain_name_servers" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['fqdn']:
            _path_params['fqdn'] = _params['fqdn']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_domain_name_servers'] is not None:
            _body_params = _params['update_domain_name_servers']

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
            '200': "GetDomainNameServers200Response",
            '400': None,
            '401': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains/{fqdn}/name-servers', 'PUT',
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
    def update_domain_request(self, request_id : Annotated[Any, Field(..., description="Идентификатор заявки на регистрацию/продление/трансфер домена.")], use : Use, **kwargs) -> CreateDomainRequest201Response:  # noqa: E501
        """Оплата/обновление заявки на регистрацию/продление/трансфер домена  # noqa: E501

        Чтобы оплатить/обновить заявку на регистрацию/продление/трансфер домена, отправьте запрос PATCH на `/api/v1/domains-requests/{request_id}`, задав необходимые атрибуты.  Заявка будет обновлена с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о обновленной заявке.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_domain_request(request_id, use, async_req=True)
        >>> result = thread.get()

        :param request_id: Идентификатор заявки на регистрацию/продление/трансфер домена. (required)
        :type request_id: object
        :param use: (required)
        :type use: Use
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateDomainRequest201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_domain_request_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_domain_request_with_http_info(request_id, use, **kwargs)  # noqa: E501

    @validate_arguments
    def update_domain_request_with_http_info(self, request_id : Annotated[Any, Field(..., description="Идентификатор заявки на регистрацию/продление/трансфер домена.")], use : Use, **kwargs) -> ApiResponse:  # noqa: E501
        """Оплата/обновление заявки на регистрацию/продление/трансфер домена  # noqa: E501

        Чтобы оплатить/обновить заявку на регистрацию/продление/трансфер домена, отправьте запрос PATCH на `/api/v1/domains-requests/{request_id}`, задав необходимые атрибуты.  Заявка будет обновлена с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о обновленной заявке.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_domain_request_with_http_info(request_id, use, async_req=True)
        >>> result = thread.get()

        :param request_id: Идентификатор заявки на регистрацию/продление/трансфер домена. (required)
        :type request_id: object
        :param use: (required)
        :type use: Use
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
        :rtype: tuple(CreateDomainRequest201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'request_id',
            'use'
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
                    " to method update_domain_request" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['request_id']:
            _path_params['request_id'] = _params['request_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['use'] is not None:
            _body_params = _params['use']

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
            '200': "CreateDomainRequest201Response",
            '400': None,
            '401': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/domains-requests/{request_id}', 'PATCH',
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
