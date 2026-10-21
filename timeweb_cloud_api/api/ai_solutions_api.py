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

from timeweb_cloud_api.models.add_ai_solution_telegram_bot201_response import AddAiSolutionTelegramBot201Response
from timeweb_cloud_api.models.approve_telegram_pairing import ApproveTelegramPairing
from timeweb_cloud_api.models.connect_telegram import ConnectTelegram
from timeweb_cloud_api.models.create_ai_solution import CreateAiSolution
from timeweb_cloud_api.models.create_ai_solution201_response import CreateAiSolution201Response
from timeweb_cloud_api.models.get_ai_solution_chat_status200_response import GetAiSolutionChatStatus200Response
from timeweb_cloud_api.models.get_ai_solution_main_chat_history200_response import GetAiSolutionMainChatHistory200Response
from timeweb_cloud_api.models.list_ai_solution_conversations200_response import ListAiSolutionConversations200Response
from timeweb_cloud_api.models.list_ai_solution_telegram_bots200_response import ListAiSolutionTelegramBots200Response
from timeweb_cloud_api.models.list_ai_solution_types200_response import ListAiSolutionTypes200Response
from timeweb_cloud_api.models.list_ai_solutions200_response import ListAiSolutions200Response
from timeweb_cloud_api.models.regenerate_ai_solution_ai_key200_response import RegenerateAiSolutionAiKey200Response
from timeweb_cloud_api.models.reset_ai_solution_chat import ResetAiSolutionChat
from timeweb_cloud_api.models.reset_ai_solution_chat200_response import ResetAiSolutionChat200Response
from timeweb_cloud_api.models.send_ai_solution_message import SendAiSolutionMessage
from timeweb_cloud_api.models.send_ai_solution_message200_response import SendAiSolutionMessage200Response
from timeweb_cloud_api.models.stop_ai_solution_chat import StopAiSolutionChat
from timeweb_cloud_api.models.update_ai_solution import UpdateAiSolution

from timeweb_cloud_api.api_client import ApiClient
from timeweb_cloud_api.api_response import ApiResponse
from timeweb_cloud_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AISolutionsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_ai_solution_telegram_bot(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], connect_telegram : ConnectTelegram, **kwargs) -> AddAiSolutionTelegramBot201Response:  # noqa: E501
        """Подключение Telegram-бота к AI-решению  # noqa: E501

        Чтобы подключить Telegram-бота к решению, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots`.  Принимает токен бота от @BotFather, проверяет его в Telegram и настраивает бота на сервере решения. Владелец подтверждается кодом: пока он не подтверждён, бот никому не отвечает. Напишите боту в личные сообщения, получите в ответ код и передайте его в метод подтверждения владельца.  К решению можно подключить только одного бота: повторный запрос для того же бота обновляет его токен, для другого бота — возвращает 409 `ai_solution_already_has_a_connected_telegram_bot`. Если Telegram отклонил токен, ответ — 400 `ai_solution_telegram_token_is_invalid`.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_ai_solution_telegram_bot(solution_id, connect_telegram, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param connect_telegram: (required)
        :type connect_telegram: ConnectTelegram
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddAiSolutionTelegramBot201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the add_ai_solution_telegram_bot_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_ai_solution_telegram_bot_with_http_info(solution_id, connect_telegram, **kwargs)  # noqa: E501

    @validate_arguments
    def add_ai_solution_telegram_bot_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], connect_telegram : ConnectTelegram, **kwargs) -> ApiResponse:  # noqa: E501
        """Подключение Telegram-бота к AI-решению  # noqa: E501

        Чтобы подключить Telegram-бота к решению, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots`.  Принимает токен бота от @BotFather, проверяет его в Telegram и настраивает бота на сервере решения. Владелец подтверждается кодом: пока он не подтверждён, бот никому не отвечает. Напишите боту в личные сообщения, получите в ответ код и передайте его в метод подтверждения владельца.  К решению можно подключить только одного бота: повторный запрос для того же бота обновляет его токен, для другого бота — возвращает 409 `ai_solution_already_has_a_connected_telegram_bot`. Если Telegram отклонил токен, ответ — 400 `ai_solution_telegram_token_is_invalid`.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_ai_solution_telegram_bot_with_http_info(solution_id, connect_telegram, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param connect_telegram: (required)
        :type connect_telegram: ConnectTelegram
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
        :rtype: tuple(AddAiSolutionTelegramBot201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id',
            'connect_telegram'
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
                    " to method add_ai_solution_telegram_bot" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['connect_telegram'] is not None:
            _body_params = _params['connect_telegram']

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
            '201': "AddAiSolutionTelegramBot201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
            '502': "ErrorResponse",
            '503': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots', 'POST',
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
    def approve_ai_solution_telegram_pairing(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], account_key : Annotated[Any, Field(..., description="ID Telegram-бота в решении (`account_key` из списка ботов) в формате `b<число>`, например `b123456789`")], approve_telegram_pairing : ApproveTelegramPairing, **kwargs) -> None:  # noqa: E501
        """Подтверждение владельца Telegram-бота AI-решения  # noqa: E501

        Чтобы подтвердить владельца Telegram-бота, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key}/pairing/approve`.  Передайте код, который бот прислал в личные сообщения в ответ на первое сообщение. После подтверждения агент отвечает этому пользователю Telegram в боте, а бот переходит в состояние `connected`. Владелец привязывается к конкретному боту. Повторный запрос с кодом, уже подтверждённым в последние 15 минут, считается успешным. Некорректный `account_key` — ответ 400 `ai_solution_telegram_token_is_invalid`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.approve_ai_solution_telegram_pairing(solution_id, account_key, approve_telegram_pairing, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param account_key: ID Telegram-бота в решении (`account_key` из списка ботов) в формате `b<число>`, например `b123456789` (required)
        :type account_key: object
        :param approve_telegram_pairing: (required)
        :type approve_telegram_pairing: ApproveTelegramPairing
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
            raise ValueError("Error! Please call the approve_ai_solution_telegram_pairing_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.approve_ai_solution_telegram_pairing_with_http_info(solution_id, account_key, approve_telegram_pairing, **kwargs)  # noqa: E501

    @validate_arguments
    def approve_ai_solution_telegram_pairing_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], account_key : Annotated[Any, Field(..., description="ID Telegram-бота в решении (`account_key` из списка ботов) в формате `b<число>`, например `b123456789`")], approve_telegram_pairing : ApproveTelegramPairing, **kwargs) -> ApiResponse:  # noqa: E501
        """Подтверждение владельца Telegram-бота AI-решения  # noqa: E501

        Чтобы подтвердить владельца Telegram-бота, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key}/pairing/approve`.  Передайте код, который бот прислал в личные сообщения в ответ на первое сообщение. После подтверждения агент отвечает этому пользователю Telegram в боте, а бот переходит в состояние `connected`. Владелец привязывается к конкретному боту. Повторный запрос с кодом, уже подтверждённым в последние 15 минут, считается успешным. Некорректный `account_key` — ответ 400 `ai_solution_telegram_token_is_invalid`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.approve_ai_solution_telegram_pairing_with_http_info(solution_id, account_key, approve_telegram_pairing, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param account_key: ID Telegram-бота в решении (`account_key` из списка ботов) в формате `b<число>`, например `b123456789` (required)
        :type account_key: object
        :param approve_telegram_pairing: (required)
        :type approve_telegram_pairing: ApproveTelegramPairing
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
            'solution_id',
            'account_key',
            'approve_telegram_pairing'
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
                    " to method approve_ai_solution_telegram_pairing" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']

        if _params['account_key']:
            _path_params['account_key'] = _params['account_key']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['approve_telegram_pairing'] is not None:
            _body_params = _params['approve_telegram_pairing']

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
            '/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key}/pairing/approve', 'POST',
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
    def create_ai_solution(self, create_ai_solution : CreateAiSolution, **kwargs) -> CreateAiSolution201Response:  # noqa: E501
        """Создание AI-решения  # noqa: E501

        Чтобы создать AI-решение, отправьте POST-запрос на `/api/v1/cloud-ai/solutions`.  Выпускает для решения ключ AI Gateway и создаёт облачный сервер из образа решения; агент на сервере настраивается на выбранную модель через этот ключ. Сервер тарифицируется по выбранному тарифу, обращения к модели — через ключ AI Gateway.  Решение возвращается в статусе `creating`: развёртывание сервера и настройка агента занимают несколько минут. Дождитесь статуса `active`, а затем `ready: true` в методе получения статуса чата.  Тариф (`preset_id`) должен быть из той же локации, что и зона доступности (`availability_zone` или зона по умолчанию для региона аккаунта), иначе — 400 `invalid_location_zone`. Соответствие тарифа `requirements` типа решения при создании не проверяется — выбирайте тариф не ниже требований сами. Ответ 409 `no_free_node` означает, что в выбранной зоне сейчас нет свободных ресурсов под этот тариф — выберите другой тариф или зону. Неподходящая или устаревшая модель — 404 `model_not_found`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_solution(create_ai_solution, async_req=True)
        >>> result = thread.get()

        :param create_ai_solution: (required)
        :type create_ai_solution: CreateAiSolution
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAiSolution201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_ai_solution_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_ai_solution_with_http_info(create_ai_solution, **kwargs)  # noqa: E501

    @validate_arguments
    def create_ai_solution_with_http_info(self, create_ai_solution : CreateAiSolution, **kwargs) -> ApiResponse:  # noqa: E501
        """Создание AI-решения  # noqa: E501

        Чтобы создать AI-решение, отправьте POST-запрос на `/api/v1/cloud-ai/solutions`.  Выпускает для решения ключ AI Gateway и создаёт облачный сервер из образа решения; агент на сервере настраивается на выбранную модель через этот ключ. Сервер тарифицируется по выбранному тарифу, обращения к модели — через ключ AI Gateway.  Решение возвращается в статусе `creating`: развёртывание сервера и настройка агента занимают несколько минут. Дождитесь статуса `active`, а затем `ready: true` в методе получения статуса чата.  Тариф (`preset_id`) должен быть из той же локации, что и зона доступности (`availability_zone` или зона по умолчанию для региона аккаунта), иначе — 400 `invalid_location_zone`. Соответствие тарифа `requirements` типа решения при создании не проверяется — выбирайте тариф не ниже требований сами. Ответ 409 `no_free_node` означает, что в выбранной зоне сейчас нет свободных ресурсов под этот тариф — выберите другой тариф или зону. Неподходящая или устаревшая модель — 404 `model_not_found`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_ai_solution_with_http_info(create_ai_solution, async_req=True)
        >>> result = thread.get()

        :param create_ai_solution: (required)
        :type create_ai_solution: CreateAiSolution
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
        :rtype: tuple(CreateAiSolution201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'create_ai_solution'
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
                    " to method create_ai_solution" % _key
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
        if _params['create_ai_solution'] is not None:
            _body_params = _params['create_ai_solution']

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
            '201': "CreateAiSolution201Response",
            '400': None,
            '401': None,
            '402': "ErrorResponse",
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
            '503': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions', 'POST',
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
    def delete_ai_solution(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> None:  # noqa: E501
        """Удаление AI-решения  # noqa: E501

        Чтобы удалить AI-решение, отправьте DELETE-запрос на `/api/v1/cloud-ai/solutions/{solution_id}`.  Решение удаляется вместе с сервером и ключом AI Gateway. Действие необратимо: решение и история его чата становятся недоступны.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_ai_solution(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
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
            raise ValueError("Error! Please call the delete_ai_solution_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_ai_solution_with_http_info(solution_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_ai_solution_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление AI-решения  # noqa: E501

        Чтобы удалить AI-решение, отправьте DELETE-запрос на `/api/v1/cloud-ai/solutions/{solution_id}`.  Решение удаляется вместе с сервером и ключом AI Gateway. Действие необратимо: решение и история его чата становятся недоступны.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_ai_solution_with_http_info(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
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
            'solution_id'
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
                    " to method delete_ai_solution" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


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
            '/api/v1/cloud-ai/solutions/{solution_id}', 'DELETE',
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
    def get_ai_solution(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> CreateAiSolution201Response:  # noqa: E501
        """Получение AI-решения  # noqa: E501

        Чтобы получить AI-решение, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}`.  Статус решения выводится из текущего состояния его сервера. Тело ответа будет представлять собой объект JSON с ключом `ai_solution`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_solution(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAiSolution201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_solution_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_solution_with_http_info(solution_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_solution_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение AI-решения  # noqa: E501

        Чтобы получить AI-решение, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}`.  Статус решения выводится из текущего состояния его сервера. Тело ответа будет представлять собой объект JSON с ключом `ai_solution`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_solution_with_http_info(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
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
        :rtype: tuple(CreateAiSolution201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id'
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
                    " to method get_ai_solution" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


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
            '200': "CreateAiSolution201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}', 'GET',
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
    def get_ai_solution_chat_full_history(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], limit : Annotated[Optional[Any], Field(description="Количество сообщений на странице, от 1 до 10 000")] = None, offset : Annotated[Optional[Any], Field(description="Количество сообщений, которые нужно пропустить")] = None, **kwargs) -> GetAiSolutionMainChatHistory200Response:  # noqa: E501
        """Получение всей истории чата AI-решения  # noqa: E501

        Чтобы получить сообщения всех разговоров решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/history`.  В отличие от `chat/messages` (только основной разговор) и `chat/conversations/{conversation_id}/messages` (конкретный разговор), возвращает сообщения из всех разговоров сразу. Сообщения отсортированы по дате создания от новых к старым. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_chat_messages` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_solution_chat_full_history(solution_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param limit: Количество сообщений на странице, от 1 до 10 000
        :type limit: object
        :param offset: Количество сообщений, которые нужно пропустить
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
        :rtype: GetAiSolutionMainChatHistory200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_solution_chat_full_history_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_solution_chat_full_history_with_http_info(solution_id, limit, offset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_solution_chat_full_history_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], limit : Annotated[Optional[Any], Field(description="Количество сообщений на странице, от 1 до 10 000")] = None, offset : Annotated[Optional[Any], Field(description="Количество сообщений, которые нужно пропустить")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение всей истории чата AI-решения  # noqa: E501

        Чтобы получить сообщения всех разговоров решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/history`.  В отличие от `chat/messages` (только основной разговор) и `chat/conversations/{conversation_id}/messages` (конкретный разговор), возвращает сообщения из всех разговоров сразу. Сообщения отсортированы по дате создания от новых к старым. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_chat_messages` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_solution_chat_full_history_with_http_info(solution_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param limit: Количество сообщений на странице, от 1 до 10 000
        :type limit: object
        :param offset: Количество сообщений, которые нужно пропустить
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
        :rtype: tuple(GetAiSolutionMainChatHistory200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id',
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
                    " to method get_ai_solution_chat_full_history" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


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
            '200': "GetAiSolutionMainChatHistory200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}/chat/history', 'GET',
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
    def get_ai_solution_chat_history(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], conversation_id : Annotated[Any, Field(..., description="ID разговора. У основного разговора решения — `solution-<solution_id>`")], limit : Annotated[Optional[Any], Field(description="Количество сообщений на странице, от 1 до 10 000")] = None, offset : Annotated[Optional[Any], Field(description="Количество сообщений, которые нужно пропустить")] = None, **kwargs) -> GetAiSolutionMainChatHistory200Response:  # noqa: E501
        """Получение истории разговора AI-решения  # noqa: E501

        Чтобы получить историю разговора, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/conversations/{conversation_id}/messages`.  Сообщения отсортированы по дате создания от новых к старым: первая страница — последние сообщения разговора. Для несуществующего разговора возвращается пустой список. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_chat_messages` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_solution_chat_history(solution_id, conversation_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param conversation_id: ID разговора. У основного разговора решения — `solution-<solution_id>` (required)
        :type conversation_id: object
        :param limit: Количество сообщений на странице, от 1 до 10 000
        :type limit: object
        :param offset: Количество сообщений, которые нужно пропустить
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
        :rtype: GetAiSolutionMainChatHistory200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_solution_chat_history_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_solution_chat_history_with_http_info(solution_id, conversation_id, limit, offset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_solution_chat_history_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], conversation_id : Annotated[Any, Field(..., description="ID разговора. У основного разговора решения — `solution-<solution_id>`")], limit : Annotated[Optional[Any], Field(description="Количество сообщений на странице, от 1 до 10 000")] = None, offset : Annotated[Optional[Any], Field(description="Количество сообщений, которые нужно пропустить")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение истории разговора AI-решения  # noqa: E501

        Чтобы получить историю разговора, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/conversations/{conversation_id}/messages`.  Сообщения отсортированы по дате создания от новых к старым: первая страница — последние сообщения разговора. Для несуществующего разговора возвращается пустой список. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_chat_messages` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_solution_chat_history_with_http_info(solution_id, conversation_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param conversation_id: ID разговора. У основного разговора решения — `solution-<solution_id>` (required)
        :type conversation_id: object
        :param limit: Количество сообщений на странице, от 1 до 10 000
        :type limit: object
        :param offset: Количество сообщений, которые нужно пропустить
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
        :rtype: tuple(GetAiSolutionMainChatHistory200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id',
            'conversation_id',
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
                    " to method get_ai_solution_chat_history" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']

        if _params['conversation_id']:
            _path_params['conversation_id'] = _params['conversation_id']


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
            '200': "GetAiSolutionMainChatHistory200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}/chat/conversations/{conversation_id}/messages', 'GET',
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
    def get_ai_solution_chat_status(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> GetAiSolutionChatStatus200Response:  # noqa: E501
        """Получение статуса чата AI-решения  # noqa: E501

        Чтобы узнать, готов ли агент решения принимать сообщения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/status`.  Готовность чата отличается от статуса решения: тот выводится из состояния сервера, а сервер включается задолго до того, как будет установлено и настроено ПО агента. После создания или запуска решения опрашивайте этот метод, пока `ready` не станет `true`. Тело ответа будет представлять собой объект JSON с ключом `ai_solution_chat_status`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_solution_chat_status(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAiSolutionChatStatus200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_solution_chat_status_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_solution_chat_status_with_http_info(solution_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_solution_chat_status_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение статуса чата AI-решения  # noqa: E501

        Чтобы узнать, готов ли агент решения принимать сообщения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/status`.  Готовность чата отличается от статуса решения: тот выводится из состояния сервера, а сервер включается задолго до того, как будет установлено и настроено ПО агента. После создания или запуска решения опрашивайте этот метод, пока `ready` не станет `true`. Тело ответа будет представлять собой объект JSON с ключом `ai_solution_chat_status`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_solution_chat_status_with_http_info(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
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
        :rtype: tuple(GetAiSolutionChatStatus200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id'
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
                    " to method get_ai_solution_chat_status" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


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
            '200': "GetAiSolutionChatStatus200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}/chat/status', 'GET',
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
    def get_ai_solution_main_chat_history(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], limit : Annotated[Optional[Any], Field(description="Количество сообщений на странице, от 1 до 10 000")] = None, offset : Annotated[Optional[Any], Field(description="Количество сообщений, которые нужно пропустить")] = None, **kwargs) -> GetAiSolutionMainChatHistory200Response:  # noqa: E501
        """Получение истории основного разговора AI-решения  # noqa: E501

        Чтобы получить историю основного разговора решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/messages`.  ID основного разговора знать не нужно; для других разговоров используйте метод с явным `conversation_id`. Сообщения отсортированы по дате создания от новых к старым: первая страница — последние сообщения. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_chat_messages` и `meta` (`meta.total` — общее количество сообщений).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_solution_main_chat_history(solution_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param limit: Количество сообщений на странице, от 1 до 10 000
        :type limit: object
        :param offset: Количество сообщений, которые нужно пропустить
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
        :rtype: GetAiSolutionMainChatHistory200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_ai_solution_main_chat_history_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_ai_solution_main_chat_history_with_http_info(solution_id, limit, offset, **kwargs)  # noqa: E501

    @validate_arguments
    def get_ai_solution_main_chat_history_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], limit : Annotated[Optional[Any], Field(description="Количество сообщений на странице, от 1 до 10 000")] = None, offset : Annotated[Optional[Any], Field(description="Количество сообщений, которые нужно пропустить")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение истории основного разговора AI-решения  # noqa: E501

        Чтобы получить историю основного разговора решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/messages`.  ID основного разговора знать не нужно; для других разговоров используйте метод с явным `conversation_id`. Сообщения отсортированы по дате создания от новых к старым: первая страница — последние сообщения. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_chat_messages` и `meta` (`meta.total` — общее количество сообщений).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_ai_solution_main_chat_history_with_http_info(solution_id, limit, offset, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param limit: Количество сообщений на странице, от 1 до 10 000
        :type limit: object
        :param offset: Количество сообщений, которые нужно пропустить
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
        :rtype: tuple(GetAiSolutionMainChatHistory200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id',
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
                    " to method get_ai_solution_main_chat_history" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


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
            '200': "GetAiSolutionMainChatHistory200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}/chat/messages', 'GET',
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
    def list_ai_solution_conversations(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> ListAiSolutionConversations200Response:  # noqa: E501
        """Получение списка разговоров AI-решения  # noqa: E501

        Чтобы получить список разговоров с агентом решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/conversations`.  Возвращает все разговоры решения, в которых есть сообщения, включая основной, отсортированные по дате последнего сообщения от новых к старым. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_conversations` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_ai_solution_conversations(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListAiSolutionConversations200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_ai_solution_conversations_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_ai_solution_conversations_with_http_info(solution_id, **kwargs)  # noqa: E501

    @validate_arguments
    def list_ai_solution_conversations_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка разговоров AI-решения  # noqa: E501

        Чтобы получить список разговоров с агентом решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/conversations`.  Возвращает все разговоры решения, в которых есть сообщения, включая основной, отсортированные по дате последнего сообщения от новых к старым. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_conversations` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_ai_solution_conversations_with_http_info(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
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
        :rtype: tuple(ListAiSolutionConversations200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id'
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
                    " to method list_ai_solution_conversations" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


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
            '200': "ListAiSolutionConversations200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}/chat/conversations', 'GET',
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
    def list_ai_solution_telegram_bots(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> ListAiSolutionTelegramBots200Response:  # noqa: E501
        """Получение списка Telegram-ботов AI-решения  # noqa: E501

        Чтобы получить список Telegram-ботов решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots`.  Возвращает подключённых к решению ботов и состояние их подтверждения. Список читается с сервера решения. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_telegram_bots` и `meta`.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_ai_solution_telegram_bots(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ListAiSolutionTelegramBots200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_ai_solution_telegram_bots_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_ai_solution_telegram_bots_with_http_info(solution_id, **kwargs)  # noqa: E501

    @validate_arguments
    def list_ai_solution_telegram_bots_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка Telegram-ботов AI-решения  # noqa: E501

        Чтобы получить список Telegram-ботов решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots`.  Возвращает подключённых к решению ботов и состояние их подтверждения. Список читается с сервера решения. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_telegram_bots` и `meta`.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_ai_solution_telegram_bots_with_http_info(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
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
        :rtype: tuple(ListAiSolutionTelegramBots200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id'
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
                    " to method list_ai_solution_telegram_bots" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


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
            '200': "ListAiSolutionTelegramBots200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
            '502': "ErrorResponse",
            '503': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots', 'GET',
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
    def list_ai_solution_types(self, **kwargs) -> ListAiSolutionTypes200Response:  # noqa: E501
        """Получение списка типов AI-решений  # noqa: E501

        Чтобы получить список типов AI-решений, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/types`.  Возвращает каталог готовых решений, которые можно развернуть на облачном сервере, с минимальными требованиями к конфигурации сервера (`requirements`). Тело ответа будет представлять собой объект JSON с ключами `ai_solution_types` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_ai_solution_types(async_req=True)
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
        :rtype: ListAiSolutionTypes200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_ai_solution_types_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_ai_solution_types_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def list_ai_solution_types_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка типов AI-решений  # noqa: E501

        Чтобы получить список типов AI-решений, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/types`.  Возвращает каталог готовых решений, которые можно развернуть на облачном сервере, с минимальными требованиями к конфигурации сервера (`requirements`). Тело ответа будет представлять собой объект JSON с ключами `ai_solution_types` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_ai_solution_types_with_http_info(async_req=True)
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
        :rtype: tuple(ListAiSolutionTypes200Response, status_code(int), headers(HTTPHeaderDict))
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
                    " to method list_ai_solution_types" % _key
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
            '200': "ListAiSolutionTypes200Response",
            '400': None,
            '401': None,
            '403': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/types', 'GET',
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
    def list_ai_solutions(self, **kwargs) -> ListAiSolutions200Response:  # noqa: E501
        """Получение списка AI-решений  # noqa: E501

        Чтобы получить список AI-решений аккаунта, отправьте GET-запрос на `/api/v1/cloud-ai/solutions`.  Возвращает все решения аккаунта, кроме удалённых. Статус каждого решения выводится из текущего состояния его сервера. Тело ответа будет представлять собой объект JSON с ключами `ai_solutions` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_ai_solutions(async_req=True)
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
        :rtype: ListAiSolutions200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the list_ai_solutions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.list_ai_solutions_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def list_ai_solutions_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка AI-решений  # noqa: E501

        Чтобы получить список AI-решений аккаунта, отправьте GET-запрос на `/api/v1/cloud-ai/solutions`.  Возвращает все решения аккаунта, кроме удалённых. Статус каждого решения выводится из текущего состояния его сервера. Тело ответа будет представлять собой объект JSON с ключами `ai_solutions` и `meta`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_ai_solutions_with_http_info(async_req=True)
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
        :rtype: tuple(ListAiSolutions200Response, status_code(int), headers(HTTPHeaderDict))
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
                    " to method list_ai_solutions" % _key
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
            '200': "ListAiSolutions200Response",
            '400': None,
            '401': None,
            '403': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions', 'GET',
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
    def regenerate_ai_solution_ai_key(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> RegenerateAiSolutionAiKey200Response:  # noqa: E501
        """Перевыпуск ключа AI Gateway решения  # noqa: E501

        Чтобы перевыпустить ключ AI Gateway решения, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/ai-key/regenerate`.  Единственный способ сменить этот ключ: он выпущен платформой для решения и в разделе AI Gateway доступен только для чтения. Новый ключ сразу записывается в конфигурацию агента на сервере решения, старый перестаёт работать немедленно. Сервер должен быть включён и полностью развёрнут — это проверяется до перевыпуска, потому что отменить его нельзя. Если записать новый ключ на сервер не удалось, повторите запрос.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.regenerate_ai_solution_ai_key(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: RegenerateAiSolutionAiKey200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the regenerate_ai_solution_ai_key_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.regenerate_ai_solution_ai_key_with_http_info(solution_id, **kwargs)  # noqa: E501

    @validate_arguments
    def regenerate_ai_solution_ai_key_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> ApiResponse:  # noqa: E501
        """Перевыпуск ключа AI Gateway решения  # noqa: E501

        Чтобы перевыпустить ключ AI Gateway решения, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/ai-key/regenerate`.  Единственный способ сменить этот ключ: он выпущен платформой для решения и в разделе AI Gateway доступен только для чтения. Новый ключ сразу записывается в конфигурацию агента на сервере решения, старый перестаёт работать немедленно. Сервер должен быть включён и полностью развёрнут — это проверяется до перевыпуска, потому что отменить его нельзя. Если записать новый ключ на сервер не удалось, повторите запрос.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.regenerate_ai_solution_ai_key_with_http_info(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
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
        :rtype: tuple(RegenerateAiSolutionAiKey200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id'
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
                    " to method regenerate_ai_solution_ai_key" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


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
            '200': "RegenerateAiSolutionAiKey200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
            '502': "ErrorResponse",
            '503': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}/ai-key/regenerate', 'POST',
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
    def remove_ai_solution_telegram_bot(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], account_key : Annotated[Any, Field(..., description="ID Telegram-бота в решении (`account_key` из списка ботов) в формате `b<число>`, например `b123456789`")], **kwargs) -> None:  # noqa: E501
        """Отключение Telegram-бота от AI-решения  # noqa: E501

        Чтобы отключить Telegram-бота от решения, отправьте DELETE-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key}`.  Удаляет бота из конфигурации сервера решения: агент перестаёт отвечать в этом боте. Если бот не подключён, запрос всё равно возвращает 204. Некорректный `account_key` — ответ 400 `ai_solution_telegram_token_is_invalid`.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_ai_solution_telegram_bot(solution_id, account_key, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param account_key: ID Telegram-бота в решении (`account_key` из списка ботов) в формате `b<число>`, например `b123456789` (required)
        :type account_key: object
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
            raise ValueError("Error! Please call the remove_ai_solution_telegram_bot_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.remove_ai_solution_telegram_bot_with_http_info(solution_id, account_key, **kwargs)  # noqa: E501

    @validate_arguments
    def remove_ai_solution_telegram_bot_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], account_key : Annotated[Any, Field(..., description="ID Telegram-бота в решении (`account_key` из списка ботов) в формате `b<число>`, например `b123456789`")], **kwargs) -> ApiResponse:  # noqa: E501
        """Отключение Telegram-бота от AI-решения  # noqa: E501

        Чтобы отключить Telegram-бота от решения, отправьте DELETE-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key}`.  Удаляет бота из конфигурации сервера решения: агент перестаёт отвечать в этом боте. Если бот не подключён, запрос всё равно возвращает 204. Некорректный `account_key` — ответ 400 `ai_solution_telegram_token_is_invalid`.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_ai_solution_telegram_bot_with_http_info(solution_id, account_key, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param account_key: ID Telegram-бота в решении (`account_key` из списка ботов) в формате `b<число>`, например `b123456789` (required)
        :type account_key: object
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
            'solution_id',
            'account_key'
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
                    " to method remove_ai_solution_telegram_bot" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']

        if _params['account_key']:
            _path_params['account_key'] = _params['account_key']


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
            '/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key}', 'DELETE',
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
    def reset_ai_solution_chat(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], reset_ai_solution_chat : Optional[ResetAiSolutionChat] = None, **kwargs) -> ResetAiSolutionChat200Response:  # noqa: E501
        """Сброс контекста разговора AI-решения  # noqa: E501

        Чтобы сбросить контекст разговора, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/reset`.  Контекст сбрасывается на месте: разговор сохраняет `conversation_id`, но агент больше не видит предыдущих сообщений. Без `conversation_id` сбрасывается основной разговор решения. В историю добавляется служебное сообщение с ролью `context-reset`, отмечающее границу текущего контекста, — оно и возвращается в ответе (с ключом `ai_solution_chat_message`). Отметка добавляется и для разговора, в котором ещё не было сообщений.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reset_ai_solution_chat(solution_id, reset_ai_solution_chat, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param reset_ai_solution_chat:
        :type reset_ai_solution_chat: ResetAiSolutionChat
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ResetAiSolutionChat200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the reset_ai_solution_chat_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.reset_ai_solution_chat_with_http_info(solution_id, reset_ai_solution_chat, **kwargs)  # noqa: E501

    @validate_arguments
    def reset_ai_solution_chat_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], reset_ai_solution_chat : Optional[ResetAiSolutionChat] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Сброс контекста разговора AI-решения  # noqa: E501

        Чтобы сбросить контекст разговора, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/reset`.  Контекст сбрасывается на месте: разговор сохраняет `conversation_id`, но агент больше не видит предыдущих сообщений. Без `conversation_id` сбрасывается основной разговор решения. В историю добавляется служебное сообщение с ролью `context-reset`, отмечающее границу текущего контекста, — оно и возвращается в ответе (с ключом `ai_solution_chat_message`). Отметка добавляется и для разговора, в котором ещё не было сообщений.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reset_ai_solution_chat_with_http_info(solution_id, reset_ai_solution_chat, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param reset_ai_solution_chat:
        :type reset_ai_solution_chat: ResetAiSolutionChat
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
        :rtype: tuple(ResetAiSolutionChat200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id',
            'reset_ai_solution_chat'
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
                    " to method reset_ai_solution_chat" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['reset_ai_solution_chat'] is not None:
            _body_params = _params['reset_ai_solution_chat']

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
            '200': "ResetAiSolutionChat200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
            '502': "ErrorResponse",
            '503': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}/chat/reset', 'POST',
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
    def send_ai_solution_message(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], send_ai_solution_message : SendAiSolutionMessage, **kwargs) -> SendAiSolutionMessage200Response:  # noqa: E501
        """Отправка сообщения агенту AI-решения  # noqa: E501

        Чтобы отправить сообщение агенту решения, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/messages`.  Ответ возвращается целиком после завершения хода агента (ожидание — до 3 минут). Без `conversation_id` сообщение уходит в основной разговор решения; новый разговор начинается только при явной передаче нового ID. Без `message` агент сам здоровается — так можно показать первую реплику чата. Чтобы получать ответ по мере генерации, используйте потоковый метод.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_ai_solution_message(solution_id, send_ai_solution_message, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param send_ai_solution_message: (required)
        :type send_ai_solution_message: SendAiSolutionMessage
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SendAiSolutionMessage200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the send_ai_solution_message_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.send_ai_solution_message_with_http_info(solution_id, send_ai_solution_message, **kwargs)  # noqa: E501

    @validate_arguments
    def send_ai_solution_message_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], send_ai_solution_message : SendAiSolutionMessage, **kwargs) -> ApiResponse:  # noqa: E501
        """Отправка сообщения агенту AI-решения  # noqa: E501

        Чтобы отправить сообщение агенту решения, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/messages`.  Ответ возвращается целиком после завершения хода агента (ожидание — до 3 минут). Без `conversation_id` сообщение уходит в основной разговор решения; новый разговор начинается только при явной передаче нового ID. Без `message` агент сам здоровается — так можно показать первую реплику чата. Чтобы получать ответ по мере генерации, используйте потоковый метод.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.send_ai_solution_message_with_http_info(solution_id, send_ai_solution_message, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param send_ai_solution_message: (required)
        :type send_ai_solution_message: SendAiSolutionMessage
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
        :rtype: tuple(SendAiSolutionMessage200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id',
            'send_ai_solution_message'
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
                    " to method send_ai_solution_message" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['send_ai_solution_message'] is not None:
            _body_params = _params['send_ai_solution_message']

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
            '200': "SendAiSolutionMessage200Response",
            '400': None,
            '401': None,
            '402': "ErrorResponse",
            '403': None,
            '404': None,
            '429': None,
            '500': None,
            '502': "ErrorResponse",
            '503': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}/chat/messages', 'POST',
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
    def shutdown_ai_solution(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> None:  # noqa: E501
        """Выключение AI-решения  # noqa: E501

        Чтобы выключить AI-решение, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/shutdown`.  Выключает сервер решения. Действие асинхронное: следите за результатом по статусу решения (обычно 1–2 минуты до `stopped`). Пока сервер выключен, чат недоступен, а сервер продолжает тарифицироваться. Выключение уже выключенного решения возвращает 204. Пока над сервером выполняется другое действие, ответ — 409 `ai_solution_is_busy`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.shutdown_ai_solution(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
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
            raise ValueError("Error! Please call the shutdown_ai_solution_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.shutdown_ai_solution_with_http_info(solution_id, **kwargs)  # noqa: E501

    @validate_arguments
    def shutdown_ai_solution_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> ApiResponse:  # noqa: E501
        """Выключение AI-решения  # noqa: E501

        Чтобы выключить AI-решение, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/shutdown`.  Выключает сервер решения. Действие асинхронное: следите за результатом по статусу решения (обычно 1–2 минуты до `stopped`). Пока сервер выключен, чат недоступен, а сервер продолжает тарифицироваться. Выключение уже выключенного решения возвращает 204. Пока над сервером выполняется другое действие, ответ — 409 `ai_solution_is_busy`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.shutdown_ai_solution_with_http_info(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
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
            'solution_id'
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
                    " to method shutdown_ai_solution" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


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
            '/api/v1/cloud-ai/solutions/{solution_id}/shutdown', 'POST',
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
    def start_ai_solution(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> None:  # noqa: E501
        """Запуск AI-решения  # noqa: E501

        Чтобы запустить AI-решение, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/start`.  Включает сервер решения. Действие асинхронное: следите за результатом по статусу решения, а готовность агента проверяйте методом получения статуса чата. Пока над сервером выполняется действие, запуск и выключение возвращают 409 `ai_solution_is_busy`.  Не вызывайте метод для работающего решения: запрос будет принят (204) и запустит действие над сервером, а решение на несколько минут станет занятым.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.start_ai_solution(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
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
            raise ValueError("Error! Please call the start_ai_solution_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.start_ai_solution_with_http_info(solution_id, **kwargs)  # noqa: E501

    @validate_arguments
    def start_ai_solution_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], **kwargs) -> ApiResponse:  # noqa: E501
        """Запуск AI-решения  # noqa: E501

        Чтобы запустить AI-решение, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/start`.  Включает сервер решения. Действие асинхронное: следите за результатом по статусу решения, а готовность агента проверяйте методом получения статуса чата. Пока над сервером выполняется действие, запуск и выключение возвращают 409 `ai_solution_is_busy`.  Не вызывайте метод для работающего решения: запрос будет принят (204) и запустит действие над сервером, а решение на несколько минут станет занятым.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.start_ai_solution_with_http_info(solution_id, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
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
            'solution_id'
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
                    " to method start_ai_solution" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


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
            '/api/v1/cloud-ai/solutions/{solution_id}/start', 'POST',
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
    def stop_ai_solution_chat(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], stop_ai_solution_chat : Optional[StopAiSolutionChat] = None, **kwargs) -> None:  # noqa: E501
        """Остановка хода агента AI-решения  # noqa: E501

        Чтобы остановить текущий ход агента, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/stop`.  Прерывает генерацию ответа — например, если ответ зациклился или тратит слишком много токенов. Без `conversation_id` останавливается текущий ход основного разговора решения. Ход прерывается на стороне агента: закрыть соединение недостаточно, потому что принятый агентом ход продолжает выполняться независимо от клиента. Если хода нет, запрос всё равно возвращает 204.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.stop_ai_solution_chat(solution_id, stop_ai_solution_chat, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param stop_ai_solution_chat:
        :type stop_ai_solution_chat: StopAiSolutionChat
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
            raise ValueError("Error! Please call the stop_ai_solution_chat_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.stop_ai_solution_chat_with_http_info(solution_id, stop_ai_solution_chat, **kwargs)  # noqa: E501

    @validate_arguments
    def stop_ai_solution_chat_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], stop_ai_solution_chat : Optional[StopAiSolutionChat] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Остановка хода агента AI-решения  # noqa: E501

        Чтобы остановить текущий ход агента, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/stop`.  Прерывает генерацию ответа — например, если ответ зациклился или тратит слишком много токенов. Без `conversation_id` останавливается текущий ход основного разговора решения. Ход прерывается на стороне агента: закрыть соединение недостаточно, потому что принятый агентом ход продолжает выполняться независимо от клиента. Если хода нет, запрос всё равно возвращает 204.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.stop_ai_solution_chat_with_http_info(solution_id, stop_ai_solution_chat, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param stop_ai_solution_chat:
        :type stop_ai_solution_chat: StopAiSolutionChat
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
            'solution_id',
            'stop_ai_solution_chat'
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
                    " to method stop_ai_solution_chat" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['stop_ai_solution_chat'] is not None:
            _body_params = _params['stop_ai_solution_chat']

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
            '/api/v1/cloud-ai/solutions/{solution_id}/chat/stop', 'POST',
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
    def stream_ai_solution_chat(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], send_ai_solution_message : SendAiSolutionMessage, **kwargs) -> object:  # noqa: E501
        """Отправка сообщения агенту AI-решения с потоковым ответом  # noqa: E501

        Чтобы отправить сообщение агенту решения и получать ответ потоком, отправьте POST-запрос на `https://agent.timeweb.cloud/api/v1/cloud-ai/solutions/{solution_id}/chat/stream`.  Метод работает на `https://agent.timeweb.cloud`, а не на `https://api.timeweb.cloud`: шлюз публичного API накапливает ответ целиком и не может передавать его по частям. Авторизация та же — API-токен в заголовке `Authorization`; токену с ограниченными правами нужен доступ на запись к AI-сервисам. Тело запроса такое же, как у метода отправки сообщения.  Ответ — `text/event-stream`: каждое событие приходит как `event: <тип>` и `data: <JSON>`. Отправка сообщения и подписка на ответ — один запрос, поэтому начало ответа не теряется. Строки, начинающиеся с `:`, — комментарии для поддержания соединения (каждые 15 секунд), их нужно игнорировать. ID разговора возвращается в заголовке ответа `X-Conversation-Id`.  Типы событий: - `subscribed` `{}` — ход принят; - `delta` `{text, seq, runId}` — очередной фрагмент ответа; - `tool` `{name, target, phase, status, seq, runId}` — агент использует инструмент; - `message` `{text, seq, id, stopReason}` — финальный ответ целиком, всегда после последнего `delta`; - `done` `{phase, seq, runId}` — ход завершён; - `error` `{reason, message, budget?}` — ход не удался. `reason`: `empty_reply` — агент не выдал текста; `stream_failed` — поток прервался; `agent_failed` — ход упал на стороне агента при исправном соединении, повтор имеет смысл; `budget_exceeded` — исчерпан лимит расходов ключа AI Gateway решения, в `budget` `{max, spent, resetAt}` — цифры лимита, если они известны. `error` всегда последнее событие потока и может прийти после `done` (например, с `empty_reply`).  Ошибки, возникшие до начала потока (решение не найдено, некорректный запрос, нет доступа), возвращаются обычным JSON-ответом с соответствующим HTTP-статусом. Если сервер решения выключен или недоступен, поток может открыться и сразу завершиться событием `error` с `reason: stream_failed` — проверяйте готовность чата заранее методом получения статуса чата.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.stream_ai_solution_chat(solution_id, send_ai_solution_message, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param send_ai_solution_message: (required)
        :type send_ai_solution_message: SendAiSolutionMessage
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
            raise ValueError("Error! Please call the stream_ai_solution_chat_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.stream_ai_solution_chat_with_http_info(solution_id, send_ai_solution_message, **kwargs)  # noqa: E501

    @validate_arguments
    def stream_ai_solution_chat_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], send_ai_solution_message : SendAiSolutionMessage, **kwargs) -> ApiResponse:  # noqa: E501
        """Отправка сообщения агенту AI-решения с потоковым ответом  # noqa: E501

        Чтобы отправить сообщение агенту решения и получать ответ потоком, отправьте POST-запрос на `https://agent.timeweb.cloud/api/v1/cloud-ai/solutions/{solution_id}/chat/stream`.  Метод работает на `https://agent.timeweb.cloud`, а не на `https://api.timeweb.cloud`: шлюз публичного API накапливает ответ целиком и не может передавать его по частям. Авторизация та же — API-токен в заголовке `Authorization`; токену с ограниченными правами нужен доступ на запись к AI-сервисам. Тело запроса такое же, как у метода отправки сообщения.  Ответ — `text/event-stream`: каждое событие приходит как `event: <тип>` и `data: <JSON>`. Отправка сообщения и подписка на ответ — один запрос, поэтому начало ответа не теряется. Строки, начинающиеся с `:`, — комментарии для поддержания соединения (каждые 15 секунд), их нужно игнорировать. ID разговора возвращается в заголовке ответа `X-Conversation-Id`.  Типы событий: - `subscribed` `{}` — ход принят; - `delta` `{text, seq, runId}` — очередной фрагмент ответа; - `tool` `{name, target, phase, status, seq, runId}` — агент использует инструмент; - `message` `{text, seq, id, stopReason}` — финальный ответ целиком, всегда после последнего `delta`; - `done` `{phase, seq, runId}` — ход завершён; - `error` `{reason, message, budget?}` — ход не удался. `reason`: `empty_reply` — агент не выдал текста; `stream_failed` — поток прервался; `agent_failed` — ход упал на стороне агента при исправном соединении, повтор имеет смысл; `budget_exceeded` — исчерпан лимит расходов ключа AI Gateway решения, в `budget` `{max, spent, resetAt}` — цифры лимита, если они известны. `error` всегда последнее событие потока и может прийти после `done` (например, с `empty_reply`).  Ошибки, возникшие до начала потока (решение не найдено, некорректный запрос, нет доступа), возвращаются обычным JSON-ответом с соответствующим HTTP-статусом. Если сервер решения выключен или недоступен, поток может открыться и сразу завершиться событием `error` с `reason: stream_failed` — проверяйте готовность чата заранее методом получения статуса чата.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.stream_ai_solution_chat_with_http_info(solution_id, send_ai_solution_message, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param send_ai_solution_message: (required)
        :type send_ai_solution_message: SendAiSolutionMessage
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
            'https://agent.timeweb.cloud'
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
            'solution_id',
            'send_ai_solution_message'
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
                    " to method stream_ai_solution_chat" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['send_ai_solution_message'] is not None:
            _body_params = _params['send_ai_solution_message']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['text/event-stream', 'application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "object",
            '400': "StreamError",
            '403': "StreamError",
            '404': "StreamError",
            '500': "StreamError",
            '503': "StreamError",
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}/chat/stream', 'POST',
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
    def update_ai_solution(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], update_ai_solution : UpdateAiSolution, **kwargs) -> CreateAiSolution201Response:  # noqa: E501
        """Изменение AI-решения  # noqa: E501

        Чтобы изменить AI-решение, отправьте PATCH-запрос на `/api/v1/cloud-ai/solutions/{solution_id}`.  Меняются только переданные поля; `description: null` очищает описание. Смена модели переписывает конфигурацию агента на сервере решения и перезапускает агента, поэтому сервер должен быть включён и полностью развёрнут — иначе запрос завершится ошибкой и ничего не изменится. Смена только названия или описания сервер не затрагивает. Неподходящая модель — 404 `model_not_found`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_ai_solution(solution_id, update_ai_solution, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param update_ai_solution: (required)
        :type update_ai_solution: UpdateAiSolution
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAiSolution201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_ai_solution_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_ai_solution_with_http_info(solution_id, update_ai_solution, **kwargs)  # noqa: E501

    @validate_arguments
    def update_ai_solution_with_http_info(self, solution_id : Annotated[Any, Field(..., description="ID AI-решения")], update_ai_solution : UpdateAiSolution, **kwargs) -> ApiResponse:  # noqa: E501
        """Изменение AI-решения  # noqa: E501

        Чтобы изменить AI-решение, отправьте PATCH-запрос на `/api/v1/cloud-ai/solutions/{solution_id}`.  Меняются только переданные поля; `description: null` очищает описание. Смена модели переписывает конфигурацию агента на сервере решения и перезапускает агента, поэтому сервер должен быть включён и полностью развёрнут — иначе запрос завершится ошибкой и ничего не изменится. Смена только названия или описания сервер не затрагивает. Неподходящая модель — 404 `model_not_found`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_ai_solution_with_http_info(solution_id, update_ai_solution, async_req=True)
        >>> result = thread.get()

        :param solution_id: ID AI-решения (required)
        :type solution_id: object
        :param update_ai_solution: (required)
        :type update_ai_solution: UpdateAiSolution
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
        :rtype: tuple(CreateAiSolution201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'solution_id',
            'update_ai_solution'
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
                    " to method update_ai_solution" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['solution_id']:
            _path_params['solution_id'] = _params['solution_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_ai_solution'] is not None:
            _body_params = _params['update_ai_solution']

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
            '200': "CreateAiSolution201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
            '502': "ErrorResponse",
            '503': "ErrorResponse",
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/solutions/{solution_id}', 'PATCH',
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
