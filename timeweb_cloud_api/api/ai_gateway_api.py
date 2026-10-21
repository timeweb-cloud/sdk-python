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

from timeweb_cloud_api.models.create_ai_key import CreateAiKey
from timeweb_cloud_api.models.create_ai_key201_response import CreateAiKey201Response
from timeweb_cloud_api.models.create_ai_key_limit import CreateAiKeyLimit
from timeweb_cloud_api.models.create_ai_key_limit201_response import CreateAiKeyLimit201Response
from timeweb_cloud_api.models.get_ai_key_calls_statistic200_response import GetAiKeyCallsStatistic200Response
from timeweb_cloud_api.models.get_ai_key_limits200_response import GetAiKeyLimits200Response
from timeweb_cloud_api.models.get_ai_key_models_statistic200_response import GetAiKeyModelsStatistic200Response
from timeweb_cloud_api.models.get_ai_key_token_usage_statistic200_response import GetAiKeyTokenUsageStatistic200Response
from timeweb_cloud_api.models.get_ai_keys200_response import GetAiKeys200Response
from timeweb_cloud_api.models.sync_ai_key_limits import SyncAiKeyLimits
from timeweb_cloud_api.models.update_ai_key import UpdateAiKey
from timeweb_cloud_api.models.update_ai_key200_response import UpdateAiKey200Response
from timeweb_cloud_api.models.update_ai_key_limit import UpdateAiKeyLimit

from timeweb_cloud_api.api_client import ApiClient
from timeweb_cloud_api.api_response import ApiResponse
from timeweb_cloud_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AIGatewayApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def create_ai_key(self, create_ai_key : CreateAiKey, **kwargs) -> CreateAiKey201Response:  # noqa: E501
        """Создание ключа AI Gateway  # noqa: E501

        Чтобы создать ключ AI Gateway, отправьте POST-запрос на `/api/v1/cloud-ai/ai-keys`.  Значение ключа (`sk-...`) возвращается в поле `key` только в ответе на этот запрос — сохраните его. Если значение утеряно, перевыпустите ключ.  Если список `fallback_models` некорректен, вернётся 400 с `error_code` `fallback_chain_invalid` (больше двух моделей или повторы, правило — в `details.reason`) или `fallback_model_not_found` (модели нет среди действующих текстовых моделей, список — в `details.model_names`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_key(create_ai_key, async_req=True)
        >>> result = thread.get()

        :param create_ai_key: (required)
        :type create_ai_key: CreateAiKey
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAiKey201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_key_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_key_with_http_info(create_ai_key, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_key_with_http_info(self, create_ai_key : CreateAiKey, **kwargs) -> ApiResponse:  # noqa: E501
        """Создание ключа AI Gateway  # noqa: E501

        Чтобы создать ключ AI Gateway, отправьте POST-запрос на `/api/v1/cloud-ai/ai-keys`.  Значение ключа (`sk-...`) возвращается в поле `key` только в ответе на этот запрос — сохраните его. Если значение утеряно, перевыпустите ключ.  Если список `fallback_models` некорректен, вернётся 400 с `error_code` `fallback_chain_invalid` (больше двух моделей или повторы, правило — в `details.reason`) или `fallback_model_not_found` (модели нет среди действующих текстовых моделей, список — в `details.model_names`).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_key_with_http_info(create_ai_key, async_req=True)
        >>> result = thread.get()

        :param create_ai_key: (required)
        :type create_ai_key: CreateAiKey
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
        :rtype: tuple(CreateAiKey201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'create_ai_key'
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
                    " to method create_ai_key" % _key
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
        if _params['create_ai_key'] is not None:
            _body_params = _params['create_ai_key']

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
            '201': "CreateAiKey201Response",
            '400': None,
            '401': None,
            '403': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys', 'POST',
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
    def create_ai_key_limit(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], create_ai_key_limit : CreateAiKeyLimit, **kwargs) -> CreateAiKeyLimit201Response:  # noqa: E501
        """Создание лимита ключа AI Gateway  # noqa: E501

        Чтобы ограничить расход ключа AI Gateway, отправьте POST-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits`.  Лимит задаётся в токенах (`limit`) или в деньгах (`money_limit`, приоритетнее) на период `limit_type` — для всех моделей или для одной (`model_id`). Когда лимит исчерпан, запросы ключа к AI Gateway API завершаются ошибкой 422 до начала следующего периода. Если от лимита осталась часть, максимальный размер ответа текстового запроса уменьшается так, чтобы уложиться в остаток.  На один период и одну модель (или на все модели) можно завести только один лимит — повторный вернёт 409 с `error_code` `entity_keys_limit_already_exists`. Если не передан ни `limit`, ни `money_limit`, вернётся 400 с `error_code` `entity_keys_limit_value_required`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_key_limit(key_id, create_ai_key_limit, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param create_ai_key_limit: (required)
        :type create_ai_key_limit: CreateAiKeyLimit
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAiKeyLimit201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_key_limit_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_key_limit_with_http_info(key_id, create_ai_key_limit, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_key_limit_with_http_info(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], create_ai_key_limit : CreateAiKeyLimit, **kwargs) -> ApiResponse:  # noqa: E501
        """Создание лимита ключа AI Gateway  # noqa: E501

        Чтобы ограничить расход ключа AI Gateway, отправьте POST-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits`.  Лимит задаётся в токенах (`limit`) или в деньгах (`money_limit`, приоритетнее) на период `limit_type` — для всех моделей или для одной (`model_id`). Когда лимит исчерпан, запросы ключа к AI Gateway API завершаются ошибкой 422 до начала следующего периода. Если от лимита осталась часть, максимальный размер ответа текстового запроса уменьшается так, чтобы уложиться в остаток.  На один период и одну модель (или на все модели) можно завести только один лимит — повторный вернёт 409 с `error_code` `entity_keys_limit_already_exists`. Если не передан ни `limit`, ни `money_limit`, вернётся 400 с `error_code` `entity_keys_limit_value_required`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_key_limit_with_http_info(key_id, create_ai_key_limit, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param create_ai_key_limit: (required)
        :type create_ai_key_limit: CreateAiKeyLimit
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
        :rtype: tuple(CreateAiKeyLimit201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'key_id',
            'create_ai_key_limit'
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
                    " to method create_ai_key_limit" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['key_id']:
            _path_params['key_id'] = _params['key_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['create_ai_key_limit'] is not None:
            _body_params = _params['create_ai_key_limit']

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
            '201': "CreateAiKeyLimit201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits', 'POST',
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
    def delete_ai_key(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], **kwargs) -> None:  # noqa: E501
        """Удаление ключа AI Gateway  # noqa: E501

        Чтобы удалить ключ AI Gateway, отправьте DELETE-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}`.  После удаления запросы с этим ключом перестают приниматься. Ключи, которыми управляет платформа (`is_readonly: true`), удалить нельзя: вернётся 403 с `error_code` `ai_key_is_readonly`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_ai_key(key_id, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
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
            raise ValueError("Error! Please call the delete_ai_key_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_ai_key_with_http_info(key_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_ai_key_with_http_info(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление ключа AI Gateway  # noqa: E501

        Чтобы удалить ключ AI Gateway, отправьте DELETE-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}`.  После удаления запросы с этим ключом перестают приниматься. Ключи, которыми управляет платформа (`is_readonly: true`), удалить нельзя: вернётся 403 с `error_code` `ai_key_is_readonly`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_ai_key_with_http_info(key_id, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
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
            'key_id'
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
                    " to method delete_ai_key" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['key_id']:
            _path_params['key_id'] = _params['key_id']


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
            '/api/v1/cloud-ai/ai-keys/{key_id}', 'DELETE',
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
    def delete_ai_key_limit(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], limit_id : Annotated[Any, Field(..., description="ID лимита (UUID)")], **kwargs) -> None:  # noqa: E501
        """Удаление лимита ключа AI Gateway  # noqa: E501

        Чтобы удалить лимит ключа AI Gateway, отправьте DELETE-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}`.  Если лимит относится к другому ключу, вернётся 403.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_ai_key_limit(key_id, limit_id, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param limit_id: ID лимита (UUID) (required)
        :type limit_id: object
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
            raise ValueError("Error! Please call the delete_ai_key_limit_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_ai_key_limit_with_http_info(key_id, limit_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_ai_key_limit_with_http_info(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], limit_id : Annotated[Any, Field(..., description="ID лимита (UUID)")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление лимита ключа AI Gateway  # noqa: E501

        Чтобы удалить лимит ключа AI Gateway, отправьте DELETE-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}`.  Если лимит относится к другому ключу, вернётся 403.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_ai_key_limit_with_http_info(key_id, limit_id, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param limit_id: ID лимита (UUID) (required)
        :type limit_id: object
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
            'key_id',
            'limit_id'
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
                    " to method delete_ai_key_limit" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['key_id']:
            _path_params['key_id'] = _params['key_id']

        if _params['limit_id']:
            _path_params['limit_id'] = _params['limit_id']


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
            '/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}', 'DELETE',
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
    def get_ai_key_calls_statistic(self, entity_id : Annotated[Any, Field(..., description="ID ключа — поле `id` из списка ключей.")], entity_type : Annotated[Any, Field(..., description="Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404.")], model_name : Annotated[Optional[Any], Field(description="Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.")] = None, start_time : Annotated[Optional[Any], Field(description="Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.")] = None, end_time : Annotated[Optional[Any], Field(description="Конец периода в формате ISO 8601. По умолчанию — текущий момент.")] = None, interval : Annotated[Optional[Any], Field(description="Шаг агрегации в минутах.")] = None, **kwargs) -> GetAiKeyCallsStatistic200Response:  # noqa: E501
        """Получение статистики запросов ключа AI Gateway  # noqa: E501

        Чтобы получить количество запросов ключа по интервалам времени, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/statistic/calls`.  Ключ задаётся параметрами `entity_id` (ID ключа) и `entity_type` (тип ключа). Если ключ не найден, вернётся 404. Период по умолчанию — последние 24 часа. Точки возвращаются для каждого интервала периода, включая интервалы без запросов.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_calls_statistics` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_key_calls_statistic(entity_id, entity_type, model_name, start_time, end_time, interval, async_req=True)
        >>> result = thread.get()

        :param entity_id: ID ключа — поле `id` из списка ключей. (required)
        :type entity_id: object
        :param entity_type: Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404. (required)
        :type entity_type: object
        :param model_name: Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.
        :type model_name: object
        :param start_time: Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.
        :type start_time: object
        :param end_time: Конец периода в формате ISO 8601. По умолчанию — текущий момент.
        :type end_time: object
        :param interval: Шаг агрегации в минутах.
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
        :rtype: GetAiKeyCallsStatistic200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_key_calls_statistic_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_key_calls_statistic_with_http_info(entity_id, entity_type, model_name, start_time, end_time, interval, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_key_calls_statistic_with_http_info(self, entity_id : Annotated[Any, Field(..., description="ID ключа — поле `id` из списка ключей.")], entity_type : Annotated[Any, Field(..., description="Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404.")], model_name : Annotated[Optional[Any], Field(description="Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.")] = None, start_time : Annotated[Optional[Any], Field(description="Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.")] = None, end_time : Annotated[Optional[Any], Field(description="Конец периода в формате ISO 8601. По умолчанию — текущий момент.")] = None, interval : Annotated[Optional[Any], Field(description="Шаг агрегации в минутах.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение статистики запросов ключа AI Gateway  # noqa: E501

        Чтобы получить количество запросов ключа по интервалам времени, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/statistic/calls`.  Ключ задаётся параметрами `entity_id` (ID ключа) и `entity_type` (тип ключа). Если ключ не найден, вернётся 404. Период по умолчанию — последние 24 часа. Точки возвращаются для каждого интервала периода, включая интервалы без запросов.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_calls_statistics` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_key_calls_statistic_with_http_info(entity_id, entity_type, model_name, start_time, end_time, interval, async_req=True)
        >>> result = thread.get()

        :param entity_id: ID ключа — поле `id` из списка ключей. (required)
        :type entity_id: object
        :param entity_type: Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404. (required)
        :type entity_type: object
        :param model_name: Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.
        :type model_name: object
        :param start_time: Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.
        :type start_time: object
        :param end_time: Конец периода в формате ISO 8601. По умолчанию — текущий момент.
        :type end_time: object
        :param interval: Шаг агрегации в минутах.
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
        :rtype: tuple(GetAiKeyCallsStatistic200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'entity_id',
            'entity_type',
            'model_name',
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
                    " to method get_ai_key_calls_statistic" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('entity_id') is not None:  # noqa: E501
            _query_params.append(('entity_id', _params['entity_id']))

        if _params.get('entity_type') is not None:  # noqa: E501
            _query_params.append(('entity_type', _params['entity_type'].value))

        if _params.get('model_name') is not None:  # noqa: E501
            _query_params.append(('model_name', _params['model_name']))

        if _params.get('start_time') is not None:  # noqa: E501
            _query_params.append(('start_time', _params['start_time']))

        if _params.get('end_time') is not None:  # noqa: E501
            _query_params.append(('end_time', _params['end_time']))

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
            '200': "GetAiKeyCallsStatistic200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys/statistic/calls', 'GET',
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
    def get_ai_key_limit(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], limit_id : Annotated[Any, Field(..., description="ID лимита (UUID)")], **kwargs) -> CreateAiKeyLimit201Response:  # noqa: E501
        """Получение лимита ключа AI Gateway  # noqa: E501

        Чтобы получить лимит ключа AI Gateway, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}`.  Если лимит относится к другому ключу, вернётся 403 с `error_code` `entity_keys_limit_forbidden`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_key_limit(key_id, limit_id, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param limit_id: ID лимита (UUID) (required)
        :type limit_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAiKeyLimit201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_key_limit_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_key_limit_with_http_info(key_id, limit_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_key_limit_with_http_info(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], limit_id : Annotated[Any, Field(..., description="ID лимита (UUID)")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение лимита ключа AI Gateway  # noqa: E501

        Чтобы получить лимит ключа AI Gateway, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}`.  Если лимит относится к другому ключу, вернётся 403 с `error_code` `entity_keys_limit_forbidden`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_key_limit_with_http_info(key_id, limit_id, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param limit_id: ID лимита (UUID) (required)
        :type limit_id: object
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
        :rtype: tuple(CreateAiKeyLimit201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'key_id',
            'limit_id'
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
                    " to method get_ai_key_limit" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['key_id']:
            _path_params['key_id'] = _params['key_id']

        if _params['limit_id']:
            _path_params['limit_id'] = _params['limit_id']


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
            '200': "CreateAiKeyLimit201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}', 'GET',
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
    def get_ai_key_limits(self, entity_type : Annotated[Optional[Any], Field(description="Фильтр по типу сущности лимита (`entity_type`).")] = None, limit_type : Annotated[Optional[Any], Field(description="Фильтр по периоду лимита.")] = None, **kwargs) -> GetAiKeyLimits200Response:  # noqa: E501
        """Получение списка лимитов ключа AI Gateway  # noqa: E501

        Чтобы получить лимиты расхода ключа AI Gateway, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits`.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_entity_limits` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_key_limits(entity_type, limit_type, async_req=True)
        >>> result = thread.get()

        :param entity_type: Фильтр по типу сущности лимита (`entity_type`).
        :type entity_type: object
        :param limit_type: Фильтр по периоду лимита.
        :type limit_type: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAiKeyLimits200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_key_limits_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_key_limits_with_http_info(entity_type, limit_type, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_key_limits_with_http_info(self, entity_type : Annotated[Optional[Any], Field(description="Фильтр по типу сущности лимита (`entity_type`).")] = None, limit_type : Annotated[Optional[Any], Field(description="Фильтр по периоду лимита.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка лимитов ключа AI Gateway  # noqa: E501

        Чтобы получить лимиты расхода ключа AI Gateway, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits`.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_entity_limits` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_key_limits_with_http_info(entity_type, limit_type, async_req=True)
        >>> result = thread.get()

        :param entity_type: Фильтр по типу сущности лимита (`entity_type`).
        :type entity_type: object
        :param limit_type: Фильтр по периоду лимита.
        :type limit_type: object
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
        :rtype: tuple(GetAiKeyLimits200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'entity_type',
            'limit_type'
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
                    " to method get_ai_key_limits" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('entity_type') is not None:  # noqa: E501
            _query_params.append(('entity_type', _params['entity_type']))

        if _params.get('limit_type') is not None:  # noqa: E501
            _query_params.append(('limit_type', _params['limit_type'].value))

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
            '200': "GetAiKeyLimits200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits', 'GET',
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
    def get_ai_key_models_statistic(self, entity_id : Annotated[Any, Field(..., description="ID ключа — поле `id` из списка ключей.")], entity_type : Annotated[Any, Field(..., description="Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404.")], model_name : Annotated[Optional[Any], Field(description="Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.")] = None, start_time : Annotated[Optional[Any], Field(description="Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.")] = None, end_time : Annotated[Optional[Any], Field(description="Конец периода в формате ISO 8601. По умолчанию — текущий момент.")] = None, **kwargs) -> GetAiKeyModelsStatistic200Response:  # noqa: E501
        """Получение списка моделей, использованных ключом AI Gateway  # noqa: E501

        Чтобы получить список моделей, к которым обращался ключ за период, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/statistic/models`.  Ключ задаётся параметрами `entity_id` (ID ключа) и `entity_type` (тип ключа). Если ключ не найден, вернётся 404. Период по умолчанию — последние 24 часа. Модели отсортированы по алфавиту.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_models_statistics` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_key_models_statistic(entity_id, entity_type, model_name, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param entity_id: ID ключа — поле `id` из списка ключей. (required)
        :type entity_id: object
        :param entity_type: Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404. (required)
        :type entity_type: object
        :param model_name: Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.
        :type model_name: object
        :param start_time: Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.
        :type start_time: object
        :param end_time: Конец периода в формате ISO 8601. По умолчанию — текущий момент.
        :type end_time: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAiKeyModelsStatistic200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_key_models_statistic_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_key_models_statistic_with_http_info(entity_id, entity_type, model_name, start_time, end_time, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_key_models_statistic_with_http_info(self, entity_id : Annotated[Any, Field(..., description="ID ключа — поле `id` из списка ключей.")], entity_type : Annotated[Any, Field(..., description="Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404.")], model_name : Annotated[Optional[Any], Field(description="Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.")] = None, start_time : Annotated[Optional[Any], Field(description="Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.")] = None, end_time : Annotated[Optional[Any], Field(description="Конец периода в формате ISO 8601. По умолчанию — текущий момент.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка моделей, использованных ключом AI Gateway  # noqa: E501

        Чтобы получить список моделей, к которым обращался ключ за период, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/statistic/models`.  Ключ задаётся параметрами `entity_id` (ID ключа) и `entity_type` (тип ключа). Если ключ не найден, вернётся 404. Период по умолчанию — последние 24 часа. Модели отсортированы по алфавиту.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_models_statistics` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_key_models_statistic_with_http_info(entity_id, entity_type, model_name, start_time, end_time, async_req=True)
        >>> result = thread.get()

        :param entity_id: ID ключа — поле `id` из списка ключей. (required)
        :type entity_id: object
        :param entity_type: Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404. (required)
        :type entity_type: object
        :param model_name: Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.
        :type model_name: object
        :param start_time: Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.
        :type start_time: object
        :param end_time: Конец периода в формате ISO 8601. По умолчанию — текущий момент.
        :type end_time: object
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
        :rtype: tuple(GetAiKeyModelsStatistic200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'entity_id',
            'entity_type',
            'model_name',
            'start_time',
            'end_time'
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
                    " to method get_ai_key_models_statistic" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('entity_id') is not None:  # noqa: E501
            _query_params.append(('entity_id', _params['entity_id']))

        if _params.get('entity_type') is not None:  # noqa: E501
            _query_params.append(('entity_type', _params['entity_type'].value))

        if _params.get('model_name') is not None:  # noqa: E501
            _query_params.append(('model_name', _params['model_name']))

        if _params.get('start_time') is not None:  # noqa: E501
            _query_params.append(('start_time', _params['start_time']))

        if _params.get('end_time') is not None:  # noqa: E501
            _query_params.append(('end_time', _params['end_time']))

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
            '200': "GetAiKeyModelsStatistic200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys/statistic/models', 'GET',
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
    def get_ai_key_token_usage_statistic(self, entity_id : Annotated[Any, Field(..., description="ID ключа — поле `id` из списка ключей.")], entity_type : Annotated[Any, Field(..., description="Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404.")], model_name : Annotated[Optional[Any], Field(description="Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.")] = None, start_time : Annotated[Optional[Any], Field(description="Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.")] = None, end_time : Annotated[Optional[Any], Field(description="Конец периода в формате ISO 8601. По умолчанию — текущий момент.")] = None, interval : Annotated[Optional[Any], Field(description="Шаг агрегации в минутах.")] = None, **kwargs) -> GetAiKeyTokenUsageStatistic200Response:  # noqa: E501
        """Получение статистики расхода токенов ключа AI Gateway  # noqa: E501

        Чтобы получить расход токенов и стоимость запросов ключа по интервалам времени, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/statistic/token-usage`.  Ключ задаётся параметрами `entity_id` (ID ключа) и `entity_type` (тип ключа). Если ключ не найден, вернётся 404. Период по умолчанию — последние 24 часа. Точки возвращаются для каждого интервала периода, включая интервалы без запросов.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_token_statistics` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_key_token_usage_statistic(entity_id, entity_type, model_name, start_time, end_time, interval, async_req=True)
        >>> result = thread.get()

        :param entity_id: ID ключа — поле `id` из списка ключей. (required)
        :type entity_id: object
        :param entity_type: Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404. (required)
        :type entity_type: object
        :param model_name: Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.
        :type model_name: object
        :param start_time: Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.
        :type start_time: object
        :param end_time: Конец периода в формате ISO 8601. По умолчанию — текущий момент.
        :type end_time: object
        :param interval: Шаг агрегации в минутах.
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
        :rtype: GetAiKeyTokenUsageStatistic200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_key_token_usage_statistic_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_key_token_usage_statistic_with_http_info(entity_id, entity_type, model_name, start_time, end_time, interval, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_key_token_usage_statistic_with_http_info(self, entity_id : Annotated[Any, Field(..., description="ID ключа — поле `id` из списка ключей.")], entity_type : Annotated[Any, Field(..., description="Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404.")], model_name : Annotated[Optional[Any], Field(description="Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.")] = None, start_time : Annotated[Optional[Any], Field(description="Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.")] = None, end_time : Annotated[Optional[Any], Field(description="Конец периода в формате ISO 8601. По умолчанию — текущий момент.")] = None, interval : Annotated[Optional[Any], Field(description="Шаг агрегации в минутах.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение статистики расхода токенов ключа AI Gateway  # noqa: E501

        Чтобы получить расход токенов и стоимость запросов ключа по интервалам времени, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/statistic/token-usage`.  Ключ задаётся параметрами `entity_id` (ID ключа) и `entity_type` (тип ключа). Если ключ не найден, вернётся 404. Период по умолчанию — последние 24 часа. Точки возвращаются для каждого интервала периода, включая интервалы без запросов.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_token_statistics` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_key_token_usage_statistic_with_http_info(entity_id, entity_type, model_name, start_time, end_time, interval, async_req=True)
        >>> result = thread.get()

        :param entity_id: ID ключа — поле `id` из списка ключей. (required)
        :type entity_id: object
        :param entity_type: Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404. (required)
        :type entity_type: object
        :param model_name: Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям.
        :type model_name: object
        :param start_time: Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`.
        :type start_time: object
        :param end_time: Конец периода в формате ISO 8601. По умолчанию — текущий момент.
        :type end_time: object
        :param interval: Шаг агрегации в минутах.
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
        :rtype: tuple(GetAiKeyTokenUsageStatistic200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'entity_id',
            'entity_type',
            'model_name',
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
                    " to method get_ai_key_token_usage_statistic" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('entity_id') is not None:  # noqa: E501
            _query_params.append(('entity_id', _params['entity_id']))

        if _params.get('entity_type') is not None:  # noqa: E501
            _query_params.append(('entity_type', _params['entity_type'].value))

        if _params.get('model_name') is not None:  # noqa: E501
            _query_params.append(('model_name', _params['model_name']))

        if _params.get('start_time') is not None:  # noqa: E501
            _query_params.append(('start_time', _params['start_time']))

        if _params.get('end_time') is not None:  # noqa: E501
            _query_params.append(('end_time', _params['end_time']))

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
            '200': "GetAiKeyTokenUsageStatistic200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys/statistic/token-usage', 'GET',
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
    def get_ai_keys(self, **kwargs) -> GetAiKeys200Response:  # noqa: E501
        """Получение списка ключей AI Gateway  # noqa: E501

        Чтобы получить список ключей AI Gateway, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys`.  В списке — ключи, созданные пользователем, и ключи кластеров Kubernetes, выпущенные платформой. Значения ключей (`sk-...`) не возвращаются.  Тело ответа будет представлять собой объект JSON с ключами `ai_keys` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_keys(async_req=True)
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
        :rtype: GetAiKeys200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_keys_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_keys_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_keys_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка ключей AI Gateway  # noqa: E501

        Чтобы получить список ключей AI Gateway, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys`.  В списке — ключи, созданные пользователем, и ключи кластеров Kubernetes, выпущенные платформой. Значения ключей (`sk-...`) не возвращаются.  Тело ответа будет представлять собой объект JSON с ключами `ai_keys` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_keys_with_http_info(async_req=True)
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
        :rtype: tuple(GetAiKeys200Response, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_ai_keys" % _key
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
            '200': "GetAiKeys200Response",
            '400': None,
            '401': None,
            '403': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys', 'GET',
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
    def regenerate_ai_key(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], **kwargs) -> CreateAiKey201Response:  # noqa: E501
        """Перевыпуск ключа AI Gateway  # noqa: E501

        Чтобы перевыпустить ключ AI Gateway, отправьте PUT-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/regenerate`.  Ключ получает новое значение, старое перестаёт действовать сразу. Название, лимиты, запасные модели и статистика сохраняются. Новое значение (`sk-...`) возвращается в поле `key` только в ответе на этот запрос — сохраните его. Поле `expires_at` в ответе не заполняется.  Ключи, которыми управляет платформа (`is_readonly: true`), перевыпустить нельзя: вернётся 403 с `error_code` `ai_key_is_readonly`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.regenerate_ai_key(key_id, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAiKey201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the regenerate_ai_key_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.regenerate_ai_key_with_http_info(key_id, **kwargs)  # noqa: E501

    @validate_arguments
    def regenerate_ai_key_with_http_info(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], **kwargs) -> ApiResponse:  # noqa: E501
        """Перевыпуск ключа AI Gateway  # noqa: E501

        Чтобы перевыпустить ключ AI Gateway, отправьте PUT-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/regenerate`.  Ключ получает новое значение, старое перестаёт действовать сразу. Название, лимиты, запасные модели и статистика сохраняются. Новое значение (`sk-...`) возвращается в поле `key` только в ответе на этот запрос — сохраните его. Поле `expires_at` в ответе не заполняется.  Ключи, которыми управляет платформа (`is_readonly: true`), перевыпустить нельзя: вернётся 403 с `error_code` `ai_key_is_readonly`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.regenerate_ai_key_with_http_info(key_id, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
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
        :rtype: tuple(CreateAiKey201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'key_id'
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
                    " to method regenerate_ai_key" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['key_id']:
            _path_params['key_id'] = _params['key_id']


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
            '200': "CreateAiKey201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys/{key_id}/regenerate', 'PUT',
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
    def sync_ai_key_limits(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], sync_ai_key_limits : SyncAiKeyLimits, **kwargs) -> GetAiKeyLimits200Response:  # noqa: E501
        """Синхронизация лимитов ключа AI Gateway  # noqa: E501

        Чтобы задать все лимиты ключа AI Gateway на один период одним запросом, отправьте PUT-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/sync`.  Лимиты из `limits` создаются или обновляются (по `model_id`), а лимиты того же периода, которых нет в запросе, удаляются. Изменения применяются целиком или не применяются совсем.  Если в записи не задан ни `limit`, ни `money_limit` или `money_limit` снимается без `limit`, вернётся 400 с `error_code` `entity_keys_limit_value_required`. Если лимиты одновременно изменил другой запрос, вернётся 409 с `error_code` `entity_keys_limits_sync_conflict` — повторите запрос.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_entity_limits` и `meta` — лимиты периода после синхронизации.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sync_ai_key_limits(key_id, sync_ai_key_limits, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param sync_ai_key_limits: (required)
        :type sync_ai_key_limits: SyncAiKeyLimits
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAiKeyLimits200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the sync_ai_key_limits_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.sync_ai_key_limits_with_http_info(key_id, sync_ai_key_limits, **kwargs)  # noqa: E501

    @validate_arguments
    def sync_ai_key_limits_with_http_info(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], sync_ai_key_limits : SyncAiKeyLimits, **kwargs) -> ApiResponse:  # noqa: E501
        """Синхронизация лимитов ключа AI Gateway  # noqa: E501

        Чтобы задать все лимиты ключа AI Gateway на один период одним запросом, отправьте PUT-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/sync`.  Лимиты из `limits` создаются или обновляются (по `model_id`), а лимиты того же периода, которых нет в запросе, удаляются. Изменения применяются целиком или не применяются совсем.  Если в записи не задан ни `limit`, ни `money_limit` или `money_limit` снимается без `limit`, вернётся 400 с `error_code` `entity_keys_limit_value_required`. Если лимиты одновременно изменил другой запрос, вернётся 409 с `error_code` `entity_keys_limits_sync_conflict` — повторите запрос.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_entity_limits` и `meta` — лимиты периода после синхронизации.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sync_ai_key_limits_with_http_info(key_id, sync_ai_key_limits, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param sync_ai_key_limits: (required)
        :type sync_ai_key_limits: SyncAiKeyLimits
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
        :rtype: tuple(GetAiKeyLimits200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'key_id',
            'sync_ai_key_limits'
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
                    " to method sync_ai_key_limits" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['key_id']:
            _path_params['key_id'] = _params['key_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['sync_ai_key_limits'] is not None:
            _body_params = _params['sync_ai_key_limits']

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
            '200': "GetAiKeyLimits200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/sync', 'PUT',
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
    def update_ai_key(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], update_ai_key : UpdateAiKey, **kwargs) -> UpdateAiKey200Response:  # noqa: E501
        """Изменение ключа AI Gateway  # noqa: E501

        Чтобы изменить ключ AI Gateway, отправьте PATCH-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}`, передав изменяемые поля.  Ключи, которыми управляет платформа (`is_readonly: true` — ключи AI-решений и кластеров Kubernetes), изменить нельзя: вернётся 403 с `error_code` `ai_key_is_readonly`.  Ошибки в `fallback_models` — как при создании ключа (400). Поле `expires_at` в ответе этого запроса не заполняется — срок действия ключа смотрите в списке ключей.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_ai_key(key_id, update_ai_key, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param update_ai_key: (required)
        :type update_ai_key: UpdateAiKey
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: UpdateAiKey200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_ai_key_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_ai_key_with_http_info(key_id, update_ai_key, **kwargs)  # noqa: E501

    @validate_arguments
    def update_ai_key_with_http_info(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], update_ai_key : UpdateAiKey, **kwargs) -> ApiResponse:  # noqa: E501
        """Изменение ключа AI Gateway  # noqa: E501

        Чтобы изменить ключ AI Gateway, отправьте PATCH-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}`, передав изменяемые поля.  Ключи, которыми управляет платформа (`is_readonly: true` — ключи AI-решений и кластеров Kubernetes), изменить нельзя: вернётся 403 с `error_code` `ai_key_is_readonly`.  Ошибки в `fallback_models` — как при создании ключа (400). Поле `expires_at` в ответе этого запроса не заполняется — срок действия ключа смотрите в списке ключей.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_ai_key_with_http_info(key_id, update_ai_key, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param update_ai_key: (required)
        :type update_ai_key: UpdateAiKey
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
        :rtype: tuple(UpdateAiKey200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'key_id',
            'update_ai_key'
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
                    " to method update_ai_key" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['key_id']:
            _path_params['key_id'] = _params['key_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_ai_key'] is not None:
            _body_params = _params['update_ai_key']

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
            '200': "UpdateAiKey200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys/{key_id}', 'PATCH',
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
    def update_ai_key_limit(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], limit_id : Annotated[Any, Field(..., description="ID лимита (UUID)")], update_ai_key_limit : UpdateAiKeyLimit, **kwargs) -> CreateAiKeyLimit201Response:  # noqa: E501
        """Изменение лимита ключа AI Gateway  # noqa: E501

        Чтобы изменить лимит ключа AI Gateway, отправьте PATCH-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}`.  Не переданные поля не меняются. Если не передан ни `limit`, ни `money_limit` или `money_limit` снимается без `limit`, вернётся 400 с `error_code` `entity_keys_limit_value_required`. Если лимит относится к другому ключу, вернётся 403.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_ai_key_limit(key_id, limit_id, update_ai_key_limit, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param limit_id: ID лимита (UUID) (required)
        :type limit_id: object
        :param update_ai_key_limit: (required)
        :type update_ai_key_limit: UpdateAiKeyLimit
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAiKeyLimit201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_ai_key_limit_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_ai_key_limit_with_http_info(key_id, limit_id, update_ai_key_limit, **kwargs)  # noqa: E501

    @validate_arguments
    def update_ai_key_limit_with_http_info(self, key_id : Annotated[Any, Field(..., description="ID ключа AI Gateway (UUID)")], limit_id : Annotated[Any, Field(..., description="ID лимита (UUID)")], update_ai_key_limit : UpdateAiKeyLimit, **kwargs) -> ApiResponse:  # noqa: E501
        """Изменение лимита ключа AI Gateway  # noqa: E501

        Чтобы изменить лимит ключа AI Gateway, отправьте PATCH-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}`.  Не переданные поля не меняются. Если не передан ни `limit`, ни `money_limit` или `money_limit` снимается без `limit`, вернётся 400 с `error_code` `entity_keys_limit_value_required`. Если лимит относится к другому ключу, вернётся 403.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_ai_key_limit_with_http_info(key_id, limit_id, update_ai_key_limit, async_req=True)
        >>> result = thread.get()

        :param key_id: ID ключа AI Gateway (UUID) (required)
        :type key_id: object
        :param limit_id: ID лимита (UUID) (required)
        :type limit_id: object
        :param update_ai_key_limit: (required)
        :type update_ai_key_limit: UpdateAiKeyLimit
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
        :rtype: tuple(CreateAiKeyLimit201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'key_id',
            'limit_id',
            'update_ai_key_limit'
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
                    " to method update_ai_key_limit" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['key_id']:
            _path_params['key_id'] = _params['key_id']

        if _params['limit_id']:
            _path_params['limit_id'] = _params['limit_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_ai_key_limit'] is not None:
            _body_params = _params['update_ai_key_limit']

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
            '200': "CreateAiKeyLimit201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}', 'PATCH',
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
