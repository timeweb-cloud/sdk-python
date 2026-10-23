# timeweb-cloud-api
# Введение
API Timeweb Cloud позволяет вам управлять ресурсами в облаке программным способом с использованием обычных HTTP-запросов.

Множество функций, которые доступны в панели управления Timeweb Cloud, также доступны через API, что позволяет вам автоматизировать ваши собственные сценарии.

В этой документации сперва будет описан общий дизайн и принципы работы API, а после этого конкретные конечные точки. Также будут приведены примеры запросов к ним.


## Запросы
Запросы должны выполняться по протоколу `HTTPS`, чтобы гарантировать шифрование транзакций. Поддерживаются следующие методы запроса:
|Метод|Применение|
|--- |--- |
|GET|Извлекает данные о коллекциях и отдельных ресурсах.|
|POST|Для коллекций создает новый ресурс этого типа. Также используется для выполнения действий с конкретным ресурсом.|
|PUT|Обновляет существующий ресурс.|
|PATCH|Некоторые ресурсы поддерживают частичное обновление, то есть обновление только части атрибутов ресурса, в этом случае вместо метода PUT будет использован PATCH.|
|DELETE|Удаляет ресурс.|

Методы `POST`, `PUT` и `PATCH` могут включать объект в тело запроса с типом содержимого `application/json`.

### Параметры в запросах
Некоторые коллекции поддерживают пагинацию, поиск или сортировку в запросах. В параметрах запроса требуется передать:
- `limit` — обозначает количество записей, которое необходимо вернуть
 - `offset` — указывает на смещение, относительно начала списка
 - `search` — позволяет указать набор символов для поиска
 - `sort` — можно задать правило сортировки коллекции

## Ответы
Запросы вернут один из следующих кодов состояния ответа HTTP:

|Статус|Описание|
|--- |--- |
|200 OK|Действие с ресурсом было выполнено успешно.|
|201 Created|Ресурс был успешно создан. При этом ресурс может быть как уже готовым к использованию, так и находиться в процессе запуска.|
|204 No Content|Действие с ресурсом было выполнено успешно, и ответ не содержит дополнительной информации в теле.|
|400 Bad Request|Был отправлен неверный запрос, например, в нем отсутствуют обязательные параметры и т. д. Тело ответа будет содержать дополнительную информацию об ошибке.|
|401 Unauthorized|Ошибка аутентификации.|
|403 Forbidden|Аутентификация прошла успешно, но недостаточно прав для выполнения действия.|
|404 Not Found|Запрашиваемый ресурс не найден.|
|409 Conflict|Запрос конфликтует с текущим состоянием.|
|423 Locked|Ресурс из запроса заблокирован от применения к нему указанного метода.|
|429 Too Many Requests|Был достигнут лимит по количеству запросов в единицу времени.|
|500 Internal Server Error|При выполнении запроса произошла какая-то внутренняя ошибка. Чтобы решить эту проблему, лучше всего создать тикет в панели управления.|

### Структура успешного ответа
Все конечные точки будут возвращать данные в формате `JSON`. Ответы на `GET`-запросы будут иметь на верхнем уровне следующую структуру атрибутов: 
|Название поля|Тип|Описание|
|--- |--- |--- |
|[entity_name]|object, object[], string[], number[], boolean|Динамическое поле, которое будет меняться в зависимости от запрашиваемого ресурса и будет содержать все атрибуты, необходимые для описания этого ресурса. Например, при запросе списка баз данных будет возвращаться поле `dbs`, а при запросе конкретного облачного сервера `server`. Для некоторых конечных точек в ответе может возвращаться сразу несколько ресурсов.|
|meta|object|Опционально. Объект, который содержит вспомогательную информацию о ресурсе. Чаще всего будет встречаться при запросе коллекций и содержать поле `total`, которое будет указывать на количество элементов в коллекции.|
|response_id|string|Опционально. В большинстве случаев в ответе будет содержаться ID ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот ID— так мы сможем найти ответ на него намного быстрее. Также вы можете использовать этот ID, чтобы убедиться, что это новый ответ на запрос и результат не был получен из кэша.|

Пример запроса на получение списка SSH-ключей:
```
    HTTP/2.0 200 OK
    {
      \"ssh_keys\":[
          {
            \"body\":\"ssh-rsa AAAAB3NzaC1sdfghjkOAsBwWhs= example@device.local\",
            \"created_at\":\"2021-09-15T19:52:27Z\",
            \"expired_at\":null,
            \"id\":5297,
            \"is_default\":false,
            \"name\":\"example@device.local\",
            \"used_at\":null,
            \"used_by\":[]
          }
      ],
      \"meta\":{
          \"total\":1
      },
      \"response_id\":\"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"
    }
```

### Структура ответа с ошибкой
|Название поля|Тип|Описание|
|--- |--- |--- |
|status_code|number|Короткий числовой идентификатор ошибки.|
|error_code|string|Короткий текстовый идентификатор ошибки, который уточняет числовой идентификатор и удобен для программной обработки. Самый простой пример — это код `not_found` для ошибки 404.|
|message|string, string[]|Опционально. В большинстве случаев в ответе будет содержаться человекочитаемое подробное описание ошибки или ошибок, которые помогут понять, что нужно исправить.|
|response_id|string|Опционально. В большинстве случае в ответе будет содержаться ID ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот ID — так мы сможем найти ответ на него намного быстрее.|

Пример:
```
    HTTP/2.0 403 Forbidden
    {
      \"status_code\": 403,
      \"error_code\":  \"forbidden\",
      \"message\":     \"You do not have access for the attempted action\",
      \"response_id\": \"94608d15-8672-4eed-8ab6-28bd6fa3cdf7\"
    }
```

## Статусы ресурсов
Важно учесть, что при создании большинства ресурсов внутри платформы вам будет сразу возвращен ответ от сервера со статусом `200 OK` или `201 Created` и ID созданного ресурса в теле ответа, но при этом этот ресурс может быть ещё в *состоянии запуска*.

Для того чтобы понять, в каком состоянии сейчас находится ваш ресурс, мы добавили поле `status` в ответ на получение информации о ресурсе.

Список статусов будет отличаться в зависимости от типа ресурса. Увидеть поддерживаемый список статусов вы сможете в описании каждого конкретного ресурса.

 

## Ограничение скорости запросов (Rate Limiting)
Чтобы обеспечить стабильность для всех пользователей, Timeweb Cloud защищает API от всплесков входящего трафика, анализируя количество запросов c каждого аккаунта к каждой конечной точке.

Если ваше приложение отправляет более 20 запросов в секунду на одну конечную точку, то для этого запроса API может вернуть код состояния HTTP `429 Too Many Requests`.


## Аутентификация
Доступ к API осуществляется с помощью JWT-токена. Токенами можно управлять внутри панели управления Timeweb Cloud в разделе *API и Terraform*.

Токен необходимо передавать в заголовке каждого запроса в формате:
```
  Authorization: Bearer $TIMEWEB_CLOUD_TOKEN
```

## Формат примеров API
Примеры в этой документации описаны с помощью `curl`, HTTP-клиента командной строки. На компьютерах `Linux` и `macOS` обычно по умолчанию установлен `curl`, и он доступен для загрузки на всех популярных платформах, включая `Windows`.

Каждый пример разделен на несколько строк символом `\\`, который совместим с `bash`. Типичный пример выглядит так:
```
  curl -X PATCH 
    -H \"Content-Type: application/json\" 
    -H \"Authorization: Bearer $TIMEWEB_CLOUD_TOKEN\" 
    -d '{\"name\":\"Cute Corvus\",\"comment\":\"Development Server\"}' 
    \"https://api.timeweb.cloud/api/v1/dedicated/1051\"
```
- Параметр `-X` задает метод запроса. Для согласованности метод будет указан во всех примерах, даже если он явно не требуется для методов `GET`.
- Строки `-H` задают требуемые HTTP-заголовки.
- Примеры, для которых требуется объект JSON в теле запроса, передают требуемые данные через параметр `-d`.

Чтобы использовать приведенные примеры, не подставляя каждый раз в них свой токен, вы можете добавить токен один раз в переменные окружения в вашей консоли. Например, на `Linux` это можно сделать с помощью команды:

```
TIMEWEB_CLOUD_TOKEN=\"token\"
```

После этого токен будет автоматически подставляться в ваши запросы.

Обратите внимание, что все значения в этой документации являются примерами. Не полагайтесь на IDы операционных систем, тарифов и т.д., используемые в примерах. Используйте соответствующую конечную точку для получения значений перед созданием ресурсов.


## Версионирование
API построено согласно принципам [семантического версионирования](https://semver.org/lang/ru). Это значит, что мы гарантируем обратную совместимость всех изменений в пределах одной мажорной версии.

Мажорная версия каждой конечной точки обозначается в пути запроса, например, запрос `/api/v1/servers` указывает, что этот метод имеет версию 1.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import timeweb_cloud_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import timeweb_cloud_api
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import timeweb_cloud_api
from timeweb_cloud_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = timeweb_cloud_api.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)


# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    create_max_bot = timeweb_cloud_api.CreateMaxBot() # CreateMaxBot | 

    try:
        # Подключение бота MAX к агенту
        api_response = api_instance.create_agent_bot_max_bot(create_max_bot)
        print("The response of AIAgentIntegrationsApi->create_agent_bot_max_bot:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AIAgentIntegrationsApi->create_agent_bot_max_bot: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.timeweb.cloud*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AIAgentIntegrationsApi* | [**create_agent_bot_max_bot**](docs/AIAgentIntegrationsApi.md#create_agent_bot_max_bot) | **POST** /api/v1/cloud-ai/max-bots | Подключение бота MAX к агенту
*AIAgentIntegrationsApi* | [**create_agent_bot_telegram_bot**](docs/AIAgentIntegrationsApi.md#create_agent_bot_telegram_bot) | **POST** /api/v1/cloud-ai/bots | Подключение Telegram-бота к агенту
*AIAgentIntegrationsApi* | [**create_agent_integration_crisp**](docs/AIAgentIntegrationsApi.md#create_agent_integration_crisp) | **POST** /api/v1/cloud-ai/agent/{agent_id}/crisp | Подключение агента к Crisp
*AIAgentIntegrationsApi* | [**create_agent_integration_jivo**](docs/AIAgentIntegrationsApi.md#create_agent_integration_jivo) | **POST** /api/v1/cloud-ai/agent/{agent_id}/jivo | Подключение агента к Jivo
*AIAgentIntegrationsApi* | [**delete_agent_bot_max_bot**](docs/AIAgentIntegrationsApi.md#delete_agent_bot_max_bot) | **DELETE** /api/v1/cloud-ai/max-bots/{bot_id} | Отключение бота MAX
*AIAgentIntegrationsApi* | [**delete_agent_bot_telegram_bot**](docs/AIAgentIntegrationsApi.md#delete_agent_bot_telegram_bot) | **DELETE** /api/v1/cloud-ai/bots/{bot_id} | Отключение Telegram-бота
*AIAgentIntegrationsApi* | [**delete_agent_integration_crisp**](docs/AIAgentIntegrationsApi.md#delete_agent_integration_crisp) | **DELETE** /api/v1/cloud-ai/agent/{agent_id}/crisp | Отключение агента от Crisp
*AIAgentIntegrationsApi* | [**delete_agent_integration_jivo**](docs/AIAgentIntegrationsApi.md#delete_agent_integration_jivo) | **DELETE** /api/v1/cloud-ai/agent/{agent_id}/jivo | Отключение агента от Jivo
*AIAgentIntegrationsApi* | [**get_agent_bot_max_bot**](docs/AIAgentIntegrationsApi.md#get_agent_bot_max_bot) | **GET** /api/v1/cloud-ai/max-bots/{bot_id} | Получение информации о боте MAX
*AIAgentIntegrationsApi* | [**get_agent_bot_max_bots**](docs/AIAgentIntegrationsApi.md#get_agent_bot_max_bots) | **GET** /api/v1/cloud-ai/max-bots | Получение списка ботов MAX
*AIAgentIntegrationsApi* | [**get_agent_bot_max_bots_by_agent**](docs/AIAgentIntegrationsApi.md#get_agent_bot_max_bots_by_agent) | **GET** /api/v1/cloud-ai/agents/{agent_id}/max-bots | Получение списка ботов MAX агента
*AIAgentIntegrationsApi* | [**get_agent_bot_telegram_bot**](docs/AIAgentIntegrationsApi.md#get_agent_bot_telegram_bot) | **GET** /api/v1/cloud-ai/bots/{bot_id} | Получение информации о Telegram-боте
*AIAgentIntegrationsApi* | [**get_agent_bot_telegram_bots**](docs/AIAgentIntegrationsApi.md#get_agent_bot_telegram_bots) | **GET** /api/v1/cloud-ai/bots | Получение списка Telegram-ботов
*AIAgentIntegrationsApi* | [**get_agent_bot_telegram_bots_by_agent**](docs/AIAgentIntegrationsApi.md#get_agent_bot_telegram_bots_by_agent) | **GET** /api/v1/cloud-ai/agents/{agent_id}/bots | Получение списка Telegram-ботов агента
*AIAgentIntegrationsApi* | [**get_agent_integration_crisp**](docs/AIAgentIntegrationsApi.md#get_agent_integration_crisp) | **GET** /api/v1/cloud-ai/agent/{agent_id}/crisp | Получение интеграции агента с Crisp
*AIAgentIntegrationsApi* | [**get_agent_integration_jivo**](docs/AIAgentIntegrationsApi.md#get_agent_integration_jivo) | **GET** /api/v1/cloud-ai/agent/{agent_id}/jivo | Получение интеграции агента с Jivo
*AIAgentIntegrationsApi* | [**update_agent_bot_max_bot**](docs/AIAgentIntegrationsApi.md#update_agent_bot_max_bot) | **PATCH** /api/v1/cloud-ai/max-bots/{bot_id} | Изменение бота MAX
*AIAgentIntegrationsApi* | [**update_agent_bot_telegram_bot**](docs/AIAgentIntegrationsApi.md#update_agent_bot_telegram_bot) | **PATCH** /api/v1/cloud-ai/bots/{bot_id} | Изменение Telegram-бота
*AIAgentSkillsApi* | [**apply_agent_skill_catalog_update**](docs/AIAgentSkillsApi.md#apply_agent_skill_catalog_update) | **POST** /api/v1/cloud-ai/skills/{skill_id}/apply-catalog-update | Применение обновления навыка из каталога
*AIAgentSkillsApi* | [**connect_agent_skills_to_agent**](docs/AIAgentSkillsApi.md#connect_agent_skills_to_agent) | **POST** /api/v1/cloud-ai/agents/{agent_id}/skills/connect | Подключение нескольких навыков к агенту
*AIAgentSkillsApi* | [**create_agent_skill**](docs/AIAgentSkillsApi.md#create_agent_skill) | **POST** /api/v1/cloud-ai/skills | Создание навыка
*AIAgentSkillsApi* | [**delete_agent_skill**](docs/AIAgentSkillsApi.md#delete_agent_skill) | **DELETE** /api/v1/cloud-ai/skills/{skill_id} | Удаление навыка
*AIAgentSkillsApi* | [**disconnect_agent_skill_from_agent**](docs/AIAgentSkillsApi.md#disconnect_agent_skill_from_agent) | **DELETE** /api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id} | Отключение навыка от агента
*AIAgentSkillsApi* | [**duplicate_agent_skill**](docs/AIAgentSkillsApi.md#duplicate_agent_skill) | **POST** /api/v1/cloud-ai/skills/{skill_id}/duplicate | Копирование навыка
*AIAgentSkillsApi* | [**get_agent_skill**](docs/AIAgentSkillsApi.md#get_agent_skill) | **GET** /api/v1/cloud-ai/skills/{skill_id} | Получение навыка
*AIAgentSkillsApi* | [**get_agent_skill_catalog**](docs/AIAgentSkillsApi.md#get_agent_skill_catalog) | **GET** /api/v1/cloud-ai/skill-catalog | Получение каталога навыков
*AIAgentSkillsApi* | [**get_agent_skill_library**](docs/AIAgentSkillsApi.md#get_agent_skill_library) | **GET** /api/v1/cloud-ai/skills | Получение списка навыков
*AIAgentSkillsApi* | [**get_agent_skill_version**](docs/AIAgentSkillsApi.md#get_agent_skill_version) | **GET** /api/v1/cloud-ai/skills/{skill_id}/versions/{version} | Получение версии навыка
*AIAgentSkillsApi* | [**get_agent_skill_versions**](docs/AIAgentSkillsApi.md#get_agent_skill_versions) | **GET** /api/v1/cloud-ai/skills/{skill_id}/versions | Получение истории версий навыка
*AIAgentSkillsApi* | [**get_agent_skills_for_agent**](docs/AIAgentSkillsApi.md#get_agent_skills_for_agent) | **GET** /api/v1/cloud-ai/agents/{agent_id}/skills | Получение навыков агента
*AIAgentSkillsApi* | [**install_agent_skill_from_catalog**](docs/AIAgentSkillsApi.md#install_agent_skill_from_catalog) | **POST** /api/v1/cloud-ai/skill-catalog/{catalog_item_id}/install | Установка навыка из каталога
*AIAgentSkillsApi* | [**install_and_connect_agent_skill**](docs/AIAgentSkillsApi.md#install_and_connect_agent_skill) | **POST** /api/v1/cloud-ai/agents/{agent_id}/skills/install-and-connect | Установка навыка из каталога и включение у агента
*AIAgentSkillsApi* | [**rollback_agent_skill_version**](docs/AIAgentSkillsApi.md#rollback_agent_skill_version) | **POST** /api/v1/cloud-ai/skills/{skill_id}/versions/{version}/rollback | Переключение навыка на версию из истории
*AIAgentSkillsApi* | [**set_agent_skill_for_agent**](docs/AIAgentSkillsApi.md#set_agent_skill_for_agent) | **PUT** /api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id} | Включение и выключение навыка у агента
*AIAgentSkillsApi* | [**sync_agent_skill_agents_versions**](docs/AIAgentSkillsApi.md#sync_agent_skill_agents_versions) | **POST** /api/v1/cloud-ai/skills/{skill_id}/agents/sync-versions | Перевод всех агентов навыка на текущую версию
*AIAgentSkillsApi* | [**sync_agent_skill_versions_for_agent**](docs/AIAgentSkillsApi.md#sync_agent_skill_versions_for_agent) | **POST** /api/v1/cloud-ai/agents/{agent_id}/skills/sync-versions | Перевод всех навыков агента на текущие версии
*AIAgentSkillsApi* | [**update_agent_skill**](docs/AIAgentSkillsApi.md#update_agent_skill) | **PATCH** /api/v1/cloud-ai/skills/{skill_id} | Изменение навыка
*AIAgentSkillsApi* | [**update_agent_skill_version_for_agent**](docs/AIAgentSkillsApi.md#update_agent_skill_version_for_agent) | **POST** /api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}/update-version | Перевод агента на текущую версию навыка
*AIAgentToolsApi* | [**connect_agent_tool_to_agent**](docs/AIAgentToolsApi.md#connect_agent_tool_to_agent) | **POST** /api/v1/cloud-ai/agents/{agent_id}/tools | Подключение MCP-инструмента к агенту
*AIAgentToolsApi* | [**create_agent_tool**](docs/AIAgentToolsApi.md#create_agent_tool) | **POST** /api/v1/cloud-ai/tools | Подключение собственного MCP-сервера
*AIAgentToolsApi* | [**delete_agent_tool**](docs/AIAgentToolsApi.md#delete_agent_tool) | **DELETE** /api/v1/cloud-ai/tools/{id} | Удаление MCP-инструмента
*AIAgentToolsApi* | [**disconnect_agent_tool_from_agent**](docs/AIAgentToolsApi.md#disconnect_agent_tool_from_agent) | **DELETE** /api/v1/cloud-ai/agents/{agent_id}/tools/{tool_id} | Отключение MCP-инструмента от агента
*AIAgentToolsApi* | [**get_agent_tool**](docs/AIAgentToolsApi.md#get_agent_tool) | **GET** /api/v1/cloud-ai/tools/{id} | Получение MCP-инструмента
*AIAgentToolsApi* | [**get_agent_tool_o_auth2_authorize_url**](docs/AIAgentToolsApi.md#get_agent_tool_o_auth2_authorize_url) | **GET** /api/v1/cloud-ai/tools/oauth2/authorize-url/{tool_id} | Получение ссылки на OAuth2-авторизацию инструмента
*AIAgentToolsApi* | [**get_agent_tool_template_prices**](docs/AIAgentToolsApi.md#get_agent_tool_template_prices) | **GET** /api/v1/cloud-ai/tools/templates/prices | Получение цен системных инструментов
*AIAgentToolsApi* | [**get_agent_tool_templates**](docs/AIAgentToolsApi.md#get_agent_tool_templates) | **GET** /api/v1/cloud-ai/tools/templates/marketplace | Получение шаблонов MCP-инструментов из маркетплейса
*AIAgentToolsApi* | [**get_agent_tools**](docs/AIAgentToolsApi.md#get_agent_tools) | **GET** /api/v1/cloud-ai/tools | Получение списка MCP-инструментов
*AIAgentToolsApi* | [**get_agent_tools_by_agent**](docs/AIAgentToolsApi.md#get_agent_tools_by_agent) | **GET** /api/v1/cloud-ai/agents/{agent_id}/tools | Получение MCP-инструментов агента
*AIAgentToolsApi* | [**install_agent_tool_from_template**](docs/AIAgentToolsApi.md#install_agent_tool_from_template) | **POST** /api/v1/cloud-ai/tools/install | Установка MCP-инструмента из маркетплейса
*AIAgentToolsApi* | [**refresh_agent_tool_methods**](docs/AIAgentToolsApi.md#refresh_agent_tool_methods) | **POST** /api/v1/cloud-ai/tools/{id}/refresh-methods | Обновление списка методов MCP-инструмента
*AIAgentToolsApi* | [**update_agent_tool**](docs/AIAgentToolsApi.md#update_agent_tool) | **PUT** /api/v1/cloud-ai/tools/{id} | Изменение MCP-инструмента
*AIAgentToolsApi* | [**update_agent_tool_connection**](docs/AIAgentToolsApi.md#update_agent_tool_connection) | **PUT** /api/v1/cloud-ai/agents/{agent_id}/tools/{tool_id} | Изменение разрешённых методов MCP-инструмента у агента
*AIAgentsApi* | [**add_additional_token_package**](docs/AIAgentsApi.md#add_additional_token_package) | **POST** /api/v1/cloud-ai/agents/{id}/add-additional-token-package | Добавление дополнительного пакета токенов
*AIAgentsApi* | [**change_agent_model**](docs/AIAgentsApi.md#change_agent_model) | **PATCH** /api/v1/cloud-ai/agents/{id}/model | Смена модели AI агента
*AIAgentsApi* | [**create_agent**](docs/AIAgentsApi.md#create_agent) | **POST** /api/v1/cloud-ai/agents | Создание AI агента
*AIAgentsApi* | [**create_agent_entity_limit**](docs/AIAgentsApi.md#create_agent_entity_limit) | **POST** /api/v1/cloud-ai/agents/{id}/entity-limits | Создание лимита агента
*AIAgentsApi* | [**create_agent_v2**](docs/AIAgentsApi.md#create_agent_v2) | **POST** /api/v2/cloud-ai/agents | Создание AI агента
*AIAgentsApi* | [**delete_agent**](docs/AIAgentsApi.md#delete_agent) | **DELETE** /api/v1/cloud-ai/agents/{id} | Удаление AI агента
*AIAgentsApi* | [**delete_agent_entity_limit**](docs/AIAgentsApi.md#delete_agent_entity_limit) | **DELETE** /api/v1/cloud-ai/agents/{id}/entity-limits/{limit_id} | Удаление лимита агента
*AIAgentsApi* | [**export_agent_chats_csv**](docs/AIAgentsApi.md#export_agent_chats_csv) | **GET** /api/v1/cloud-ai/agents/{id}/chats/docs | Выгрузка чатов агента в CSV
*AIAgentsApi* | [**get_agent**](docs/AIAgentsApi.md#get_agent) | **GET** /api/v1/cloud-ai/agents/{id} | Получение AI агента
*AIAgentsApi* | [**get_agent_chat_list**](docs/AIAgentsApi.md#get_agent_chat_list) | **GET** /api/v1/cloud-ai/agents/{id}/chat-list | Получение списка чатов агента
*AIAgentsApi* | [**get_agent_chat_messages**](docs/AIAgentsApi.md#get_agent_chat_messages) | **GET** /api/v1/cloud-ai/agents/{id}/chat-list/{chat_id}/messages | Получение сообщений чата агента
*AIAgentsApi* | [**get_agent_entity_limit**](docs/AIAgentsApi.md#get_agent_entity_limit) | **GET** /api/v1/cloud-ai/agents/{id}/entity-limits/{limit_id} | Получение лимита агента
*AIAgentsApi* | [**get_agent_entity_limits**](docs/AIAgentsApi.md#get_agent_entity_limits) | **GET** /api/v1/cloud-ai/agents/{id}/entity-limits | Получение лимитов агента
*AIAgentsApi* | [**get_agent_statistics**](docs/AIAgentsApi.md#get_agent_statistics) | **GET** /api/v1/cloud-ai/agents/{id}/statistic | Получение статистики использования токенов агента
*AIAgentsApi* | [**get_agent_v3**](docs/AIAgentsApi.md#get_agent_v3) | **GET** /api/v3/cloud-ai/agents/{id} | Получение AI агента (v3)
*AIAgentsApi* | [**get_agents**](docs/AIAgentsApi.md#get_agents) | **GET** /api/v1/cloud-ai/agents | Получение списка AI агентов
*AIAgentsApi* | [**get_agents_v3**](docs/AIAgentsApi.md#get_agents_v3) | **GET** /api/v3/cloud-ai/agents | Получение списка AI агентов (v3)
*AIAgentsApi* | [**sync_agent_entity_limits**](docs/AIAgentsApi.md#sync_agent_entity_limits) | **PUT** /api/v1/cloud-ai/agents/{id}/entity-limits/sync | Синхронизация лимитов агента за период
*AIAgentsApi* | [**update_agent**](docs/AIAgentsApi.md#update_agent) | **PATCH** /api/v1/cloud-ai/agents/{id} | Обновление AI агента
*AIAgentsApi* | [**update_agent_entity_limit**](docs/AIAgentsApi.md#update_agent_entity_limit) | **PATCH** /api/v1/cloud-ai/agents/{id}/entity-limits/{limit_id} | Изменение лимита агента
*AIGatewayApi* | [**create_ai_key**](docs/AIGatewayApi.md#create_ai_key) | **POST** /api/v1/cloud-ai/ai-keys | Создание ключа AI Gateway
*AIGatewayApi* | [**create_ai_key_limit**](docs/AIGatewayApi.md#create_ai_key_limit) | **POST** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits | Создание лимита ключа AI Gateway
*AIGatewayApi* | [**delete_ai_key**](docs/AIGatewayApi.md#delete_ai_key) | **DELETE** /api/v1/cloud-ai/ai-keys/{key_id} | Удаление ключа AI Gateway
*AIGatewayApi* | [**delete_ai_key_limit**](docs/AIGatewayApi.md#delete_ai_key_limit) | **DELETE** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id} | Удаление лимита ключа AI Gateway
*AIGatewayApi* | [**get_ai_key_calls_statistic**](docs/AIGatewayApi.md#get_ai_key_calls_statistic) | **GET** /api/v1/cloud-ai/ai-keys/statistic/calls | Получение статистики запросов ключа AI Gateway
*AIGatewayApi* | [**get_ai_key_limit**](docs/AIGatewayApi.md#get_ai_key_limit) | **GET** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id} | Получение лимита ключа AI Gateway
*AIGatewayApi* | [**get_ai_key_limits**](docs/AIGatewayApi.md#get_ai_key_limits) | **GET** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits | Получение списка лимитов ключа AI Gateway
*AIGatewayApi* | [**get_ai_key_models_statistic**](docs/AIGatewayApi.md#get_ai_key_models_statistic) | **GET** /api/v1/cloud-ai/ai-keys/statistic/models | Получение списка моделей, использованных ключом AI Gateway
*AIGatewayApi* | [**get_ai_key_token_usage_statistic**](docs/AIGatewayApi.md#get_ai_key_token_usage_statistic) | **GET** /api/v1/cloud-ai/ai-keys/statistic/token-usage | Получение статистики расхода токенов ключа AI Gateway
*AIGatewayApi* | [**get_ai_keys**](docs/AIGatewayApi.md#get_ai_keys) | **GET** /api/v1/cloud-ai/ai-keys | Получение списка ключей AI Gateway
*AIGatewayApi* | [**regenerate_ai_key**](docs/AIGatewayApi.md#regenerate_ai_key) | **PUT** /api/v1/cloud-ai/ai-keys/{key_id}/regenerate | Перевыпуск ключа AI Gateway
*AIGatewayApi* | [**sync_ai_key_limits**](docs/AIGatewayApi.md#sync_ai_key_limits) | **PUT** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/sync | Синхронизация лимитов ключа AI Gateway
*AIGatewayApi* | [**update_ai_key**](docs/AIGatewayApi.md#update_ai_key) | **PATCH** /api/v1/cloud-ai/ai-keys/{key_id} | Изменение ключа AI Gateway
*AIGatewayApi* | [**update_ai_key_limit**](docs/AIGatewayApi.md#update_ai_key_limit) | **PATCH** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id} | Изменение лимита ключа AI Gateway
*AIGatewayInferenceApi* | [**cancel_ai_gateway_batch**](docs/AIGatewayInferenceApi.md#cancel_ai_gateway_batch) | **POST** /v1/batches/{batch_id}/cancel | Отмена батча
*AIGatewayInferenceApi* | [**cancel_ai_gateway_response**](docs/AIGatewayInferenceApi.md#cancel_ai_gateway_response) | **POST** /v1/responses/{response_id}/cancel | Отмена фонового ответа (Responses API)
*AIGatewayInferenceApi* | [**create_ai_gateway_batch**](docs/AIGatewayInferenceApi.md#create_ai_gateway_batch) | **POST** /v1/batches | Создание батча
*AIGatewayInferenceApi* | [**create_ai_gateway_chat_completion**](docs/AIGatewayInferenceApi.md#create_ai_gateway_chat_completion) | **POST** /v1/chat/completions | Генерация ответа в диалоге (Chat Completions)
*AIGatewayInferenceApi* | [**create_ai_gateway_completion**](docs/AIGatewayInferenceApi.md#create_ai_gateway_completion) | **POST** /v1/completions | Продолжение текста (Completions)
*AIGatewayInferenceApi* | [**create_ai_gateway_embedding**](docs/AIGatewayInferenceApi.md#create_ai_gateway_embedding) | **POST** /v1/embeddings | Получение эмбеддингов
*AIGatewayInferenceApi* | [**create_ai_gateway_image**](docs/AIGatewayInferenceApi.md#create_ai_gateway_image) | **POST** /v1/images/generations | Генерация изображений
*AIGatewayInferenceApi* | [**create_ai_gateway_image_edit**](docs/AIGatewayInferenceApi.md#create_ai_gateway_image_edit) | **POST** /v1/images/edits | Редактирование изображений
*AIGatewayInferenceApi* | [**create_ai_gateway_response**](docs/AIGatewayInferenceApi.md#create_ai_gateway_response) | **POST** /v1/responses | Создание ответа (Responses API)
*AIGatewayInferenceApi* | [**create_ai_gateway_speech**](docs/AIGatewayInferenceApi.md#create_ai_gateway_speech) | **POST** /v1/audio/speech | Синтез речи
*AIGatewayInferenceApi* | [**create_ai_gateway_transcription**](docs/AIGatewayInferenceApi.md#create_ai_gateway_transcription) | **POST** /v1/audio/transcriptions | Распознавание речи
*AIGatewayInferenceApi* | [**delete_ai_gateway_file**](docs/AIGatewayInferenceApi.md#delete_ai_gateway_file) | **DELETE** /v1/files/{file_id} | Удаление файла
*AIGatewayInferenceApi* | [**delete_ai_gateway_response**](docs/AIGatewayInferenceApi.md#delete_ai_gateway_response) | **DELETE** /v1/responses/{response_id} | Удаление ответа (Responses API)
*AIGatewayInferenceApi* | [**download_ai_gateway_file_content**](docs/AIGatewayInferenceApi.md#download_ai_gateway_file_content) | **GET** /v1/files/{file_id}/content | Скачивание файла
*AIGatewayInferenceApi* | [**get_ai_gateway_batch**](docs/AIGatewayInferenceApi.md#get_ai_gateway_batch) | **GET** /v1/batches/{batch_id} | Получение батча
*AIGatewayInferenceApi* | [**get_ai_gateway_batches**](docs/AIGatewayInferenceApi.md#get_ai_gateway_batches) | **GET** /v1/batches | Получение списка батчей
*AIGatewayInferenceApi* | [**get_ai_gateway_file**](docs/AIGatewayInferenceApi.md#get_ai_gateway_file) | **GET** /v1/files/{file_id} | Получение информации о файле
*AIGatewayInferenceApi* | [**get_ai_gateway_models**](docs/AIGatewayInferenceApi.md#get_ai_gateway_models) | **GET** /v1/models | Получение списка моделей AI Gateway
*AIGatewayInferenceApi* | [**get_ai_gateway_response**](docs/AIGatewayInferenceApi.md#get_ai_gateway_response) | **GET** /v1/responses/{response_id} | Получение ответа (Responses API)
*AIGatewayInferenceApi* | [**upload_ai_gateway_file**](docs/AIGatewayInferenceApi.md#upload_ai_gateway_file) | **POST** /v1/files | Загрузка файла
*AIModelsApi* | [**get_agents_token_packages**](docs/AIModelsApi.md#get_agents_token_packages) | **GET** /api/v1/cloud-ai/token-packages/agents | Получение списка пакетов токенов для агентов
*AIModelsApi* | [**get_ai_model_parameters**](docs/AIModelsApi.md#get_ai_model_parameters) | **GET** /api/v3/cloud-ai/model-parameters | Получение справочника характеристик моделей
*AIModelsApi* | [**get_ai_model_token_packages**](docs/AIModelsApi.md#get_ai_model_token_packages) | **GET** /api/v1/cloud-ai/models/{id}/token-packages | Получение пакетов токенов модели
*AIModelsApi* | [**get_ai_provider**](docs/AIModelsApi.md#get_ai_provider) | **GET** /api/v1/cloud-ai/providers/{id} | Получение провайдера моделей
*AIModelsApi* | [**get_ai_providers**](docs/AIModelsApi.md#get_ai_providers) | **GET** /api/v1/cloud-ai/providers | Получение списка провайдеров моделей
*AIModelsApi* | [**get_knowledgebases_token_packages**](docs/AIModelsApi.md#get_knowledgebases_token_packages) | **GET** /api/v1/cloud-ai/token-packages/knowledge-bases | Получение списка пакетов токенов для баз знаний
*AIModelsApi* | [**get_models**](docs/AIModelsApi.md#get_models) | **GET** /api/v1/cloud-ai/models | Получение списка моделей (v1)
*AIModelsApi* | [**get_models_v3**](docs/AIModelsApi.md#get_models_v3) | **GET** /api/v3/cloud-ai/models | Получение списка моделей
*AISolutionsApi* | [**add_ai_solution_telegram_bot**](docs/AISolutionsApi.md#add_ai_solution_telegram_bot) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/telegram/bots | Подключение Telegram-бота к AI-решению
*AISolutionsApi* | [**approve_ai_solution_telegram_pairing**](docs/AISolutionsApi.md#approve_ai_solution_telegram_pairing) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key}/pairing/approve | Подтверждение владельца Telegram-бота AI-решения
*AISolutionsApi* | [**create_ai_solution**](docs/AISolutionsApi.md#create_ai_solution) | **POST** /api/v1/cloud-ai/solutions | Создание AI-решения
*AISolutionsApi* | [**delete_ai_solution**](docs/AISolutionsApi.md#delete_ai_solution) | **DELETE** /api/v1/cloud-ai/solutions/{solution_id} | Удаление AI-решения
*AISolutionsApi* | [**get_ai_solution**](docs/AISolutionsApi.md#get_ai_solution) | **GET** /api/v1/cloud-ai/solutions/{solution_id} | Получение AI-решения
*AISolutionsApi* | [**get_ai_solution_chat_full_history**](docs/AISolutionsApi.md#get_ai_solution_chat_full_history) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/chat/history | Получение всей истории чата AI-решения
*AISolutionsApi* | [**get_ai_solution_chat_history**](docs/AISolutionsApi.md#get_ai_solution_chat_history) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/chat/conversations/{conversation_id}/messages | Получение истории разговора AI-решения
*AISolutionsApi* | [**get_ai_solution_chat_status**](docs/AISolutionsApi.md#get_ai_solution_chat_status) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/chat/status | Получение статуса чата AI-решения
*AISolutionsApi* | [**get_ai_solution_main_chat_history**](docs/AISolutionsApi.md#get_ai_solution_main_chat_history) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/chat/messages | Получение истории основного разговора AI-решения
*AISolutionsApi* | [**list_ai_solution_conversations**](docs/AISolutionsApi.md#list_ai_solution_conversations) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/chat/conversations | Получение списка разговоров AI-решения
*AISolutionsApi* | [**list_ai_solution_telegram_bots**](docs/AISolutionsApi.md#list_ai_solution_telegram_bots) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/telegram/bots | Получение списка Telegram-ботов AI-решения
*AISolutionsApi* | [**list_ai_solution_types**](docs/AISolutionsApi.md#list_ai_solution_types) | **GET** /api/v1/cloud-ai/solutions/types | Получение списка типов AI-решений
*AISolutionsApi* | [**list_ai_solutions**](docs/AISolutionsApi.md#list_ai_solutions) | **GET** /api/v1/cloud-ai/solutions | Получение списка AI-решений
*AISolutionsApi* | [**regenerate_ai_solution_ai_key**](docs/AISolutionsApi.md#regenerate_ai_solution_ai_key) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/ai-key/regenerate | Перевыпуск ключа AI Gateway решения
*AISolutionsApi* | [**remove_ai_solution_telegram_bot**](docs/AISolutionsApi.md#remove_ai_solution_telegram_bot) | **DELETE** /api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key} | Отключение Telegram-бота от AI-решения
*AISolutionsApi* | [**reset_ai_solution_chat**](docs/AISolutionsApi.md#reset_ai_solution_chat) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/chat/reset | Сброс контекста разговора AI-решения
*AISolutionsApi* | [**send_ai_solution_message**](docs/AISolutionsApi.md#send_ai_solution_message) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/chat/messages | Отправка сообщения агенту AI-решения
*AISolutionsApi* | [**shutdown_ai_solution**](docs/AISolutionsApi.md#shutdown_ai_solution) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/shutdown | Выключение AI-решения
*AISolutionsApi* | [**start_ai_solution**](docs/AISolutionsApi.md#start_ai_solution) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/start | Запуск AI-решения
*AISolutionsApi* | [**stop_ai_solution_chat**](docs/AISolutionsApi.md#stop_ai_solution_chat) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/chat/stop | Остановка хода агента AI-решения
*AISolutionsApi* | [**stream_ai_solution_chat**](docs/AISolutionsApi.md#stream_ai_solution_chat) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/chat/stream | Отправка сообщения агенту AI-решения с потоковым ответом
*AISolutionsApi* | [**update_ai_solution**](docs/AISolutionsApi.md#update_ai_solution) | **PATCH** /api/v1/cloud-ai/solutions/{solution_id} | Изменение AI-решения
*AccountApi* | [**add_countries_to_allowed_list**](docs/AccountApi.md#add_countries_to_allowed_list) | **POST** /api/v1/auth/access/countries | Добавление стран в список разрешенных
*AccountApi* | [**add_ips_to_allowed_list**](docs/AccountApi.md#add_ips_to_allowed_list) | **POST** /api/v1/auth/access/ips | Добавление IP-адресов в список разрешенных
*AccountApi* | [**delete_countries_from_allowed_list**](docs/AccountApi.md#delete_countries_from_allowed_list) | **DELETE** /api/v1/auth/access/countries | Удаление стран из списка разрешенных
*AccountApi* | [**delete_ips_from_allowed_list**](docs/AccountApi.md#delete_ips_from_allowed_list) | **DELETE** /api/v1/auth/access/ips | Удаление IP-адресов из списка разрешенных
*AccountApi* | [**get_account_status**](docs/AccountApi.md#get_account_status) | **GET** /api/v1/account/status | Получение статуса аккаунта
*AccountApi* | [**get_auth_access_settings**](docs/AccountApi.md#get_auth_access_settings) | **GET** /api/v1/auth/access | Получить информацию о ограничениях авторизации пользователя
*AccountApi* | [**get_countries**](docs/AccountApi.md#get_countries) | **GET** /api/v1/auth/access/countries | Получение списка стран
*AccountApi* | [**get_notification_settings**](docs/AccountApi.md#get_notification_settings) | **GET** /api/v1/account/notification-settings | Получение настроек уведомлений аккаунта
*AccountApi* | [**update_auth_restrictions_by_countries**](docs/AccountApi.md#update_auth_restrictions_by_countries) | **POST** /api/v1/auth/access/countries/enabled | Включение/отключение ограничений по стране
*AccountApi* | [**update_auth_restrictions_by_ip**](docs/AccountApi.md#update_auth_restrictions_by_ip) | **POST** /api/v1/auth/access/ips/enabled | Включение/отключение ограничений по IP-адресу
*AccountApi* | [**update_notification_settings**](docs/AccountApi.md#update_notification_settings) | **PATCH** /api/v1/account/notification-settings | Изменение настроек уведомлений аккаунта
*AppsApi* | [**add_provider**](docs/AppsApi.md#add_provider) | **POST** /api/v1/vcs-provider | Привязка vcs провайдера
*AppsApi* | [**create_app**](docs/AppsApi.md#create_app) | **POST** /api/v1/apps | Создание приложения
*AppsApi* | [**create_deploy**](docs/AppsApi.md#create_deploy) | **POST** /api/v1/apps/{app_id}/deploy | Запуск деплоя приложения
*AppsApi* | [**delete_app**](docs/AppsApi.md#delete_app) | **DELETE** /api/v1/apps/{app_id} | Удаление приложения
*AppsApi* | [**delete_provider**](docs/AppsApi.md#delete_provider) | **DELETE** /api/v1/vcs-provider/{provider_id} | Отвязка vcs провайдера от аккаунта
*AppsApi* | [**deploy_action**](docs/AppsApi.md#deploy_action) | **POST** /api/v1/apps/{app_id}/deploy/{deploy_id}/stop | Остановка деплоя приложения
*AppsApi* | [**get_app**](docs/AppsApi.md#get_app) | **GET** /api/v1/apps/{app_id} | Получение приложения по id
*AppsApi* | [**get_app_deploys**](docs/AppsApi.md#get_app_deploys) | **GET** /api/v1/apps/{app_id}/deploys | Получение списка деплоев приложения
*AppsApi* | [**get_app_logs**](docs/AppsApi.md#get_app_logs) | **GET** /api/v1/apps/{app_id}/logs | Получение логов приложения
*AppsApi* | [**get_app_statistics**](docs/AppsApi.md#get_app_statistics) | **GET** /api/v1/apps/{app_id}/statistics | Получение статистики приложения
*AppsApi* | [**get_apps**](docs/AppsApi.md#get_apps) | **GET** /api/v1/apps | Получение списка приложений
*AppsApi* | [**get_apps_presets**](docs/AppsApi.md#get_apps_presets) | **GET** /api/v1/presets/apps | Получение списка доступных тарифов для приложения
*AppsApi* | [**get_branches**](docs/AppsApi.md#get_branches) | **GET** /api/v1/vcs-provider/{provider_id}/repository/{repository_id} | Получение списка веток репозитория
*AppsApi* | [**get_commits**](docs/AppsApi.md#get_commits) | **GET** /api/v1/vcs-provider/{provider_id}/repository/{repository_id}/branch | Получение списка коммитов ветки репозитория
*AppsApi* | [**get_deploy_logs**](docs/AppsApi.md#get_deploy_logs) | **GET** /api/v1/apps/{app_id}/deploy/{deploy_id}/logs | Получение логов деплоя приложения
*AppsApi* | [**get_deploy_settings**](docs/AppsApi.md#get_deploy_settings) | **GET** /api/v1/deploy-settings/apps | Получение списка дефолтных настроек деплоя для приложения
*AppsApi* | [**get_frameworks**](docs/AppsApi.md#get_frameworks) | **GET** /api/v1/frameworks/apps | Получение списка доступных фреймворков для приложения
*AppsApi* | [**get_providers**](docs/AppsApi.md#get_providers) | **GET** /api/v1/vcs-provider | Получение списка vcs провайдеров
*AppsApi* | [**get_repositories**](docs/AppsApi.md#get_repositories) | **GET** /api/v1/vcs-provider/{provider_id} | Получение списка репозиториев vcs провайдера
*AppsApi* | [**update_app_settings**](docs/AppsApi.md#update_app_settings) | **PATCH** /api/v1/apps/{app_id} | Изменение настроек приложения
*AppsApi* | [**update_app_state**](docs/AppsApi.md#update_app_state) | **PATCH** /api/v1/apps/{app_id}/action/{action} | Изменение состояния приложения
*BalancersApi* | [**add_ips_to_balancer**](docs/BalancersApi.md#add_ips_to_balancer) | **POST** /api/v1/balancers/{balancer_id}/ips | Добавление IP-адресов к балансировщику
*BalancersApi* | [**create_balancer**](docs/BalancersApi.md#create_balancer) | **POST** /api/v1/balancers | Создание бaлансировщика
*BalancersApi* | [**create_balancer_rule**](docs/BalancersApi.md#create_balancer_rule) | **POST** /api/v1/balancers/{balancer_id}/rules | Создание правила для балансировщика
*BalancersApi* | [**delete_balancer**](docs/BalancersApi.md#delete_balancer) | **DELETE** /api/v1/balancers/{balancer_id} | Удаление балансировщика
*BalancersApi* | [**delete_balancer_rule**](docs/BalancersApi.md#delete_balancer_rule) | **DELETE** /api/v1/balancers/{balancer_id}/rules/{rule_id} | Удаление правила для балансировщика
*BalancersApi* | [**delete_ips_from_balancer**](docs/BalancersApi.md#delete_ips_from_balancer) | **DELETE** /api/v1/balancers/{balancer_id}/ips | Удаление IP-адресов из балансировщика
*BalancersApi* | [**get_balancer**](docs/BalancersApi.md#get_balancer) | **GET** /api/v1/balancers/{balancer_id} | Получение бaлансировщика
*BalancersApi* | [**get_balancer_ips**](docs/BalancersApi.md#get_balancer_ips) | **GET** /api/v1/balancers/{balancer_id}/ips | Получение списка IP-адресов балансировщика
*BalancersApi* | [**get_balancer_rules**](docs/BalancersApi.md#get_balancer_rules) | **GET** /api/v1/balancers/{balancer_id}/rules | Получение правил балансировщика
*BalancersApi* | [**get_balancers**](docs/BalancersApi.md#get_balancers) | **GET** /api/v1/balancers | Получение списка всех бaлансировщиков
*BalancersApi* | [**get_balancers_presets**](docs/BalancersApi.md#get_balancers_presets) | **GET** /api/v1/presets/balancers | Получение списка тарифов для балансировщика
*BalancersApi* | [**update_balancer**](docs/BalancersApi.md#update_balancer) | **PATCH** /api/v1/balancers/{balancer_id} | Обновление балансировщика
*BalancersApi* | [**update_balancer_rule**](docs/BalancersApi.md#update_balancer_rule) | **PATCH** /api/v1/balancers/{balancer_id}/rules/{rule_id} | Обновление правила для балансировщика
*CDNApi* | [**add_cdn_certificate**](docs/CDNApi.md#add_cdn_certificate) | **POST** /api/v1/cdn/certificates | Загрузка собственного сертификата CDN
*CDNApi* | [**archive_cdn_certificate_task**](docs/CDNApi.md#archive_cdn_certificate_task) | **POST** /api/v1/cdn/certificates/tasks/{task_id}/archive | Архивация задачи на выпуск сертификата
*CDNApi* | [**clear_cdn_resource_cache**](docs/CDNApi.md#clear_cdn_resource_cache) | **POST** /api/v1/cdn/http-resources/{resource_id}/clear-cache | Очистка кэша CDN-ресурса
*CDNApi* | [**create_cdn_resource**](docs/CDNApi.md#create_cdn_resource) | **POST** /api/v1/cdn/http-resources | Создание CDN-ресурса
*CDNApi* | [**delete_cdn_certificate**](docs/CDNApi.md#delete_cdn_certificate) | **DELETE** /api/v1/cdn/certificates/{certificate_id} | Удаление сертификата CDN
*CDNApi* | [**delete_cdn_resource**](docs/CDNApi.md#delete_cdn_resource) | **DELETE** /api/v1/cdn/http-resources/{resource_id} | Удаление CDN-ресурса
*CDNApi* | [**get_cdn_certificate_tasks**](docs/CDNApi.md#get_cdn_certificate_tasks) | **GET** /api/v1/cdn/certificates/tasks | Получение списка задач на выпуск сертификатов
*CDNApi* | [**get_cdn_certificates**](docs/CDNApi.md#get_cdn_certificates) | **GET** /api/v1/cdn/certificates | Получение списка сертификатов CDN
*CDNApi* | [**get_cdn_origin_nodes**](docs/CDNApi.md#get_cdn_origin_nodes) | **GET** /api/v1/cdn/nodes/origin | Получение списка подсетей узлов CDN
*CDNApi* | [**get_cdn_presets**](docs/CDNApi.md#get_cdn_presets) | **GET** /api/v1/cdn/presets | Получение списка тарифов CDN
*CDNApi* | [**get_cdn_resource**](docs/CDNApi.md#get_cdn_resource) | **GET** /api/v1/cdn/http-resources/{resource_id} | Получение CDN-ресурса
*CDNApi* | [**get_cdn_resource_configuration**](docs/CDNApi.md#get_cdn_resource_configuration) | **GET** /api/v1/cdn/http-resources/{resource_id}/configuration | Получение конфигурации CDN-ресурса
*CDNApi* | [**get_cdn_resource_nodes**](docs/CDNApi.md#get_cdn_resource_nodes) | **GET** /api/v1/cdn/nodes/http-resources/{resource_id} | Получение списка раздающих узлов CDN-ресурса
*CDNApi* | [**get_cdn_resource_statistics**](docs/CDNApi.md#get_cdn_resource_statistics) | **GET** /api/v1/cdn/http-resources/{resource_id}/statistics | Получение статистики CDN-ресурса
*CDNApi* | [**get_cdn_resources**](docs/CDNApi.md#get_cdn_resources) | **GET** /api/v1/cdn/http-resources | Получение списка CDN-ресурсов
*CDNApi* | [**issue_cdn_certificate**](docs/CDNApi.md#issue_cdn_certificate) | **POST** /api/v1/cdn/certificates/issue | Выпуск сертификата Let&#39;s Encrypt для CDN-ресурса
*CDNApi* | [**preload_cdn_resource_cache**](docs/CDNApi.md#preload_cdn_resource_cache) | **POST** /api/v1/cdn/http-resources/{resource_id}/preload-cache | Предварительная загрузка кэша CDN-ресурса
*CDNApi* | [**resume_cdn_resource**](docs/CDNApi.md#resume_cdn_resource) | **POST** /api/v1/cdn/http-resources/{resource_id}/resume | Возобновление раздачи CDN-ресурса
*CDNApi* | [**suspend_cdn_resource**](docs/CDNApi.md#suspend_cdn_resource) | **POST** /api/v1/cdn/http-resources/{resource_id}/suspend | Приостановка раздачи CDN-ресурса
*CDNApi* | [**update_cdn_resource**](docs/CDNApi.md#update_cdn_resource) | **PATCH** /api/v1/cdn/http-resources/{resource_id} | Изменение CDN-ресурса
*ContainerRegistryApi* | [**create_registry**](docs/ContainerRegistryApi.md#create_registry) | **POST** /api/v1/container-registry | Создание реестра
*ContainerRegistryApi* | [**delete_registry**](docs/ContainerRegistryApi.md#delete_registry) | **DELETE** /api/v1/container-registry/{registry_id} | Удаление реестра
*ContainerRegistryApi* | [**get_registries**](docs/ContainerRegistryApi.md#get_registries) | **GET** /api/v1/container-registry | Получение списка реестров контейнеров
*ContainerRegistryApi* | [**get_registry**](docs/ContainerRegistryApi.md#get_registry) | **GET** /api/v1/container-registry/{registry_id} | Получение информации о реестре
*ContainerRegistryApi* | [**get_registry_presets**](docs/ContainerRegistryApi.md#get_registry_presets) | **GET** /api/v1/container-registry/presets | Получение списка тарифов
*ContainerRegistryApi* | [**get_registry_repositories**](docs/ContainerRegistryApi.md#get_registry_repositories) | **GET** /api/v1/container-registry/{registry_id}/repositories | Получение списка репозиториев
*ContainerRegistryApi* | [**update_registry**](docs/ContainerRegistryApi.md#update_registry) | **PATCH** /api/v1/container-registry/{registry_id} | Обновление информации о реестре
*DatabasesApi* | [**create_database_backup**](docs/DatabasesApi.md#create_database_backup) | **POST** /api/v1/dbs/{db_id}/backups | Создание бэкапа базы данных
*DatabasesApi* | [**create_database_backup_download_url**](docs/DatabasesApi.md#create_database_backup_download_url) | **POST** /api/v1/dbs/{db_id}/backups/{backup_id}/download-url | Получение ссылки для скачивания бэкапа базы данных
*DatabasesApi* | [**create_database_cluster**](docs/DatabasesApi.md#create_database_cluster) | **POST** /api/v1/databases | Создание кластера базы данных
*DatabasesApi* | [**create_database_instance**](docs/DatabasesApi.md#create_database_instance) | **POST** /api/v1/databases/{db_cluster_id}/instances | Создание инстанса базы данных
*DatabasesApi* | [**create_database_s3_backup**](docs/DatabasesApi.md#create_database_s3_backup) | **POST** /api/v2/databases/{db_id}/backups | Создание S3-бэкапа базы данных
*DatabasesApi* | [**create_database_user**](docs/DatabasesApi.md#create_database_user) | **POST** /api/v1/databases/{db_cluster_id}/admins | Создание пользователя базы данных
*DatabasesApi* | [**delete_database_backup**](docs/DatabasesApi.md#delete_database_backup) | **DELETE** /api/v1/dbs/{db_id}/backups/{backup_id} | Удаление бэкапа базы данных
*DatabasesApi* | [**delete_database_cluster**](docs/DatabasesApi.md#delete_database_cluster) | **DELETE** /api/v1/databases/{db_cluster_id} | Удаление кластера базы данных
*DatabasesApi* | [**delete_database_instance**](docs/DatabasesApi.md#delete_database_instance) | **DELETE** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Удаление инстанса базы данных
*DatabasesApi* | [**delete_database_s3_backup**](docs/DatabasesApi.md#delete_database_s3_backup) | **DELETE** /api/v2/databases/{db_id}/backups/{backup_id} | Удаление S3-бэкапа базы данных
*DatabasesApi* | [**delete_database_user**](docs/DatabasesApi.md#delete_database_user) | **DELETE** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Удаление пользователя базы данных
*DatabasesApi* | [**get_database_auto_backups_settings**](docs/DatabasesApi.md#get_database_auto_backups_settings) | **GET** /api/v1/dbs/{db_id}/auto-backups | Получение настроек автобэкапов базы данных
*DatabasesApi* | [**get_database_backup**](docs/DatabasesApi.md#get_database_backup) | **GET** /api/v1/dbs/{db_id}/backups/{backup_id} | Получение бэкапа базы данных
*DatabasesApi* | [**get_database_backups**](docs/DatabasesApi.md#get_database_backups) | **GET** /api/v1/dbs/{db_id}/backups | Список бэкапов базы данных
*DatabasesApi* | [**get_database_cluster**](docs/DatabasesApi.md#get_database_cluster) | **GET** /api/v1/databases/{db_cluster_id} | Получение кластера базы данных
*DatabasesApi* | [**get_database_cluster_replicas**](docs/DatabasesApi.md#get_database_cluster_replicas) | **GET** /api/v1/databases/{db_cluster_id}/replicas | Получение списка реплик кластера базы данных
*DatabasesApi* | [**get_database_cluster_types**](docs/DatabasesApi.md#get_database_cluster_types) | **GET** /api/v1/database-types | Получение списка типов кластеров баз данных
*DatabasesApi* | [**get_database_clusters**](docs/DatabasesApi.md#get_database_clusters) | **GET** /api/v1/databases | Получение списка кластеров баз данных
*DatabasesApi* | [**get_database_configurators**](docs/DatabasesApi.md#get_database_configurators) | **GET** /api/v1/configurator/databases | Получение списка конфигураторов баз данных
*DatabasesApi* | [**get_database_default_parameters**](docs/DatabasesApi.md#get_database_default_parameters) | **GET** /api/v1/dbs/default-parameters | Получение рекомендуемых значений параметров баз данных
*DatabasesApi* | [**get_database_instance**](docs/DatabasesApi.md#get_database_instance) | **GET** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Получение инстанса базы данных
*DatabasesApi* | [**get_database_instances**](docs/DatabasesApi.md#get_database_instances) | **GET** /api/v1/databases/{db_cluster_id}/instances | Получение списка инстансов баз данных
*DatabasesApi* | [**get_database_parameters**](docs/DatabasesApi.md#get_database_parameters) | **GET** /api/v1/dbs/parameters | Получение списка параметров баз данных
*DatabasesApi* | [**get_database_preset**](docs/DatabasesApi.md#get_database_preset) | **GET** /api/v2/dbs/presets/{preset_id} | Получение тарифа для базы данных
*DatabasesApi* | [**get_database_privileges**](docs/DatabasesApi.md#get_database_privileges) | **GET** /api/v1/databases/{db_cluster_id}/privileges | Получение привилегий кластера базы данных
*DatabasesApi* | [**get_database_s3_backup**](docs/DatabasesApi.md#get_database_s3_backup) | **GET** /api/v2/databases/{db_id}/backups/{backup_id} | Получение S3-бэкапа базы данных
*DatabasesApi* | [**get_database_s3_backups**](docs/DatabasesApi.md#get_database_s3_backups) | **GET** /api/v2/databases/{db_id}/backups | Список S3-бэкапов базы данных
*DatabasesApi* | [**get_database_user**](docs/DatabasesApi.md#get_database_user) | **GET** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Получение пользователя базы данных
*DatabasesApi* | [**get_database_users**](docs/DatabasesApi.md#get_database_users) | **GET** /api/v1/databases/{db_cluster_id}/admins | Получение списка пользователей базы данных
*DatabasesApi* | [**get_databases_presets**](docs/DatabasesApi.md#get_databases_presets) | **GET** /api/v2/presets/dbs | Получение списка тарифов для баз данных
*DatabasesApi* | [**perform_database_cluster_action**](docs/DatabasesApi.md#perform_database_cluster_action) | **POST** /api/v1/databases/{db_cluster_id}/action | Выполнение действия над кластером базы данных
*DatabasesApi* | [**restore_database_from_backup**](docs/DatabasesApi.md#restore_database_from_backup) | **PUT** /api/v1/dbs/{db_id}/backups/{backup_id} | Восстановление базы данных из бэкапа
*DatabasesApi* | [**restore_database_from_s3_backup**](docs/DatabasesApi.md#restore_database_from_s3_backup) | **POST** /api/v2/databases/{db_id}/backups/{backup_id}/restore | Восстановление базы данных из S3-бэкапа
*DatabasesApi* | [**update_database_auto_backups_settings**](docs/DatabasesApi.md#update_database_auto_backups_settings) | **PATCH** /api/v1/dbs/{db_id}/auto-backups | Изменение настроек автобэкапов базы данных
*DatabasesApi* | [**update_database_backup**](docs/DatabasesApi.md#update_database_backup) | **PATCH** /api/v1/dbs/{db_id}/backups/{backup_id} | Изменение комментария к бэкапу базы данных
*DatabasesApi* | [**update_database_cluster**](docs/DatabasesApi.md#update_database_cluster) | **PATCH** /api/v1/databases/{db_cluster_id} | Изменение кластера базы данных
*DatabasesApi* | [**update_database_cluster_v2**](docs/DatabasesApi.md#update_database_cluster_v2) | **PATCH** /api/v2/databases/{db_cluster_id} | Изменение кластера базы данных (v2)
*DatabasesApi* | [**update_database_instance**](docs/DatabasesApi.md#update_database_instance) | **PATCH** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Изменение инстанса базы данных
*DatabasesApi* | [**update_database_s3_backup**](docs/DatabasesApi.md#update_database_s3_backup) | **PATCH** /api/v2/databases/{db_id}/backups/{backup_id} | Изменение комментария S3-бэкапа базы данных
*DatabasesApi* | [**update_database_user**](docs/DatabasesApi.md#update_database_user) | **PATCH** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Изменение пользователя базы данных
*DedicatedServersApi* | [**create_dedicated_server**](docs/DedicatedServersApi.md#create_dedicated_server) | **POST** /api/v1/dedicated-servers | Создание выделенного сервера
*DedicatedServersApi* | [**delete_dedicated_server**](docs/DedicatedServersApi.md#delete_dedicated_server) | **DELETE** /api/v1/dedicated-servers/{dedicated_id} | Удаление выделенного сервера
*DedicatedServersApi* | [**get_dedicated_server**](docs/DedicatedServersApi.md#get_dedicated_server) | **GET** /api/v1/dedicated-servers/{dedicated_id} | Получение выделенного сервера
*DedicatedServersApi* | [**get_dedicated_server_preset_additional_services**](docs/DedicatedServersApi.md#get_dedicated_server_preset_additional_services) | **GET** /api/v1/presets/dedicated-servers/{preset_id}/additional-services | Получение дополнительных услуг для выделенного сервера
*DedicatedServersApi* | [**get_dedicated_servers**](docs/DedicatedServersApi.md#get_dedicated_servers) | **GET** /api/v1/dedicated-servers | Получение списка выделенных серверов
*DedicatedServersApi* | [**get_dedicated_servers_presets**](docs/DedicatedServersApi.md#get_dedicated_servers_presets) | **GET** /api/v1/presets/dedicated-servers | Получение списка тарифов для выделенного сервера
*DedicatedServersApi* | [**update_dedicated_server**](docs/DedicatedServersApi.md#update_dedicated_server) | **PATCH** /api/v1/dedicated-servers/{dedicated_id} | Обновление выделенного сервера
*DomainsApi* | [**add_domain**](docs/DomainsApi.md#add_domain) | **POST** /api/v1/add-domain/{fqdn} | Добавление домена на аккаунт
*DomainsApi* | [**add_subdomain**](docs/DomainsApi.md#add_subdomain) | **POST** /api/v1/domains/{fqdn}/subdomains/{subdomain} | Добавление поддомена
*DomainsApi* | [**check_domain**](docs/DomainsApi.md#check_domain) | **GET** /api/v1/check-domain/{fqdn} | Проверить, доступен ли домен для регистрации
*DomainsApi* | [**create_domain_dns_record**](docs/DomainsApi.md#create_domain_dns_record) | **POST** /api/v1/domains/{fqdn}/dns-records | Добавить информацию о DNS-записи для домена или поддомена
*DomainsApi* | [**create_domain_dns_record_v2**](docs/DomainsApi.md#create_domain_dns_record_v2) | **POST** /api/v2/domains/{fqdn}/dns-records | Добавить информацию о DNS-записи для домена или поддомена
*DomainsApi* | [**create_domain_request**](docs/DomainsApi.md#create_domain_request) | **POST** /api/v1/domains-requests | Создание заявки на регистрацию/продление/трансфер домена
*DomainsApi* | [**create_person**](docs/DomainsApi.md#create_person) | **POST** /api/v1/persons | Создание администратора доменов
*DomainsApi* | [**delete_domain**](docs/DomainsApi.md#delete_domain) | **DELETE** /api/v1/domains/{fqdn} | Удаление домена
*DomainsApi* | [**delete_domain_dns_record**](docs/DomainsApi.md#delete_domain_dns_record) | **DELETE** /api/v1/domains/{fqdn}/dns-records/{record_id} | Удалить информацию о DNS-записи для домена или поддомена
*DomainsApi* | [**delete_domain_dns_record_v2**](docs/DomainsApi.md#delete_domain_dns_record_v2) | **DELETE** /api/v2/domains/{fqdn}/dns-records/{record_id} | Удалить информацию о DNS-записи для домена или поддомена
*DomainsApi* | [**delete_person**](docs/DomainsApi.md#delete_person) | **DELETE** /api/v1/persons/{person_id} | Удаление администратора доменов
*DomainsApi* | [**delete_subdomain**](docs/DomainsApi.md#delete_subdomain) | **DELETE** /api/v1/domains/{fqdn}/subdomains/{subdomain} | Удаление поддомена
*DomainsApi* | [**get_domain**](docs/DomainsApi.md#get_domain) | **GET** /api/v1/domains/{fqdn} | Получение информации о домене
*DomainsApi* | [**get_domain_default_dns_records**](docs/DomainsApi.md#get_domain_default_dns_records) | **GET** /api/v1/domains/{fqdn}/default-dns-records | Получить информацию обо всех DNS-записях по умолчанию домена или поддомена
*DomainsApi* | [**get_domain_dns_records**](docs/DomainsApi.md#get_domain_dns_records) | **GET** /api/v1/domains/{fqdn}/dns-records | Получить информацию обо всех пользовательских DNS-записях домена или поддомена
*DomainsApi* | [**get_domain_name_servers**](docs/DomainsApi.md#get_domain_name_servers) | **GET** /api/v1/domains/{fqdn}/name-servers | Получение списка name-серверов домена
*DomainsApi* | [**get_domain_request**](docs/DomainsApi.md#get_domain_request) | **GET** /api/v1/domains-requests/{request_id} | Получение заявки на регистрацию/продление/трансфер домена
*DomainsApi* | [**get_domain_requests**](docs/DomainsApi.md#get_domain_requests) | **GET** /api/v1/domains-requests | Получение списка заявок на регистрацию/продление/трансфер домена
*DomainsApi* | [**get_domains**](docs/DomainsApi.md#get_domains) | **GET** /api/v1/domains | Получение списка всех доменов
*DomainsApi* | [**get_person**](docs/DomainsApi.md#get_person) | **GET** /api/v1/persons/{person_id} | Получение администратора доменов
*DomainsApi* | [**get_persons**](docs/DomainsApi.md#get_persons) | **GET** /api/v1/persons | Получение списка администраторов доменов
*DomainsApi* | [**get_tld**](docs/DomainsApi.md#get_tld) | **GET** /api/v1/tlds/{tld_id} | Получить информацию о доменной зоне по ID
*DomainsApi* | [**get_tlds**](docs/DomainsApi.md#get_tlds) | **GET** /api/v1/tlds | Получить информацию о доменных зонах
*DomainsApi* | [**update_domain_auto_prolongation**](docs/DomainsApi.md#update_domain_auto_prolongation) | **PATCH** /api/v1/domains/{fqdn} | Включение/выключение автопродления домена
*DomainsApi* | [**update_domain_dns_record**](docs/DomainsApi.md#update_domain_dns_record) | **PATCH** /api/v1/domains/{fqdn}/dns-records/{record_id} | Обновить информацию о DNS-записи домена или поддомена
*DomainsApi* | [**update_domain_dns_record_v2**](docs/DomainsApi.md#update_domain_dns_record_v2) | **PATCH** /api/v2/domains/{fqdn}/dns-records/{record_id} | Обновить информацию о DNS-записи домена или поддомена
*DomainsApi* | [**update_domain_name_servers**](docs/DomainsApi.md#update_domain_name_servers) | **PUT** /api/v1/domains/{fqdn}/name-servers | Изменение name-серверов домена
*DomainsApi* | [**update_domain_request**](docs/DomainsApi.md#update_domain_request) | **PATCH** /api/v1/domains-requests/{request_id} | Оплата/обновление заявки на регистрацию/продление/трансфер домена
*DomainsApi* | [**update_person**](docs/DomainsApi.md#update_person) | **PUT** /api/v1/persons/{person_id} | Обновление контактных данных администратора доменов
*FirewallApi* | [**add_resource_to_group**](docs/FirewallApi.md#add_resource_to_group) | **POST** /api/v1/firewall/groups/{group_id}/resources/{resource_id} | Линковка ресурса в firewall group
*FirewallApi* | [**create_group**](docs/FirewallApi.md#create_group) | **POST** /api/v1/firewall/groups | Создание группы правил
*FirewallApi* | [**create_group_rule**](docs/FirewallApi.md#create_group_rule) | **POST** /api/v1/firewall/groups/{group_id}/rules | Создание firewall правила
*FirewallApi* | [**delete_group**](docs/FirewallApi.md#delete_group) | **DELETE** /api/v1/firewall/groups/{group_id} | Удаление группы правил
*FirewallApi* | [**delete_group_rule**](docs/FirewallApi.md#delete_group_rule) | **DELETE** /api/v1/firewall/groups/{group_id}/rules/{rule_id} | Удаление firewall правила
*FirewallApi* | [**delete_resource_from_group**](docs/FirewallApi.md#delete_resource_from_group) | **DELETE** /api/v1/firewall/groups/{group_id}/resources/{resource_id} | Отлинковка ресурса из firewall group
*FirewallApi* | [**get_group**](docs/FirewallApi.md#get_group) | **GET** /api/v1/firewall/groups/{group_id} | Получение информации о группе правил
*FirewallApi* | [**get_group_resources**](docs/FirewallApi.md#get_group_resources) | **GET** /api/v1/firewall/groups/{group_id}/resources | Получение слинкованных ресурсов
*FirewallApi* | [**get_group_rule**](docs/FirewallApi.md#get_group_rule) | **GET** /api/v1/firewall/groups/{group_id}/rules/{rule_id} | Получение информации о правиле
*FirewallApi* | [**get_group_rules**](docs/FirewallApi.md#get_group_rules) | **GET** /api/v1/firewall/groups/{group_id}/rules | Получение списка правил
*FirewallApi* | [**get_groups**](docs/FirewallApi.md#get_groups) | **GET** /api/v1/firewall/groups | Получение групп правил
*FirewallApi* | [**get_rules_for_resource**](docs/FirewallApi.md#get_rules_for_resource) | **GET** /api/v1/firewall/service/{resource_type}/{resource_id} | Получение групп правил для ресурса
*FirewallApi* | [**update_group**](docs/FirewallApi.md#update_group) | **PATCH** /api/v1/firewall/groups/{group_id} | Обновление группы правил
*FirewallApi* | [**update_group_rule**](docs/FirewallApi.md#update_group_rule) | **PATCH** /api/v1/firewall/groups/{group_id}/rules/{rule_id} | Обновление firewall правила
*FloatingIPApi* | [**bind_floating_ip**](docs/FloatingIPApi.md#bind_floating_ip) | **POST** /api/v1/floating-ips/{floating_ip_id}/bind | Привязать IP к сервису
*FloatingIPApi* | [**create_floating_ip**](docs/FloatingIPApi.md#create_floating_ip) | **POST** /api/v1/floating-ips | Создание плавающего IP
*FloatingIPApi* | [**delete_floating_ip**](docs/FloatingIPApi.md#delete_floating_ip) | **DELETE** /api/v1/floating-ips/{floating_ip_id} | Удаление плавающего IP по ID
*FloatingIPApi* | [**get_floating_ip**](docs/FloatingIPApi.md#get_floating_ip) | **GET** /api/v1/floating-ips/{floating_ip_id} | Получение плавающего IP
*FloatingIPApi* | [**get_floating_ips**](docs/FloatingIPApi.md#get_floating_ips) | **GET** /api/v1/floating-ips | Получение списка плавающих IP
*FloatingIPApi* | [**unbind_floating_ip**](docs/FloatingIPApi.md#unbind_floating_ip) | **POST** /api/v1/floating-ips/{floating_ip_id}/unbind | Отвязать IP от сервиса
*FloatingIPApi* | [**update_floating_ip**](docs/FloatingIPApi.md#update_floating_ip) | **PATCH** /api/v1/floating-ips/{floating_ip_id} | Изменение плавающего IP по ID
*ImagesApi* | [**create_image**](docs/ImagesApi.md#create_image) | **POST** /api/v1/images | Создание образа
*ImagesApi* | [**create_image_download_url**](docs/ImagesApi.md#create_image_download_url) | **POST** /api/v1/images/{image_id}/download-url | Создание ссылки на скачивание образа
*ImagesApi* | [**delete_image**](docs/ImagesApi.md#delete_image) | **DELETE** /api/v1/images/{image_id} | Удаление образа
*ImagesApi* | [**delete_image_download_url**](docs/ImagesApi.md#delete_image_download_url) | **DELETE** /api/v1/images/{image_id}/download-url/{image_url_id} | Удаление ссылки на образ
*ImagesApi* | [**get_image**](docs/ImagesApi.md#get_image) | **GET** /api/v1/images/{image_id} | Получение информации о образе
*ImagesApi* | [**get_image_download_url**](docs/ImagesApi.md#get_image_download_url) | **GET** /api/v1/images/{image_id}/download-url/{image_url_id} | Получение информации о ссылке на скачивание образа
*ImagesApi* | [**get_image_download_urls**](docs/ImagesApi.md#get_image_download_urls) | **GET** /api/v1/images/{image_id}/download-url | Получение информации о ссылках на скачивание образов
*ImagesApi* | [**get_images**](docs/ImagesApi.md#get_images) | **GET** /api/v1/images | Получение списка образов
*ImagesApi* | [**update_image**](docs/ImagesApi.md#update_image) | **PATCH** /api/v1/images/{image_id} | Обновление информации о образе
*ImagesApi* | [**upload_image**](docs/ImagesApi.md#upload_image) | **POST** /api/v1/images/{image_id} | Загрузка образа
*KnowledgeBasesApi* | [**add_additional_token_package_to_knowledgebase**](docs/KnowledgeBasesApi.md#add_additional_token_package_to_knowledgebase) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/add-additional-token-package | Покупка дополнительных пакетов токенов
*KnowledgeBasesApi* | [**create_knowledgebase**](docs/KnowledgeBasesApi.md#create_knowledgebase) | **POST** /api/v1/cloud-ai/knowledge-bases | Создание базы знаний
*KnowledgeBasesApi* | [**create_knowledgebase_document**](docs/KnowledgeBasesApi.md#create_knowledgebase_document) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/documents | Добавление документа по ссылке
*KnowledgeBasesApi* | [**delete_document**](docs/KnowledgeBasesApi.md#delete_document) | **DELETE** /api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id} | Удаление документа из базы знаний
*KnowledgeBasesApi* | [**delete_knowledgebase**](docs/KnowledgeBasesApi.md#delete_knowledgebase) | **DELETE** /api/v1/cloud-ai/knowledge-bases/{id} | Удаление базы знаний
*KnowledgeBasesApi* | [**download_document**](docs/KnowledgeBasesApi.md#download_document) | **GET** /api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/download | Скачивание файла документа
*KnowledgeBasesApi* | [**get_knowledgebase**](docs/KnowledgeBasesApi.md#get_knowledgebase) | **GET** /api/v1/cloud-ai/knowledge-bases/{id} | Получение базы знаний со списком документов
*KnowledgeBasesApi* | [**get_knowledgebase_documents_v2**](docs/KnowledgeBasesApi.md#get_knowledgebase_documents_v2) | **GET** /api/v2/cloud-ai/knowledge-bases/{id}/documents | Получение списка документов базы знаний
*KnowledgeBasesApi* | [**get_knowledgebase_v3**](docs/KnowledgeBasesApi.md#get_knowledgebase_v3) | **GET** /api/v3/cloud-ai/knowledge-bases/{id} | Получение базы знаний
*KnowledgeBasesApi* | [**get_knowledgebases**](docs/KnowledgeBasesApi.md#get_knowledgebases) | **GET** /api/v1/cloud-ai/knowledge-bases | Получение списка баз знаний (v1)
*KnowledgeBasesApi* | [**get_knowledgebases_v2**](docs/KnowledgeBasesApi.md#get_knowledgebases_v2) | **GET** /api/v2/cloud-ai/knowledge-bases | Получение списка баз знаний (v2)
*KnowledgeBasesApi* | [**get_knowledgebases_v3**](docs/KnowledgeBasesApi.md#get_knowledgebases_v3) | **GET** /api/v3/cloud-ai/knowledge-bases | Получение списка баз знаний
*KnowledgeBasesApi* | [**link_knowledgebase_to_agent**](docs/KnowledgeBasesApi.md#link_knowledgebase_to_agent) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id} | Привязка базы знаний к агенту
*KnowledgeBasesApi* | [**reindex_document**](docs/KnowledgeBasesApi.md#reindex_document) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/reindex | Переиндексация документа
*KnowledgeBasesApi* | [**unlink_knowledgebase_from_agent**](docs/KnowledgeBasesApi.md#unlink_knowledgebase_from_agent) | **DELETE** /api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id} | Отвязка базы знаний от агента
*KnowledgeBasesApi* | [**update_knowledgebase**](docs/KnowledgeBasesApi.md#update_knowledgebase) | **PATCH** /api/v1/cloud-ai/knowledge-bases/{id} | Изменение базы знаний
*KnowledgeBasesApi* | [**update_knowledgebase_agent_link**](docs/KnowledgeBasesApi.md#update_knowledgebase_agent_link) | **PATCH** /api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id} | Изменение режима поиска по базе знаний для агента
*KnowledgeBasesApi* | [**update_knowledgebase_document**](docs/KnowledgeBasesApi.md#update_knowledgebase_document) | **PATCH** /api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id} | Изменение документа
*KnowledgeBasesApi* | [**upload_files_to_knowledgebase**](docs/KnowledgeBasesApi.md#upload_files_to_knowledgebase) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/upload | Загрузка файлов в базу знаний
*KubernetesApi* | [**create_cluster**](docs/KubernetesApi.md#create_cluster) | **POST** /api/v1/k8s/clusters | Создание кластера
*KubernetesApi* | [**create_cluster_node_group**](docs/KubernetesApi.md#create_cluster_node_group) | **POST** /api/v1/k8s/clusters/{cluster_id}/groups | Создание группы нод
*KubernetesApi* | [**delete_cluster**](docs/KubernetesApi.md#delete_cluster) | **DELETE** /api/v1/k8s/clusters/{cluster_id} | Удаление кластера
*KubernetesApi* | [**delete_cluster_node**](docs/KubernetesApi.md#delete_cluster_node) | **DELETE** /api/v1/k8s/clusters/{cluster_id}/nodes/{node_id} | Удаление ноды
*KubernetesApi* | [**delete_cluster_node_group**](docs/KubernetesApi.md#delete_cluster_node_group) | **DELETE** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id} | Удаление группы нод
*KubernetesApi* | [**delete_kubernetes_addons**](docs/KubernetesApi.md#delete_kubernetes_addons) | **DELETE** /api/v1/k8s/clusters/{cluster_id}/addons/{addon_id} | Удаление дополнения
*KubernetesApi* | [**get_cluster**](docs/KubernetesApi.md#get_cluster) | **GET** /api/v1/k8s/clusters/{cluster_id} | Получение информации о кластере
*KubernetesApi* | [**get_cluster_kubeconfig**](docs/KubernetesApi.md#get_cluster_kubeconfig) | **GET** /api/v1/k8s/clusters/{cluster_id}/kubeconfig | Получение файла kubeconfig
*KubernetesApi* | [**get_cluster_node_group**](docs/KubernetesApi.md#get_cluster_node_group) | **GET** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id} | Получение информации о группе нод
*KubernetesApi* | [**get_cluster_node_groups**](docs/KubernetesApi.md#get_cluster_node_groups) | **GET** /api/v1/k8s/clusters/{cluster_id}/groups | Получение групп нод кластера
*KubernetesApi* | [**get_cluster_nodes**](docs/KubernetesApi.md#get_cluster_nodes) | **GET** /api/v1/k8s/clusters/{cluster_id}/nodes | Получение списка нод
*KubernetesApi* | [**get_cluster_nodes_from_group**](docs/KubernetesApi.md#get_cluster_nodes_from_group) | **GET** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes | Получение списка нод, принадлежащих группе
*KubernetesApi* | [**get_cluster_resources**](docs/KubernetesApi.md#get_cluster_resources) | **GET** /api/v1/k8s/clusters/{cluster_id}/resources | Получение ресурсов кластера
*KubernetesApi* | [**get_clusters**](docs/KubernetesApi.md#get_clusters) | **GET** /api/v1/k8s/clusters | Получение списка кластеров
*KubernetesApi* | [**get_k8_s_network_drivers**](docs/KubernetesApi.md#get_k8_s_network_drivers) | **GET** /api/v1/k8s/network-drivers | Получение списка сетевых драйверов k8s
*KubernetesApi* | [**get_k8_s_versions**](docs/KubernetesApi.md#get_k8_s_versions) | **GET** /api/v1/k8s/k8s-versions | Получение списка версий k8s
*KubernetesApi* | [**get_kubernetes_addons**](docs/KubernetesApi.md#get_kubernetes_addons) | **GET** /api/v1/k8s/clusters/{cluster_id}/addons | Получение списка установленных дополнений
*KubernetesApi* | [**get_kubernetes_addons_config**](docs/KubernetesApi.md#get_kubernetes_addons_config) | **GET** /api/v1/k8s/clusters/{cluster_id}/addons-configs | Получение списка конфигураций дополнений
*KubernetesApi* | [**get_kubernetes_presets**](docs/KubernetesApi.md#get_kubernetes_presets) | **GET** /api/v1/presets/k8s | Получение списка тарифов
*KubernetesApi* | [**increase_count_of_nodes_in_group**](docs/KubernetesApi.md#increase_count_of_nodes_in_group) | **POST** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes | Увеличение количества нод в группе на указанное количество
*KubernetesApi* | [**post_kubernetes_addons**](docs/KubernetesApi.md#post_kubernetes_addons) | **POST** /api/v1/k8s/clusters/{cluster_id}/addons | Установка дополнения
*KubernetesApi* | [**post_kubernetes_addons_update**](docs/KubernetesApi.md#post_kubernetes_addons_update) | **POST** /api/v1/k8s/clusters/{cluster_id}/addons/{addon_id} | Изменение конфигурации дополнения
*KubernetesApi* | [**reduce_count_of_nodes_in_group**](docs/KubernetesApi.md#reduce_count_of_nodes_in_group) | **DELETE** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes | Уменьшение количества нод в группе на указанное количество
*KubernetesApi* | [**update_cluster**](docs/KubernetesApi.md#update_cluster) | **PATCH** /api/v1/k8s/clusters/{cluster_id} | Обновление информации о кластере
*KubernetesApi* | [**update_cluster_version**](docs/KubernetesApi.md#update_cluster_version) | **PATCH** /api/v1/k8s/clusters/{cluster_id}/versions/update | Обновление версии кластера
*LocationsApi* | [**get_locations**](docs/LocationsApi.md#get_locations) | **GET** /api/v2/locations | Получение списка локаций
*MCPApi* | [**delete_mcp_search_session**](docs/MCPApi.md#delete_mcp_search_session) | **DELETE** /api/v1/mcp/search | Завершение сессии сервера MCP с поиском инструментов
*MCPApi* | [**delete_mcp_session**](docs/MCPApi.md#delete_mcp_session) | **DELETE** /api/v1/mcp | Завершение сессии сервера MCP
*MCPApi* | [**open_mcp_search_stream**](docs/MCPApi.md#open_mcp_search_stream) | **GET** /api/v1/mcp/search | Открытие потока событий сервера MCP с поиском инструментов
*MCPApi* | [**open_mcp_stream**](docs/MCPApi.md#open_mcp_stream) | **GET** /api/v1/mcp | Открытие потока событий сервера MCP
*MCPApi* | [**send_mcp_message**](docs/MCPApi.md#send_mcp_message) | **POST** /api/v1/mcp | Отправка JSON-RPC-сообщения серверу MCP
*MCPApi* | [**send_mcp_search_message**](docs/MCPApi.md#send_mcp_search_message) | **POST** /api/v1/mcp/search | Отправка JSON-RPC-сообщения серверу MCP с поиском инструментов
*MailApi* | [**create_domain_mailbox**](docs/MailApi.md#create_domain_mailbox) | **POST** /api/v1/mail/domains/{domain} | Создание почтового ящика
*MailApi* | [**create_domain_mailbox_v2**](docs/MailApi.md#create_domain_mailbox_v2) | **POST** /api/v2/mail/domains/{domain} | Создание почтового ящика
*MailApi* | [**create_multiple_domain_mailboxes**](docs/MailApi.md#create_multiple_domain_mailboxes) | **POST** /api/v1/mail/domains/{domain}/batch | Множественное создание почтовых ящиков
*MailApi* | [**create_multiple_domain_mailboxes_v2**](docs/MailApi.md#create_multiple_domain_mailboxes_v2) | **POST** /api/v2/mail/domains/{domain}/batch | Множественное создание почтовых ящиков
*MailApi* | [**delete_mailbox**](docs/MailApi.md#delete_mailbox) | **DELETE** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Удаление почтового ящика
*MailApi* | [**get_all_mailboxes_v2**](docs/MailApi.md#get_all_mailboxes_v2) | **GET** /api/v2/mail | Получение списка всех почтовых ящиков аккаунта
*MailApi* | [**get_domain_mail_info**](docs/MailApi.md#get_domain_mail_info) | **GET** /api/v1/mail/domains/{domain}/info | Получение почтовой информации о домене
*MailApi* | [**get_domain_mailboxes**](docs/MailApi.md#get_domain_mailboxes) | **GET** /api/v1/mail/domains/{domain} | Получение списка почтовых ящиков домена
*MailApi* | [**get_mailbox**](docs/MailApi.md#get_mailbox) | **GET** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Получение почтового ящика
*MailApi* | [**get_mailbox_v2**](docs/MailApi.md#get_mailbox_v2) | **GET** /api/v2/mail/domains/{domain}/mailboxes/{mailbox} | Получение почтового ящика
*MailApi* | [**get_mailboxes**](docs/MailApi.md#get_mailboxes) | **GET** /api/v1/mail | Получение списка почтовых ящиков аккаунта
*MailApi* | [**update_domain_mail_info**](docs/MailApi.md#update_domain_mail_info) | **PATCH** /api/v1/mail/domains/{domain}/info | Изменение почтовой информации о домене
*MailApi* | [**update_mailbox**](docs/MailApi.md#update_mailbox) | **PATCH** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Изменение почтового ящика
*MailApi* | [**update_mailbox_v2**](docs/MailApi.md#update_mailbox_v2) | **PATCH** /api/v2/mail/domains/{domain}/mailboxes/{mailbox} | Изменение почтового ящика
*NetworkDrivesApi* | [**create_network_drive**](docs/NetworkDrivesApi.md#create_network_drive) | **POST** /api/v1/network-drives | Создание сетевого диска
*NetworkDrivesApi* | [**delete_network_drive**](docs/NetworkDrivesApi.md#delete_network_drive) | **DELETE** /api/v1/network-drives/{network_drive_id} | Удаление сетевого диска по идентификатору
*NetworkDrivesApi* | [**get_network_drive**](docs/NetworkDrivesApi.md#get_network_drive) | **GET** /api/v1/network-drives/{network_drive_id} | Получение сетевого диска
*NetworkDrivesApi* | [**get_network_drives**](docs/NetworkDrivesApi.md#get_network_drives) | **GET** /api/v1/network-drives | Получение списка cетевых дисков
*NetworkDrivesApi* | [**get_network_drives_available_resources**](docs/NetworkDrivesApi.md#get_network_drives_available_resources) | **GET** /api/v1/network-drives/available-resources | Получение списка сервисов доступных для подключения диска
*NetworkDrivesApi* | [**get_network_drives_presets**](docs/NetworkDrivesApi.md#get_network_drives_presets) | **GET** /api/v1/presets/network-drives | Получение списка доступных тарифов для сетевого диска
*NetworkDrivesApi* | [**mount_network_drive**](docs/NetworkDrivesApi.md#mount_network_drive) | **POST** /api/v1/network-drives/{network_drive_id}/mount | Подключить сетевой диск к сервису
*NetworkDrivesApi* | [**unmount_network_drive**](docs/NetworkDrivesApi.md#unmount_network_drive) | **POST** /api/v1/network-drives/{network_drive_id}/unmount | Отключить сетевой диск от сервиса
*NetworkDrivesApi* | [**update_network_drive**](docs/NetworkDrivesApi.md#update_network_drive) | **PATCH** /api/v1/network-drives/{network_drive_id} | Изменение сетевого диска по ID
*PaymentsApi* | [**get_finances**](docs/PaymentsApi.md#get_finances) | **GET** /api/v1/account/finances | Получение платежной информации
*PaymentsApi* | [**get_service_prices**](docs/PaymentsApi.md#get_service_prices) | **GET** /api/v1/account/services/cost | Получение стоимости сервисов
*ProjectsApi* | [**add_balancer_to_project**](docs/ProjectsApi.md#add_balancer_to_project) | **POST** /api/v1/projects/{project_id}/resources/balancers | Добавление балансировщика в проект
*ProjectsApi* | [**add_cluster_to_project**](docs/ProjectsApi.md#add_cluster_to_project) | **POST** /api/v1/projects/{project_id}/resources/clusters | Добавление кластера в проект
*ProjectsApi* | [**add_database_to_project**](docs/ProjectsApi.md#add_database_to_project) | **POST** /api/v1/projects/{project_id}/resources/databases | Добавление базы данных в проект
*ProjectsApi* | [**add_dedicated_server_to_project**](docs/ProjectsApi.md#add_dedicated_server_to_project) | **POST** /api/v1/projects/{project_id}/resources/dedicated | Добавление выделенного сервера в проект
*ProjectsApi* | [**add_server_to_project**](docs/ProjectsApi.md#add_server_to_project) | **POST** /api/v1/projects/{project_id}/resources/servers | Добавление сервера в проект
*ProjectsApi* | [**add_storage_to_project**](docs/ProjectsApi.md#add_storage_to_project) | **POST** /api/v1/projects/{project_id}/resources/buckets | Добавление хранилища в проект
*ProjectsApi* | [**create_project**](docs/ProjectsApi.md#create_project) | **POST** /api/v1/projects | Создание проекта
*ProjectsApi* | [**delete_project**](docs/ProjectsApi.md#delete_project) | **DELETE** /api/v1/projects/{project_id} | Удаление проекта
*ProjectsApi* | [**get_account_balancers**](docs/ProjectsApi.md#get_account_balancers) | **GET** /api/v1/projects/resources/balancers | Получение списка всех балансировщиков на аккаунте
*ProjectsApi* | [**get_account_clusters**](docs/ProjectsApi.md#get_account_clusters) | **GET** /api/v1/projects/resources/clusters | Получение списка всех кластеров на аккаунте
*ProjectsApi* | [**get_account_databases**](docs/ProjectsApi.md#get_account_databases) | **GET** /api/v1/projects/resources/databases | Получение списка всех баз данных на аккаунте
*ProjectsApi* | [**get_account_dedicated_servers**](docs/ProjectsApi.md#get_account_dedicated_servers) | **GET** /api/v1/projects/resources/dedicated | Получение списка всех выделенных серверов на аккаунте
*ProjectsApi* | [**get_account_servers**](docs/ProjectsApi.md#get_account_servers) | **GET** /api/v1/projects/resources/servers | Получение списка всех серверов на аккаунте
*ProjectsApi* | [**get_account_storages**](docs/ProjectsApi.md#get_account_storages) | **GET** /api/v1/projects/resources/buckets | Получение списка всех хранилищ на аккаунте
*ProjectsApi* | [**get_all_project_resources**](docs/ProjectsApi.md#get_all_project_resources) | **GET** /api/v1/projects/{project_id}/resources | Получение всех ресурсов проекта
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /api/v1/projects/{project_id} | Получение проекта по ID
*ProjectsApi* | [**get_project_balancers**](docs/ProjectsApi.md#get_project_balancers) | **GET** /api/v1/projects/{project_id}/resources/balancers | Получение списка балансировщиков проекта
*ProjectsApi* | [**get_project_clusters**](docs/ProjectsApi.md#get_project_clusters) | **GET** /api/v1/projects/{project_id}/resources/clusters | Получение списка кластеров проекта
*ProjectsApi* | [**get_project_databases**](docs/ProjectsApi.md#get_project_databases) | **GET** /api/v1/projects/{project_id}/resources/databases | Получение списка баз данных проекта
*ProjectsApi* | [**get_project_dedicated_servers**](docs/ProjectsApi.md#get_project_dedicated_servers) | **GET** /api/v1/projects/{project_id}/resources/dedicated | Получение списка выделенных серверов проекта
*ProjectsApi* | [**get_project_servers**](docs/ProjectsApi.md#get_project_servers) | **GET** /api/v1/projects/{project_id}/resources/servers | Получение списка серверов проекта
*ProjectsApi* | [**get_project_storages**](docs/ProjectsApi.md#get_project_storages) | **GET** /api/v1/projects/{project_id}/resources/buckets | Получение списка хранилищ проекта
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /api/v1/projects | Получение списка проектов
*ProjectsApi* | [**transfer_resource_to_another_project**](docs/ProjectsApi.md#transfer_resource_to_another_project) | **PUT** /api/v1/projects/{project_id}/resources/transfer | Перенести ресурс в другой проект
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /api/v1/projects/{project_id} | Изменение проекта
*RoutersApi* | [**add_networks**](docs/RoutersApi.md#add_networks) | **POST** /api/v1/routers/{router_id}/networks | Подключение сетей к роутеру
*RoutersApi* | [**create_router**](docs/RoutersApi.md#create_router) | **POST** /api/v1/routers | Создание роутера
*RoutersApi* | [**delete_dnat**](docs/RoutersApi.md#delete_dnat) | **DELETE** /api/v1/routers/{router_id}/dnat-rules/{dnat_id} | Удаление правила проброса портов
*RoutersApi* | [**delete_router**](docs/RoutersApi.md#delete_router) | **DELETE** /api/v1/routers/{router_id} | Удаление роутера
*RoutersApi* | [**delete_router_nat**](docs/RoutersApi.md#delete_router_nat) | **DELETE** /api/v1/routers/{router_id}/networks/{network_name}/nat | Выключение NAT для сети
*RoutersApi* | [**delete_router_network**](docs/RoutersApi.md#delete_router_network) | **DELETE** /api/v1/routers/{router_id}/networks/{network_name} | Удаление сети из роутера
*RoutersApi* | [**delete_static_route**](docs/RoutersApi.md#delete_static_route) | **DELETE** /api/v1/routers/{router_id}/static-routes/{static_route_id} | Удаление статического маршрута
*RoutersApi* | [**get_available_static_routes**](docs/RoutersApi.md#get_available_static_routes) | **GET** /api/v1/routers/{router_id}/static-routes/available | Получение доступных подсетей для статических маршрутов
*RoutersApi* | [**get_dnat**](docs/RoutersApi.md#get_dnat) | **GET** /api/v1/routers/{router_id}/dnat-rules | Получение списка правил проброса портов
*RoutersApi* | [**get_dnat_rule**](docs/RoutersApi.md#get_dnat_rule) | **GET** /api/v1/routers/{router_id}/dnat-rules/{dnat_id} | Получение правила проброса портов
*RoutersApi* | [**get_networks**](docs/RoutersApi.md#get_networks) | **GET** /api/v1/routers/{router_id}/networks | Получение списка сетей роутера
*RoutersApi* | [**get_router**](docs/RoutersApi.md#get_router) | **GET** /api/v1/routers/{router_id} | Получение информации о роутере
*RoutersApi* | [**get_router_available_networks**](docs/RoutersApi.md#get_router_available_networks) | **GET** /api/v1/routers/networks/available | Получение списка доступных сетей
*RoutersApi* | [**get_router_presets**](docs/RoutersApi.md#get_router_presets) | **GET** /api/v1/presets/routers | Получение списка тарифов роутеров
*RoutersApi* | [**get_router_statistics**](docs/RoutersApi.md#get_router_statistics) | **GET** /api/v1/routers/{router_id}/statistics/{time_from}/{period}/{keys} | Получение статистики роутера
*RoutersApi* | [**get_routers**](docs/RoutersApi.md#get_routers) | **GET** /api/v1/routers | Получение списка роутеров
*RoutersApi* | [**get_static_routes**](docs/RoutersApi.md#get_static_routes) | **GET** /api/v1/routers/{router_id}/static-routes | Получение списка статических маршрутов
*RoutersApi* | [**patch_network**](docs/RoutersApi.md#patch_network) | **PATCH** /api/v1/routers/{router_id}/networks/{network_name} | Обновление информации о сети
*RoutersApi* | [**patch_networks**](docs/RoutersApi.md#patch_networks) | **PATCH** /api/v1/routers/{router_id}/networks | Обновление сетей роутера
*RoutersApi* | [**post_dnat**](docs/RoutersApi.md#post_dnat) | **POST** /api/v1/routers/{router_id}/dnat-rules | Добавление правила проброса портов
*RoutersApi* | [**post_static_route**](docs/RoutersApi.md#post_static_route) | **POST** /api/v1/routers/{router_id}/static-routes | Добавление статического маршрута
*RoutersApi* | [**update_router**](docs/RoutersApi.md#update_router) | **PATCH** /api/v1/routers/{router_id} | Обновление информации о роутере
*RoutersApi* | [**update_router_nat**](docs/RoutersApi.md#update_router_nat) | **PATCH** /api/v1/routers/{router_id}/networks/{network_name}/nat | Включение NAT для сети
*S3Api* | [**add_storage_subdomain_certificate**](docs/S3Api.md#add_storage_subdomain_certificate) | **POST** /api/v1/storages/certificates/generate | Добавление сертификата для поддомена хранилища
*S3Api* | [**add_storage_subdomains**](docs/S3Api.md#add_storage_subdomains) | **POST** /api/v1/storages/buckets/{bucket_id}/subdomains | Добавление поддоменов для хранилища
*S3Api* | [**create_storage**](docs/S3Api.md#create_storage) | **POST** /api/v1/storages/buckets | Создание хранилища
*S3Api* | [**delete_storage**](docs/S3Api.md#delete_storage) | **DELETE** /api/v1/storages/buckets/{bucket_id} | Удаление хранилища на аккаунте
*S3Api* | [**delete_storage_subdomains**](docs/S3Api.md#delete_storage_subdomains) | **DELETE** /api/v1/storages/buckets/{bucket_id}/subdomains | Удаление поддоменов хранилища
*S3Api* | [**get_storage**](docs/S3Api.md#get_storage) | **GET** /api/v1/storages/buckets/{bucket_id} | Получение хранилища по ID
*S3Api* | [**get_storage_subdomains**](docs/S3Api.md#get_storage_subdomains) | **GET** /api/v1/storages/buckets/{bucket_id}/subdomains | Получение списка поддоменов хранилища
*S3Api* | [**get_storage_transfer_status**](docs/S3Api.md#get_storage_transfer_status) | **GET** /api/v1/storages/buckets/{bucket_id}/transfer-status | Получение статуса переноса хранилища от стороннего S3 в Timeweb Cloud
*S3Api* | [**get_storage_users**](docs/S3Api.md#get_storage_users) | **GET** /api/v1/storages/users | Получение списка пользователей хранилищ аккаунта
*S3Api* | [**get_storages**](docs/S3Api.md#get_storages) | **GET** /api/v1/storages/buckets | Получение списка хранилищ аккаунта
*S3Api* | [**get_storages_presets**](docs/S3Api.md#get_storages_presets) | **GET** /api/v1/presets/storages | Получение списка тарифов для хранилищ
*S3Api* | [**transfer_storage**](docs/S3Api.md#transfer_storage) | **POST** /api/v1/storages/transfer | Перенос хранилища от стороннего провайдера S3 в Timeweb Cloud
*S3Api* | [**update_storage**](docs/S3Api.md#update_storage) | **PATCH** /api/v1/storages/buckets/{bucket_id} | Изменение хранилища на аккаунте
*S3Api* | [**update_storage_user**](docs/S3Api.md#update_storage_user) | **PATCH** /api/v1/storages/users/{user_id} | Изменение пароля пользователя-администратора хранилища
*SSHApi* | [**add_key_to_server**](docs/SSHApi.md#add_key_to_server) | **POST** /api/v1/servers/{server_id}/ssh-keys | Добавление SSH-ключей на сервер
*SSHApi* | [**create_key**](docs/SSHApi.md#create_key) | **POST** /api/v1/ssh-keys | Создание SSH-ключа
*SSHApi* | [**delete_key**](docs/SSHApi.md#delete_key) | **DELETE** /api/v1/ssh-keys/{ssh_key_id} | Удаление SSH-ключа по ID
*SSHApi* | [**delete_key_from_server**](docs/SSHApi.md#delete_key_from_server) | **DELETE** /api/v1/servers/{server_id}/ssh-keys/{ssh_key_id} | Удаление SSH-ключей с сервера
*SSHApi* | [**get_key**](docs/SSHApi.md#get_key) | **GET** /api/v1/ssh-keys/{ssh_key_id} | Получение SSH-ключа по ID
*SSHApi* | [**get_keys**](docs/SSHApi.md#get_keys) | **GET** /api/v1/ssh-keys | Получение списка SSH-ключей
*SSHApi* | [**update_key**](docs/SSHApi.md#update_key) | **PATCH** /api/v1/ssh-keys/{ssh_key_id} | Изменение SSH-ключа по ID
*ServersApi* | [**add_server_ip**](docs/ServersApi.md#add_server_ip) | **POST** /api/v1/servers/{server_id}/ips | Добавление IP-адреса сервера
*ServersApi* | [**clone_server**](docs/ServersApi.md#clone_server) | **POST** /api/v1/servers/{server_id}/clone | Клонирование сервера
*ServersApi* | [**commit_restore_point**](docs/ServersApi.md#commit_restore_point) | **POST** /api/v1/restore-points/{vds_id}/commit | Фиксация снапшота
*ServersApi* | [**create_restore_point**](docs/ServersApi.md#create_restore_point) | **POST** /api/v1/restore-points/{vds_id}/create | Создание снапшота
*ServersApi* | [**create_server**](docs/ServersApi.md#create_server) | **POST** /api/v1/servers | Создание сервера
*ServersApi* | [**create_server_disk**](docs/ServersApi.md#create_server_disk) | **POST** /api/v1/servers/{server_id}/disks | Создание диска сервера
*ServersApi* | [**create_server_disk_backup**](docs/ServersApi.md#create_server_disk_backup) | **POST** /api/v1/servers/{server_id}/disks/{disk_id}/backups | Создание бэкапа диска сервера
*ServersApi* | [**create_server_disk_backup_download_url**](docs/ServersApi.md#create_server_disk_backup_download_url) | **POST** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id}/download-url | Получение ссылки для скачивания бэкапа диска сервера
*ServersApi* | [**delete_server**](docs/ServersApi.md#delete_server) | **DELETE** /api/v1/servers/{server_id} | Удаление сервера
*ServersApi* | [**delete_server_disk**](docs/ServersApi.md#delete_server_disk) | **DELETE** /api/v1/servers/{server_id}/disks/{disk_id} | Удаление диска сервера
*ServersApi* | [**delete_server_disk_backup**](docs/ServersApi.md#delete_server_disk_backup) | **DELETE** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id} | Удаление бэкапа диска сервера
*ServersApi* | [**delete_server_ip**](docs/ServersApi.md#delete_server_ip) | **DELETE** /api/v1/servers/{server_id}/ips | Удаление IP-адреса сервера
*ServersApi* | [**get_configurators**](docs/ServersApi.md#get_configurators) | **GET** /api/v1/configurator/servers | Получение списка конфигураторов серверов
*ServersApi* | [**get_os_list**](docs/ServersApi.md#get_os_list) | **GET** /api/v1/os/servers | Получение списка операционных систем
*ServersApi* | [**get_restore_point**](docs/ServersApi.md#get_restore_point) | **GET** /api/v1/restore-points/{vds_id} | Получение снапшота сервера
*ServersApi* | [**get_restore_points**](docs/ServersApi.md#get_restore_points) | **GET** /api/v1/restore-points | Получение списка снапшотов
*ServersApi* | [**get_server**](docs/ServersApi.md#get_server) | **GET** /api/v1/servers/{server_id} | Получение сервера
*ServersApi* | [**get_server_disk**](docs/ServersApi.md#get_server_disk) | **GET** /api/v1/servers/{server_id}/disks/{disk_id} | Получение диска сервера
*ServersApi* | [**get_server_disk_auto_backup_settings**](docs/ServersApi.md#get_server_disk_auto_backup_settings) | **GET** /api/v1/servers/{server_id}/disks/{disk_id}/auto-backups | Получить настройки автобэкапов диска сервера
*ServersApi* | [**get_server_disk_backup**](docs/ServersApi.md#get_server_disk_backup) | **GET** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id} | Получение бэкапа диска сервера
*ServersApi* | [**get_server_disk_backups**](docs/ServersApi.md#get_server_disk_backups) | **GET** /api/v1/servers/{server_id}/disks/{disk_id}/backups | Получение списка бэкапов диска сервера
*ServersApi* | [**get_server_disks**](docs/ServersApi.md#get_server_disks) | **GET** /api/v1/servers/{server_id}/disks | Получение списка дисков сервера
*ServersApi* | [**get_server_ips**](docs/ServersApi.md#get_server_ips) | **GET** /api/v1/servers/{server_id}/ips | Получение списка IP-адресов сервера
*ServersApi* | [**get_server_logs**](docs/ServersApi.md#get_server_logs) | **GET** /api/v1/servers/{server_id}/logs | Получение списка логов сервера
*ServersApi* | [**get_server_statistics**](docs/ServersApi.md#get_server_statistics) | **GET** /api/v1/servers/{server_id}/statistics | Получение статистики сервера
*ServersApi* | [**get_server_statistics_new**](docs/ServersApi.md#get_server_statistics_new) | **GET** /api/v1/servers/{server_id}/statistics/{time_from}/{period}/{keys} | Получение статистики сервера
*ServersApi* | [**get_servers**](docs/ServersApi.md#get_servers) | **GET** /api/v1/servers | Получение списка серверов
*ServersApi* | [**get_servers_presets**](docs/ServersApi.md#get_servers_presets) | **GET** /api/v1/presets/servers | Получение списка тарифов серверов
*ServersApi* | [**get_software**](docs/ServersApi.md#get_software) | **GET** /api/v1/software/servers | Получение списка ПО из маркетплейса
*ServersApi* | [**hard_shutdown_server**](docs/ServersApi.md#hard_shutdown_server) | **POST** /api/v1/servers/{server_id}/hard-shutdown | Принудительное выключение сервера
*ServersApi* | [**image_unmount_and_server_reload**](docs/ServersApi.md#image_unmount_and_server_reload) | **POST** /api/v1/servers/{server_id}/image-unmount | Отмонтирование ISO образа и перезагрузка сервера
*ServersApi* | [**perform_action_on_backup**](docs/ServersApi.md#perform_action_on_backup) | **POST** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id}/action | Выполнение действия над бэкапом диска сервера
*ServersApi* | [**perform_action_on_server**](docs/ServersApi.md#perform_action_on_server) | **POST** /api/v1/servers/{server_id}/action | Выполнение действия над сервером
*ServersApi* | [**reboot_server**](docs/ServersApi.md#reboot_server) | **POST** /api/v1/servers/{server_id}/reboot | Перезагрузка сервера
*ServersApi* | [**reboot_server_hard**](docs/ServersApi.md#reboot_server_hard) | **POST** /api/v1/servers/{server_id}/hard-reboot | Принудительная перезагрузка сервера
*ServersApi* | [**reset_server_password**](docs/ServersApi.md#reset_server_password) | **POST** /api/v1/servers/{server_id}/reset-password | Сброс пароля сервера
*ServersApi* | [**rollback_restore_point**](docs/ServersApi.md#rollback_restore_point) | **POST** /api/v1/restore-points/{vds_id}/rollback | Откат к снапшоту
*ServersApi* | [**shutdown_server**](docs/ServersApi.md#shutdown_server) | **POST** /api/v1/servers/{server_id}/shutdown | Выключение сервера
*ServersApi* | [**start_server**](docs/ServersApi.md#start_server) | **POST** /api/v1/servers/{server_id}/start | Запуск сервера
*ServersApi* | [**update_server**](docs/ServersApi.md#update_server) | **PATCH** /api/v1/servers/{server_id} | Изменение сервера
*ServersApi* | [**update_server_disk**](docs/ServersApi.md#update_server_disk) | **PATCH** /api/v1/servers/{server_id}/disks/{disk_id} | Изменение параметров диска сервера
*ServersApi* | [**update_server_disk_auto_backup_settings**](docs/ServersApi.md#update_server_disk_auto_backup_settings) | **PATCH** /api/v1/servers/{server_id}/disks/{disk_id}/auto-backups | Изменение настроек автобэкапов диска сервера
*ServersApi* | [**update_server_disk_backup**](docs/ServersApi.md#update_server_disk_backup) | **PATCH** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id} | Изменение бэкапа диска сервера
*ServersApi* | [**update_server_ip**](docs/ServersApi.md#update_server_ip) | **PATCH** /api/v1/servers/{server_id}/ips | Изменение IP-адреса сервера
*ServersApi* | [**update_server_nat**](docs/ServersApi.md#update_server_nat) | **PATCH** /api/v1/servers/{server_id}/local-networks/nat-mode | Изменение правил маршрутизации трафика сервера (NAT)
*ServersApi* | [**update_server_os_boot_mode**](docs/ServersApi.md#update_server_os_boot_mode) | **POST** /api/v1/servers/{server_id}/boot-mode | Выбор типа загрузки операционной системы сервера
*VPCApi* | [**create_vpc**](docs/VPCApi.md#create_vpc) | **POST** /api/v2/vpcs | Создание VPC
*VPCApi* | [**delete_vpc**](docs/VPCApi.md#delete_vpc) | **DELETE** /api/v1/vpcs/{vpc_id} | Удаление VPC по ID сети
*VPCApi* | [**get_vpc**](docs/VPCApi.md#get_vpc) | **GET** /api/v2/vpcs/{vpc_id} | Получение VPC
*VPCApi* | [**get_vpc_ports**](docs/VPCApi.md#get_vpc_ports) | **GET** /api/v1/vpcs/{vpc_id}/ports | Получение списка портов для VPC
*VPCApi* | [**get_vpc_services**](docs/VPCApi.md#get_vpc_services) | **GET** /api/v2/vpcs/{vpc_id}/services | Получение списка сервисов в VPC
*VPCApi* | [**get_vpcs**](docs/VPCApi.md#get_vpcs) | **GET** /api/v2/vpcs | Получение списка VPCs
*VPCApi* | [**update_vpcs**](docs/VPCApi.md#update_vpcs) | **PATCH** /api/v2/vpcs/{vpc_id} | Изменение VPC по ID сети


## Documentation For Models

 - [AddAiSolutionTelegramBot201Response](docs/AddAiSolutionTelegramBot201Response.md)
 - [AddBalancerToProject200Response](docs/AddBalancerToProject200Response.md)
 - [AddBalancerToProjectRequest](docs/AddBalancerToProjectRequest.md)
 - [AddBitbucket](docs/AddBitbucket.md)
 - [AddCertificate](docs/AddCertificate.md)
 - [AddClusterToProjectRequest](docs/AddClusterToProjectRequest.md)
 - [AddCountries](docs/AddCountries.md)
 - [AddCountriesToAllowedList201Response](docs/AddCountriesToAllowedList201Response.md)
 - [AddCountriesToAllowedListRequest](docs/AddCountriesToAllowedListRequest.md)
 - [AddDatabaseToProjectRequest](docs/AddDatabaseToProjectRequest.md)
 - [AddDedicatedServerToProjectRequest](docs/AddDedicatedServerToProjectRequest.md)
 - [AddGit](docs/AddGit.md)
 - [AddGithub](docs/AddGithub.md)
 - [AddGitlab](docs/AddGitlab.md)
 - [AddIPsToAllowedList201Response](docs/AddIPsToAllowedList201Response.md)
 - [AddIPsToAllowedListRequest](docs/AddIPsToAllowedListRequest.md)
 - [AddIPsToBalancerRequest](docs/AddIPsToBalancerRequest.md)
 - [AddIps](docs/AddIps.md)
 - [AddKeyToServerRequest](docs/AddKeyToServerRequest.md)
 - [AddProvider201Response](docs/AddProvider201Response.md)
 - [AddServerIP201Response](docs/AddServerIP201Response.md)
 - [AddServerIPRequest](docs/AddServerIPRequest.md)
 - [AddServerToProjectRequest](docs/AddServerToProjectRequest.md)
 - [AddStorageSubdomainCertificateRequest](docs/AddStorageSubdomainCertificateRequest.md)
 - [AddStorageSubdomains200Response](docs/AddStorageSubdomains200Response.md)
 - [AddStorageSubdomainsRequest](docs/AddStorageSubdomainsRequest.md)
 - [AddStorageToProjectRequest](docs/AddStorageToProjectRequest.md)
 - [AddSubdomain201Response](docs/AddSubdomain201Response.md)
 - [AddTokenPackage](docs/AddTokenPackage.md)
 - [AddedSubdomain](docs/AddedSubdomain.md)
 - [AddonConfigOut](docs/AddonConfigOut.md)
 - [AddonOut](docs/AddonOut.md)
 - [AddonsConfigResponse](docs/AddonsConfigResponse.md)
 - [AddonsResponse](docs/AddonsResponse.md)
 - [Agent](docs/Agent.md)
 - [AgentAdditionalModel](docs/AgentAdditionalModel.md)
 - [AgentEntityLimit](docs/AgentEntityLimit.md)
 - [AgentModelSettings](docs/AgentModelSettings.md)
 - [AgentSettings](docs/AgentSettings.md)
 - [AgentSkill](docs/AgentSkill.md)
 - [AgentTokenStatistic](docs/AgentTokenStatistic.md)
 - [AgentV3](docs/AgentV3.md)
 - [AgentWidgetSettings](docs/AgentWidgetSettings.md)
 - [AiGatewayBatch](docs/AiGatewayBatch.md)
 - [AiGatewayBatchCreateRequest](docs/AiGatewayBatchCreateRequest.md)
 - [AiGatewayBatchList](docs/AiGatewayBatchList.md)
 - [AiGatewayBatchRequestCounts](docs/AiGatewayBatchRequestCounts.md)
 - [AiGatewayChatCompletion](docs/AiGatewayChatCompletion.md)
 - [AiGatewayChatCompletionChunk](docs/AiGatewayChatCompletionChunk.md)
 - [AiGatewayChatCompletionRequest](docs/AiGatewayChatCompletionRequest.md)
 - [AiGatewayChatCompletionRequestStreamOptions](docs/AiGatewayChatCompletionRequestStreamOptions.md)
 - [AiGatewayChatMessage](docs/AiGatewayChatMessage.md)
 - [AiGatewayCompletion](docs/AiGatewayCompletion.md)
 - [AiGatewayCompletionRequest](docs/AiGatewayCompletionRequest.md)
 - [AiGatewayEmbeddingList](docs/AiGatewayEmbeddingList.md)
 - [AiGatewayEmbeddingListUsage](docs/AiGatewayEmbeddingListUsage.md)
 - [AiGatewayEmbeddingRequest](docs/AiGatewayEmbeddingRequest.md)
 - [AiGatewayError](docs/AiGatewayError.md)
 - [AiGatewayErrorError](docs/AiGatewayErrorError.md)
 - [AiGatewayFile](docs/AiGatewayFile.md)
 - [AiGatewayFileDeleted](docs/AiGatewayFileDeleted.md)
 - [AiGatewayImageGenerationRequest](docs/AiGatewayImageGenerationRequest.md)
 - [AiGatewayImagesResponse](docs/AiGatewayImagesResponse.md)
 - [AiGatewayModel](docs/AiGatewayModel.md)
 - [AiGatewayModelList](docs/AiGatewayModelList.md)
 - [AiGatewayResponse](docs/AiGatewayResponse.md)
 - [AiGatewayResponseCreateRequest](docs/AiGatewayResponseCreateRequest.md)
 - [AiGatewayResponseCreateRequestReasoning](docs/AiGatewayResponseCreateRequestReasoning.md)
 - [AiGatewayResponseDeleted](docs/AiGatewayResponseDeleted.md)
 - [AiGatewayResponseIncompleteDetails](docs/AiGatewayResponseIncompleteDetails.md)
 - [AiGatewayResponseUsage](docs/AiGatewayResponseUsage.md)
 - [AiGatewaySpeechRequest](docs/AiGatewaySpeechRequest.md)
 - [AiGatewayToolCall](docs/AiGatewayToolCall.md)
 - [AiGatewayToolCallFunction](docs/AiGatewayToolCallFunction.md)
 - [AiGatewayTranscription](docs/AiGatewayTranscription.md)
 - [AiGatewayUsage](docs/AiGatewayUsage.md)
 - [AiGatewayUsageCompletionTokensDetails](docs/AiGatewayUsageCompletionTokensDetails.md)
 - [AiGatewayUsagePromptTokensDetails](docs/AiGatewayUsagePromptTokensDetails.md)
 - [AiGatewayValidationError](docs/AiGatewayValidationError.md)
 - [AiKey](docs/AiKey.md)
 - [AiKeyCallsStatisticPoint](docs/AiKeyCallsStatisticPoint.md)
 - [AiKeyLimit](docs/AiKeyLimit.md)
 - [AiKeyTokenStatisticPoint](docs/AiKeyTokenStatisticPoint.md)
 - [AiProvider](docs/AiProvider.md)
 - [AiSolution](docs/AiSolution.md)
 - [AiSolutionAiKey](docs/AiSolutionAiKey.md)
 - [AiSolutionChatMessage](docs/AiSolutionChatMessage.md)
 - [AiSolutionChatReply](docs/AiSolutionChatReply.md)
 - [AiSolutionChatStatus](docs/AiSolutionChatStatus.md)
 - [AiSolutionConversation](docs/AiSolutionConversation.md)
 - [AiSolutionTelegramBot](docs/AiSolutionTelegramBot.md)
 - [AiSolutionType](docs/AiSolutionType.md)
 - [AiSolutionTypeRequirements](docs/AiSolutionTypeRequirements.md)
 - [App](docs/App.md)
 - [AppConfiguration](docs/AppConfiguration.md)
 - [AppDiskStatus](docs/AppDiskStatus.md)
 - [AppProvider](docs/AppProvider.md)
 - [ApproveTelegramPairing](docs/ApproveTelegramPairing.md)
 - [AppsPresets](docs/AppsPresets.md)
 - [AuthorizeUrl](docs/AuthorizeUrl.md)
 - [AutoBackup](docs/AutoBackup.md)
 - [AutoReplyIsDisabled](docs/AutoReplyIsDisabled.md)
 - [AutoReplyIsEnabled](docs/AutoReplyIsEnabled.md)
 - [AutoreplyIsDisabled](docs/AutoreplyIsDisabled.md)
 - [AutoreplyIsEnabled](docs/AutoreplyIsEnabled.md)
 - [AvailabilityZone](docs/AvailabilityZone.md)
 - [AvailableFrameworks](docs/AvailableFrameworks.md)
 - [AvailableNetwork](docs/AvailableNetwork.md)
 - [AvailableNetworksResponse](docs/AvailableNetworksResponse.md)
 - [AvailableStaticRoute](docs/AvailableStaticRoute.md)
 - [AvailableStaticRoutesResponse](docs/AvailableStaticRoutesResponse.md)
 - [Backup](docs/Backup.md)
 - [BackupDownloadUrl](docs/BackupDownloadUrl.md)
 - [BackupDownloadUrlRequest](docs/BackupDownloadUrlRequest.md)
 - [Balancer](docs/Balancer.md)
 - [BaseError](docs/BaseError.md)
 - [BindFloatingIp](docs/BindFloatingIp.md)
 - [Bonus](docs/Bonus.md)
 - [Bot](docs/Bot.md)
 - [Branch](docs/Branch.md)
 - [Bucket](docs/Bucket.md)
 - [BucketDiskStats](docs/BucketDiskStats.md)
 - [BucketUser](docs/BucketUser.md)
 - [BucketWebsiteConfig](docs/BucketWebsiteConfig.md)
 - [Certificate](docs/Certificate.md)
 - [CertificateTask](docs/CertificateTask.md)
 - [ChangeAgentModel](docs/ChangeAgentModel.md)
 - [Chat](docs/Chat.md)
 - [ChatFirstMessage](docs/ChatFirstMessage.md)
 - [ChatListMetrics](docs/ChatListMetrics.md)
 - [ChatMessage](docs/ChatMessage.md)
 - [ChatMessageFile](docs/ChatMessageFile.md)
 - [ChatsCsv](docs/ChatsCsv.md)
 - [CheckDomain200Response](docs/CheckDomain200Response.md)
 - [ClearCache](docs/ClearCache.md)
 - [Clickhouse](docs/Clickhouse.md)
 - [ClusterAction](docs/ClusterAction.md)
 - [ClusterEdit](docs/ClusterEdit.md)
 - [ClusterEditOidcProvider](docs/ClusterEditOidcProvider.md)
 - [ClusterIn](docs/ClusterIn.md)
 - [ClusterIn1](docs/ClusterIn1.md)
 - [ClusterInClusterNetworkCidr](docs/ClusterInClusterNetworkCidr.md)
 - [ClusterInConfiguration](docs/ClusterInConfiguration.md)
 - [ClusterInMaintenanceSlot](docs/ClusterInMaintenanceSlot.md)
 - [ClusterInOidcProvider](docs/ClusterInOidcProvider.md)
 - [ClusterOut](docs/ClusterOut.md)
 - [ClusterResponse](docs/ClusterResponse.md)
 - [ClusterVersionEdit](docs/ClusterVersionEdit.md)
 - [Clusterk8s](docs/Clusterk8s.md)
 - [ClustersResponse](docs/ClustersResponse.md)
 - [Commit](docs/Commit.md)
 - [ComponentsSchemasBaseError](docs/ComponentsSchemasBaseError.md)
 - [ComponentsSchemasMeta](docs/ComponentsSchemasMeta.md)
 - [ConfigAccess](docs/ConfigAccess.md)
 - [ConfigCache](docs/ConfigCache.md)
 - [ConfigCacheAlwaysOnline](docs/ConfigCacheAlwaysOnline.md)
 - [ConfigCacheBrowser](docs/ConfigCacheBrowser.md)
 - [ConfigCacheCdn](docs/ConfigCacheCdn.md)
 - [ConfigCacheCdnTtl](docs/ConfigCacheCdnTtl.md)
 - [ConfigCacheQueryArgs](docs/ConfigCacheQueryArgs.md)
 - [ConfigDelivery](docs/ConfigDelivery.md)
 - [ConfigDeliveryPackaging](docs/ConfigDeliveryPackaging.md)
 - [ConfigDeliveryPackagingMp4](docs/ConfigDeliveryPackagingMp4.md)
 - [ConfigDomains](docs/ConfigDomains.md)
 - [ConfigHttpHeaders](docs/ConfigHttpHeaders.md)
 - [ConfigHttpHeadersCors](docs/ConfigHttpHeadersCors.md)
 - [ConfigOrigin](docs/ConfigOrigin.md)
 - [ConfigOriginAws](docs/ConfigOriginAws.md)
 - [ConfigRobots](docs/ConfigRobots.md)
 - [ConfigSecurity](docs/ConfigSecurity.md)
 - [ConfigSecuritySecureToken](docs/ConfigSecuritySecureToken.md)
 - [ConnectAgentTool](docs/ConnectAgentTool.md)
 - [ConnectSkillItem](docs/ConnectSkillItem.md)
 - [ConnectSkills](docs/ConnectSkills.md)
 - [ConnectTelegram](docs/ConnectTelegram.md)
 - [CreateAdmin](docs/CreateAdmin.md)
 - [CreateAgent](docs/CreateAgent.md)
 - [CreateAgent201Response](docs/CreateAgent201Response.md)
 - [CreateAgentBotTelegramBot201Response](docs/CreateAgentBotTelegramBot201Response.md)
 - [CreateAgentEntityLimit](docs/CreateAgentEntityLimit.md)
 - [CreateAgentEntityLimit201Response](docs/CreateAgentEntityLimit201Response.md)
 - [CreateAgentSkill201Response](docs/CreateAgentSkill201Response.md)
 - [CreateAgentTool201Response](docs/CreateAgentTool201Response.md)
 - [CreateAgentV2](docs/CreateAgentV2.md)
 - [CreateAiKey](docs/CreateAiKey.md)
 - [CreateAiKey201Response](docs/CreateAiKey201Response.md)
 - [CreateAiKeyLimit](docs/CreateAiKeyLimit.md)
 - [CreateAiKeyLimit201Response](docs/CreateAiKeyLimit201Response.md)
 - [CreateAiSolution](docs/CreateAiSolution.md)
 - [CreateAiSolution201Response](docs/CreateAiSolution201Response.md)
 - [CreateApp](docs/CreateApp.md)
 - [CreateApp201Response](docs/CreateApp201Response.md)
 - [CreateBalancer](docs/CreateBalancer.md)
 - [CreateBalancer200Response](docs/CreateBalancer200Response.md)
 - [CreateBalancerCertificates](docs/CreateBalancerCertificates.md)
 - [CreateBalancerRule200Response](docs/CreateBalancerRule200Response.md)
 - [CreateBot](docs/CreateBot.md)
 - [CreateCdnResource201Response](docs/CreateCdnResource201Response.md)
 - [CreateCluster](docs/CreateCluster.md)
 - [CreateClusterAdmin](docs/CreateClusterAdmin.md)
 - [CreateClusterBackupSchedule](docs/CreateClusterBackupSchedule.md)
 - [CreateClusterConfiguration](docs/CreateClusterConfiguration.md)
 - [CreateClusterDiskAutoscaling](docs/CreateClusterDiskAutoscaling.md)
 - [CreateClusterInstance](docs/CreateClusterInstance.md)
 - [CreateClusterMaintenanceSlot](docs/CreateClusterMaintenanceSlot.md)
 - [CreateCrispIntegration](docs/CreateCrispIntegration.md)
 - [CreateDatabaseBackup201Response](docs/CreateDatabaseBackup201Response.md)
 - [CreateDatabaseBackupDownloadUrl201Response](docs/CreateDatabaseBackupDownloadUrl201Response.md)
 - [CreateDatabaseCluster201Response](docs/CreateDatabaseCluster201Response.md)
 - [CreateDatabaseInstance201Response](docs/CreateDatabaseInstance201Response.md)
 - [CreateDatabaseS3Backup201Response](docs/CreateDatabaseS3Backup201Response.md)
 - [CreateDatabaseUser201Response](docs/CreateDatabaseUser201Response.md)
 - [CreateDbAutoBackups](docs/CreateDbAutoBackups.md)
 - [CreateDedicatedServer](docs/CreateDedicatedServer.md)
 - [CreateDedicatedServer201Response](docs/CreateDedicatedServer201Response.md)
 - [CreateDeploy201Response](docs/CreateDeploy201Response.md)
 - [CreateDeployRequest](docs/CreateDeployRequest.md)
 - [CreateDns](docs/CreateDns.md)
 - [CreateDnsV2](docs/CreateDnsV2.md)
 - [CreateDocument](docs/CreateDocument.md)
 - [CreateDomainDNSRecord201Response](docs/CreateDomainDNSRecord201Response.md)
 - [CreateDomainDNSRecordV2201Response](docs/CreateDomainDNSRecordV2201Response.md)
 - [CreateDomainMailbox201Response](docs/CreateDomainMailbox201Response.md)
 - [CreateDomainMailboxRequest](docs/CreateDomainMailboxRequest.md)
 - [CreateDomainMailboxV2201Response](docs/CreateDomainMailboxV2201Response.md)
 - [CreateDomainMailboxV2Request](docs/CreateDomainMailboxV2Request.md)
 - [CreateDomainRequest201Response](docs/CreateDomainRequest201Response.md)
 - [CreateFloatingIp](docs/CreateFloatingIp.md)
 - [CreateFloatingIp201Response](docs/CreateFloatingIp201Response.md)
 - [CreateHttpResource](docs/CreateHttpResource.md)
 - [CreateInstance](docs/CreateInstance.md)
 - [CreateJivoIntegration](docs/CreateJivoIntegration.md)
 - [CreateKey201Response](docs/CreateKey201Response.md)
 - [CreateKeyRequest](docs/CreateKeyRequest.md)
 - [CreateKnowledgebase](docs/CreateKnowledgebase.md)
 - [CreateKnowledgebase201Response](docs/CreateKnowledgebase201Response.md)
 - [CreateKnowledgebaseDocument201Response](docs/CreateKnowledgebaseDocument201Response.md)
 - [CreateMaxBot](docs/CreateMaxBot.md)
 - [CreateMultipleDomainMailboxes201Response](docs/CreateMultipleDomainMailboxes201Response.md)
 - [CreateMultipleDomainMailboxesRequest](docs/CreateMultipleDomainMailboxesRequest.md)
 - [CreateMultipleDomainMailboxesV2201Response](docs/CreateMultipleDomainMailboxesV2201Response.md)
 - [CreateNetworkDrive](docs/CreateNetworkDrive.md)
 - [CreateNetworkDrive201Response](docs/CreateNetworkDrive201Response.md)
 - [CreatePerson201Response](docs/CreatePerson201Response.md)
 - [CreateProject](docs/CreateProject.md)
 - [CreateProject201Response](docs/CreateProject201Response.md)
 - [CreateRule](docs/CreateRule.md)
 - [CreateS3Backup](docs/CreateS3Backup.md)
 - [CreateServer](docs/CreateServer.md)
 - [CreateServer201Response](docs/CreateServer201Response.md)
 - [CreateServerConfiguration](docs/CreateServerConfiguration.md)
 - [CreateServerDisk201Response](docs/CreateServerDisk201Response.md)
 - [CreateServerDiskBackup201Response](docs/CreateServerDiskBackup201Response.md)
 - [CreateServerDiskBackupDownloadUrl201Response](docs/CreateServerDiskBackupDownloadUrl201Response.md)
 - [CreateServerDiskBackupRequest](docs/CreateServerDiskBackupRequest.md)
 - [CreateServerDiskRequest](docs/CreateServerDiskRequest.md)
 - [CreateServerNetwork](docs/CreateServerNetwork.md)
 - [CreateSkill](docs/CreateSkill.md)
 - [CreateStorage201Response](docs/CreateStorage201Response.md)
 - [CreateStorageRequest](docs/CreateStorageRequest.md)
 - [CreateStorageRequestConfigurator](docs/CreateStorageRequestConfigurator.md)
 - [CreateTool](docs/CreateTool.md)
 - [CreateVPC201Response](docs/CreateVPC201Response.md)
 - [CreateVpc](docs/CreateVpc.md)
 - [CrispIntegration](docs/CrispIntegration.md)
 - [DatabaseAdmin](docs/DatabaseAdmin.md)
 - [DatabaseCluster](docs/DatabaseCluster.md)
 - [DatabaseClusterDisk](docs/DatabaseClusterDisk.md)
 - [DatabaseClusterDiskAutoscaling](docs/DatabaseClusterDiskAutoscaling.md)
 - [DatabaseClusterMaintenanceSlot](docs/DatabaseClusterMaintenanceSlot.md)
 - [DatabaseConfigurator](docs/DatabaseConfigurator.md)
 - [DatabaseConfiguratorPrices](docs/DatabaseConfiguratorPrices.md)
 - [DatabaseConfiguratorRequirements](docs/DatabaseConfiguratorRequirements.md)
 - [DatabaseExtensions](docs/DatabaseExtensions.md)
 - [DatabaseInstance](docs/DatabaseInstance.md)
 - [DatabaseType](docs/DatabaseType.md)
 - [DatabaseTypeRequirements](docs/DatabaseTypeRequirements.md)
 - [Db](docs/Db.md)
 - [DbDiskStats](docs/DbDiskStats.md)
 - [DbExtension](docs/DbExtension.md)
 - [DbParametersByType](docs/DbParametersByType.md)
 - [DbPrivilegeGroup](docs/DbPrivilegeGroup.md)
 - [DbReplication](docs/DbReplication.md)
 - [DbType](docs/DbType.md)
 - [DbsCreateBackup](docs/DbsCreateBackup.md)
 - [DbsUpdateBackup](docs/DbsUpdateBackup.md)
 - [DedicatedServer](docs/DedicatedServer.md)
 - [DedicatedServerAdditionalService](docs/DedicatedServerAdditionalService.md)
 - [DedicatedServerPreset](docs/DedicatedServerPreset.md)
 - [DedicatedServerPresetCpu](docs/DedicatedServerPresetCpu.md)
 - [DedicatedServerPresetDisk](docs/DedicatedServerPresetDisk.md)
 - [DedicatedServerPresetMemory](docs/DedicatedServerPresetMemory.md)
 - [DeleteAgent](docs/DeleteAgent.md)
 - [DeleteBalancer200Response](docs/DeleteBalancer200Response.md)
 - [DeleteCluster200Response](docs/DeleteCluster200Response.md)
 - [DeleteCountriesFromAllowedList200Response](docs/DeleteCountriesFromAllowedList200Response.md)
 - [DeleteCountriesFromAllowedListRequest](docs/DeleteCountriesFromAllowedListRequest.md)
 - [DeleteDatabaseCluster200Response](docs/DeleteDatabaseCluster200Response.md)
 - [DeleteDatabaseCluster200ResponseDatabaseDelete](docs/DeleteDatabaseCluster200ResponseDatabaseDelete.md)
 - [DeleteIPsFromAllowedList200Response](docs/DeleteIPsFromAllowedList200Response.md)
 - [DeleteIPsFromAllowedListRequest](docs/DeleteIPsFromAllowedListRequest.md)
 - [DeleteServer200Response](docs/DeleteServer200Response.md)
 - [DeleteServerIPRequest](docs/DeleteServerIPRequest.md)
 - [DeleteServiceResponse](docs/DeleteServiceResponse.md)
 - [DeleteStorage200Response](docs/DeleteStorage200Response.md)
 - [Deploy](docs/Deploy.md)
 - [DeployStatus](docs/DeployStatus.md)
 - [DnatIn](docs/DnatIn.md)
 - [DnatInLocal](docs/DnatInLocal.md)
 - [DnatInPublic](docs/DnatInPublic.md)
 - [DnatRuleOut](docs/DnatRuleOut.md)
 - [DnatRuleResponse](docs/DnatRuleResponse.md)
 - [DnatRulesResponse](docs/DnatRulesResponse.md)
 - [DnsRecord](docs/DnsRecord.md)
 - [DnsRecordData](docs/DnsRecordData.md)
 - [DnsRecordV2](docs/DnsRecordV2.md)
 - [DnsRecordV2Data](docs/DnsRecordV2Data.md)
 - [Document](docs/Document.md)
 - [DocumentStatusInfo](docs/DocumentStatusInfo.md)
 - [DocumentStatusInfoDetails](docs/DocumentStatusInfoDetails.md)
 - [Domain](docs/Domain.md)
 - [DomainInfo](docs/DomainInfo.md)
 - [DomainNameServer](docs/DomainNameServer.md)
 - [DomainPaymentPeriod](docs/DomainPaymentPeriod.md)
 - [DomainPrimeType](docs/DomainPrimeType.md)
 - [DomainProlong](docs/DomainProlong.md)
 - [DomainRegister](docs/DomainRegister.md)
 - [DomainRequest](docs/DomainRequest.md)
 - [DomainTransfer](docs/DomainTransfer.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [ExportAgentChatsCsv200Response](docs/ExportAgentChatsCsv200Response.md)
 - [Finances](docs/Finances.md)
 - [FirewallGroup](docs/FirewallGroup.md)
 - [FirewallGroupInAPI](docs/FirewallGroupInAPI.md)
 - [FirewallGroupOutResponse](docs/FirewallGroupOutResponse.md)
 - [FirewallGroupResource](docs/FirewallGroupResource.md)
 - [FirewallGroupResourceOutResponse](docs/FirewallGroupResourceOutResponse.md)
 - [FirewallGroupResourcesOutResponse](docs/FirewallGroupResourcesOutResponse.md)
 - [FirewallGroupsOutResponse](docs/FirewallGroupsOutResponse.md)
 - [FirewallRule](docs/FirewallRule.md)
 - [FirewallRuleDirection](docs/FirewallRuleDirection.md)
 - [FirewallRuleInAPI](docs/FirewallRuleInAPI.md)
 - [FirewallRuleOutResponse](docs/FirewallRuleOutResponse.md)
 - [FirewallRuleProtocol](docs/FirewallRuleProtocol.md)
 - [FirewallRulesOutResponse](docs/FirewallRulesOutResponse.md)
 - [FloatingIp](docs/FloatingIp.md)
 - [ForwardIsDisabled](docs/ForwardIsDisabled.md)
 - [ForwardIsEnabled](docs/ForwardIsEnabled.md)
 - [ForwardingIncomingIsDisabled](docs/ForwardingIncomingIsDisabled.md)
 - [ForwardingIncomingIsEnabled](docs/ForwardingIncomingIsEnabled.md)
 - [ForwardingOutgoingIsDisabled](docs/ForwardingOutgoingIsDisabled.md)
 - [ForwardingOutgoingIsEnabled](docs/ForwardingOutgoingIsEnabled.md)
 - [Frameworks](docs/Frameworks.md)
 - [Free](docs/Free.md)
 - [GetAccountStatus200Response](docs/GetAccountStatus200Response.md)
 - [GetAgentBotMaxBots200Response](docs/GetAgentBotMaxBots200Response.md)
 - [GetAgentBotMaxBots200ResponseMeta](docs/GetAgentBotMaxBots200ResponseMeta.md)
 - [GetAgentBotMaxBotsByAgent200Response](docs/GetAgentBotMaxBotsByAgent200Response.md)
 - [GetAgentBotMaxBotsByAgent200ResponseMeta](docs/GetAgentBotMaxBotsByAgent200ResponseMeta.md)
 - [GetAgentBotTelegramBots200Response](docs/GetAgentBotTelegramBots200Response.md)
 - [GetAgentBotTelegramBots200ResponseMeta](docs/GetAgentBotTelegramBots200ResponseMeta.md)
 - [GetAgentBotTelegramBotsByAgent200Response](docs/GetAgentBotTelegramBotsByAgent200Response.md)
 - [GetAgentBotTelegramBotsByAgent200ResponseMeta](docs/GetAgentBotTelegramBotsByAgent200ResponseMeta.md)
 - [GetAgentChatList200Response](docs/GetAgentChatList200Response.md)
 - [GetAgentChatList200ResponseMeta](docs/GetAgentChatList200ResponseMeta.md)
 - [GetAgentChatMessages200Response](docs/GetAgentChatMessages200Response.md)
 - [GetAgentChatMessages200ResponseMeta](docs/GetAgentChatMessages200ResponseMeta.md)
 - [GetAgentEntityLimits200Response](docs/GetAgentEntityLimits200Response.md)
 - [GetAgentEntityLimits200ResponseMeta](docs/GetAgentEntityLimits200ResponseMeta.md)
 - [GetAgentIntegrationCrisp200Response](docs/GetAgentIntegrationCrisp200Response.md)
 - [GetAgentIntegrationJivo200Response](docs/GetAgentIntegrationJivo200Response.md)
 - [GetAgentSkill200Response](docs/GetAgentSkill200Response.md)
 - [GetAgentSkillCatalog200Response](docs/GetAgentSkillCatalog200Response.md)
 - [GetAgentSkillCatalog200ResponseMeta](docs/GetAgentSkillCatalog200ResponseMeta.md)
 - [GetAgentSkillLibrary200Response](docs/GetAgentSkillLibrary200Response.md)
 - [GetAgentSkillLibrary200ResponseMeta](docs/GetAgentSkillLibrary200ResponseMeta.md)
 - [GetAgentSkillVersion200Response](docs/GetAgentSkillVersion200Response.md)
 - [GetAgentSkillVersions200Response](docs/GetAgentSkillVersions200Response.md)
 - [GetAgentSkillVersions200ResponseMeta](docs/GetAgentSkillVersions200ResponseMeta.md)
 - [GetAgentSkillsForAgent200Response](docs/GetAgentSkillsForAgent200Response.md)
 - [GetAgentSkillsForAgent200ResponseMeta](docs/GetAgentSkillsForAgent200ResponseMeta.md)
 - [GetAgentStatistics200Response](docs/GetAgentStatistics200Response.md)
 - [GetAgentStatistics200ResponseMeta](docs/GetAgentStatistics200ResponseMeta.md)
 - [GetAgentToolTemplatePrices200Response](docs/GetAgentToolTemplatePrices200Response.md)
 - [GetAgentToolTemplates200Response](docs/GetAgentToolTemplates200Response.md)
 - [GetAgentToolTemplates200ResponseMeta](docs/GetAgentToolTemplates200ResponseMeta.md)
 - [GetAgentTools200Response](docs/GetAgentTools200Response.md)
 - [GetAgentTools200ResponseMeta](docs/GetAgentTools200ResponseMeta.md)
 - [GetAgentToolsByAgent200Response](docs/GetAgentToolsByAgent200Response.md)
 - [GetAgentToolsByAgent200ResponseMeta](docs/GetAgentToolsByAgent200ResponseMeta.md)
 - [GetAgentV3200Response](docs/GetAgentV3200Response.md)
 - [GetAgents200Response](docs/GetAgents200Response.md)
 - [GetAgents200ResponseMeta](docs/GetAgents200ResponseMeta.md)
 - [GetAgentsTokenPackages200Response](docs/GetAgentsTokenPackages200Response.md)
 - [GetAgentsTokenPackages200ResponseMeta](docs/GetAgentsTokenPackages200ResponseMeta.md)
 - [GetAgentsV3200Response](docs/GetAgentsV3200Response.md)
 - [GetAiKeyCallsStatistic200Response](docs/GetAiKeyCallsStatistic200Response.md)
 - [GetAiKeyLimits200Response](docs/GetAiKeyLimits200Response.md)
 - [GetAiKeyLimits200ResponseMeta](docs/GetAiKeyLimits200ResponseMeta.md)
 - [GetAiKeyModelsStatistic200Response](docs/GetAiKeyModelsStatistic200Response.md)
 - [GetAiKeyModelsStatistic200ResponseMeta](docs/GetAiKeyModelsStatistic200ResponseMeta.md)
 - [GetAiKeyTokenUsageStatistic200Response](docs/GetAiKeyTokenUsageStatistic200Response.md)
 - [GetAiKeyTokenUsageStatistic200ResponseMeta](docs/GetAiKeyTokenUsageStatistic200ResponseMeta.md)
 - [GetAiKeys200Response](docs/GetAiKeys200Response.md)
 - [GetAiKeys200ResponseMeta](docs/GetAiKeys200ResponseMeta.md)
 - [GetAiModelParameters200Response](docs/GetAiModelParameters200Response.md)
 - [GetAiModelParameters200ResponseMeta](docs/GetAiModelParameters200ResponseMeta.md)
 - [GetAiModelTokenPackages200Response](docs/GetAiModelTokenPackages200Response.md)
 - [GetAiModelTokenPackages200ResponseMeta](docs/GetAiModelTokenPackages200ResponseMeta.md)
 - [GetAiProvider200Response](docs/GetAiProvider200Response.md)
 - [GetAiProviders200Response](docs/GetAiProviders200Response.md)
 - [GetAiProviders200ResponseMeta](docs/GetAiProviders200ResponseMeta.md)
 - [GetAiSolutionChatStatus200Response](docs/GetAiSolutionChatStatus200Response.md)
 - [GetAiSolutionMainChatHistory200Response](docs/GetAiSolutionMainChatHistory200Response.md)
 - [GetAllMailboxesV2200Response](docs/GetAllMailboxesV2200Response.md)
 - [GetAllProjectResources200Response](docs/GetAllProjectResources200Response.md)
 - [GetAppDeploys200Response](docs/GetAppDeploys200Response.md)
 - [GetAppLogs200Response](docs/GetAppLogs200Response.md)
 - [GetApps200Response](docs/GetApps200Response.md)
 - [GetAuthAccessSettings200Response](docs/GetAuthAccessSettings200Response.md)
 - [GetAuthAccessSettings200ResponseWhiteList](docs/GetAuthAccessSettings200ResponseWhiteList.md)
 - [GetBalancerIPs200Response](docs/GetBalancerIPs200Response.md)
 - [GetBalancerRules200Response](docs/GetBalancerRules200Response.md)
 - [GetBalancers200Response](docs/GetBalancers200Response.md)
 - [GetBalancersPresets200Response](docs/GetBalancersPresets200Response.md)
 - [GetBranches200Response](docs/GetBranches200Response.md)
 - [GetCdnCertificateTasks200Response](docs/GetCdnCertificateTasks200Response.md)
 - [GetCdnCertificates200Response](docs/GetCdnCertificates200Response.md)
 - [GetCdnOriginNodes200Response](docs/GetCdnOriginNodes200Response.md)
 - [GetCdnPresets200Response](docs/GetCdnPresets200Response.md)
 - [GetCdnResourceConfiguration200Response](docs/GetCdnResourceConfiguration200Response.md)
 - [GetCdnResourceNodes200Response](docs/GetCdnResourceNodes200Response.md)
 - [GetCdnResourceStatistics200Response](docs/GetCdnResourceStatistics200Response.md)
 - [GetCdnResources200Response](docs/GetCdnResources200Response.md)
 - [GetCommits200Response](docs/GetCommits200Response.md)
 - [GetConfigurators200Response](docs/GetConfigurators200Response.md)
 - [GetCountries200Response](docs/GetCountries200Response.md)
 - [GetDatabaseAutoBackupsSettings200Response](docs/GetDatabaseAutoBackupsSettings200Response.md)
 - [GetDatabaseBackup200Response](docs/GetDatabaseBackup200Response.md)
 - [GetDatabaseBackups200Response](docs/GetDatabaseBackups200Response.md)
 - [GetDatabaseClusterReplicas200Response](docs/GetDatabaseClusterReplicas200Response.md)
 - [GetDatabaseClusterTypes200Response](docs/GetDatabaseClusterTypes200Response.md)
 - [GetDatabaseClusters200Response](docs/GetDatabaseClusters200Response.md)
 - [GetDatabaseConfigurators200Response](docs/GetDatabaseConfigurators200Response.md)
 - [GetDatabaseDefaultParameters200Response](docs/GetDatabaseDefaultParameters200Response.md)
 - [GetDatabaseInstances200Response](docs/GetDatabaseInstances200Response.md)
 - [GetDatabasePreset200Response](docs/GetDatabasePreset200Response.md)
 - [GetDatabasePrivileges200Response](docs/GetDatabasePrivileges200Response.md)
 - [GetDatabaseS3Backups200Response](docs/GetDatabaseS3Backups200Response.md)
 - [GetDatabaseUsers200Response](docs/GetDatabaseUsers200Response.md)
 - [GetDatabasesPresets200Response](docs/GetDatabasesPresets200Response.md)
 - [GetDedicatedServerPresetAdditionalServices200Response](docs/GetDedicatedServerPresetAdditionalServices200Response.md)
 - [GetDedicatedServers200Response](docs/GetDedicatedServers200Response.md)
 - [GetDedicatedServersPresets200Response](docs/GetDedicatedServersPresets200Response.md)
 - [GetDeployLogs200Response](docs/GetDeployLogs200Response.md)
 - [GetDeploySettings200Response](docs/GetDeploySettings200Response.md)
 - [GetDomain200Response](docs/GetDomain200Response.md)
 - [GetDomainDNSRecords200Response](docs/GetDomainDNSRecords200Response.md)
 - [GetDomainMailInfo200Response](docs/GetDomainMailInfo200Response.md)
 - [GetDomainNameServers200Response](docs/GetDomainNameServers200Response.md)
 - [GetDomainRequests200Response](docs/GetDomainRequests200Response.md)
 - [GetDomains200Response](docs/GetDomains200Response.md)
 - [GetFinances200Response](docs/GetFinances200Response.md)
 - [GetFloatingIps200Response](docs/GetFloatingIps200Response.md)
 - [GetKey200Response](docs/GetKey200Response.md)
 - [GetKeys200Response](docs/GetKeys200Response.md)
 - [GetKnowledgebaseDocumentsV2200Response](docs/GetKnowledgebaseDocumentsV2200Response.md)
 - [GetKnowledgebaseDocumentsV2200ResponseMeta](docs/GetKnowledgebaseDocumentsV2200ResponseMeta.md)
 - [GetKnowledgebaseV3200Response](docs/GetKnowledgebaseV3200Response.md)
 - [GetKnowledgebases200Response](docs/GetKnowledgebases200Response.md)
 - [GetKnowledgebasesTokenPackages200Response](docs/GetKnowledgebasesTokenPackages200Response.md)
 - [GetKnowledgebasesTokenPackages200ResponseMeta](docs/GetKnowledgebasesTokenPackages200ResponseMeta.md)
 - [GetKnowledgebasesV2200Response](docs/GetKnowledgebasesV2200Response.md)
 - [GetKnowledgebasesV3200Response](docs/GetKnowledgebasesV3200Response.md)
 - [GetKnowledgebasesV3200ResponseMeta](docs/GetKnowledgebasesV3200ResponseMeta.md)
 - [GetLocations200Response](docs/GetLocations200Response.md)
 - [GetMailboxes200Response](docs/GetMailboxes200Response.md)
 - [GetModels200Response](docs/GetModels200Response.md)
 - [GetModelsV3200Response](docs/GetModelsV3200Response.md)
 - [GetModelsV3200ResponseMeta](docs/GetModelsV3200ResponseMeta.md)
 - [GetNetworkDrives200Response](docs/GetNetworkDrives200Response.md)
 - [GetNetworkDrivesAvailableResources200Response](docs/GetNetworkDrivesAvailableResources200Response.md)
 - [GetNetworkDrivesPresets200Response](docs/GetNetworkDrivesPresets200Response.md)
 - [GetNotificationSettings200Response](docs/GetNotificationSettings200Response.md)
 - [GetOsList200Response](docs/GetOsList200Response.md)
 - [GetPersons200Response](docs/GetPersons200Response.md)
 - [GetProjectClusters200Response](docs/GetProjectClusters200Response.md)
 - [GetProjectDatabases200Response](docs/GetProjectDatabases200Response.md)
 - [GetProjectStorages200Response](docs/GetProjectStorages200Response.md)
 - [GetProjects200Response](docs/GetProjects200Response.md)
 - [GetProviders200Response](docs/GetProviders200Response.md)
 - [GetRepositories200Response](docs/GetRepositories200Response.md)
 - [GetRestorePoint200Response](docs/GetRestorePoint200Response.md)
 - [GetRestorePoints200Response](docs/GetRestorePoints200Response.md)
 - [GetServerDiskBackup200Response](docs/GetServerDiskBackup200Response.md)
 - [GetServerDiskBackups200Response](docs/GetServerDiskBackups200Response.md)
 - [GetServerDisks200Response](docs/GetServerDisks200Response.md)
 - [GetServerIPs200Response](docs/GetServerIPs200Response.md)
 - [GetServerLogs200Response](docs/GetServerLogs200Response.md)
 - [GetServerStatistics200Response](docs/GetServerStatistics200Response.md)
 - [GetServerStatisticsNew200Response](docs/GetServerStatisticsNew200Response.md)
 - [GetServers200Response](docs/GetServers200Response.md)
 - [GetServersPresets200Response](docs/GetServersPresets200Response.md)
 - [GetServicePrices200Response](docs/GetServicePrices200Response.md)
 - [GetServicePrices200ResponseMeta](docs/GetServicePrices200ResponseMeta.md)
 - [GetSoftware200Response](docs/GetSoftware200Response.md)
 - [GetStorageSubdomains200Response](docs/GetStorageSubdomains200Response.md)
 - [GetStorageTransferStatus200Response](docs/GetStorageTransferStatus200Response.md)
 - [GetStorageUsers200Response](docs/GetStorageUsers200Response.md)
 - [GetStoragesPresets200Response](docs/GetStoragesPresets200Response.md)
 - [GetTLD200Response](docs/GetTLD200Response.md)
 - [GetTLDs200Response](docs/GetTLDs200Response.md)
 - [GetVPCPorts200Response](docs/GetVPCPorts200Response.md)
 - [GetVPCServices200Response](docs/GetVPCServices200Response.md)
 - [GetVPCs200Response](docs/GetVPCs200Response.md)
 - [HttpResource](docs/HttpResource.md)
 - [HttpResourceConfig](docs/HttpResourceConfig.md)
 - [Image](docs/Image.md)
 - [ImageDownload](docs/ImageDownload.md)
 - [ImageDownloadResponse](docs/ImageDownloadResponse.md)
 - [ImageDownloadsResponse](docs/ImageDownloadsResponse.md)
 - [ImageInAPI](docs/ImageInAPI.md)
 - [ImageOutResponse](docs/ImageOutResponse.md)
 - [ImageStatus](docs/ImageStatus.md)
 - [ImageUpdateAPI](docs/ImageUpdateAPI.md)
 - [ImageUrlAuth](docs/ImageUrlAuth.md)
 - [ImageUrlIn](docs/ImageUrlIn.md)
 - [ImagesOutResponse](docs/ImagesOutResponse.md)
 - [IncreaseNodes](docs/IncreaseNodes.md)
 - [IndexingSchedule](docs/IndexingSchedule.md)
 - [InfoServicePrice](docs/InfoServicePrice.md)
 - [InitializeParams](docs/InitializeParams.md)
 - [InitializeParamsClientInfo](docs/InitializeParamsClientInfo.md)
 - [InitializeResult](docs/InitializeResult.md)
 - [InitializeResultServerInfo](docs/InitializeResultServerInfo.md)
 - [InstallAgentSkillFromCatalog200Response](docs/InstallAgentSkillFromCatalog200Response.md)
 - [InstallAgentSkillFromCatalog200ResponseMeta](docs/InstallAgentSkillFromCatalog200ResponseMeta.md)
 - [InstallAndConnectAgentSkill200Response](docs/InstallAndConnectAgentSkill200Response.md)
 - [InstallAndConnectSkill](docs/InstallAndConnectSkill.md)
 - [InstallTool](docs/InstallTool.md)
 - [Invoice](docs/Invoice.md)
 - [Ip](docs/Ip.md)
 - [IssueCertificate](docs/IssueCertificate.md)
 - [JivoIntegration](docs/JivoIntegration.md)
 - [JsonRpcError](docs/JsonRpcError.md)
 - [JsonRpcErrorResponse](docs/JsonRpcErrorResponse.md)
 - [JsonRpcNotification](docs/JsonRpcNotification.md)
 - [JsonRpcRequest](docs/JsonRpcRequest.md)
 - [JsonRpcResultResponse](docs/JsonRpcResultResponse.md)
 - [K8SVersionsResponse](docs/K8SVersionsResponse.md)
 - [Kafka](docs/Kafka.md)
 - [KafkaConfigParameters](docs/KafkaConfigParameters.md)
 - [Knowledgebase](docs/Knowledgebase.md)
 - [KnowledgebaseAddTokenPackage](docs/KnowledgebaseAddTokenPackage.md)
 - [KnowledgebaseV2](docs/KnowledgebaseV2.md)
 - [KnowledgebaseV3](docs/KnowledgebaseV3.md)
 - [LinkKnowledgebase](docs/LinkKnowledgebase.md)
 - [ListAiSolutionConversations200Response](docs/ListAiSolutionConversations200Response.md)
 - [ListAiSolutionTelegramBots200Response](docs/ListAiSolutionTelegramBots200Response.md)
 - [ListAiSolutionTypes200Response](docs/ListAiSolutionTypes200Response.md)
 - [ListAiSolutions200Response](docs/ListAiSolutions200Response.md)
 - [Location](docs/Location.md)
 - [LocationDto](docs/LocationDto.md)
 - [Mailbox](docs/Mailbox.md)
 - [MailboxAutoReply](docs/MailboxAutoReply.md)
 - [MailboxForwardingIncoming](docs/MailboxForwardingIncoming.md)
 - [MailboxForwardingOutgoing](docs/MailboxForwardingOutgoing.md)
 - [MailboxResponse](docs/MailboxResponse.md)
 - [MailboxSpamFilter](docs/MailboxSpamFilter.md)
 - [MailboxV2](docs/MailboxV2.md)
 - [MailboxesBatchV2](docs/MailboxesBatchV2.md)
 - [MasterPresetOutApi](docs/MasterPresetOutApi.md)
 - [Meta](docs/Meta.md)
 - [Meta1](docs/Meta1.md)
 - [Model](docs/Model.md)
 - [ModelBatch](docs/ModelBatch.md)
 - [ModelParamInfo](docs/ModelParamInfo.md)
 - [ModelParameter](docs/ModelParameter.md)
 - [ModelPriceTier](docs/ModelPriceTier.md)
 - [ModelV3](docs/ModelV3.md)
 - [Mongodb](docs/Mongodb.md)
 - [MountNetworkDrive](docs/MountNetworkDrive.md)
 - [Mysql](docs/Mysql.md)
 - [NatIn](docs/NatIn.md)
 - [Network](docs/Network.md)
 - [NetworkDrive](docs/NetworkDrive.md)
 - [NetworkDriveAvailableResource](docs/NetworkDriveAvailableResource.md)
 - [NetworkDrivePreset](docs/NetworkDrivePreset.md)
 - [NetworkDrivePresetRead](docs/NetworkDrivePresetRead.md)
 - [NetworkDrivePresetWrite](docs/NetworkDrivePresetWrite.md)
 - [NetworkDriversResponse](docs/NetworkDriversResponse.md)
 - [NetworkEdit](docs/NetworkEdit.md)
 - [NetworkIn](docs/NetworkIn.md)
 - [NetworkOut](docs/NetworkOut.md)
 - [NetworkResponse](docs/NetworkResponse.md)
 - [NetworksResponse](docs/NetworksResponse.md)
 - [NodeGroupIn](docs/NodeGroupIn.md)
 - [NodeGroupInConfiguration](docs/NodeGroupInConfiguration.md)
 - [NodeGroupOut](docs/NodeGroupOut.md)
 - [NodeGroupResponse](docs/NodeGroupResponse.md)
 - [NodeGroupsResponse](docs/NodeGroupsResponse.md)
 - [NodeOut](docs/NodeOut.md)
 - [NodesResponse](docs/NodesResponse.md)
 - [NotificationSetting](docs/NotificationSetting.md)
 - [NotificationSettingChannel](docs/NotificationSettingChannel.md)
 - [NotificationSettingChannels](docs/NotificationSettingChannels.md)
 - [NotificationSettingType](docs/NotificationSettingType.md)
 - [OS](docs/OS.md)
 - [Opensearch](docs/Opensearch.md)
 - [Org](docs/Org.md)
 - [OriginNode](docs/OriginNode.md)
 - [OriginServer](docs/OriginServer.md)
 - [OutgoingIsDisabled](docs/OutgoingIsDisabled.md)
 - [OutgoingIsEnabled](docs/OutgoingIsEnabled.md)
 - [PerformActionOnBackupRequest](docs/PerformActionOnBackupRequest.md)
 - [PerformActionOnServerRequest](docs/PerformActionOnServerRequest.md)
 - [Person](docs/Person.md)
 - [Person2](docs/Person2.md)
 - [Policy](docs/Policy.md)
 - [Postgres](docs/Postgres.md)
 - [Postgresql](docs/Postgresql.md)
 - [PreloadCache](docs/PreloadCache.md)
 - [Preset](docs/Preset.md)
 - [PresetsBalancer](docs/PresetsBalancer.md)
 - [PresetsDbs](docs/PresetsDbs.md)
 - [PresetsResponse](docs/PresetsResponse.md)
 - [PresetsStorage](docs/PresetsStorage.md)
 - [Project](docs/Project.md)
 - [ProjectResource](docs/ProjectResource.md)
 - [PropertiesMysql](docs/PropertiesMysql.md)
 - [PropertiesValkey](docs/PropertiesValkey.md)
 - [Provider](docs/Provider.md)
 - [Providers](docs/Providers.md)
 - [Rabbitmq](docs/Rabbitmq.md)
 - [ReduceNodes](docs/ReduceNodes.md)
 - [RegenerateAiSolutionAiKey200Response](docs/RegenerateAiSolutionAiKey200Response.md)
 - [RegistriesResponse](docs/RegistriesResponse.md)
 - [RegistryEdit](docs/RegistryEdit.md)
 - [RegistryIn](docs/RegistryIn.md)
 - [RegistryInConfiguration](docs/RegistryInConfiguration.md)
 - [RegistryOut](docs/RegistryOut.md)
 - [RegistryOutDiskStats](docs/RegistryOutDiskStats.md)
 - [RegistryResponse](docs/RegistryResponse.md)
 - [RemoveCountries](docs/RemoveCountries.md)
 - [RemoveIps](docs/RemoveIps.md)
 - [Replica](docs/Replica.md)
 - [ReplicaDisk](docs/ReplicaDisk.md)
 - [RepositoriesResponse](docs/RepositoriesResponse.md)
 - [Repository](docs/Repository.md)
 - [ResetAiSolutionChat](docs/ResetAiSolutionChat.md)
 - [ResetAiSolutionChat200Response](docs/ResetAiSolutionChat200Response.md)
 - [Resource](docs/Resource.md)
 - [ResourceTransfer](docs/ResourceTransfer.md)
 - [ResourceType](docs/ResourceType.md)
 - [Resources](docs/Resources.md)
 - [ResourcesListResult](docs/ResourcesListResult.md)
 - [ResourcesReadParams](docs/ResourcesReadParams.md)
 - [ResourcesReadResult](docs/ResourcesReadResult.md)
 - [ResourcesResponse](docs/ResourcesResponse.md)
 - [RestorePoint](docs/RestorePoint.md)
 - [RetrievalMode](docs/RetrievalMode.md)
 - [RetrievalModeRef](docs/RetrievalModeRef.md)
 - [RouterEdit](docs/RouterEdit.md)
 - [RouterIn](docs/RouterIn.md)
 - [RouterInParentService](docs/RouterInParentService.md)
 - [RouterNetworkMeta](docs/RouterNetworkMeta.md)
 - [RouterNetworkMetaDhcp](docs/RouterNetworkMetaDhcp.md)
 - [RouterOut](docs/RouterOut.md)
 - [RouterPreset](docs/RouterPreset.md)
 - [RouterPresetsResponse](docs/RouterPresetsResponse.md)
 - [RouterResponse](docs/RouterResponse.md)
 - [RouterStatistic](docs/RouterStatistic.md)
 - [RouterStatisticMeta](docs/RouterStatisticMeta.md)
 - [RouterStatisticsResponse](docs/RouterStatisticsResponse.md)
 - [RoutersResponse](docs/RoutersResponse.md)
 - [Rule](docs/Rule.md)
 - [S3Backup](docs/S3Backup.md)
 - [S3Subdomain](docs/S3Subdomain.md)
 - [SchemasBaseError](docs/SchemasBaseError.md)
 - [SchemasMeta](docs/SchemasMeta.md)
 - [SchemasPresetsResponse](docs/SchemasPresetsResponse.md)
 - [SendAiSolutionMessage](docs/SendAiSolutionMessage.md)
 - [SendAiSolutionMessage200Response](docs/SendAiSolutionMessage200Response.md)
 - [ServerBackup](docs/ServerBackup.md)
 - [ServerBackupDownloadUrl](docs/ServerBackupDownloadUrl.md)
 - [ServerBackupDownloadUrlRequest](docs/ServerBackupDownloadUrlRequest.md)
 - [ServerDisk](docs/ServerDisk.md)
 - [ServerIp](docs/ServerIp.md)
 - [ServerLog](docs/ServerLog.md)
 - [ServersConfigurator](docs/ServersConfigurator.md)
 - [ServersConfiguratorRequirements](docs/ServersConfiguratorRequirements.md)
 - [ServersOs](docs/ServersOs.md)
 - [ServersOsRequirements](docs/ServersOsRequirements.md)
 - [ServersPreset](docs/ServersPreset.md)
 - [ServersSoftware](docs/ServersSoftware.md)
 - [ServersSoftwareRequirements](docs/ServersSoftwareRequirements.md)
 - [ServersStatistics](docs/ServersStatistics.md)
 - [ServersStatisticsMeta](docs/ServersStatisticsMeta.md)
 - [ServiceCostType](docs/ServiceCostType.md)
 - [ServicePrice](docs/ServicePrice.md)
 - [ServicePriceConfiguration](docs/ServicePriceConfiguration.md)
 - [ServicePriceType](docs/ServicePriceType.md)
 - [ServiceServicePrice](docs/ServiceServicePrice.md)
 - [SetAgentSkill](docs/SetAgentSkill.md)
 - [SetAgentSkillForAgent200Response](docs/SetAgentSkillForAgent200Response.md)
 - [SetLabels](docs/SetLabels.md)
 - [SettingCondition](docs/SettingCondition.md)
 - [Skill](docs/Skill.md)
 - [SkillAgent](docs/SkillAgent.md)
 - [SkillCatalogItem](docs/SkillCatalogItem.md)
 - [SkillSaveMeta](docs/SkillSaveMeta.md)
 - [SkillScript](docs/SkillScript.md)
 - [SkillScriptInput](docs/SkillScriptInput.md)
 - [SkillVersion](docs/SkillVersion.md)
 - [SpamFilterIsDisabled](docs/SpamFilterIsDisabled.md)
 - [SpamFilterIsEnabled](docs/SpamFilterIsEnabled.md)
 - [SpamProtectionIsDisabled](docs/SpamProtectionIsDisabled.md)
 - [SpamProtectionIsEnabled](docs/SpamProtectionIsEnabled.md)
 - [SshKey](docs/SshKey.md)
 - [StaticRouteIn](docs/StaticRouteIn.md)
 - [StaticRouteOut](docs/StaticRouteOut.md)
 - [StaticRouteResponse](docs/StaticRouteResponse.md)
 - [StaticRoutesResponse](docs/StaticRoutesResponse.md)
 - [Statistics](docs/Statistics.md)
 - [Status](docs/Status.md)
 - [StatusCompanyInfo](docs/StatusCompanyInfo.md)
 - [StopAiSolutionChat](docs/StopAiSolutionChat.md)
 - [StreamError](docs/StreamError.md)
 - [Subdomain](docs/Subdomain.md)
 - [SyncAgentEntityLimits](docs/SyncAgentEntityLimits.md)
 - [SyncAgentSkillAgentsVersions200Response](docs/SyncAgentSkillAgentsVersions200Response.md)
 - [SyncAgentSkillAgentsVersions200ResponseMeta](docs/SyncAgentSkillAgentsVersions200ResponseMeta.md)
 - [SyncAgentSkillVersionsForAgent200Response](docs/SyncAgentSkillVersionsForAgent200Response.md)
 - [SyncAiKeyLimits](docs/SyncAiKeyLimits.md)
 - [TextContent](docs/TextContent.md)
 - [TokenPackage](docs/TokenPackage.md)
 - [Tool](docs/Tool.md)
 - [Tool2](docs/Tool2.md)
 - [Tool2Annotations](docs/Tool2Annotations.md)
 - [ToolAuthData](docs/ToolAuthData.md)
 - [ToolAuthDataParams](docs/ToolAuthDataParams.md)
 - [ToolConfigField](docs/ToolConfigField.md)
 - [ToolMethod](docs/ToolMethod.md)
 - [ToolPrice](docs/ToolPrice.md)
 - [ToolTemplate](docs/ToolTemplate.md)
 - [ToolTemplateConfigSchema](docs/ToolTemplateConfigSchema.md)
 - [ToolsCallParams](docs/ToolsCallParams.md)
 - [ToolsCallResult](docs/ToolsCallResult.md)
 - [ToolsListResult](docs/ToolsListResult.md)
 - [TopLevelDomain](docs/TopLevelDomain.md)
 - [TrafficUsage](docs/TrafficUsage.md)
 - [TransferStatus](docs/TransferStatus.md)
 - [TransferStorageRequest](docs/TransferStorageRequest.md)
 - [URLType](docs/URLType.md)
 - [UpdateAdmin](docs/UpdateAdmin.md)
 - [UpdateAgent](docs/UpdateAgent.md)
 - [UpdateAgentEntityLimit](docs/UpdateAgentEntityLimit.md)
 - [UpdateAgentTool](docs/UpdateAgentTool.md)
 - [UpdateAiKey](docs/UpdateAiKey.md)
 - [UpdateAiKey200Response](docs/UpdateAiKey200Response.md)
 - [UpdateAiKeyLimit](docs/UpdateAiKeyLimit.md)
 - [UpdateAiSolution](docs/UpdateAiSolution.md)
 - [UpdateAppSettings200Response](docs/UpdateAppSettings200Response.md)
 - [UpdateAuthRestrictionsByCountriesRequest](docs/UpdateAuthRestrictionsByCountriesRequest.md)
 - [UpdateAutoBackup](docs/UpdateAutoBackup.md)
 - [UpdateBalancer](docs/UpdateBalancer.md)
 - [UpdateBot](docs/UpdateBot.md)
 - [UpdateCluster](docs/UpdateCluster.md)
 - [UpdateClusterConfiguration](docs/UpdateClusterConfiguration.md)
 - [UpdateClusterV2](docs/UpdateClusterV2.md)
 - [UpdateClusterV2DiskAutoscaling](docs/UpdateClusterV2DiskAutoscaling.md)
 - [UpdateClusterV2MaintenanceSlot](docs/UpdateClusterV2MaintenanceSlot.md)
 - [UpdateDatabaseCluster200Response](docs/UpdateDatabaseCluster200Response.md)
 - [UpdateDedicatedServerRequest](docs/UpdateDedicatedServerRequest.md)
 - [UpdateDocument](docs/UpdateDocument.md)
 - [UpdateDomain](docs/UpdateDomain.md)
 - [UpdateDomainAutoProlongation200Response](docs/UpdateDomainAutoProlongation200Response.md)
 - [UpdateDomainMailInfoRequest](docs/UpdateDomainMailInfoRequest.md)
 - [UpdateDomainNameServers](docs/UpdateDomainNameServers.md)
 - [UpdateFloatingIp](docs/UpdateFloatingIp.md)
 - [UpdateHttpResource](docs/UpdateHttpResource.md)
 - [UpdateInstance](docs/UpdateInstance.md)
 - [UpdateKafkaConfigParameters](docs/UpdateKafkaConfigParameters.md)
 - [UpdateKeyRequest](docs/UpdateKeyRequest.md)
 - [UpdateKnowledgebase](docs/UpdateKnowledgebase.md)
 - [UpdateMailbox](docs/UpdateMailbox.md)
 - [UpdateMailboxV2](docs/UpdateMailboxV2.md)
 - [UpdateMailboxV2200Response](docs/UpdateMailboxV2200Response.md)
 - [UpdateMaxBot](docs/UpdateMaxBot.md)
 - [UpdateNetworkDrive](docs/UpdateNetworkDrive.md)
 - [UpdateNotificationSettingsRequest](docs/UpdateNotificationSettingsRequest.md)
 - [UpdatePerson](docs/UpdatePerson.md)
 - [UpdateProject](docs/UpdateProject.md)
 - [UpdateRule](docs/UpdateRule.md)
 - [UpdateS3Backup](docs/UpdateS3Backup.md)
 - [UpdateServer](docs/UpdateServer.md)
 - [UpdateServerConfigurator](docs/UpdateServerConfigurator.md)
 - [UpdateServerDiskBackupRequest](docs/UpdateServerDiskBackupRequest.md)
 - [UpdateServerDiskRequest](docs/UpdateServerDiskRequest.md)
 - [UpdateServerIPRequest](docs/UpdateServerIPRequest.md)
 - [UpdateServerNATRequest](docs/UpdateServerNATRequest.md)
 - [UpdateServerOSBootModeRequest](docs/UpdateServerOSBootModeRequest.md)
 - [UpdateSettings](docs/UpdateSettings.md)
 - [UpdateSkill](docs/UpdateSkill.md)
 - [UpdateStorageRequest](docs/UpdateStorageRequest.md)
 - [UpdateStorageRequestConfigurator](docs/UpdateStorageRequestConfigurator.md)
 - [UpdateStorageUser200Response](docs/UpdateStorageUser200Response.md)
 - [UpdateStorageUserRequest](docs/UpdateStorageUserRequest.md)
 - [UpdateTool](docs/UpdateTool.md)
 - [UpdateVpc](docs/UpdateVpc.md)
 - [UploadResult](docs/UploadResult.md)
 - [UploadSuccessful](docs/UploadSuccessful.md)
 - [UploadSuccessfulResponse](docs/UploadSuccessfulResponse.md)
 - [UrlStatus](docs/UrlStatus.md)
 - [Use](docs/Use.md)
 - [UserNode](docs/UserNode.md)
 - [Valkey](docs/Valkey.md)
 - [Vds](docs/Vds.md)
 - [VdsImage](docs/VdsImage.md)
 - [VdsOs](docs/VdsOs.md)
 - [VdsSoftware](docs/VdsSoftware.md)
 - [Vpc](docs/Vpc.md)
 - [VpcPort](docs/VpcPort.md)
 - [VpcPortService](docs/VpcPortService.md)
 - [VpcService](docs/VpcService.md)
 - [WorkerPresetOutApi](docs/WorkerPresetOutApi.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="Bearer"></a>
### Bearer

- **Type**: Bearer authentication (JWT)

<a id="AiGatewayKey"></a>
### AiGatewayKey

- **Type**: Bearer authentication


## Author

info@timeweb.cloud


