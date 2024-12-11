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
|response_id|string|Опционально. В большинстве случаев в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее. Также вы можете использовать этот идентификатор, чтобы убедиться, что это новый ответ на запрос и результат не был получен из кэша.|

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
|response_id|string|Опционально. В большинстве случае в ответе будет содержаться уникальный идентификатор ответа в формате UUIDv4, который однозначно указывает на ваш запрос внутри нашей системы. Если вам потребуется задать вопрос нашей поддержке, приложите к вопросу этот идентификатор — так мы сможем найти ответ на него намного быстрее.|

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
Важно учесть, что при создании большинства ресурсов внутри платформы вам будет сразу возвращен ответ от сервера со статусом `200 OK` или `201 Created` и идентификатором созданного ресурса в теле ответа, но при этом этот ресурс может быть ещё в *состоянии запуска*.

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

Обратите внимание, что все значения в этой документации являются примерами. Не полагайтесь на идентификаторы операционных систем, тарифов и т.д., используемые в примерах. Используйте соответствующую конечную точку для получения значений перед созданием ресурсов.


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
    api_instance = timeweb_cloud_api.APIKeysApi(api_client)
    create_api_key = timeweb_cloud_api.CreateApiKey() # CreateApiKey | 

    try:
        # Создание токена
        api_response = api_instance.create_token(create_api_key)
        print("The response of APIKeysApi->create_token:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling APIKeysApi->create_token: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.timeweb.cloud*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*APIKeysApi* | [**create_token**](docs/APIKeysApi.md#create_token) | **POST** /api/v1/auth/api-keys | Создание токена
*APIKeysApi* | [**delete_token**](docs/APIKeysApi.md#delete_token) | **DELETE** /api/v1/auth/api-keys/{token_id} | Удалить токен
*APIKeysApi* | [**get_tokens**](docs/APIKeysApi.md#get_tokens) | **GET** /api/v1/auth/api-keys | Получение списка выпущенных токенов
*APIKeysApi* | [**reissue_token**](docs/APIKeysApi.md#reissue_token) | **PUT** /api/v1/auth/api-keys/{token_id} | Перевыпустить токен
*APIKeysApi* | [**update_token**](docs/APIKeysApi.md#update_token) | **PATCH** /api/v1/auth/api-keys/{token_id} | Изменить токен
*AccountApi* | [**add_countries_to_allowed_list**](docs/AccountApi.md#add_countries_to_allowed_list) | **POST** /api/v1/auth/access/countries | Добавление стран в список разрешенных
*AccountApi* | [**add_ips_to_allowed_list**](docs/AccountApi.md#add_ips_to_allowed_list) | **POST** /api/v1/auth/access/ips | Добавление IP-адресов в список разрешенных
*AccountApi* | [**delete_countries_from_allowed_list**](docs/AccountApi.md#delete_countries_from_allowed_list) | **DELETE** /api/v1/auth/access/countries | Удаление стран из списка разрешенных
*AccountApi* | [**delete_ips_from_allowed_list**](docs/AccountApi.md#delete_ips_from_allowed_list) | **DELETE** /api/v1/auth/access/ips | Удаление IP-адресов из списка разрешенных
*AccountApi* | [**get_account_status**](docs/AccountApi.md#get_account_status) | **GET** /api/v1/account/status | Получение статуса аккаунта
*AccountApi* | [**get_auth_access_settings**](docs/AccountApi.md#get_auth_access_settings) | **GET** /api/v1/auth/access | Получить информацию о ограничениях авторизации пользователя
*AccountApi* | [**get_countries**](docs/AccountApi.md#get_countries) | **GET** /api/v1/auth/access/countries | Получение списка стран
*AccountApi* | [**get_finances**](docs/AccountApi.md#get_finances) | **GET** /api/v1/account/finances | Получение платежной информации
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
*DatabasesApi* | [**create_database**](docs/DatabasesApi.md#create_database) | **POST** /api/v1/dbs | Создание базы данных
*DatabasesApi* | [**create_database_backup**](docs/DatabasesApi.md#create_database_backup) | **POST** /api/v1/dbs/{db_id}/backups | Создание бэкапа базы данных
*DatabasesApi* | [**create_database_cluster**](docs/DatabasesApi.md#create_database_cluster) | **POST** /api/v1/databases | Создание кластера базы данных
*DatabasesApi* | [**create_database_instance**](docs/DatabasesApi.md#create_database_instance) | **POST** /api/v1/databases/{db_cluster_id}/instances | Создание инстанса базы данных
*DatabasesApi* | [**create_database_user**](docs/DatabasesApi.md#create_database_user) | **POST** /api/v1/databases/{db_cluster_id}/admins | Создание пользователя базы данных
*DatabasesApi* | [**delete_database**](docs/DatabasesApi.md#delete_database) | **DELETE** /api/v1/dbs/{db_id} | Удаление базы данных
*DatabasesApi* | [**delete_database_backup**](docs/DatabasesApi.md#delete_database_backup) | **DELETE** /api/v1/dbs/{db_id}/backups/{backup_id} | Удаление бэкапа базы данных
*DatabasesApi* | [**delete_database_cluster**](docs/DatabasesApi.md#delete_database_cluster) | **DELETE** /api/v1/databases/{db_cluster_id} | Удаление кластера базы данных
*DatabasesApi* | [**delete_database_instance**](docs/DatabasesApi.md#delete_database_instance) | **DELETE** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Удаление инстанса базы данных
*DatabasesApi* | [**delete_database_user**](docs/DatabasesApi.md#delete_database_user) | **DELETE** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Удаление пользователя базы данных
*DatabasesApi* | [**get_database**](docs/DatabasesApi.md#get_database) | **GET** /api/v1/dbs/{db_id} | Получение базы данных
*DatabasesApi* | [**get_database_auto_backups_settings**](docs/DatabasesApi.md#get_database_auto_backups_settings) | **GET** /api/v1/dbs/{db_id}/auto-backups | Получение настроек автобэкапов базы данных
*DatabasesApi* | [**get_database_backup**](docs/DatabasesApi.md#get_database_backup) | **GET** /api/v1/dbs/{db_id}/backups/{backup_id} | Получение бэкапа базы данных
*DatabasesApi* | [**get_database_backups**](docs/DatabasesApi.md#get_database_backups) | **GET** /api/v1/dbs/{db_id}/backups | Список бэкапов базы данных
*DatabasesApi* | [**get_database_cluster**](docs/DatabasesApi.md#get_database_cluster) | **GET** /api/v1/databases/{db_cluster_id} | Получение кластера базы данных
*DatabasesApi* | [**get_database_cluster_types**](docs/DatabasesApi.md#get_database_cluster_types) | **GET** /api/v1/database-types | Получение списка типов кластеров баз данных
*DatabasesApi* | [**get_database_clusters**](docs/DatabasesApi.md#get_database_clusters) | **GET** /api/v1/databases | Получение списка кластеров баз данных
*DatabasesApi* | [**get_database_instance**](docs/DatabasesApi.md#get_database_instance) | **GET** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Получение инстанса базы данных
*DatabasesApi* | [**get_database_instances**](docs/DatabasesApi.md#get_database_instances) | **GET** /api/v1/databases/{db_cluster_id}/instances | Получение списка инстансов баз данных
*DatabasesApi* | [**get_database_parameters**](docs/DatabasesApi.md#get_database_parameters) | **GET** /api/v1/dbs/parameters | Получение списка параметров баз данных
*DatabasesApi* | [**get_database_user**](docs/DatabasesApi.md#get_database_user) | **GET** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Получение пользователя базы данных
*DatabasesApi* | [**get_database_users**](docs/DatabasesApi.md#get_database_users) | **GET** /api/v1/databases/{db_cluster_id}/admins | Получение списка пользователей базы данных
*DatabasesApi* | [**get_databases**](docs/DatabasesApi.md#get_databases) | **GET** /api/v1/dbs | Получение списка всех баз данных
*DatabasesApi* | [**get_databases_presets**](docs/DatabasesApi.md#get_databases_presets) | **GET** /api/v1/presets/dbs | Получение списка тарифов для баз данных
*DatabasesApi* | [**restore_database_from_backup**](docs/DatabasesApi.md#restore_database_from_backup) | **PUT** /api/v1/dbs/{db_id}/backups/{backup_id} | Восстановление базы данных из бэкапа
*DatabasesApi* | [**update_database**](docs/DatabasesApi.md#update_database) | **PATCH** /api/v1/dbs/{db_id} | Обновление базы данных
*DatabasesApi* | [**update_database_auto_backups_settings**](docs/DatabasesApi.md#update_database_auto_backups_settings) | **PATCH** /api/v1/dbs/{db_id}/auto-backups | Изменение настроек автобэкапов базы данных
*DatabasesApi* | [**update_database_cluster**](docs/DatabasesApi.md#update_database_cluster) | **PATCH** /api/v1/databases/{db_cluster_id} | Изменение кластера базы данных
*DatabasesApi* | [**update_database_instance**](docs/DatabasesApi.md#update_database_instance) | **PATCH** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Изменение инстанса базы данных
*DatabasesApi* | [**update_database_user**](docs/DatabasesApi.md#update_database_user) | **PATCH** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Изменение пользователя базы данных
*DedicatedServersApi* | [**create_dedicated_server**](docs/DedicatedServersApi.md#create_dedicated_server) | **POST** /api/v1/dedicated-servers | Создание выделенного сервера
*DedicatedServersApi* | [**delete_dedicated_server**](docs/DedicatedServersApi.md#delete_dedicated_server) | **DELETE** /api/v1/dedicated-servers/{dedicated_id} | Удаление выделенного сервера
*DedicatedServersApi* | [**get_dedicated_server**](docs/DedicatedServersApi.md#get_dedicated_server) | **GET** /api/v1/dedicated-servers/{dedicated_id} | Получение выделенного сервера
*DedicatedServersApi* | [**get_dedicated_server_preset_additional_services**](docs/DedicatedServersApi.md#get_dedicated_server_preset_additional_services) | **GET** /api/v1/presets/dedicated-servers/{preset_id}/additional-services | Получение дополнительных услуг для выделенного сервера
*DedicatedServersApi* | [**get_dedicated_servers**](docs/DedicatedServersApi.md#get_dedicated_servers) | **GET** /api/v1/dedicated-servers | Получение списка выделенных серверов
*DedicatedServersApi* | [**get_dedicated_servers_presets**](docs/DedicatedServersApi.md#get_dedicated_servers_presets) | **GET** /api/v1/presets/dedicated-servers | Получение списка тарифов для выделенного сервера
*DedicatedServersApi* | [**update_dedicated_server**](docs/DedicatedServersApi.md#update_dedicated_server) | **PATCH** /api/v1/dedicated-servers/{dedicated_id} | Обновление выделенного сервера
*DomainsApi* | [**add_domain**](docs/DomainsApi.md#add_domain) | **POST** /api/v1/add-domain/{fqdn} | Добавление домена на аккаунт
*DomainsApi* | [**add_subdomain**](docs/DomainsApi.md#add_subdomain) | **POST** /api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn} | Добавление поддомена
*DomainsApi* | [**check_domain**](docs/DomainsApi.md#check_domain) | **GET** /api/v1/check-domain/{fqdn} | Проверить, доступен ли домен для регистрации
*DomainsApi* | [**create_domain_dns_record**](docs/DomainsApi.md#create_domain_dns_record) | **POST** /api/v1/domains/{fqdn}/dns-records | Добавить информацию о DNS-записи для домена или поддомена
*DomainsApi* | [**create_domain_request**](docs/DomainsApi.md#create_domain_request) | **POST** /api/v1/domains-requests | Создание заявки на регистрацию/продление/трансфер домена
*DomainsApi* | [**delete_domain**](docs/DomainsApi.md#delete_domain) | **DELETE** /api/v1/domains/{fqdn} | Удаление домена
*DomainsApi* | [**delete_domain_dns_record**](docs/DomainsApi.md#delete_domain_dns_record) | **DELETE** /api/v1/domains/{fqdn}/dns-records/{record_id} | Удалить информацию о DNS-записи для домена или поддомена
*DomainsApi* | [**delete_subdomain**](docs/DomainsApi.md#delete_subdomain) | **DELETE** /api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn} | Удаление поддомена
*DomainsApi* | [**get_domain**](docs/DomainsApi.md#get_domain) | **GET** /api/v1/domains/{fqdn} | Получение информации о домене
*DomainsApi* | [**get_domain_default_dns_records**](docs/DomainsApi.md#get_domain_default_dns_records) | **GET** /api/v1/domains/{fqdn}/default-dns-records | Получить информацию обо всех DNS-записях по умолчанию домена или поддомена
*DomainsApi* | [**get_domain_dns_records**](docs/DomainsApi.md#get_domain_dns_records) | **GET** /api/v1/domains/{fqdn}/dns-records | Получить информацию обо всех пользовательских DNS-записях домена или поддомена
*DomainsApi* | [**get_domain_name_servers**](docs/DomainsApi.md#get_domain_name_servers) | **GET** /api/v1/domains/{fqdn}/name-servers | Получение списка name-серверов домена
*DomainsApi* | [**get_domain_request**](docs/DomainsApi.md#get_domain_request) | **GET** /api/v1/domains-requests/{request_id} | Получение заявки на регистрацию/продление/трансфер домена
*DomainsApi* | [**get_domain_requests**](docs/DomainsApi.md#get_domain_requests) | **GET** /api/v1/domains-requests | Получение списка заявок на регистрацию/продление/трансфер домена
*DomainsApi* | [**get_domains**](docs/DomainsApi.md#get_domains) | **GET** /api/v1/domains | Получение списка всех доменов
*DomainsApi* | [**get_tld**](docs/DomainsApi.md#get_tld) | **GET** /api/v1/tlds/{tld_id} | Получить информацию о доменной зоне по идентификатору
*DomainsApi* | [**get_tlds**](docs/DomainsApi.md#get_tlds) | **GET** /api/v1/tlds | Получить информацию о доменных зонах
*DomainsApi* | [**update_domain_auto_prolongation**](docs/DomainsApi.md#update_domain_auto_prolongation) | **PATCH** /api/v1/domains/{fqdn} | Включение/выключение автопродления домена
*DomainsApi* | [**update_domain_dns_record**](docs/DomainsApi.md#update_domain_dns_record) | **PATCH** /api/v1/domains/{fqdn}/dns-records/{record_id} | Обновить информацию о DNS-записи домена или поддомена
*DomainsApi* | [**update_domain_name_servers**](docs/DomainsApi.md#update_domain_name_servers) | **PUT** /api/v1/domains/{fqdn}/name-servers | Изменение name-серверов домена
*DomainsApi* | [**update_domain_request**](docs/DomainsApi.md#update_domain_request) | **PATCH** /api/v1/domains-requests/{request_id} | Оплата/обновление заявки на регистрацию/продление/трансфер домена
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
*FloatingIPApi* | [**delete_floating_ip**](docs/FloatingIPApi.md#delete_floating_ip) | **DELETE** /api/v1/floating-ips/{floating_ip_id} | Удаление плавающего IP по идентификатору
*FloatingIPApi* | [**get_floating_ip**](docs/FloatingIPApi.md#get_floating_ip) | **GET** /api/v1/floating-ips/{floating_ip_id} | Получение плавающего IP
*FloatingIPApi* | [**get_floating_ips**](docs/FloatingIPApi.md#get_floating_ips) | **GET** /api/v1/floating-ips | Получение списка плавающих IP
*FloatingIPApi* | [**unbind_floating_ip**](docs/FloatingIPApi.md#unbind_floating_ip) | **POST** /api/v1/floating-ips/{floating_ip_id}/unbind | Отвязать IP от сервиса
*FloatingIPApi* | [**update_floating_ip**](docs/FloatingIPApi.md#update_floating_ip) | **PATCH** /api/v1/floating-ips/{floating_ip_id} | Изменение плавающего IP по идентификатору
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
*KubernetesApi* | [**create_cluster**](docs/KubernetesApi.md#create_cluster) | **POST** /api/v1/k8s/clusters | Создание кластера
*KubernetesApi* | [**create_cluster_node_group**](docs/KubernetesApi.md#create_cluster_node_group) | **POST** /api/v1/k8s/clusters/{cluster_id}/groups | Создание группы нод
*KubernetesApi* | [**delete_cluster**](docs/KubernetesApi.md#delete_cluster) | **DELETE** /api/v1/k8s/clusters/{cluster_id} | Удаление кластера
*KubernetesApi* | [**delete_cluster_node**](docs/KubernetesApi.md#delete_cluster_node) | **DELETE** /api/v1/k8s/clusters/{cluster_id}/nodes/{node_id} | Удаление ноды
*KubernetesApi* | [**delete_cluster_node_group**](docs/KubernetesApi.md#delete_cluster_node_group) | **DELETE** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id} | Удаление группы нод
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
*KubernetesApi* | [**get_kubernetes_presets**](docs/KubernetesApi.md#get_kubernetes_presets) | **GET** /api/v1/presets/k8s | Получение списка тарифов
*KubernetesApi* | [**increase_count_of_nodes_in_group**](docs/KubernetesApi.md#increase_count_of_nodes_in_group) | **POST** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes | Увеличение количества нод в группе на указанное количество
*KubernetesApi* | [**reduce_count_of_nodes_in_group**](docs/KubernetesApi.md#reduce_count_of_nodes_in_group) | **DELETE** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes | Уменьшение количества нод в группе на указанное количество
*KubernetesApi* | [**update_cluster**](docs/KubernetesApi.md#update_cluster) | **PATCH** /api/v1/k8s/clusters/{cluster_id} | Обновление информации о кластере
*LocationsApi* | [**get_locations**](docs/LocationsApi.md#get_locations) | **GET** /api/v2/locations | Получение списка локаций
*MailApi* | [**create_domain_mailbox**](docs/MailApi.md#create_domain_mailbox) | **POST** /api/v1/mail/domains/{domain} | Создание почтового ящика
*MailApi* | [**delete_mailbox**](docs/MailApi.md#delete_mailbox) | **DELETE** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Удаление почтового ящика
*MailApi* | [**get_domain_mail_info**](docs/MailApi.md#get_domain_mail_info) | **GET** /api/v1/mail/domains/{domain}/info | Получение почтовой информации о домене
*MailApi* | [**get_domain_mailboxes**](docs/MailApi.md#get_domain_mailboxes) | **GET** /api/v1/mail/domains/{domain} | Получение списка почтовых ящиков домена
*MailApi* | [**get_mail_quota**](docs/MailApi.md#get_mail_quota) | **GET** /api/v1/mail/quota | Получение квоты почты аккаунта
*MailApi* | [**get_mailbox**](docs/MailApi.md#get_mailbox) | **GET** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Получение почтового ящика
*MailApi* | [**get_mailboxes**](docs/MailApi.md#get_mailboxes) | **GET** /api/v1/mail | Получение списка почтовых ящиков аккаунта
*MailApi* | [**update_domain_mail_info**](docs/MailApi.md#update_domain_mail_info) | **PATCH** /api/v1/mail/domains/{domain}/info | Изменение почтовой информации о домене
*MailApi* | [**update_mail_quota**](docs/MailApi.md#update_mail_quota) | **PATCH** /api/v1/mail/quota | Изменение квоты почты аккаунта
*MailApi* | [**update_mailbox**](docs/MailApi.md#update_mailbox) | **PATCH** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Изменение почтового ящика
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
*ProjectsApi* | [**get_project**](docs/ProjectsApi.md#get_project) | **GET** /api/v1/projects/{project_id} | Получение проекта по идентификатору
*ProjectsApi* | [**get_project_balancers**](docs/ProjectsApi.md#get_project_balancers) | **GET** /api/v1/projects/{project_id}/resources/balancers | Получение списка балансировщиков проекта
*ProjectsApi* | [**get_project_clusters**](docs/ProjectsApi.md#get_project_clusters) | **GET** /api/v1/projects/{project_id}/resources/clusters | Получение списка кластеров проекта
*ProjectsApi* | [**get_project_databases**](docs/ProjectsApi.md#get_project_databases) | **GET** /api/v1/projects/{project_id}/resources/databases | Получение списка баз данных проекта
*ProjectsApi* | [**get_project_dedicated_servers**](docs/ProjectsApi.md#get_project_dedicated_servers) | **GET** /api/v1/projects/{project_id}/resources/dedicated | Получение списка выделенных серверов проекта
*ProjectsApi* | [**get_project_servers**](docs/ProjectsApi.md#get_project_servers) | **GET** /api/v1/projects/{project_id}/resources/servers | Получение списка серверов проекта
*ProjectsApi* | [**get_project_storages**](docs/ProjectsApi.md#get_project_storages) | **GET** /api/v1/projects/{project_id}/resources/buckets | Получение списка хранилищ проекта
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /api/v1/projects | Получение списка проектов
*ProjectsApi* | [**transfer_resource_to_another_project**](docs/ProjectsApi.md#transfer_resource_to_another_project) | **PUT** /api/v1/projects/{project_id}/resources/transfer | Перенести ресурс в другой проект
*ProjectsApi* | [**update_project**](docs/ProjectsApi.md#update_project) | **PUT** /api/v1/projects/{project_id} | Изменение проекта
*S3Api* | [**add_storage_subdomain_certificate**](docs/S3Api.md#add_storage_subdomain_certificate) | **POST** /api/v1/storages/certificates/generate | Добавление сертификата для поддомена хранилища
*S3Api* | [**add_storage_subdomains**](docs/S3Api.md#add_storage_subdomains) | **POST** /api/v1/storages/buckets/{bucket_id}/subdomains | Добавление поддоменов для хранилища
*S3Api* | [**copy_storage_file**](docs/S3Api.md#copy_storage_file) | **POST** /api/v1/storages/buckets/{bucket_id}/object-manager/copy | Копирование файла/директории в хранилище
*S3Api* | [**create_folder_in_storage**](docs/S3Api.md#create_folder_in_storage) | **POST** /api/v1/storages/buckets/{bucket_id}/object-manager/mkdir | Создание директории в хранилище
*S3Api* | [**create_storage**](docs/S3Api.md#create_storage) | **POST** /api/v1/storages/buckets | Создание хранилища
*S3Api* | [**delete_storage**](docs/S3Api.md#delete_storage) | **DELETE** /api/v1/storages/buckets/{bucket_id} | Удаление хранилища на аккаунте
*S3Api* | [**delete_storage_file**](docs/S3Api.md#delete_storage_file) | **DELETE** /api/v1/storages/buckets/{bucket_id}/object-manager/remove | Удаление файла/директории в хранилище
*S3Api* | [**delete_storage_subdomains**](docs/S3Api.md#delete_storage_subdomains) | **DELETE** /api/v1/storages/buckets/{bucket_id}/subdomains | Удаление поддоменов хранилища
*S3Api* | [**get_storage_files_list**](docs/S3Api.md#get_storage_files_list) | **GET** /api/v1/storages/buckets/{bucket_id}/object-manager/list | Получение списка файлов в хранилище по префиксу
*S3Api* | [**get_storage_subdomains**](docs/S3Api.md#get_storage_subdomains) | **GET** /api/v1/storages/buckets/{bucket_id}/subdomains | Получение списка поддоменов хранилища
*S3Api* | [**get_storage_transfer_status**](docs/S3Api.md#get_storage_transfer_status) | **GET** /api/v1/storages/buckets/{bucket_id}/transfer-status | Получение статуса переноса хранилища от стороннего S3 в Timeweb Cloud
*S3Api* | [**get_storage_users**](docs/S3Api.md#get_storage_users) | **GET** /api/v1/storages/users | Получение списка пользователей хранилищ аккаунта
*S3Api* | [**get_storages**](docs/S3Api.md#get_storages) | **GET** /api/v1/storages/buckets | Получение списка хранилищ аккаунта
*S3Api* | [**get_storages_presets**](docs/S3Api.md#get_storages_presets) | **GET** /api/v1/presets/storages | Получение списка тарифов для хранилищ
*S3Api* | [**rename_storage_file**](docs/S3Api.md#rename_storage_file) | **POST** /api/v1/storages/buckets/{bucket_id}/object-manager/rename | Переименование файла/директории в хранилище
*S3Api* | [**transfer_storage**](docs/S3Api.md#transfer_storage) | **POST** /api/v1/storages/transfer | Перенос хранилища от стороннего провайдера S3 в Timeweb Cloud
*S3Api* | [**update_storage**](docs/S3Api.md#update_storage) | **PATCH** /api/v1/storages/buckets/{bucket_id} | Изменение хранилища на аккаунте
*S3Api* | [**update_storage_user**](docs/S3Api.md#update_storage_user) | **PATCH** /api/v1/storages/users/{user_id} | Изменение пароля пользователя-администратора хранилища
*S3Api* | [**upload_file_to_storage**](docs/S3Api.md#upload_file_to_storage) | **POST** /api/v1/storages/buckets/{bucket_id}/object-manager/upload | Загрузка файлов в хранилище
*SSHApi* | [**add_key_to_server**](docs/SSHApi.md#add_key_to_server) | **POST** /api/v1/servers/{server_id}/ssh-keys | Добавление SSH-ключей на сервер
*SSHApi* | [**create_key**](docs/SSHApi.md#create_key) | **POST** /api/v1/ssh-keys | Создание SSH-ключа
*SSHApi* | [**delete_key**](docs/SSHApi.md#delete_key) | **DELETE** /api/v1/ssh-keys/{ssh_key_id} | Удаление SSH-ключа по уникальному идентификатору
*SSHApi* | [**delete_key_from_server**](docs/SSHApi.md#delete_key_from_server) | **DELETE** /api/v1/servers/{server_id}/ssh-keys/{ssh_key_id} | Удаление SSH-ключей с сервера
*SSHApi* | [**get_key**](docs/SSHApi.md#get_key) | **GET** /api/v1/ssh-keys/{ssh_key_id} | Получение SSH-ключа по уникальному идентификатору
*SSHApi* | [**get_keys**](docs/SSHApi.md#get_keys) | **GET** /api/v1/ssh-keys | Получение списка SSH-ключей
*SSHApi* | [**update_key**](docs/SSHApi.md#update_key) | **PATCH** /api/v1/ssh-keys/{ssh_key_id} | Изменение SSH-ключа по уникальному идентификатору
*ServersApi* | [**add_server_ip**](docs/ServersApi.md#add_server_ip) | **POST** /api/v1/servers/{server_id}/ips | Добавление IP-адреса сервера
*ServersApi* | [**clone_server**](docs/ServersApi.md#clone_server) | **POST** /api/v1/servers/{server_id}/clone | Клонирование сервера
*ServersApi* | [**create_server**](docs/ServersApi.md#create_server) | **POST** /api/v1/servers | Создание сервера
*ServersApi* | [**create_server_disk**](docs/ServersApi.md#create_server_disk) | **POST** /api/v1/servers/{server_id}/disks | Создание диска сервера
*ServersApi* | [**create_server_disk_backup**](docs/ServersApi.md#create_server_disk_backup) | **POST** /api/v1/servers/{server_id}/disks/{disk_id}/backups | Создание бэкапа диска сервера
*ServersApi* | [**delete_server**](docs/ServersApi.md#delete_server) | **DELETE** /api/v1/servers/{server_id} | Удаление сервера
*ServersApi* | [**delete_server_disk**](docs/ServersApi.md#delete_server_disk) | **DELETE** /api/v1/servers/{server_id}/disks/{disk_id} | Удаление диска сервера
*ServersApi* | [**delete_server_disk_backup**](docs/ServersApi.md#delete_server_disk_backup) | **DELETE** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id} | Удаление бэкапа диска сервера
*ServersApi* | [**delete_server_ip**](docs/ServersApi.md#delete_server_ip) | **DELETE** /api/v1/servers/{server_id}/ips | Удаление IP-адреса сервера
*ServersApi* | [**get_configurators**](docs/ServersApi.md#get_configurators) | **GET** /api/v1/configurator/servers | Получение списка конфигураторов серверов
*ServersApi* | [**get_os_list**](docs/ServersApi.md#get_os_list) | **GET** /api/v1/os/servers | Получение списка операционных систем
*ServersApi* | [**get_server**](docs/ServersApi.md#get_server) | **GET** /api/v1/servers/{server_id} | Получение сервера
*ServersApi* | [**get_server_disk**](docs/ServersApi.md#get_server_disk) | **GET** /api/v1/servers/{server_id}/disks/{disk_id} | Получение диска сервера
*ServersApi* | [**get_server_disk_auto_backup_settings**](docs/ServersApi.md#get_server_disk_auto_backup_settings) | **GET** /api/v1/servers/{server_id}/disks/{disk_id}/auto-backups | Получить настройки автобэкапов диска сервера
*ServersApi* | [**get_server_disk_backup**](docs/ServersApi.md#get_server_disk_backup) | **GET** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id} | Получение бэкапа диска сервера
*ServersApi* | [**get_server_disk_backups**](docs/ServersApi.md#get_server_disk_backups) | **GET** /api/v1/servers/{server_id}/disks/{disk_id}/backups | Получение списка бэкапов диска сервера
*ServersApi* | [**get_server_disks**](docs/ServersApi.md#get_server_disks) | **GET** /api/v1/servers/{server_id}/disks | Получение списка дисков сервера
*ServersApi* | [**get_server_ips**](docs/ServersApi.md#get_server_ips) | **GET** /api/v1/servers/{server_id}/ips | Получение списка IP-адресов сервера
*ServersApi* | [**get_server_logs**](docs/ServersApi.md#get_server_logs) | **GET** /api/v1/servers/{server_id}/logs | Получение списка логов сервера
*ServersApi* | [**get_server_statistics**](docs/ServersApi.md#get_server_statistics) | **GET** /api/v1/servers/{server_id}/statistics | Получение статистики сервера
*ServersApi* | [**get_servers**](docs/ServersApi.md#get_servers) | **GET** /api/v1/servers | Получение списка серверов
*ServersApi* | [**get_servers_presets**](docs/ServersApi.md#get_servers_presets) | **GET** /api/v1/presets/servers | Получение списка тарифов серверов
*ServersApi* | [**get_software**](docs/ServersApi.md#get_software) | **GET** /api/v1/software/servers | Получение списка ПО из маркетплейса
*ServersApi* | [**hard_shutdown_server**](docs/ServersApi.md#hard_shutdown_server) | **POST** /api/v1/servers/{server_id}/hard-shutdown | Принудительное выключение сервера
*ServersApi* | [**image_unmount_and_server_reload**](docs/ServersApi.md#image_unmount_and_server_reload) | **POST** /api/v1/servers/{server_id}/image-unmount | Отмонтирование ISO образа и перезагрузка сервера
*ServersApi* | [**perform_action_on_backup**](docs/ServersApi.md#perform_action_on_backup) | **POST** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id}/action | Выполнение действия над бэкапом диска сервера
*ServersApi* | [**perform_action_on_server**](docs/ServersApi.md#perform_action_on_server) | **POST** /api/v1/servers/{server_id}/action | Выполнение действия над сервером
*ServersApi* | [**reboot_server**](docs/ServersApi.md#reboot_server) | **POST** /api/v1/servers/{server_id}/reboot | Перезагрузка сервера
*ServersApi* | [**reset_server_password**](docs/ServersApi.md#reset_server_password) | **POST** /api/v1/servers/{server_id}/reset-password | Сброс пароля сервера
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
*VPCApi* | [**delete_vpc**](docs/VPCApi.md#delete_vpc) | **DELETE** /api/v1/vpcs/{vpc_id} | Удаление VPC по идентификатору сети
*VPCApi* | [**get_vpc**](docs/VPCApi.md#get_vpc) | **GET** /api/v2/vpcs/{vpc_id} | Получение VPC
*VPCApi* | [**get_vpc_ports**](docs/VPCApi.md#get_vpc_ports) | **GET** /api/v1/vpcs/{vpc_id}/ports | Получение списка портов для VPC
*VPCApi* | [**get_vpc_services**](docs/VPCApi.md#get_vpc_services) | **GET** /api/v2/vpcs/{vpc_id}/services | Получение списка сервисов в VPC
*VPCApi* | [**get_vpcs**](docs/VPCApi.md#get_vpcs) | **GET** /api/v2/vpcs | Получение списка VPCs
*VPCApi* | [**update_vpcs**](docs/VPCApi.md#update_vpcs) | **PATCH** /api/v2/vpcs/{vpc_id} | Изменение VPC по идентификатору сети


## Documentation For Models

 - [AddBalancerToProject200Response](docs/AddBalancerToProject200Response.md)
 - [AddBalancerToProjectRequest](docs/AddBalancerToProjectRequest.md)
 - [AddBitbucket](docs/AddBitbucket.md)
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
 - [AddedSubdomain](docs/AddedSubdomain.md)
 - [ApiKey](docs/ApiKey.md)
 - [App](docs/App.md)
 - [AppConfiguration](docs/AppConfiguration.md)
 - [AppDiskStatus](docs/AppDiskStatus.md)
 - [AppProvider](docs/AppProvider.md)
 - [AppsPresets](docs/AppsPresets.md)
 - [AutoBackup](docs/AutoBackup.md)
 - [AutoReplyIsDisabled](docs/AutoReplyIsDisabled.md)
 - [AutoReplyIsEnabled](docs/AutoReplyIsEnabled.md)
 - [AvailabilityZone](docs/AvailabilityZone.md)
 - [AvailableFrameworks](docs/AvailableFrameworks.md)
 - [Backup](docs/Backup.md)
 - [Balancer](docs/Balancer.md)
 - [BaseError](docs/BaseError.md)
 - [BindFloatingIp](docs/BindFloatingIp.md)
 - [Bonus](docs/Bonus.md)
 - [Branch](docs/Branch.md)
 - [Bucket](docs/Bucket.md)
 - [BucketDiskStats](docs/BucketDiskStats.md)
 - [BucketUser](docs/BucketUser.md)
 - [CheckDomain200Response](docs/CheckDomain200Response.md)
 - [ClusterEdit](docs/ClusterEdit.md)
 - [ClusterIn](docs/ClusterIn.md)
 - [ClusterOut](docs/ClusterOut.md)
 - [ClusterResponse](docs/ClusterResponse.md)
 - [Clusterk8s](docs/Clusterk8s.md)
 - [ClustersResponse](docs/ClustersResponse.md)
 - [Commit](docs/Commit.md)
 - [ConfigParameters](docs/ConfigParameters.md)
 - [CopyStorageFileRequest](docs/CopyStorageFileRequest.md)
 - [CreateAdmin](docs/CreateAdmin.md)
 - [CreateApiKey](docs/CreateApiKey.md)
 - [CreateApp](docs/CreateApp.md)
 - [CreateApp201Response](docs/CreateApp201Response.md)
 - [CreateBalancer](docs/CreateBalancer.md)
 - [CreateBalancer200Response](docs/CreateBalancer200Response.md)
 - [CreateBalancerRule200Response](docs/CreateBalancerRule200Response.md)
 - [CreateCluster](docs/CreateCluster.md)
 - [CreateClusterAdmin](docs/CreateClusterAdmin.md)
 - [CreateClusterInstance](docs/CreateClusterInstance.md)
 - [CreateDatabase201Response](docs/CreateDatabase201Response.md)
 - [CreateDatabaseBackup201Response](docs/CreateDatabaseBackup201Response.md)
 - [CreateDatabaseCluster201Response](docs/CreateDatabaseCluster201Response.md)
 - [CreateDatabaseInstance201Response](docs/CreateDatabaseInstance201Response.md)
 - [CreateDatabaseUser201Response](docs/CreateDatabaseUser201Response.md)
 - [CreateDb](docs/CreateDb.md)
 - [CreateDbAutoBackups](docs/CreateDbAutoBackups.md)
 - [CreateDedicatedServer](docs/CreateDedicatedServer.md)
 - [CreateDedicatedServer201Response](docs/CreateDedicatedServer201Response.md)
 - [CreateDeploy201Response](docs/CreateDeploy201Response.md)
 - [CreateDeployRequest](docs/CreateDeployRequest.md)
 - [CreateDns](docs/CreateDns.md)
 - [CreateDomainDNSRecord201Response](docs/CreateDomainDNSRecord201Response.md)
 - [CreateDomainMailbox201Response](docs/CreateDomainMailbox201Response.md)
 - [CreateDomainMailboxRequest](docs/CreateDomainMailboxRequest.md)
 - [CreateDomainRequest201Response](docs/CreateDomainRequest201Response.md)
 - [CreateFloatingIp](docs/CreateFloatingIp.md)
 - [CreateFloatingIp201Response](docs/CreateFloatingIp201Response.md)
 - [CreateFolderInStorageRequest](docs/CreateFolderInStorageRequest.md)
 - [CreateInstance](docs/CreateInstance.md)
 - [CreateKey201Response](docs/CreateKey201Response.md)
 - [CreateKeyRequest](docs/CreateKeyRequest.md)
 - [CreateProject](docs/CreateProject.md)
 - [CreateProject201Response](docs/CreateProject201Response.md)
 - [CreateRule](docs/CreateRule.md)
 - [CreateServer](docs/CreateServer.md)
 - [CreateServer201Response](docs/CreateServer201Response.md)
 - [CreateServerConfiguration](docs/CreateServerConfiguration.md)
 - [CreateServerDisk201Response](docs/CreateServerDisk201Response.md)
 - [CreateServerDiskBackup201Response](docs/CreateServerDiskBackup201Response.md)
 - [CreateServerDiskBackupRequest](docs/CreateServerDiskBackupRequest.md)
 - [CreateServerDiskRequest](docs/CreateServerDiskRequest.md)
 - [CreateStorage201Response](docs/CreateStorage201Response.md)
 - [CreateStorageRequest](docs/CreateStorageRequest.md)
 - [CreateToken201Response](docs/CreateToken201Response.md)
 - [CreateVPC201Response](docs/CreateVPC201Response.md)
 - [CreateVpc](docs/CreateVpc.md)
 - [CreatedApiKey](docs/CreatedApiKey.md)
 - [DatabaseAdmin](docs/DatabaseAdmin.md)
 - [DatabaseCluster](docs/DatabaseCluster.md)
 - [DatabaseClusterDiskStats](docs/DatabaseClusterDiskStats.md)
 - [DatabaseInstance](docs/DatabaseInstance.md)
 - [DatabaseType](docs/DatabaseType.md)
 - [DatabaseTypeRequirements](docs/DatabaseTypeRequirements.md)
 - [Db](docs/Db.md)
 - [DbDiskStats](docs/DbDiskStats.md)
 - [DbType](docs/DbType.md)
 - [DedicatedServer](docs/DedicatedServer.md)
 - [DedicatedServerAdditionalService](docs/DedicatedServerAdditionalService.md)
 - [DedicatedServerPreset](docs/DedicatedServerPreset.md)
 - [DedicatedServerPresetCpu](docs/DedicatedServerPresetCpu.md)
 - [DedicatedServerPresetDisk](docs/DedicatedServerPresetDisk.md)
 - [DedicatedServerPresetMemory](docs/DedicatedServerPresetMemory.md)
 - [DeleteBalancer200Response](docs/DeleteBalancer200Response.md)
 - [DeleteCluster200Response](docs/DeleteCluster200Response.md)
 - [DeleteCountriesFromAllowedList200Response](docs/DeleteCountriesFromAllowedList200Response.md)
 - [DeleteCountriesFromAllowedListRequest](docs/DeleteCountriesFromAllowedListRequest.md)
 - [DeleteDatabase200Response](docs/DeleteDatabase200Response.md)
 - [DeleteDatabaseCluster200Response](docs/DeleteDatabaseCluster200Response.md)
 - [DeleteIPsFromAllowedList200Response](docs/DeleteIPsFromAllowedList200Response.md)
 - [DeleteIPsFromAllowedListRequest](docs/DeleteIPsFromAllowedListRequest.md)
 - [DeleteServer200Response](docs/DeleteServer200Response.md)
 - [DeleteServerIPRequest](docs/DeleteServerIPRequest.md)
 - [DeleteServiceResponse](docs/DeleteServiceResponse.md)
 - [DeleteStorage200Response](docs/DeleteStorage200Response.md)
 - [DeleteStorageFileRequest](docs/DeleteStorageFileRequest.md)
 - [Deploy](docs/Deploy.md)
 - [DeployStatus](docs/DeployStatus.md)
 - [DnsRecord](docs/DnsRecord.md)
 - [DnsRecordData](docs/DnsRecordData.md)
 - [Domain](docs/Domain.md)
 - [DomainInfo](docs/DomainInfo.md)
 - [DomainNameServer](docs/DomainNameServer.md)
 - [DomainPaymentPeriod](docs/DomainPaymentPeriod.md)
 - [DomainPrimeType](docs/DomainPrimeType.md)
 - [DomainProlong](docs/DomainProlong.md)
 - [DomainRegister](docs/DomainRegister.md)
 - [DomainRequest](docs/DomainRequest.md)
 - [DomainTransfer](docs/DomainTransfer.md)
 - [EditApiKey](docs/EditApiKey.md)
 - [Finances](docs/Finances.md)
 - [FirewallGroupInAPI](docs/FirewallGroupInAPI.md)
 - [FirewallGroupOutAPI](docs/FirewallGroupOutAPI.md)
 - [FirewallGroupOutResponse](docs/FirewallGroupOutResponse.md)
 - [FirewallGroupResourceOutAPI](docs/FirewallGroupResourceOutAPI.md)
 - [FirewallGroupResourceOutResponse](docs/FirewallGroupResourceOutResponse.md)
 - [FirewallGroupResourcesOutResponse](docs/FirewallGroupResourcesOutResponse.md)
 - [FirewallGroupsOutResponse](docs/FirewallGroupsOutResponse.md)
 - [FirewallRuleDirection](docs/FirewallRuleDirection.md)
 - [FirewallRuleInAPI](docs/FirewallRuleInAPI.md)
 - [FirewallRuleOutAPI](docs/FirewallRuleOutAPI.md)
 - [FirewallRuleOutResponse](docs/FirewallRuleOutResponse.md)
 - [FirewallRuleProtocol](docs/FirewallRuleProtocol.md)
 - [FirewallRulesOutResponse](docs/FirewallRulesOutResponse.md)
 - [FloatingIp](docs/FloatingIp.md)
 - [ForwardingIncomingIsDisabled](docs/ForwardingIncomingIsDisabled.md)
 - [ForwardingIncomingIsEnabled](docs/ForwardingIncomingIsEnabled.md)
 - [ForwardingOutgoingIsDisabled](docs/ForwardingOutgoingIsDisabled.md)
 - [ForwardingOutgoingIsEnabled](docs/ForwardingOutgoingIsEnabled.md)
 - [Frameworks](docs/Frameworks.md)
 - [Free](docs/Free.md)
 - [GetAccountStatus200Response](docs/GetAccountStatus200Response.md)
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
 - [GetCommits200Response](docs/GetCommits200Response.md)
 - [GetConfigurators200Response](docs/GetConfigurators200Response.md)
 - [GetCountries200Response](docs/GetCountries200Response.md)
 - [GetDatabaseAutoBackupsSettings200Response](docs/GetDatabaseAutoBackupsSettings200Response.md)
 - [GetDatabaseBackups200Response](docs/GetDatabaseBackups200Response.md)
 - [GetDatabaseClusterTypes200Response](docs/GetDatabaseClusterTypes200Response.md)
 - [GetDatabaseClusters200Response](docs/GetDatabaseClusters200Response.md)
 - [GetDatabaseInstances200Response](docs/GetDatabaseInstances200Response.md)
 - [GetDatabaseUsers200Response](docs/GetDatabaseUsers200Response.md)
 - [GetDatabases200Response](docs/GetDatabases200Response.md)
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
 - [GetLocations200Response](docs/GetLocations200Response.md)
 - [GetMailQuota200Response](docs/GetMailQuota200Response.md)
 - [GetMailboxes200Response](docs/GetMailboxes200Response.md)
 - [GetNotificationSettings200Response](docs/GetNotificationSettings200Response.md)
 - [GetOsList200Response](docs/GetOsList200Response.md)
 - [GetProjectClusters200Response](docs/GetProjectClusters200Response.md)
 - [GetProjectDatabases200Response](docs/GetProjectDatabases200Response.md)
 - [GetProjectStorages200Response](docs/GetProjectStorages200Response.md)
 - [GetProjects200Response](docs/GetProjects200Response.md)
 - [GetProviders200Response](docs/GetProviders200Response.md)
 - [GetRepositories200Response](docs/GetRepositories200Response.md)
 - [GetServerDiskAutoBackupSettings200Response](docs/GetServerDiskAutoBackupSettings200Response.md)
 - [GetServerDiskBackup200Response](docs/GetServerDiskBackup200Response.md)
 - [GetServerDiskBackups200Response](docs/GetServerDiskBackups200Response.md)
 - [GetServerDisks200Response](docs/GetServerDisks200Response.md)
 - [GetServerIPs200Response](docs/GetServerIPs200Response.md)
 - [GetServerLogs200Response](docs/GetServerLogs200Response.md)
 - [GetServerStatistics200Response](docs/GetServerStatistics200Response.md)
 - [GetServers200Response](docs/GetServers200Response.md)
 - [GetServersPresets200Response](docs/GetServersPresets200Response.md)
 - [GetSoftware200Response](docs/GetSoftware200Response.md)
 - [GetStorageFilesList200Response](docs/GetStorageFilesList200Response.md)
 - [GetStorageSubdomains200Response](docs/GetStorageSubdomains200Response.md)
 - [GetStorageTransferStatus200Response](docs/GetStorageTransferStatus200Response.md)
 - [GetStorageUsers200Response](docs/GetStorageUsers200Response.md)
 - [GetStoragesPresets200Response](docs/GetStoragesPresets200Response.md)
 - [GetTLD200Response](docs/GetTLD200Response.md)
 - [GetTLDs200Response](docs/GetTLDs200Response.md)
 - [GetTokens200Response](docs/GetTokens200Response.md)
 - [GetVPCPorts200Response](docs/GetVPCPorts200Response.md)
 - [GetVPCServices200Response](docs/GetVPCServices200Response.md)
 - [GetVPCs200Response](docs/GetVPCs200Response.md)
 - [ImageDownloadAPI](docs/ImageDownloadAPI.md)
 - [ImageDownloadResponse](docs/ImageDownloadResponse.md)
 - [ImageDownloadsResponse](docs/ImageDownloadsResponse.md)
 - [ImageInAPI](docs/ImageInAPI.md)
 - [ImageOutAPI](docs/ImageOutAPI.md)
 - [ImageOutResponse](docs/ImageOutResponse.md)
 - [ImageStatus](docs/ImageStatus.md)
 - [ImageUpdateAPI](docs/ImageUpdateAPI.md)
 - [ImageUrlAuth](docs/ImageUrlAuth.md)
 - [ImageUrlIn](docs/ImageUrlIn.md)
 - [ImagesOutResponse](docs/ImagesOutResponse.md)
 - [Invoice](docs/Invoice.md)
 - [K8SVersionsResponse](docs/K8SVersionsResponse.md)
 - [Location](docs/Location.md)
 - [LocationDto](docs/LocationDto.md)
 - [Mailbox](docs/Mailbox.md)
 - [MailboxAutoReply](docs/MailboxAutoReply.md)
 - [MailboxForwardingIncoming](docs/MailboxForwardingIncoming.md)
 - [MailboxForwardingOutgoing](docs/MailboxForwardingOutgoing.md)
 - [MailboxSpamFilter](docs/MailboxSpamFilter.md)
 - [MasterPresetOutApi](docs/MasterPresetOutApi.md)
 - [Meta](docs/Meta.md)
 - [Network](docs/Network.md)
 - [NetworkDriversResponse](docs/NetworkDriversResponse.md)
 - [NodeCount](docs/NodeCount.md)
 - [NodeGroupIn](docs/NodeGroupIn.md)
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
 - [PerformActionOnBackupRequest](docs/PerformActionOnBackupRequest.md)
 - [PerformActionOnServerRequest](docs/PerformActionOnServerRequest.md)
 - [Policy](docs/Policy.md)
 - [PresetsBalancer](docs/PresetsBalancer.md)
 - [PresetsDbs](docs/PresetsDbs.md)
 - [PresetsResponse](docs/PresetsResponse.md)
 - [PresetsStorage](docs/PresetsStorage.md)
 - [Project](docs/Project.md)
 - [ProjectResource](docs/ProjectResource.md)
 - [Provider](docs/Provider.md)
 - [Providers](docs/Providers.md)
 - [Quota](docs/Quota.md)
 - [RefreshApiKey](docs/RefreshApiKey.md)
 - [RemoveCountries](docs/RemoveCountries.md)
 - [RemoveIps](docs/RemoveIps.md)
 - [RenameStorageFileRequest](docs/RenameStorageFileRequest.md)
 - [Repository](docs/Repository.md)
 - [Resource](docs/Resource.md)
 - [ResourceTransfer](docs/ResourceTransfer.md)
 - [ResourceType](docs/ResourceType.md)
 - [Resources](docs/Resources.md)
 - [ResourcesResponse](docs/ResourcesResponse.md)
 - [Rule](docs/Rule.md)
 - [S3Object](docs/S3Object.md)
 - [S3ObjectOwner](docs/S3ObjectOwner.md)
 - [S3Subdomain](docs/S3Subdomain.md)
 - [SchemasBaseError](docs/SchemasBaseError.md)
 - [ServerBackup](docs/ServerBackup.md)
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
 - [SettingCondition](docs/SettingCondition.md)
 - [SpamFilterIsDisabled](docs/SpamFilterIsDisabled.md)
 - [SpamFilterIsEnabled](docs/SpamFilterIsEnabled.md)
 - [SshKey](docs/SshKey.md)
 - [Status](docs/Status.md)
 - [StatusCompanyInfo](docs/StatusCompanyInfo.md)
 - [Subdomain](docs/Subdomain.md)
 - [TopLevelDomain](docs/TopLevelDomain.md)
 - [TransferStatus](docs/TransferStatus.md)
 - [TransferStorageRequest](docs/TransferStorageRequest.md)
 - [URLType](docs/URLType.md)
 - [UpdateAdmin](docs/UpdateAdmin.md)
 - [UpdateAppSettings200Response](docs/UpdateAppSettings200Response.md)
 - [UpdateAuthRestrictionsByCountriesRequest](docs/UpdateAuthRestrictionsByCountriesRequest.md)
 - [UpdateBalancer](docs/UpdateBalancer.md)
 - [UpdateCluster](docs/UpdateCluster.md)
 - [UpdateDb](docs/UpdateDb.md)
 - [UpdateDedicatedServerRequest](docs/UpdateDedicatedServerRequest.md)
 - [UpdateDomain](docs/UpdateDomain.md)
 - [UpdateDomainAutoProlongation200Response](docs/UpdateDomainAutoProlongation200Response.md)
 - [UpdateDomainMailInfoRequest](docs/UpdateDomainMailInfoRequest.md)
 - [UpdateDomainNameServers](docs/UpdateDomainNameServers.md)
 - [UpdateFloatingIp](docs/UpdateFloatingIp.md)
 - [UpdateInstance](docs/UpdateInstance.md)
 - [UpdateKeyRequest](docs/UpdateKeyRequest.md)
 - [UpdateMailQuotaRequest](docs/UpdateMailQuotaRequest.md)
 - [UpdateMailbox](docs/UpdateMailbox.md)
 - [UpdateNotificationSettingsRequest](docs/UpdateNotificationSettingsRequest.md)
 - [UpdateProject](docs/UpdateProject.md)
 - [UpdateRule](docs/UpdateRule.md)
 - [UpdateServer](docs/UpdateServer.md)
 - [UpdateServerConfigurator](docs/UpdateServerConfigurator.md)
 - [UpdateServerDiskBackupRequest](docs/UpdateServerDiskBackupRequest.md)
 - [UpdateServerDiskRequest](docs/UpdateServerDiskRequest.md)
 - [UpdateServerIPRequest](docs/UpdateServerIPRequest.md)
 - [UpdateServerNATRequest](docs/UpdateServerNATRequest.md)
 - [UpdateServerOSBootModeRequest](docs/UpdateServerOSBootModeRequest.md)
 - [UpdateStorageRequest](docs/UpdateStorageRequest.md)
 - [UpdateStorageUser200Response](docs/UpdateStorageUser200Response.md)
 - [UpdateStorageUserRequest](docs/UpdateStorageUserRequest.md)
 - [UpdateToken200Response](docs/UpdateToken200Response.md)
 - [UpdateVpc](docs/UpdateVpc.md)
 - [UpdeteSettings](docs/UpdeteSettings.md)
 - [UploadSuccessful](docs/UploadSuccessful.md)
 - [UploadSuccessfulResponse](docs/UploadSuccessfulResponse.md)
 - [UrlStatus](docs/UrlStatus.md)
 - [Use](docs/Use.md)
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


## Author

info@timeweb.cloud


