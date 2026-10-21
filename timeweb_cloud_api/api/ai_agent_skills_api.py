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

from timeweb_cloud_api.models.connect_skills import ConnectSkills
from timeweb_cloud_api.models.create_agent_skill201_response import CreateAgentSkill201Response
from timeweb_cloud_api.models.create_skill import CreateSkill
from timeweb_cloud_api.models.get_agent_skill200_response import GetAgentSkill200Response
from timeweb_cloud_api.models.get_agent_skill_catalog200_response import GetAgentSkillCatalog200Response
from timeweb_cloud_api.models.get_agent_skill_library200_response import GetAgentSkillLibrary200Response
from timeweb_cloud_api.models.get_agent_skill_version200_response import GetAgentSkillVersion200Response
from timeweb_cloud_api.models.get_agent_skill_versions200_response import GetAgentSkillVersions200Response
from timeweb_cloud_api.models.get_agent_skills_for_agent200_response import GetAgentSkillsForAgent200Response
from timeweb_cloud_api.models.install_agent_skill_from_catalog200_response import InstallAgentSkillFromCatalog200Response
from timeweb_cloud_api.models.install_and_connect_agent_skill200_response import InstallAndConnectAgentSkill200Response
from timeweb_cloud_api.models.install_and_connect_skill import InstallAndConnectSkill
from timeweb_cloud_api.models.set_agent_skill import SetAgentSkill
from timeweb_cloud_api.models.set_agent_skill_for_agent200_response import SetAgentSkillForAgent200Response
from timeweb_cloud_api.models.sync_agent_skill_agents_versions200_response import SyncAgentSkillAgentsVersions200Response
from timeweb_cloud_api.models.sync_agent_skill_versions_for_agent200_response import SyncAgentSkillVersionsForAgent200Response
from timeweb_cloud_api.models.update_skill import UpdateSkill

from timeweb_cloud_api.api_client import ApiClient
from timeweb_cloud_api.api_response import ApiResponse
from timeweb_cloud_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AIAgentSkillsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def apply_agent_skill_catalog_update(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> CreateAgentSkill201Response:  # noqa: E501
        """Применение обновления навыка из каталога  # noqa: E501

        Чтобы применить к установленному навыку новую версию из каталога, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/apply-catalog-update`.  Текст «когда применять» и инструкция заменяются каталожными, при этом создаётся новая версия: прежний текст, в том числе ваши правки, остаётся в истории. Название навыка не меняется. Если обновления нет, ничего не меняется (`meta.version_created` — `false`).  Для навыка, установленного не из каталога, вернётся 409 с `error_code` `skill_is_not_installed_from_catalog`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.apply_agent_skill_catalog_update(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAgentSkill201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the apply_agent_skill_catalog_update_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.apply_agent_skill_catalog_update_with_http_info(skill_id, **kwargs)  # noqa: E501

    @validate_arguments
    def apply_agent_skill_catalog_update_with_http_info(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> ApiResponse:  # noqa: E501
        """Применение обновления навыка из каталога  # noqa: E501

        Чтобы применить к установленному навыку новую версию из каталога, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/apply-catalog-update`.  Текст «когда применять» и инструкция заменяются каталожными, при этом создаётся новая версия: прежний текст, в том числе ваши правки, остаётся в истории. Название навыка не меняется. Если обновления нет, ничего не меняется (`meta.version_created` — `false`).  Для навыка, установленного не из каталога, вернётся 409 с `error_code` `skill_is_not_installed_from_catalog`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.apply_agent_skill_catalog_update_with_http_info(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
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
        :rtype: tuple(CreateAgentSkill201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'skill_id'
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
                    " to method apply_agent_skill_catalog_update" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']


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
            '200': "CreateAgentSkill201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skills/{skill_id}/apply-catalog-update', 'POST',
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
    def connect_agent_skills_to_agent(self, agent_id : Annotated[Any, Field(..., description="ID агента")], connect_skills : ConnectSkills, **kwargs) -> GetAgentSkillsForAgent200Response:  # noqa: E501
        """Подключение нескольких навыков к агенту  # noqa: E501

        Чтобы подключить и сразу включить у агента несколько навыков, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/connect`.  Навыки, которых нет в аккаунте, пропускаются без ошибки. Уже подключённые навыки включаются; если для них передана версия, агент закрепляется на ней. В ответе — только навыки, которые удалось подключить.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.connect_agent_skills_to_agent(agent_id, connect_skills, async_req=True)
        >>> result = thread.get()

        :param agent_id: ID агента (required)
        :type agent_id: object
        :param connect_skills: (required)
        :type connect_skills: ConnectSkills
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAgentSkillsForAgent200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the connect_agent_skills_to_agent_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.connect_agent_skills_to_agent_with_http_info(agent_id, connect_skills, **kwargs)  # noqa: E501

    @validate_arguments
    def connect_agent_skills_to_agent_with_http_info(self, agent_id : Annotated[Any, Field(..., description="ID агента")], connect_skills : ConnectSkills, **kwargs) -> ApiResponse:  # noqa: E501
        """Подключение нескольких навыков к агенту  # noqa: E501

        Чтобы подключить и сразу включить у агента несколько навыков, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/connect`.  Навыки, которых нет в аккаунте, пропускаются без ошибки. Уже подключённые навыки включаются; если для них передана версия, агент закрепляется на ней. В ответе — только навыки, которые удалось подключить.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.connect_agent_skills_to_agent_with_http_info(agent_id, connect_skills, async_req=True)
        >>> result = thread.get()

        :param agent_id: ID агента (required)
        :type agent_id: object
        :param connect_skills: (required)
        :type connect_skills: ConnectSkills
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
        :rtype: tuple(GetAgentSkillsForAgent200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'agent_id',
            'connect_skills'
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
                    " to method connect_agent_skills_to_agent" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
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
        if _params['connect_skills'] is not None:
            _body_params = _params['connect_skills']

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
            '200': "GetAgentSkillsForAgent200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/agents/{agent_id}/skills/connect', 'POST',
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
    def create_agent_skill(self, create_skill : CreateSkill, **kwargs) -> CreateAgentSkill201Response:  # noqa: E501
        """Создание навыка  # noqa: E501

        Чтобы создать навык, отправьте POST-запрос на `/api/v1/cloud-ai/skills`.  Навык создаётся с версией 1 и ни к одному агенту не подключается. Предупреждения о качестве текста приходят в `meta.warnings` и не мешают сохранению. Скрипты передаются в теле запроса. Их общий размер — до 10 МБ, а всё тело запроса — до 16 МБ; запрос с телом больше отклоняется до проверки.  Если навык с таким названием уже есть, вернётся 409 с `error_code` `skill_name_already_exists`. Если скрипты не прошли проверку (больше 20 файлов, повторяющиеся имена, общий размер больше 10 МБ, файл без содержимого), вернётся 400 с `error_code` `skill_scripts_invalid`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_agent_skill(create_skill, async_req=True)
        >>> result = thread.get()

        :param create_skill: (required)
        :type create_skill: CreateSkill
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAgentSkill201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the create_agent_skill_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.create_agent_skill_with_http_info(create_skill, **kwargs)  # noqa: E501

    @validate_arguments
    def create_agent_skill_with_http_info(self, create_skill : CreateSkill, **kwargs) -> ApiResponse:  # noqa: E501
        """Создание навыка  # noqa: E501

        Чтобы создать навык, отправьте POST-запрос на `/api/v1/cloud-ai/skills`.  Навык создаётся с версией 1 и ни к одному агенту не подключается. Предупреждения о качестве текста приходят в `meta.warnings` и не мешают сохранению. Скрипты передаются в теле запроса. Их общий размер — до 10 МБ, а всё тело запроса — до 16 МБ; запрос с телом больше отклоняется до проверки.  Если навык с таким названием уже есть, вернётся 409 с `error_code` `skill_name_already_exists`. Если скрипты не прошли проверку (больше 20 файлов, повторяющиеся имена, общий размер больше 10 МБ, файл без содержимого), вернётся 400 с `error_code` `skill_scripts_invalid`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_agent_skill_with_http_info(create_skill, async_req=True)
        >>> result = thread.get()

        :param create_skill: (required)
        :type create_skill: CreateSkill
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
        :rtype: tuple(CreateAgentSkill201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'create_skill'
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
                    " to method create_agent_skill" % _key
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
        if _params['create_skill'] is not None:
            _body_params = _params['create_skill']

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
            '201': "CreateAgentSkill201Response",
            '400': None,
            '401': None,
            '403': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skills', 'POST',
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
    def delete_agent_skill(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> None:  # noqa: E501
        """Удаление навыка  # noqa: E501

        Чтобы удалить навык, отправьте DELETE-запрос на `/api/v1/cloud-ai/skills/{skill_id}`.  Навык отключается от всех агентов, история версий и скрипты удаляются. Срабатывания навыка под старыми ответами агентов сохраняются.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_agent_skill(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
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
            raise ValueError("Error! Please call the delete_agent_skill_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.delete_agent_skill_with_http_info(skill_id, **kwargs)  # noqa: E501

    @validate_arguments
    def delete_agent_skill_with_http_info(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> ApiResponse:  # noqa: E501
        """Удаление навыка  # noqa: E501

        Чтобы удалить навык, отправьте DELETE-запрос на `/api/v1/cloud-ai/skills/{skill_id}`.  Навык отключается от всех агентов, история версий и скрипты удаляются. Срабатывания навыка под старыми ответами агентов сохраняются.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_agent_skill_with_http_info(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
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
            'skill_id'
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
                    " to method delete_agent_skill" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']


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
            '/api/v1/cloud-ai/skills/{skill_id}', 'DELETE',
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
    def disconnect_agent_skill_from_agent(self, agent_id : Annotated[Any, Field(..., description="ID агента")], skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> None:  # noqa: E501
        """Отключение навыка от агента  # noqa: E501

        Чтобы полностью отключить навык от агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}`.  Закреплённая версия при этом не сохраняется. Чтобы выключить навык на время, используйте PUT-запрос с `is_enabled: false`. Если навык не подключён к агенту, вернётся 404 с `error_code` `agent_skill_link_not_found`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.disconnect_agent_skill_from_agent(agent_id, skill_id, async_req=True)
        >>> result = thread.get()

        :param agent_id: ID агента (required)
        :type agent_id: object
        :param skill_id: ID навыка (required)
        :type skill_id: object
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
            raise ValueError("Error! Please call the disconnect_agent_skill_from_agent_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.disconnect_agent_skill_from_agent_with_http_info(agent_id, skill_id, **kwargs)  # noqa: E501

    @validate_arguments
    def disconnect_agent_skill_from_agent_with_http_info(self, agent_id : Annotated[Any, Field(..., description="ID агента")], skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> ApiResponse:  # noqa: E501
        """Отключение навыка от агента  # noqa: E501

        Чтобы полностью отключить навык от агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}`.  Закреплённая версия при этом не сохраняется. Чтобы выключить навык на время, используйте PUT-запрос с `is_enabled: false`. Если навык не подключён к агенту, вернётся 404 с `error_code` `agent_skill_link_not_found`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.disconnect_agent_skill_from_agent_with_http_info(agent_id, skill_id, async_req=True)
        >>> result = thread.get()

        :param agent_id: ID агента (required)
        :type agent_id: object
        :param skill_id: ID навыка (required)
        :type skill_id: object
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
            'agent_id',
            'skill_id'
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
                    " to method disconnect_agent_skill_from_agent" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['agent_id']:
            _path_params['agent_id'] = _params['agent_id']

        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']


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
            '/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}', 'DELETE',
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
    def duplicate_agent_skill(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> CreateAgentSkill201Response:  # noqa: E501
        """Копирование навыка  # noqa: E501

        Чтобы создать копию навыка, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/duplicate`.  Копия получает свободное название вида «Название (копия)» или «Название (копия 2)», текст и скрипты текущей версии оригинала и собственную историю с версии 1. К агентам копия не подключается. Копия навыка из каталога становится обычным навыком аккаунта.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.duplicate_agent_skill(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAgentSkill201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the duplicate_agent_skill_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.duplicate_agent_skill_with_http_info(skill_id, **kwargs)  # noqa: E501

    @validate_arguments
    def duplicate_agent_skill_with_http_info(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> ApiResponse:  # noqa: E501
        """Копирование навыка  # noqa: E501

        Чтобы создать копию навыка, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/duplicate`.  Копия получает свободное название вида «Название (копия)» или «Название (копия 2)», текст и скрипты текущей версии оригинала и собственную историю с версии 1. К агентам копия не подключается. Копия навыка из каталога становится обычным навыком аккаунта.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.duplicate_agent_skill_with_http_info(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
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
        :rtype: tuple(CreateAgentSkill201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'skill_id'
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
                    " to method duplicate_agent_skill" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']


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
            '201': "CreateAgentSkill201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skills/{skill_id}/duplicate', 'POST',
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
    def get_agent_skill(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> GetAgentSkill200Response:  # noqa: E501
        """Получение навыка  # noqa: E501

        Чтобы получить карточку навыка, отправьте GET-запрос на `/api/v1/cloud-ai/skills/{skill_id}`.  В карточке есть скрипты текущей версии (без содержимого), счётчик версий и агенты, к которым подключён навык.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skill(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAgentSkill200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_agent_skill_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_agent_skill_with_http_info(skill_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_agent_skill_with_http_info(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение навыка  # noqa: E501

        Чтобы получить карточку навыка, отправьте GET-запрос на `/api/v1/cloud-ai/skills/{skill_id}`.  В карточке есть скрипты текущей версии (без содержимого), счётчик версий и агенты, к которым подключён навык.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skill_with_http_info(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
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
        :rtype: tuple(GetAgentSkill200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'skill_id'
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
                    " to method get_agent_skill" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']


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
            '200': "GetAgentSkill200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skills/{skill_id}', 'GET',
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
    def get_agent_skill_catalog(self, **kwargs) -> GetAgentSkillCatalog200Response:  # noqa: E501
        """Получение каталога навыков  # noqa: E501

        Чтобы получить каталог готовых навыков Timeweb Cloud, отправьте GET-запрос на `/api/v1/cloud-ai/skill-catalog`.  Навыки приходят в порядке показа, сгруппированные по `category`. Инструкция возвращается полностью, чтобы её можно было прочитать до установки. Для установленных навыков заполнены `is_installed`, `installed_skill_id`, `is_modified` и `has_catalog_update`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skill_catalog(async_req=True)
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
        :rtype: GetAgentSkillCatalog200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_agent_skill_catalog_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_agent_skill_catalog_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_agent_skill_catalog_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение каталога навыков  # noqa: E501

        Чтобы получить каталог готовых навыков Timeweb Cloud, отправьте GET-запрос на `/api/v1/cloud-ai/skill-catalog`.  Навыки приходят в порядке показа, сгруппированные по `category`. Инструкция возвращается полностью, чтобы её можно было прочитать до установки. Для установленных навыков заполнены `is_installed`, `installed_skill_id`, `is_modified` и `has_catalog_update`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skill_catalog_with_http_info(async_req=True)
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
        :rtype: tuple(GetAgentSkillCatalog200Response, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_agent_skill_catalog" % _key
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
            '200': "GetAgentSkillCatalog200Response",
            '400': None,
            '401': None,
            '403': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skill-catalog', 'GET',
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
    def get_agent_skill_library(self, search : Annotated[Optional[Any], Field(description="Поиск по названию навыка и по тексту инструкции")] = None, **kwargs) -> GetAgentSkillLibrary200Response:  # noqa: E501
        """Получение списка навыков  # noqa: E501

        Чтобы получить навыки аккаунта, отправьте GET-запрос на `/api/v1/cloud-ai/skills`.  Сначала идут недавно изменённые. Параметр `search` ищет по названию и по тексту инструкции.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skill_library(search, async_req=True)
        >>> result = thread.get()

        :param search: Поиск по названию навыка и по тексту инструкции
        :type search: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAgentSkillLibrary200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_agent_skill_library_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_agent_skill_library_with_http_info(search, **kwargs)  # noqa: E501

    @validate_arguments
    def get_agent_skill_library_with_http_info(self, search : Annotated[Optional[Any], Field(description="Поиск по названию навыка и по тексту инструкции")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Получение списка навыков  # noqa: E501

        Чтобы получить навыки аккаунта, отправьте GET-запрос на `/api/v1/cloud-ai/skills`.  Сначала идут недавно изменённые. Параметр `search` ищет по названию и по тексту инструкции.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skill_library_with_http_info(search, async_req=True)
        >>> result = thread.get()

        :param search: Поиск по названию навыка и по тексту инструкции
        :type search: object
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
        :rtype: tuple(GetAgentSkillLibrary200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'search'
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
                    " to method get_agent_skill_library" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))

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
            '200': "GetAgentSkillLibrary200Response",
            '400': None,
            '401': None,
            '403': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skills', 'GET',
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
    def get_agent_skill_version(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], version : Annotated[Any, Field(..., description="Номер версии навыка")], **kwargs) -> GetAgentSkillVersion200Response:  # noqa: E501
        """Получение версии навыка  # noqa: E501

        Чтобы получить текст конкретной версии навыка, отправьте GET-запрос на `/api/v1/cloud-ai/skills/{skill_id}/versions/{version}`.  Номер версии сработавшего навыка есть в срабатываниях под ответами агента.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skill_version(skill_id, version, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param version: Номер версии навыка (required)
        :type version: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAgentSkillVersion200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_agent_skill_version_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_agent_skill_version_with_http_info(skill_id, version, **kwargs)  # noqa: E501

    @validate_arguments
    def get_agent_skill_version_with_http_info(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], version : Annotated[Any, Field(..., description="Номер версии навыка")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение версии навыка  # noqa: E501

        Чтобы получить текст конкретной версии навыка, отправьте GET-запрос на `/api/v1/cloud-ai/skills/{skill_id}/versions/{version}`.  Номер версии сработавшего навыка есть в срабатываниях под ответами агента.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skill_version_with_http_info(skill_id, version, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param version: Номер версии навыка (required)
        :type version: object
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
        :rtype: tuple(GetAgentSkillVersion200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'skill_id',
            'version'
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
                    " to method get_agent_skill_version" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']

        if _params['version']:
            _path_params['version'] = _params['version']


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
            '200': "GetAgentSkillVersion200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skills/{skill_id}/versions/{version}', 'GET',
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
    def get_agent_skill_versions(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> GetAgentSkillVersions200Response:  # noqa: E501
        """Получение истории версий навыка  # noqa: E501

        Чтобы получить историю версий навыка, отправьте GET-запрос на `/api/v1/cloud-ai/skills/{skill_id}/versions`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skill_versions(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAgentSkillVersions200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_agent_skill_versions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_agent_skill_versions_with_http_info(skill_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_agent_skill_versions_with_http_info(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение истории версий навыка  # noqa: E501

        Чтобы получить историю версий навыка, отправьте GET-запрос на `/api/v1/cloud-ai/skills/{skill_id}/versions`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skill_versions_with_http_info(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
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
        :rtype: tuple(GetAgentSkillVersions200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'skill_id'
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
                    " to method get_agent_skill_versions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']


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
            '200': "GetAgentSkillVersions200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skills/{skill_id}/versions', 'GET',
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
    def get_agent_skills_for_agent(self, agent_id : Annotated[Any, Field(..., description="ID агента")], **kwargs) -> GetAgentSkillsForAgent200Response:  # noqa: E501
        """Получение навыков агента  # noqa: E501

        Чтобы получить навыки агента, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills`.  В ответе все навыки аккаунта: неподключённые приходят с `is_connected: false`. `has_newer_version: true` означает, что агент закреплён на устаревшей версии.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skills_for_agent(agent_id, async_req=True)
        >>> result = thread.get()

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
        :rtype: GetAgentSkillsForAgent200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_agent_skills_for_agent_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_agent_skills_for_agent_with_http_info(agent_id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_agent_skills_for_agent_with_http_info(self, agent_id : Annotated[Any, Field(..., description="ID агента")], **kwargs) -> ApiResponse:  # noqa: E501
        """Получение навыков агента  # noqa: E501

        Чтобы получить навыки агента, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills`.  В ответе все навыки аккаунта: неподключённые приходят с `is_connected: false`. `has_newer_version: true` означает, что агент закреплён на устаревшей версии.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_agent_skills_for_agent_with_http_info(agent_id, async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(GetAgentSkillsForAgent200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method get_agent_skills_for_agent" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
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
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "GetAgentSkillsForAgent200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/agents/{agent_id}/skills', 'GET',
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
    def install_agent_skill_from_catalog(self, catalog_item_id : Annotated[Any, Field(..., description="ID навыка в каталоге")], **kwargs) -> InstallAgentSkillFromCatalog200Response:  # noqa: E501
        """Установка навыка из каталога  # noqa: E501

        Чтобы установить навык из каталога в библиотеку аккаунта, отправьте POST-запрос на `/api/v1/cloud-ai/skill-catalog/{catalog_item_id}/install`.  Повторная установка не создаёт копию, а возвращает уже установленный навык с `meta.already_installed: true`. Если название занято вашим навыком, к нему добавляется «(копия)». Чтобы сразу включить навык у агента, используйте `POST /api/v1/cloud-ai/agents/{agent_id}/skills/install-and-connect`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.install_agent_skill_from_catalog(catalog_item_id, async_req=True)
        >>> result = thread.get()

        :param catalog_item_id: ID навыка в каталоге (required)
        :type catalog_item_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InstallAgentSkillFromCatalog200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the install_agent_skill_from_catalog_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.install_agent_skill_from_catalog_with_http_info(catalog_item_id, **kwargs)  # noqa: E501

    @validate_arguments
    def install_agent_skill_from_catalog_with_http_info(self, catalog_item_id : Annotated[Any, Field(..., description="ID навыка в каталоге")], **kwargs) -> ApiResponse:  # noqa: E501
        """Установка навыка из каталога  # noqa: E501

        Чтобы установить навык из каталога в библиотеку аккаунта, отправьте POST-запрос на `/api/v1/cloud-ai/skill-catalog/{catalog_item_id}/install`.  Повторная установка не создаёт копию, а возвращает уже установленный навык с `meta.already_installed: true`. Если название занято вашим навыком, к нему добавляется «(копия)». Чтобы сразу включить навык у агента, используйте `POST /api/v1/cloud-ai/agents/{agent_id}/skills/install-and-connect`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.install_agent_skill_from_catalog_with_http_info(catalog_item_id, async_req=True)
        >>> result = thread.get()

        :param catalog_item_id: ID навыка в каталоге (required)
        :type catalog_item_id: object
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
        :rtype: tuple(InstallAgentSkillFromCatalog200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'catalog_item_id'
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
                    " to method install_agent_skill_from_catalog" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['catalog_item_id']:
            _path_params['catalog_item_id'] = _params['catalog_item_id']


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
            '200': "InstallAgentSkillFromCatalog200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skill-catalog/{catalog_item_id}/install', 'POST',
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
    def install_and_connect_agent_skill(self, agent_id : Annotated[Any, Field(..., description="ID агента")], install_and_connect_skill : InstallAndConnectSkill, **kwargs) -> InstallAndConnectAgentSkill200Response:  # noqa: E501
        """Установка навыка из каталога и включение у агента  # noqa: E501

        Чтобы установить навык из каталога и сразу включить его у агента, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/install-and-connect`.  Если навык уже установлен, копия не создаётся (`meta.already_installed: true`), навык просто включается у агента.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.install_and_connect_agent_skill(agent_id, install_and_connect_skill, async_req=True)
        >>> result = thread.get()

        :param agent_id: ID агента (required)
        :type agent_id: object
        :param install_and_connect_skill: (required)
        :type install_and_connect_skill: InstallAndConnectSkill
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: InstallAndConnectAgentSkill200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the install_and_connect_agent_skill_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.install_and_connect_agent_skill_with_http_info(agent_id, install_and_connect_skill, **kwargs)  # noqa: E501

    @validate_arguments
    def install_and_connect_agent_skill_with_http_info(self, agent_id : Annotated[Any, Field(..., description="ID агента")], install_and_connect_skill : InstallAndConnectSkill, **kwargs) -> ApiResponse:  # noqa: E501
        """Установка навыка из каталога и включение у агента  # noqa: E501

        Чтобы установить навык из каталога и сразу включить его у агента, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/install-and-connect`.  Если навык уже установлен, копия не создаётся (`meta.already_installed: true`), навык просто включается у агента.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.install_and_connect_agent_skill_with_http_info(agent_id, install_and_connect_skill, async_req=True)
        >>> result = thread.get()

        :param agent_id: ID агента (required)
        :type agent_id: object
        :param install_and_connect_skill: (required)
        :type install_and_connect_skill: InstallAndConnectSkill
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
        :rtype: tuple(InstallAndConnectAgentSkill200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'agent_id',
            'install_and_connect_skill'
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
                    " to method install_and_connect_agent_skill" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
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
        if _params['install_and_connect_skill'] is not None:
            _body_params = _params['install_and_connect_skill']

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
            '200': "InstallAndConnectAgentSkill200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/agents/{agent_id}/skills/install-and-connect', 'POST',
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
    def rollback_agent_skill_version(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], version : Annotated[Any, Field(..., description="Номер версии навыка")], **kwargs) -> CreateAgentSkill201Response:  # noqa: E501
        """Переключение навыка на версию из истории  # noqa: E501

        Чтобы сделать версию из истории текущей, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/versions/{version}/rollback`.  Новая версия не создаётся (`meta.version_created` — `false`), название навыка не меняется. Агенты остаются на своих закреплённых версиях. Если выбранная версия уже текущая, ничего не меняется.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.rollback_agent_skill_version(skill_id, version, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param version: Номер версии навыка (required)
        :type version: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAgentSkill201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the rollback_agent_skill_version_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.rollback_agent_skill_version_with_http_info(skill_id, version, **kwargs)  # noqa: E501

    @validate_arguments
    def rollback_agent_skill_version_with_http_info(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], version : Annotated[Any, Field(..., description="Номер версии навыка")], **kwargs) -> ApiResponse:  # noqa: E501
        """Переключение навыка на версию из истории  # noqa: E501

        Чтобы сделать версию из истории текущей, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/versions/{version}/rollback`.  Новая версия не создаётся (`meta.version_created` — `false`), название навыка не меняется. Агенты остаются на своих закреплённых версиях. Если выбранная версия уже текущая, ничего не меняется.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.rollback_agent_skill_version_with_http_info(skill_id, version, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param version: Номер версии навыка (required)
        :type version: object
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
        :rtype: tuple(CreateAgentSkill201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'skill_id',
            'version'
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
                    " to method rollback_agent_skill_version" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']

        if _params['version']:
            _path_params['version'] = _params['version']


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
            '200': "CreateAgentSkill201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skills/{skill_id}/versions/{version}/rollback', 'POST',
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
    def set_agent_skill_for_agent(self, agent_id : Annotated[Any, Field(..., description="ID агента")], skill_id : Annotated[Any, Field(..., description="ID навыка")], set_agent_skill : SetAgentSkill, **kwargs) -> SetAgentSkillForAgent200Response:  # noqa: E501
        """Включение и выключение навыка у агента  # noqa: E501

        Чтобы включить или выключить навык у агента, отправьте PUT-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}`.  Первое включение подключает навык и закрепляет агента на текущей версии навыка или на версии из `version`. Выключение сохраняет закреплённую версию, поэтому повторное включение вернёт то же поведение. Изменения действуют сразу. Выключение неподключённого навыка ничего не меняет.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_agent_skill_for_agent(agent_id, skill_id, set_agent_skill, async_req=True)
        >>> result = thread.get()

        :param agent_id: ID агента (required)
        :type agent_id: object
        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param set_agent_skill: (required)
        :type set_agent_skill: SetAgentSkill
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SetAgentSkillForAgent200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the set_agent_skill_for_agent_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.set_agent_skill_for_agent_with_http_info(agent_id, skill_id, set_agent_skill, **kwargs)  # noqa: E501

    @validate_arguments
    def set_agent_skill_for_agent_with_http_info(self, agent_id : Annotated[Any, Field(..., description="ID агента")], skill_id : Annotated[Any, Field(..., description="ID навыка")], set_agent_skill : SetAgentSkill, **kwargs) -> ApiResponse:  # noqa: E501
        """Включение и выключение навыка у агента  # noqa: E501

        Чтобы включить или выключить навык у агента, отправьте PUT-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}`.  Первое включение подключает навык и закрепляет агента на текущей версии навыка или на версии из `version`. Выключение сохраняет закреплённую версию, поэтому повторное включение вернёт то же поведение. Изменения действуют сразу. Выключение неподключённого навыка ничего не меняет.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_agent_skill_for_agent_with_http_info(agent_id, skill_id, set_agent_skill, async_req=True)
        >>> result = thread.get()

        :param agent_id: ID агента (required)
        :type agent_id: object
        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param set_agent_skill: (required)
        :type set_agent_skill: SetAgentSkill
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
        :rtype: tuple(SetAgentSkillForAgent200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'agent_id',
            'skill_id',
            'set_agent_skill'
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
                    " to method set_agent_skill_for_agent" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['agent_id']:
            _path_params['agent_id'] = _params['agent_id']

        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['set_agent_skill'] is not None:
            _body_params = _params['set_agent_skill']

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
            '200': "SetAgentSkillForAgent200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}', 'PUT',
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
    def sync_agent_skill_agents_versions(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> SyncAgentSkillAgentsVersions200Response:  # noqa: E501
        """Перевод всех агентов навыка на текущую версию  # noqa: E501

        Чтобы перевести всех агентов, у которых включён навык, на его текущую версию, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/agents/sync-versions`.  Агенты, у которых навык выключен, остаются на своих версиях. Сколько агентов переведено, видно в `meta.updated_count`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sync_agent_skill_agents_versions(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SyncAgentSkillAgentsVersions200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the sync_agent_skill_agents_versions_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.sync_agent_skill_agents_versions_with_http_info(skill_id, **kwargs)  # noqa: E501

    @validate_arguments
    def sync_agent_skill_agents_versions_with_http_info(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> ApiResponse:  # noqa: E501
        """Перевод всех агентов навыка на текущую версию  # noqa: E501

        Чтобы перевести всех агентов, у которых включён навык, на его текущую версию, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/agents/sync-versions`.  Агенты, у которых навык выключен, остаются на своих версиях. Сколько агентов переведено, видно в `meta.updated_count`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sync_agent_skill_agents_versions_with_http_info(skill_id, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
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
        :rtype: tuple(SyncAgentSkillAgentsVersions200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'skill_id'
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
                    " to method sync_agent_skill_agents_versions" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']


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
            '200': "SyncAgentSkillAgentsVersions200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skills/{skill_id}/agents/sync-versions', 'POST',
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
    def sync_agent_skill_versions_for_agent(self, agent_id : Annotated[Any, Field(..., description="ID агента")], **kwargs) -> SyncAgentSkillVersionsForAgent200Response:  # noqa: E501
        """Перевод всех навыков агента на текущие версии  # noqa: E501

        Чтобы перевести все включённые у агента навыки на их текущие версии, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/sync-versions`.  В ответе все навыки аккаунта с состоянием у агента, как в списке навыков агента. Сколько навыков переведено, видно в `updated_count` в корне ответа.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sync_agent_skill_versions_for_agent(agent_id, async_req=True)
        >>> result = thread.get()

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
        :rtype: SyncAgentSkillVersionsForAgent200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the sync_agent_skill_versions_for_agent_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.sync_agent_skill_versions_for_agent_with_http_info(agent_id, **kwargs)  # noqa: E501

    @validate_arguments
    def sync_agent_skill_versions_for_agent_with_http_info(self, agent_id : Annotated[Any, Field(..., description="ID агента")], **kwargs) -> ApiResponse:  # noqa: E501
        """Перевод всех навыков агента на текущие версии  # noqa: E501

        Чтобы перевести все включённые у агента навыки на их текущие версии, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/sync-versions`.  В ответе все навыки аккаунта с состоянием у агента, как в списке навыков агента. Сколько навыков переведено, видно в `updated_count` в корне ответа.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.sync_agent_skill_versions_for_agent_with_http_info(agent_id, async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(SyncAgentSkillVersionsForAgent200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method sync_agent_skill_versions_for_agent" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
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
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['Bearer']  # noqa: E501

        _response_types_map = {
            '200': "SyncAgentSkillVersionsForAgent200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/agents/{agent_id}/skills/sync-versions', 'POST',
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
    def update_agent_skill(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], update_skill : UpdateSkill, **kwargs) -> CreateAgentSkill201Response:  # noqa: E501
        """Изменение навыка  # noqa: E501

        Чтобы изменить навык, отправьте PATCH-запрос на `/api/v1/cloud-ai/skills/{skill_id}`, передав только изменяемые поля.  Изменение «когда применять», инструкции или скриптов создаёт новую версию. Переименование и сохранение без изменений версию не создают (`meta.version_created`). Подключённые агенты остаются на своих версиях. Сколько агентов затронуто, видно в `meta.affected_agents_count`. Если в истории уже 50 версий, самая старая свободная версия удаляется (`meta.pruned_versions`). Скрипты передаются в теле запроса. Их общий размер — до 10 МБ, а всё тело запроса — до 16 МБ; запрос с телом больше отклоняется до проверки.  Возможные ошибки 409: `skill_name_already_exists` — название занято; `skill_versions_limit_exceeded` — все 50 версий заняты текущей и закреплёнными за агентами; `skill_was_modified_concurrently` — навык одновременно изменён другим запросом, повторите сохранение.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_agent_skill(skill_id, update_skill, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param update_skill: (required)
        :type update_skill: UpdateSkill
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: CreateAgentSkill201Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_agent_skill_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_agent_skill_with_http_info(skill_id, update_skill, **kwargs)  # noqa: E501

    @validate_arguments
    def update_agent_skill_with_http_info(self, skill_id : Annotated[Any, Field(..., description="ID навыка")], update_skill : UpdateSkill, **kwargs) -> ApiResponse:  # noqa: E501
        """Изменение навыка  # noqa: E501

        Чтобы изменить навык, отправьте PATCH-запрос на `/api/v1/cloud-ai/skills/{skill_id}`, передав только изменяемые поля.  Изменение «когда применять», инструкции или скриптов создаёт новую версию. Переименование и сохранение без изменений версию не создают (`meta.version_created`). Подключённые агенты остаются на своих версиях. Сколько агентов затронуто, видно в `meta.affected_agents_count`. Если в истории уже 50 версий, самая старая свободная версия удаляется (`meta.pruned_versions`). Скрипты передаются в теле запроса. Их общий размер — до 10 МБ, а всё тело запроса — до 16 МБ; запрос с телом больше отклоняется до проверки.  Возможные ошибки 409: `skill_name_already_exists` — название занято; `skill_versions_limit_exceeded` — все 50 версий заняты текущей и закреплёнными за агентами; `skill_was_modified_concurrently` — навык одновременно изменён другим запросом, повторите сохранение.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_agent_skill_with_http_info(skill_id, update_skill, async_req=True)
        >>> result = thread.get()

        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param update_skill: (required)
        :type update_skill: UpdateSkill
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
        :rtype: tuple(CreateAgentSkill201Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'skill_id',
            'update_skill'
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
                    " to method update_agent_skill" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['update_skill'] is not None:
            _body_params = _params['update_skill']

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
            '200': "CreateAgentSkill201Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '409': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/skills/{skill_id}', 'PATCH',
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
    def update_agent_skill_version_for_agent(self, agent_id : Annotated[Any, Field(..., description="ID агента")], skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> SetAgentSkillForAgent200Response:  # noqa: E501
        """Перевод агента на текущую версию навыка  # noqa: E501

        Чтобы перевести агента на текущую версию навыка, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}/update-version`.  Если навык не подключён к агенту, вернётся 404 с `error_code` `agent_skill_link_not_found`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_agent_skill_version_for_agent(agent_id, skill_id, async_req=True)
        >>> result = thread.get()

        :param agent_id: ID агента (required)
        :type agent_id: object
        :param skill_id: ID навыка (required)
        :type skill_id: object
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: SetAgentSkillForAgent200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the update_agent_skill_version_for_agent_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_agent_skill_version_for_agent_with_http_info(agent_id, skill_id, **kwargs)  # noqa: E501

    @validate_arguments
    def update_agent_skill_version_for_agent_with_http_info(self, agent_id : Annotated[Any, Field(..., description="ID агента")], skill_id : Annotated[Any, Field(..., description="ID навыка")], **kwargs) -> ApiResponse:  # noqa: E501
        """Перевод агента на текущую версию навыка  # noqa: E501

        Чтобы перевести агента на текущую версию навыка, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}/update-version`.  Если навык не подключён к агенту, вернётся 404 с `error_code` `agent_skill_link_not_found`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_agent_skill_version_for_agent_with_http_info(agent_id, skill_id, async_req=True)
        >>> result = thread.get()

        :param agent_id: ID агента (required)
        :type agent_id: object
        :param skill_id: ID навыка (required)
        :type skill_id: object
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
        :rtype: tuple(SetAgentSkillForAgent200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'agent_id',
            'skill_id'
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
                    " to method update_agent_skill_version_for_agent" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['agent_id']:
            _path_params['agent_id'] = _params['agent_id']

        if _params['skill_id']:
            _path_params['skill_id'] = _params['skill_id']


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
            '200': "SetAgentSkillForAgent200Response",
            '400': None,
            '401': None,
            '403': None,
            '404': None,
            '429': None,
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}/update-version', 'POST',
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
