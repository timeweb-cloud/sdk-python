# timeweb_cloud_api.AIAgentsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_additional_token_package**](AIAgentsApi.md#add_additional_token_package) | **POST** /api/v1/cloud-ai/agents/{id}/add-additional-token-package | Добавление дополнительного пакета токенов
[**change_agent_model**](AIAgentsApi.md#change_agent_model) | **PATCH** /api/v1/cloud-ai/agents/{id}/model | Смена модели AI агента
[**create_agent**](AIAgentsApi.md#create_agent) | **POST** /api/v1/cloud-ai/agents | Создание AI агента
[**create_agent_entity_limit**](AIAgentsApi.md#create_agent_entity_limit) | **POST** /api/v1/cloud-ai/agents/{id}/entity-limits | Создание лимита агента
[**create_agent_v2**](AIAgentsApi.md#create_agent_v2) | **POST** /api/v2/cloud-ai/agents | Создание AI агента
[**delete_agent**](AIAgentsApi.md#delete_agent) | **DELETE** /api/v1/cloud-ai/agents/{id} | Удаление AI агента
[**delete_agent_entity_limit**](AIAgentsApi.md#delete_agent_entity_limit) | **DELETE** /api/v1/cloud-ai/agents/{id}/entity-limits/{limit_id} | Удаление лимита агента
[**export_agent_chats_csv**](AIAgentsApi.md#export_agent_chats_csv) | **GET** /api/v1/cloud-ai/agents/{id}/chats/docs | Выгрузка чатов агента в CSV
[**get_agent**](AIAgentsApi.md#get_agent) | **GET** /api/v1/cloud-ai/agents/{id} | Получение AI агента
[**get_agent_chat_list**](AIAgentsApi.md#get_agent_chat_list) | **GET** /api/v1/cloud-ai/agents/{id}/chat-list | Получение списка чатов агента
[**get_agent_chat_messages**](AIAgentsApi.md#get_agent_chat_messages) | **GET** /api/v1/cloud-ai/agents/{id}/chat-list/{chat_id}/messages | Получение сообщений чата агента
[**get_agent_entity_limit**](AIAgentsApi.md#get_agent_entity_limit) | **GET** /api/v1/cloud-ai/agents/{id}/entity-limits/{limit_id} | Получение лимита агента
[**get_agent_entity_limits**](AIAgentsApi.md#get_agent_entity_limits) | **GET** /api/v1/cloud-ai/agents/{id}/entity-limits | Получение лимитов агента
[**get_agent_statistics**](AIAgentsApi.md#get_agent_statistics) | **GET** /api/v1/cloud-ai/agents/{id}/statistic | Получение статистики использования токенов агента
[**get_agent_v3**](AIAgentsApi.md#get_agent_v3) | **GET** /api/v3/cloud-ai/agents/{id} | Получение AI агента (v3)
[**get_agents**](AIAgentsApi.md#get_agents) | **GET** /api/v1/cloud-ai/agents | Получение списка AI агентов
[**get_agents_v3**](AIAgentsApi.md#get_agents_v3) | **GET** /api/v3/cloud-ai/agents | Получение списка AI агентов (v3)
[**sync_agent_entity_limits**](AIAgentsApi.md#sync_agent_entity_limits) | **PUT** /api/v1/cloud-ai/agents/{id}/entity-limits/sync | Синхронизация лимитов агента за период
[**update_agent**](AIAgentsApi.md#update_agent) | **PATCH** /api/v1/cloud-ai/agents/{id} | Обновление AI агента
[**update_agent_entity_limit**](AIAgentsApi.md#update_agent_entity_limit) | **PATCH** /api/v1/cloud-ai/agents/{id}/entity-limits/{limit_id} | Изменение лимита агента


# **add_additional_token_package**
> add_additional_token_package(id, add_token_package=add_token_package)

Добавление дополнительного пакета токенов

Чтобы докупить дополнительные пакеты токенов для AI агента, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{id}/add-additional-token-package`.  Метод относится к устаревшей схеме оплаты пакетами токенов и работает только для агентов с пакетом (`token_package_id` в ответе агента). Для агентов с поресурсной оплатой вернётся 400 `per-resource_agents_do_not_support_additional_token_packages`. Стоимость (цена дополнительного пакета модели агента × `count`) сразу списывается с баланса; при нехватке средств — 400 `insufficient_balance`, если подписка агента истекла — 400 `subscription_expired`. После покупки заблокированный агент разблокируется.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:write`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_token_package import AddTokenPackage
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    add_token_package = timeweb_cloud_api.AddTokenPackage() # AddTokenPackage |  (optional)

    try:
        # Добавление дополнительного пакета токенов
        api_instance.add_additional_token_package(id, add_token_package=add_token_package)
    except Exception as e:
        print("Exception when calling AIAgentsApi->add_additional_token_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **add_token_package** | [**AddTokenPackage**](AddTokenPackage.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Дополнительный пакет токенов успешно добавлен |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_agent_model**
> CreateAgent201Response change_agent_model(id, change_agent_model)

Смена модели AI агента

Чтобы сменить основную модель AI агента, отправьте PATCH-запрос на `/api/v1/cloud-ai/agents/{id}/model`.  Параметры модели из `settings.model`, которые новая модель не поддерживает, отбрасываются. Смена модели доступна только агентам с поресурсной оплатой (для агента с пакетом токенов — 400 `model_change_is_allowed_only_for_per-resource_account_and_agent`). Если модель не найдена или недоступна — 404 `model_not_found`.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:write`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.change_agent_model import ChangeAgentModel
from timeweb_cloud_api.models.create_agent201_response import CreateAgent201Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    change_agent_model = timeweb_cloud_api.ChangeAgentModel() # ChangeAgentModel | 

    try:
        # Смена модели AI агента
        api_response = api_instance.change_agent_model(id, change_agent_model)
        print("The response of AIAgentsApi->change_agent_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->change_agent_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **change_agent_model** | [**ChangeAgentModel**](ChangeAgentModel.md)|  | 

### Return type

[**CreateAgent201Response**](CreateAgent201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;agent&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent**
> CreateAgent201Response create_agent(create_agent)

Создание AI агента

Чтобы создать AI агента, отправьте POST-запрос на `/api/v1/cloud-ai/agents`, задав необходимые атрибуты.  Метод устарел — используйте `POST /api/v2/cloud-ai/agents`. Поле `token_package_id` обязательно, но не учитывается: агент всегда создаётся с поресурсной оплатой (оплачиваются фактические запросы к модели).  Для токенов дополнительных пользователей аккаунта нужна роль `ai:write`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent import CreateAgent
from timeweb_cloud_api.models.create_agent201_response import CreateAgent201Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    create_agent = timeweb_cloud_api.CreateAgent() # CreateAgent | 

    try:
        # Создание AI агента
        api_response = api_instance.create_agent(create_agent)
        print("The response of AIAgentsApi->create_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->create_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_agent** | [**CreateAgent**](CreateAgent.md)|  | 

### Return type

[**CreateAgent201Response**](CreateAgent201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;agent&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_entity_limit**
> CreateAgentEntityLimit201Response create_agent_entity_limit(id, create_agent_entity_limit)

Создание лимита агента

Чтобы создать лимит AI агента, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{id}/entity-limits`.  Лимиты агента ограничивают расход на его запросы за период (`hour`, `day`, `week`, `month`) — в токенах (`limit`) или в деньгах (`money_limit`, приоритетнее). Лимит действует на все модели агента (`model_id` = `null`) или на одну модель. При достижении лимита запросы к агенту отклоняются до конца периода.  Нужно передать `limit` или `money_limit` (иначе — 400 `entity_keys_limit_value_required`). Если лимит с тем же периодом и моделью уже есть — 409 `entity_keys_limit_already_exists` (измените его или используйте синхронизацию).  Для токенов дополнительных пользователей аккаунта нужна роль `ai:write`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_entity_limit import CreateAgentEntityLimit
from timeweb_cloud_api.models.create_agent_entity_limit201_response import CreateAgentEntityLimit201Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    create_agent_entity_limit = timeweb_cloud_api.CreateAgentEntityLimit() # CreateAgentEntityLimit | 

    try:
        # Создание лимита агента
        api_response = api_instance.create_agent_entity_limit(id, create_agent_entity_limit)
        print("The response of AIAgentsApi->create_agent_entity_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->create_agent_entity_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **create_agent_entity_limit** | [**CreateAgentEntityLimit**](CreateAgentEntityLimit.md)|  | 

### Return type

[**CreateAgentEntityLimit201Response**](CreateAgentEntityLimit201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;agent_entity_limit&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_v2**
> CreateAgent201Response create_agent_v2(create_agent_v2)

Создание AI агента

Чтобы создать AI агента, отправьте POST-запрос на `/api/v2/cloud-ai/agents`, задав необходимые атрибуты.  Агент создаётся с поресурсной оплатой: оплачиваются фактические запросы к модели. Если не переданы настройки виджета, подставляются значения по умолчанию. Дневной лимит расходов можно задать сразу полем `money_limit`, остальные лимиты — через лимиты агента (`/api/v1/cloud-ai/agents/{id}/entity-limits`).  Если модель не найдена или недоступна, вернётся 404 `model_not_found`; если модель не поддерживается — 400 `model_not_supported`; недопустимые параметры модели в `settings.model` — 400.  Вызывать созданного агента из своих приложений можно через OpenAI-совместимое API по его `access_id` — см. [документацию](https://agent.timeweb.cloud/docs).  Для токенов дополнительных пользователей аккаунта нужна роль `ai:write`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent201_response import CreateAgent201Response
from timeweb_cloud_api.models.create_agent_v2 import CreateAgentV2
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    create_agent_v2 = timeweb_cloud_api.CreateAgentV2() # CreateAgentV2 | 

    try:
        # Создание AI агента
        api_response = api_instance.create_agent_v2(create_agent_v2)
        print("The response of AIAgentsApi->create_agent_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->create_agent_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_agent_v2** | [**CreateAgentV2**](CreateAgentV2.md)|  | 

### Return type

[**CreateAgent201Response**](CreateAgent201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;agent&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent**
> delete_agent(id, delete_agent=delete_agent)

Удаление AI агента

Чтобы удалить AI агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/agents/{id}`.  Вместе с агентом отключаются его базы знаний, навыки и интеграции (Telegram, MAX, Jivo, Crisp). В теле запроса можно необязательно указать причину удаления.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:write`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.delete_agent import DeleteAgent
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    delete_agent = timeweb_cloud_api.DeleteAgent() # DeleteAgent |  (optional)

    try:
        # Удаление AI агента
        api_instance.delete_agent(id, delete_agent=delete_agent)
    except Exception as e:
        print("Exception when calling AIAgentsApi->delete_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **delete_agent** | [**DeleteAgent**](DeleteAgent.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | AI агент успешно удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_entity_limit**
> delete_agent_entity_limit(id, limit_id)

Удаление лимита агента

Чтобы удалить лимит AI агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/agents/{id}/entity-limits/{limit_id}`.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:write`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    limit_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID лимита агента

    try:
        # Удаление лимита агента
        api_instance.delete_agent_entity_limit(id, limit_id)
    except Exception as e:
        print("Exception when calling AIAgentsApi->delete_agent_entity_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **limit_id** | [**object**](.md)| ID лимита агента | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Лимит удалён |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_agent_chats_csv**
> ExportAgentChatsCsv200Response export_agent_chats_csv(id, offset=offset, limit=limit, order=order, var_from=var_from, to=to, locale=locale)

Выгрузка чатов агента в CSV

Чтобы выгрузить чаты AI агента в формате CSV, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{id}/chats/docs`.  CSV возвращается строкой в поле `chats_csv.csv` тела JSON. `limit` и `offset` применяются к сообщениям, а не к чатам. Если передан `from`, выгружаются сообщения от `from` до `to` (по умолчанию — до текущего момента). Чаты внешнего чата не выгружаются.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:read`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.export_agent_chats_csv200_response import ExportAgentChatsCsv200Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    offset = 0 # object | Смещение относительно начала списка (optional)
    limit = 100 # object | Количество сообщений в ответе (optional)
    order = desc # object | Сортировка по дате сообщения (optional)
    var_from = 2026-10-01T00:00:00.000Z # object | Начало периода (дата и время в формате ISO 8601) (optional)
    to = 2026-10-20T23:59:59.999Z # object | Конец периода (дата и время в формате ISO 8601) (optional)
    locale = ru # object | Язык заголовков и значений CSV (optional)

    try:
        # Выгрузка чатов агента в CSV
        api_response = api_instance.export_agent_chats_csv(id, offset=offset, limit=limit, order=order, var_from=var_from, to=to, locale=locale)
        print("The response of AIAgentsApi->export_agent_chats_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->export_agent_chats_csv: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **offset** | [**object**](.md)| Смещение относительно начала списка | [optional] 
 **limit** | [**object**](.md)| Количество сообщений в ответе | [optional] 
 **order** | [**object**](.md)| Сортировка по дате сообщения | [optional] 
 **var_from** | [**object**](.md)| Начало периода (дата и время в формате ISO 8601) | [optional] 
 **to** | [**object**](.md)| Конец периода (дата и время в формате ISO 8601) | [optional] 
 **locale** | [**object**](.md)| Язык заголовков и значений CSV | [optional] 

### Return type

[**ExportAgentChatsCsv200Response**](ExportAgentChatsCsv200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;chats_csv&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent**
> CreateAgent201Response get_agent(id)

Получение AI агента

Чтобы получить информацию об AI агенте, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{id}`.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:read`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent201_response import CreateAgent201Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента

    try:
        # Получение AI агента
        api_response = api_instance.get_agent(id)
        print("The response of AIAgentsApi->get_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->get_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 

### Return type

[**CreateAgent201Response**](CreateAgent201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;agent&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_chat_list**
> GetAgentChatList200Response get_agent_chat_list(id, offset=offset, limit=limit, order=order, var_from=var_from, to=to, reaction_type=reaction_type, response_time_ranges=response_time_ranges)

Получение списка чатов агента

Чтобы получить список чатов (диалогов) AI агента, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{id}/chat-list`.  Для каждого чата возвращаются первое сообщение пользователя, количество оценок и среднее время ответа. Чаты внешнего чата сюда не входят. Фильтр по периоду применяется, только если переданы оба параметра `from` и `to`. В `meta.metrics` — сводка по чатам для фильтров.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:read`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_chat_list200_response import GetAgentChatList200Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    offset = 0 # object | Смещение относительно начала списка (optional)
    limit = 100 # object | Количество чатов в ответе (optional)
    order = asc # object | Сортировка по дате первого сообщения (optional)
    var_from = 2026-10-01T00:00:00.000Z # object | Начало периода (дата и время в формате ISO 8601) (optional)
    to = 2026-10-20T23:59:59.999Z # object | Конец периода (дата и время в формате ISO 8601) (optional)
    reaction_type = likes # object | Фильтр по оценкам: `likes` — есть положительная, `dislikes` — есть отрицательная, `with` — есть любая, `none` — без оценок (optional)
    response_time_ranges = ["1-5","15-"] # object | Фильтр по среднему времени ответа в секундах: диапазоны `мин-макс` или `мин-` («от мин и больше»). Можно передать несколько диапазонов — они объединяются по ИЛИ. (optional)

    try:
        # Получение списка чатов агента
        api_response = api_instance.get_agent_chat_list(id, offset=offset, limit=limit, order=order, var_from=var_from, to=to, reaction_type=reaction_type, response_time_ranges=response_time_ranges)
        print("The response of AIAgentsApi->get_agent_chat_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->get_agent_chat_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **offset** | [**object**](.md)| Смещение относительно начала списка | [optional] 
 **limit** | [**object**](.md)| Количество чатов в ответе | [optional] 
 **order** | [**object**](.md)| Сортировка по дате первого сообщения | [optional] 
 **var_from** | [**object**](.md)| Начало периода (дата и время в формате ISO 8601) | [optional] 
 **to** | [**object**](.md)| Конец периода (дата и время в формате ISO 8601) | [optional] 
 **reaction_type** | [**object**](.md)| Фильтр по оценкам: &#x60;likes&#x60; — есть положительная, &#x60;dislikes&#x60; — есть отрицательная, &#x60;with&#x60; — есть любая, &#x60;none&#x60; — без оценок | [optional] 
 **response_time_ranges** | [**object**](.md)| Фильтр по среднему времени ответа в секундах: диапазоны &#x60;мин-макс&#x60; или &#x60;мин-&#x60; («от мин и больше»). Можно передать несколько диапазонов — они объединяются по ИЛИ. | [optional] 

### Return type

[**GetAgentChatList200Response**](GetAgentChatList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;chat_list&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_chat_messages**
> GetAgentChatMessages200Response get_agent_chat_messages(id, chat_id, offset=offset, limit=limit, order=order, var_from=var_from, to=to)

Получение сообщений чата агента

Чтобы получить сообщения чата AI агента, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{id}/chat-list/{chat_id}/messages`.  Возвращаются сообщения пользователя и ответы агента. Фильтр по периоду применяется, только если переданы оба параметра `from` и `to`.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:read`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_chat_messages200_response import GetAgentChatMessages200Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    chat_id = ai-agent-1-0b1c2d3e-4f50-4a6b-8c7d-9e0f1a2b3c4d # object | ID чата (диалога) из поля `id` списка чатов агента
    offset = 0 # object | Смещение относительно начала списка (optional)
    limit = 100 # object | Количество сообщений в ответе (optional)
    order = desc # object | Сортировка по дате сообщения (optional)
    var_from = 2026-10-01T00:00:00.000Z # object | Начало периода (дата и время в формате ISO 8601) (optional)
    to = 2026-10-20T23:59:59.999Z # object | Конец периода (дата и время в формате ISO 8601) (optional)

    try:
        # Получение сообщений чата агента
        api_response = api_instance.get_agent_chat_messages(id, chat_id, offset=offset, limit=limit, order=order, var_from=var_from, to=to)
        print("The response of AIAgentsApi->get_agent_chat_messages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->get_agent_chat_messages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **chat_id** | [**object**](.md)| ID чата (диалога) из поля &#x60;id&#x60; списка чатов агента | 
 **offset** | [**object**](.md)| Смещение относительно начала списка | [optional] 
 **limit** | [**object**](.md)| Количество сообщений в ответе | [optional] 
 **order** | [**object**](.md)| Сортировка по дате сообщения | [optional] 
 **var_from** | [**object**](.md)| Начало периода (дата и время в формате ISO 8601) | [optional] 
 **to** | [**object**](.md)| Конец периода (дата и время в формате ISO 8601) | [optional] 

### Return type

[**GetAgentChatMessages200Response**](GetAgentChatMessages200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;chat_list_messages&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_entity_limit**
> CreateAgentEntityLimit201Response get_agent_entity_limit(id, limit_id)

Получение лимита агента

Чтобы получить лимит AI агента, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{id}/entity-limits/{limit_id}`.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:read`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_entity_limit201_response import CreateAgentEntityLimit201Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    limit_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID лимита агента

    try:
        # Получение лимита агента
        api_response = api_instance.get_agent_entity_limit(id, limit_id)
        print("The response of AIAgentsApi->get_agent_entity_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->get_agent_entity_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **limit_id** | [**object**](.md)| ID лимита агента | 

### Return type

[**CreateAgentEntityLimit201Response**](CreateAgentEntityLimit201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;agent_entity_limit&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_entity_limits**
> GetAgentEntityLimits200Response get_agent_entity_limits(id, limit_type=limit_type)

Получение лимитов агента

Чтобы получить лимиты AI агента, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{id}/entity-limits`.  Лимиты агента ограничивают расход на его запросы за период (`hour`, `day`, `week`, `month`) — в токенах (`limit`) или в деньгах (`money_limit`, приоритетнее). Лимит действует на все модели агента (`model_id` = `null`) или на одну модель. При достижении лимита запросы к агенту отклоняются до конца периода.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:read`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_entity_limits200_response import GetAgentEntityLimits200Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    limit_type = day # object | Фильтр по периоду лимита (optional)

    try:
        # Получение лимитов агента
        api_response = api_instance.get_agent_entity_limits(id, limit_type=limit_type)
        print("The response of AIAgentsApi->get_agent_entity_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->get_agent_entity_limits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **limit_type** | [**object**](.md)| Фильтр по периоду лимита | [optional] 

### Return type

[**GetAgentEntityLimits200Response**](GetAgentEntityLimits200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;agent_entity_limits&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_statistics**
> GetAgentStatistics200Response get_agent_statistics(id, start_time=start_time, end_time=end_time, interval=interval)

Получение статистики использования токенов агента

Чтобы получить статистику использования токенов AI агента, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{id}/statistic`.  Статистика разбита на интервалы длиной `interval` минут: для каждого интервала возвращается по точке на каждую модель, к которой были запросы за период, а для интервалов без запросов — одна нулевая точка без `model_name`. По умолчанию возвращаются последние 24 часа.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:read`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_statistics200_response import GetAgentStatistics200Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    start_time = 2026-10-19T00:00:00.000Z # object | Начало периода (ISO 8601). По умолчанию — за 24 часа до `endTime`. (optional)
    end_time = 2026-10-20T00:00:00.000Z # object | Конец периода (ISO 8601). По умолчанию — текущий момент. (optional)
    interval = 60 # object | Длина интервала агрегации в минутах (optional)

    try:
        # Получение статистики использования токенов агента
        api_response = api_instance.get_agent_statistics(id, start_time=start_time, end_time=end_time, interval=interval)
        print("The response of AIAgentsApi->get_agent_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->get_agent_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **start_time** | [**object**](.md)| Начало периода (ISO 8601). По умолчанию — за 24 часа до &#x60;endTime&#x60;. | [optional] 
 **end_time** | [**object**](.md)| Конец периода (ISO 8601). По умолчанию — текущий момент. | [optional] 
 **interval** | [**object**](.md)| Длина интервала агрегации в минутах | [optional] 

### Return type

[**GetAgentStatistics200Response**](GetAgentStatistics200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;agent_statistics&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_v3**
> GetAgentV3200Response get_agent_v3(id)

Получение AI агента (v3)

Чтобы получить информацию об AI агенте, отправьте GET-запрос на `/api/v3/cloud-ai/agents/{id}`.  Отличается от `/api/v1/cloud-ai/agents/{id}` тем, что вместо `knowledge_bases_ids` возвращает `knowledge_bases` — подключённые базы знаний с режимом поиска.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:read`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_v3200_response import GetAgentV3200Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента

    try:
        # Получение AI агента (v3)
        api_response = api_instance.get_agent_v3(id)
        print("The response of AIAgentsApi->get_agent_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->get_agent_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 

### Return type

[**GetAgentV3200Response**](GetAgentV3200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;agent&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents**
> GetAgents200Response get_agents()

Получение списка AI агентов

Чтобы получить список AI агентов, отправьте GET-запрос на `/api/v1/cloud-ai/agents`.  Возвращаются все агенты аккаунта (без пагинации), включая приостановленных и заблокированных. Тело ответа будет представлять собой объект JSON с ключами `agents` и `meta`. Подключённые базы знаний вместе с режимом поиска возвращает метод `/api/v3/cloud-ai/agents`.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:read`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agents200_response import GetAgents200Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)

    try:
        # Получение списка AI агентов
        api_response = api_instance.get_agents()
        print("The response of AIAgentsApi->get_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->get_agents: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAgents200Response**](GetAgents200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;agents&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents_v3**
> GetAgentsV3200Response get_agents_v3()

Получение списка AI агентов (v3)

Чтобы получить список AI агентов, отправьте GET-запрос на `/api/v3/cloud-ai/agents`.  Отличается от `/api/v1/cloud-ai/agents` тем, что вместо `knowledge_bases_ids` возвращает `knowledge_bases` — подключённые базы знаний с режимом поиска.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:read`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agents_v3200_response import GetAgentsV3200Response
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)

    try:
        # Получение списка AI агентов (v3)
        api_response = api_instance.get_agents_v3()
        print("The response of AIAgentsApi->get_agents_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->get_agents_v3: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAgentsV3200Response**](GetAgentsV3200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;agents&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_agent_entity_limits**
> GetAgentEntityLimits200Response sync_agent_entity_limits(id, sync_agent_entity_limits)

Синхронизация лимитов агента за период

Чтобы задать полный набор лимитов AI агента за период, отправьте PUT-запрос на `/api/v1/cloud-ai/agents/{id}/entity-limits/sync`.  Лимиты из запроса создаются или обновляются (сопоставление по `model_id`), а лимиты этого периода, которых нет в запросе, удаляются. Лимиты других периодов не затрагиваются. В ответе — актуальные лимиты периода. Если лимиты одновременно изменил другой запрос, вернётся 409 `entity_keys_limits_sync_conflict` — повторите запрос.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:write`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_entity_limits200_response import GetAgentEntityLimits200Response
from timeweb_cloud_api.models.sync_agent_entity_limits import SyncAgentEntityLimits
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    sync_agent_entity_limits = timeweb_cloud_api.SyncAgentEntityLimits() # SyncAgentEntityLimits | 

    try:
        # Синхронизация лимитов агента за период
        api_response = api_instance.sync_agent_entity_limits(id, sync_agent_entity_limits)
        print("The response of AIAgentsApi->sync_agent_entity_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->sync_agent_entity_limits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **sync_agent_entity_limits** | [**SyncAgentEntityLimits**](SyncAgentEntityLimits.md)|  | 

### Return type

[**GetAgentEntityLimits200Response**](GetAgentEntityLimits200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;agent_entity_limits&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent**
> CreateAgent201Response update_agent(id, update_agent)

Обновление AI агента

Чтобы обновить AI агента, отправьте PATCH-запрос на `/api/v1/cloud-ai/agents/{id}`, передав изменяемые поля.  Особенности: - `settings` заменяются целиком (кроме `web_search_allowed_sites`, `additional_models` и `memory_enabled`, которые сохраняются, если не переданы) — передавайте полный объект настроек, включая `widget`; - основную модель меняет отдельный метод `PATCH /api/v1/cloud-ai/agents/{id}/model`; - поле `token_limit` больше не поддерживается: запрос с ним отклоняется с кодом 410 — лимиты задаются через `/api/v1/cloud-ai/agents/{id}/entity-limits`; - ошибки привязки `ai_gateway_key_id`: 400 `ai_gateway_key_not_found`, `agent_is_already_migrated_to_another_ai_gateway_key`, `agent_is_not_eligible_for_ai_gateway_migration`; 503 — проверку временно не удалось выполнить; - изменить статус заблокированного или удалённого агента нельзя (400 `agent_can't_change_status`).  Для токенов дополнительных пользователей аккаунта нужна роль `ai:write`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent201_response import CreateAgent201Response
from timeweb_cloud_api.models.update_agent import UpdateAgent
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    update_agent = timeweb_cloud_api.UpdateAgent() # UpdateAgent | 

    try:
        # Обновление AI агента
        api_response = api_instance.update_agent(id, update_agent)
        print("The response of AIAgentsApi->update_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->update_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **update_agent** | [**UpdateAgent**](UpdateAgent.md)|  | 

### Return type

[**CreateAgent201Response**](CreateAgent201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;agent&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**410** | Передано удалённое поле &#x60;token_limit&#x60; |  -  |
**429** |  |  -  |
**500** |  |  -  |
**503** | Не удалось проверить возможность привязки &#x60;ai_gateway_key_id&#x60;, повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_entity_limit**
> CreateAgentEntityLimit201Response update_agent_entity_limit(id, limit_id, update_agent_entity_limit)

Изменение лимита агента

Чтобы изменить значение лимита AI агента, отправьте PATCH-запрос на `/api/v1/cloud-ai/agents/{id}/entity-limits/{limit_id}`.  Непереданные поля не меняются. Снять денежный лимит (`money_limit`: `null`) можно только вместе с передачей `limit`.  Для токенов дополнительных пользователей аккаунта нужна роль `ai:write`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_entity_limit201_response import CreateAgentEntityLimit201Response
from timeweb_cloud_api.models.update_agent_entity_limit import UpdateAgentEntityLimit
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
    api_instance = timeweb_cloud_api.AIAgentsApi(api_client)
    id = 1 # object | ID агента
    limit_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID лимита агента
    update_agent_entity_limit = timeweb_cloud_api.UpdateAgentEntityLimit() # UpdateAgentEntityLimit | 

    try:
        # Изменение лимита агента
        api_response = api_instance.update_agent_entity_limit(id, limit_id, update_agent_entity_limit)
        print("The response of AIAgentsApi->update_agent_entity_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentsApi->update_agent_entity_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 
 **limit_id** | [**object**](.md)| ID лимита агента | 
 **update_agent_entity_limit** | [**UpdateAgentEntityLimit**](UpdateAgentEntityLimit.md)|  | 

### Return type

[**CreateAgentEntityLimit201Response**](CreateAgentEntityLimit201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;agent_entity_limit&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

