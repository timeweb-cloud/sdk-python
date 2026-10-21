# timeweb_cloud_api.AIGatewayApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ai_key**](AIGatewayApi.md#create_ai_key) | **POST** /api/v1/cloud-ai/ai-keys | Создание ключа AI Gateway
[**create_ai_key_limit**](AIGatewayApi.md#create_ai_key_limit) | **POST** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits | Создание лимита ключа AI Gateway
[**delete_ai_key**](AIGatewayApi.md#delete_ai_key) | **DELETE** /api/v1/cloud-ai/ai-keys/{key_id} | Удаление ключа AI Gateway
[**delete_ai_key_limit**](AIGatewayApi.md#delete_ai_key_limit) | **DELETE** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id} | Удаление лимита ключа AI Gateway
[**get_ai_key_calls_statistic**](AIGatewayApi.md#get_ai_key_calls_statistic) | **GET** /api/v1/cloud-ai/ai-keys/statistic/calls | Получение статистики запросов ключа AI Gateway
[**get_ai_key_limit**](AIGatewayApi.md#get_ai_key_limit) | **GET** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id} | Получение лимита ключа AI Gateway
[**get_ai_key_limits**](AIGatewayApi.md#get_ai_key_limits) | **GET** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits | Получение списка лимитов ключа AI Gateway
[**get_ai_key_models_statistic**](AIGatewayApi.md#get_ai_key_models_statistic) | **GET** /api/v1/cloud-ai/ai-keys/statistic/models | Получение списка моделей, использованных ключом AI Gateway
[**get_ai_key_token_usage_statistic**](AIGatewayApi.md#get_ai_key_token_usage_statistic) | **GET** /api/v1/cloud-ai/ai-keys/statistic/token-usage | Получение статистики расхода токенов ключа AI Gateway
[**get_ai_keys**](AIGatewayApi.md#get_ai_keys) | **GET** /api/v1/cloud-ai/ai-keys | Получение списка ключей AI Gateway
[**regenerate_ai_key**](AIGatewayApi.md#regenerate_ai_key) | **PUT** /api/v1/cloud-ai/ai-keys/{key_id}/regenerate | Перевыпуск ключа AI Gateway
[**sync_ai_key_limits**](AIGatewayApi.md#sync_ai_key_limits) | **PUT** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/sync | Синхронизация лимитов ключа AI Gateway
[**update_ai_key**](AIGatewayApi.md#update_ai_key) | **PATCH** /api/v1/cloud-ai/ai-keys/{key_id} | Изменение ключа AI Gateway
[**update_ai_key_limit**](AIGatewayApi.md#update_ai_key_limit) | **PATCH** /api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id} | Изменение лимита ключа AI Gateway


# **create_ai_key**
> CreateAiKey201Response create_ai_key(create_ai_key)

Создание ключа AI Gateway

Чтобы создать ключ AI Gateway, отправьте POST-запрос на `/api/v1/cloud-ai/ai-keys`.  Значение ключа (`sk-...`) возвращается в поле `key` только в ответе на этот запрос — сохраните его. Если значение утеряно, перевыпустите ключ.  Если список `fallback_models` некорректен, вернётся 400 с `error_code` `fallback_chain_invalid` (больше двух моделей или повторы, правило — в `details.reason`) или `fallback_model_not_found` (модели нет среди действующих текстовых моделей, список — в `details.model_names`).

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_ai_key import CreateAiKey
from timeweb_cloud_api.models.create_ai_key201_response import CreateAiKey201Response
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    create_ai_key = timeweb_cloud_api.CreateAiKey() # CreateAiKey | 

    try:
        # Создание ключа AI Gateway
        api_response = api_instance.create_ai_key(create_ai_key)
        print("The response of AIGatewayApi->create_ai_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->create_ai_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ai_key** | [**CreateAiKey**](CreateAiKey.md)|  | 

### Return type

[**CreateAiKey201Response**](CreateAiKey201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключами &#x60;ai_key&#x60; и &#x60;key&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_key_limit**
> CreateAiKeyLimit201Response create_ai_key_limit(key_id, create_ai_key_limit)

Создание лимита ключа AI Gateway

Чтобы ограничить расход ключа AI Gateway, отправьте POST-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits`.  Лимит задаётся в токенах (`limit`) или в деньгах (`money_limit`, приоритетнее) на период `limit_type` — для всех моделей или для одной (`model_id`). Когда лимит исчерпан, запросы ключа к AI Gateway API завершаются ошибкой 422 до начала следующего периода. Если от лимита осталась часть, максимальный размер ответа текстового запроса уменьшается так, чтобы уложиться в остаток.  На один период и одну модель (или на все модели) можно завести только один лимит — повторный вернёт 409 с `error_code` `entity_keys_limit_already_exists`. Если не передан ни `limit`, ни `money_limit`, вернётся 400 с `error_code` `entity_keys_limit_value_required`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_ai_key_limit import CreateAiKeyLimit
from timeweb_cloud_api.models.create_ai_key_limit201_response import CreateAiKeyLimit201Response
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    key_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID ключа AI Gateway (UUID)
    create_ai_key_limit = timeweb_cloud_api.CreateAiKeyLimit() # CreateAiKeyLimit | 

    try:
        # Создание лимита ключа AI Gateway
        api_response = api_instance.create_ai_key_limit(key_id, create_ai_key_limit)
        print("The response of AIGatewayApi->create_ai_key_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->create_ai_key_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | [**object**](.md)| ID ключа AI Gateway (UUID) | 
 **create_ai_key_limit** | [**CreateAiKeyLimit**](CreateAiKeyLimit.md)|  | 

### Return type

[**CreateAiKeyLimit201Response**](CreateAiKeyLimit201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;ai_key_entity_limit&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ai_key**
> delete_ai_key(key_id)

Удаление ключа AI Gateway

Чтобы удалить ключ AI Gateway, отправьте DELETE-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}`.  После удаления запросы с этим ключом перестают приниматься. Ключи, которыми управляет платформа (`is_readonly: true`), удалить нельзя: вернётся 403 с `error_code` `ai_key_is_readonly`.

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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    key_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID ключа AI Gateway (UUID)

    try:
        # Удаление ключа AI Gateway
        api_instance.delete_ai_key(key_id)
    except Exception as e:
        print("Exception when calling AIGatewayApi->delete_ai_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | [**object**](.md)| ID ключа AI Gateway (UUID) | 

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
**204** | Ключ удалён |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ai_key_limit**
> delete_ai_key_limit(key_id, limit_id)

Удаление лимита ключа AI Gateway

Чтобы удалить лимит ключа AI Gateway, отправьте DELETE-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}`.  Если лимит относится к другому ключу, вернётся 403.

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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    key_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID ключа AI Gateway (UUID)
    limit_id = 0f6b7d8e-1c2a-4b3d-9e8f-7a6b5c4d3e2f # object | ID лимита (UUID)

    try:
        # Удаление лимита ключа AI Gateway
        api_instance.delete_ai_key_limit(key_id, limit_id)
    except Exception as e:
        print("Exception when calling AIGatewayApi->delete_ai_key_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | [**object**](.md)| ID ключа AI Gateway (UUID) | 
 **limit_id** | [**object**](.md)| ID лимита (UUID) | 

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

# **get_ai_key_calls_statistic**
> GetAiKeyCallsStatistic200Response get_ai_key_calls_statistic(entity_id, entity_type, model_name=model_name, start_time=start_time, end_time=end_time, interval=interval)

Получение статистики запросов ключа AI Gateway

Чтобы получить количество запросов ключа по интервалам времени, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/statistic/calls`.  Ключ задаётся параметрами `entity_id` (ID ключа) и `entity_type` (тип ключа). Если ключ не найден, вернётся 404. Период по умолчанию — последние 24 часа. Точки возвращаются для каждого интервала периода, включая интервалы без запросов.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_calls_statistics` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_key_calls_statistic200_response import GetAiKeyCallsStatistic200Response
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    entity_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID ключа — поле `id` из списка ключей.
    entity_type = aikey # object | Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404.
    model_name = openai/gpt-5.4-mini,openai/gpt-4.1-mini # object | Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям. (optional)
    start_time = 2026-10-19T00:00:00.000Z # object | Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`. (optional)
    end_time = 2026-10-20T00:00:00.000Z # object | Конец периода в формате ISO 8601. По умолчанию — текущий момент. (optional)
    interval = 60 # object | Шаг агрегации в минутах. (optional)

    try:
        # Получение статистики запросов ключа AI Gateway
        api_response = api_instance.get_ai_key_calls_statistic(entity_id, entity_type, model_name=model_name, start_time=start_time, end_time=end_time, interval=interval)
        print("The response of AIGatewayApi->get_ai_key_calls_statistic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->get_ai_key_calls_statistic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | [**object**](.md)| ID ключа — поле &#x60;id&#x60; из списка ключей. | 
 **entity_type** | [**object**](.md)| Тип ключа — поле &#x60;entity_type&#x60; из списка ключей: &#x60;aikey&#x60; — ключ, созданный пользователем, &#x60;k8s&#x60; — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404. | 
 **model_name** | [**object**](.md)| Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям. | [optional] 
 **start_time** | [**object**](.md)| Начало периода в формате ISO 8601. По умолчанию — за 24 часа до &#x60;end_time&#x60;. | [optional] 
 **end_time** | [**object**](.md)| Конец периода в формате ISO 8601. По умолчанию — текущий момент. | [optional] 
 **interval** | [**object**](.md)| Шаг агрегации в минутах. | [optional] 

### Return type

[**GetAiKeyCallsStatistic200Response**](GetAiKeyCallsStatistic200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_key_calls_statistics&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_key_limit**
> CreateAiKeyLimit201Response get_ai_key_limit(key_id, limit_id)

Получение лимита ключа AI Gateway

Чтобы получить лимит ключа AI Gateway, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}`.  Если лимит относится к другому ключу, вернётся 403 с `error_code` `entity_keys_limit_forbidden`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_ai_key_limit201_response import CreateAiKeyLimit201Response
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    key_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID ключа AI Gateway (UUID)
    limit_id = 0f6b7d8e-1c2a-4b3d-9e8f-7a6b5c4d3e2f # object | ID лимита (UUID)

    try:
        # Получение лимита ключа AI Gateway
        api_response = api_instance.get_ai_key_limit(key_id, limit_id)
        print("The response of AIGatewayApi->get_ai_key_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->get_ai_key_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | [**object**](.md)| ID ключа AI Gateway (UUID) | 
 **limit_id** | [**object**](.md)| ID лимита (UUID) | 

### Return type

[**CreateAiKeyLimit201Response**](CreateAiKeyLimit201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ai_key_entity_limit&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_key_limits**
> GetAiKeyLimits200Response get_ai_key_limits(entity_type=entity_type, limit_type=limit_type)

Получение списка лимитов ключа AI Gateway

Чтобы получить лимиты расхода ключа AI Gateway, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits`.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_entity_limits` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_key_limits200_response import GetAiKeyLimits200Response
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    entity_type = aikey # object | Фильтр по типу сущности лимита (`entity_type`). (optional)
    limit_type = day # object | Фильтр по периоду лимита. (optional)

    try:
        # Получение списка лимитов ключа AI Gateway
        api_response = api_instance.get_ai_key_limits(entity_type=entity_type, limit_type=limit_type)
        print("The response of AIGatewayApi->get_ai_key_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->get_ai_key_limits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_type** | [**object**](.md)| Фильтр по типу сущности лимита (&#x60;entity_type&#x60;). | [optional] 
 **limit_type** | [**object**](.md)| Фильтр по периоду лимита. | [optional] 

### Return type

[**GetAiKeyLimits200Response**](GetAiKeyLimits200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_key_entity_limits&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_key_models_statistic**
> GetAiKeyModelsStatistic200Response get_ai_key_models_statistic(entity_id, entity_type, model_name=model_name, start_time=start_time, end_time=end_time)

Получение списка моделей, использованных ключом AI Gateway

Чтобы получить список моделей, к которым обращался ключ за период, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/statistic/models`.  Ключ задаётся параметрами `entity_id` (ID ключа) и `entity_type` (тип ключа). Если ключ не найден, вернётся 404. Период по умолчанию — последние 24 часа. Модели отсортированы по алфавиту.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_models_statistics` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_key_models_statistic200_response import GetAiKeyModelsStatistic200Response
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    entity_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID ключа — поле `id` из списка ключей.
    entity_type = aikey # object | Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404.
    model_name = openai/gpt-5.4-mini,openai/gpt-4.1-mini # object | Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям. (optional)
    start_time = 2026-10-19T00:00:00.000Z # object | Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`. (optional)
    end_time = 2026-10-20T00:00:00.000Z # object | Конец периода в формате ISO 8601. По умолчанию — текущий момент. (optional)

    try:
        # Получение списка моделей, использованных ключом AI Gateway
        api_response = api_instance.get_ai_key_models_statistic(entity_id, entity_type, model_name=model_name, start_time=start_time, end_time=end_time)
        print("The response of AIGatewayApi->get_ai_key_models_statistic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->get_ai_key_models_statistic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | [**object**](.md)| ID ключа — поле &#x60;id&#x60; из списка ключей. | 
 **entity_type** | [**object**](.md)| Тип ключа — поле &#x60;entity_type&#x60; из списка ключей: &#x60;aikey&#x60; — ключ, созданный пользователем, &#x60;k8s&#x60; — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404. | 
 **model_name** | [**object**](.md)| Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям. | [optional] 
 **start_time** | [**object**](.md)| Начало периода в формате ISO 8601. По умолчанию — за 24 часа до &#x60;end_time&#x60;. | [optional] 
 **end_time** | [**object**](.md)| Конец периода в формате ISO 8601. По умолчанию — текущий момент. | [optional] 

### Return type

[**GetAiKeyModelsStatistic200Response**](GetAiKeyModelsStatistic200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_key_models_statistics&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_key_token_usage_statistic**
> GetAiKeyTokenUsageStatistic200Response get_ai_key_token_usage_statistic(entity_id, entity_type, model_name=model_name, start_time=start_time, end_time=end_time, interval=interval)

Получение статистики расхода токенов ключа AI Gateway

Чтобы получить расход токенов и стоимость запросов ключа по интервалам времени, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys/statistic/token-usage`.  Ключ задаётся параметрами `entity_id` (ID ключа) и `entity_type` (тип ключа). Если ключ не найден, вернётся 404. Период по умолчанию — последние 24 часа. Точки возвращаются для каждого интервала периода, включая интервалы без запросов.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_token_statistics` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_key_token_usage_statistic200_response import GetAiKeyTokenUsageStatistic200Response
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    entity_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID ключа — поле `id` из списка ключей.
    entity_type = aikey # object | Тип ключа — поле `entity_type` из списка ключей: `aikey` — ключ, созданный пользователем, `k8s` — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404.
    model_name = openai/gpt-5.4-mini,openai/gpt-4.1-mini # object | Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям. (optional)
    start_time = 2026-10-19T00:00:00.000Z # object | Начало периода в формате ISO 8601. По умолчанию — за 24 часа до `end_time`. (optional)
    end_time = 2026-10-20T00:00:00.000Z # object | Конец периода в формате ISO 8601. По умолчанию — текущий момент. (optional)
    interval = 60 # object | Шаг агрегации в минутах. (optional)

    try:
        # Получение статистики расхода токенов ключа AI Gateway
        api_response = api_instance.get_ai_key_token_usage_statistic(entity_id, entity_type, model_name=model_name, start_time=start_time, end_time=end_time, interval=interval)
        print("The response of AIGatewayApi->get_ai_key_token_usage_statistic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->get_ai_key_token_usage_statistic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | [**object**](.md)| ID ключа — поле &#x60;id&#x60; из списка ключей. | 
 **entity_type** | [**object**](.md)| Тип ключа — поле &#x60;entity_type&#x60; из списка ключей: &#x60;aikey&#x60; — ключ, созданный пользователем, &#x60;k8s&#x60; — ключ кластера Kubernetes. Если тип не совпадает с типом ключа, вернётся 404. | 
 **model_name** | [**object**](.md)| Фильтр по моделям: ID модели или несколько ID через запятую. Значение другого формата (например, с заглавными буквами) игнорируется — статистика возвращается по всем моделям. | [optional] 
 **start_time** | [**object**](.md)| Начало периода в формате ISO 8601. По умолчанию — за 24 часа до &#x60;end_time&#x60;. | [optional] 
 **end_time** | [**object**](.md)| Конец периода в формате ISO 8601. По умолчанию — текущий момент. | [optional] 
 **interval** | [**object**](.md)| Шаг агрегации в минутах. | [optional] 

### Return type

[**GetAiKeyTokenUsageStatistic200Response**](GetAiKeyTokenUsageStatistic200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_key_token_statistics&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_keys**
> GetAiKeys200Response get_ai_keys()

Получение списка ключей AI Gateway

Чтобы получить список ключей AI Gateway, отправьте GET-запрос на `/api/v1/cloud-ai/ai-keys`.  В списке — ключи, созданные пользователем, и ключи кластеров Kubernetes, выпущенные платформой. Значения ключей (`sk-...`) не возвращаются.  Тело ответа будет представлять собой объект JSON с ключами `ai_keys` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_keys200_response import GetAiKeys200Response
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)

    try:
        # Получение списка ключей AI Gateway
        api_response = api_instance.get_ai_keys()
        print("The response of AIGatewayApi->get_ai_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->get_ai_keys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAiKeys200Response**](GetAiKeys200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_keys&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_ai_key**
> CreateAiKey201Response regenerate_ai_key(key_id)

Перевыпуск ключа AI Gateway

Чтобы перевыпустить ключ AI Gateway, отправьте PUT-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/regenerate`.  Ключ получает новое значение, старое перестаёт действовать сразу. Название, лимиты, запасные модели и статистика сохраняются. Новое значение (`sk-...`) возвращается в поле `key` только в ответе на этот запрос — сохраните его. Поле `expires_at` в ответе не заполняется.  Ключи, которыми управляет платформа (`is_readonly: true`), перевыпустить нельзя: вернётся 403 с `error_code` `ai_key_is_readonly`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_ai_key201_response import CreateAiKey201Response
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    key_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID ключа AI Gateway (UUID)

    try:
        # Перевыпуск ключа AI Gateway
        api_response = api_instance.regenerate_ai_key(key_id)
        print("The response of AIGatewayApi->regenerate_ai_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->regenerate_ai_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | [**object**](.md)| ID ключа AI Gateway (UUID) | 

### Return type

[**CreateAiKey201Response**](CreateAiKey201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_key&#x60; и &#x60;key&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_ai_key_limits**
> GetAiKeyLimits200Response sync_ai_key_limits(key_id, sync_ai_key_limits)

Синхронизация лимитов ключа AI Gateway

Чтобы задать все лимиты ключа AI Gateway на один период одним запросом, отправьте PUT-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/sync`.  Лимиты из `limits` создаются или обновляются (по `model_id`), а лимиты того же периода, которых нет в запросе, удаляются. Изменения применяются целиком или не применяются совсем.  Если в записи не задан ни `limit`, ни `money_limit` или `money_limit` снимается без `limit`, вернётся 400 с `error_code` `entity_keys_limit_value_required`. Если лимиты одновременно изменил другой запрос, вернётся 409 с `error_code` `entity_keys_limits_sync_conflict` — повторите запрос.  Тело ответа будет представлять собой объект JSON с ключами `ai_key_entity_limits` и `meta` — лимиты периода после синхронизации.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_key_limits200_response import GetAiKeyLimits200Response
from timeweb_cloud_api.models.sync_ai_key_limits import SyncAiKeyLimits
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    key_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID ключа AI Gateway (UUID)
    sync_ai_key_limits = timeweb_cloud_api.SyncAiKeyLimits() # SyncAiKeyLimits | 

    try:
        # Синхронизация лимитов ключа AI Gateway
        api_response = api_instance.sync_ai_key_limits(key_id, sync_ai_key_limits)
        print("The response of AIGatewayApi->sync_ai_key_limits:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->sync_ai_key_limits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | [**object**](.md)| ID ключа AI Gateway (UUID) | 
 **sync_ai_key_limits** | [**SyncAiKeyLimits**](SyncAiKeyLimits.md)|  | 

### Return type

[**GetAiKeyLimits200Response**](GetAiKeyLimits200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_key_entity_limits&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ai_key**
> UpdateAiKey200Response update_ai_key(key_id, update_ai_key)

Изменение ключа AI Gateway

Чтобы изменить ключ AI Gateway, отправьте PATCH-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}`, передав изменяемые поля.  Ключи, которыми управляет платформа (`is_readonly: true` — ключи AI-решений и кластеров Kubernetes), изменить нельзя: вернётся 403 с `error_code` `ai_key_is_readonly`.  Ошибки в `fallback_models` — как при создании ключа (400). Поле `expires_at` в ответе этого запроса не заполняется — срок действия ключа смотрите в списке ключей.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.update_ai_key import UpdateAiKey
from timeweb_cloud_api.models.update_ai_key200_response import UpdateAiKey200Response
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    key_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID ключа AI Gateway (UUID)
    update_ai_key = timeweb_cloud_api.UpdateAiKey() # UpdateAiKey | 

    try:
        # Изменение ключа AI Gateway
        api_response = api_instance.update_ai_key(key_id, update_ai_key)
        print("The response of AIGatewayApi->update_ai_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->update_ai_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | [**object**](.md)| ID ключа AI Gateway (UUID) | 
 **update_ai_key** | [**UpdateAiKey**](UpdateAiKey.md)|  | 

### Return type

[**UpdateAiKey200Response**](UpdateAiKey200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ai_key&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ai_key_limit**
> CreateAiKeyLimit201Response update_ai_key_limit(key_id, limit_id, update_ai_key_limit)

Изменение лимита ключа AI Gateway

Чтобы изменить лимит ключа AI Gateway, отправьте PATCH-запрос на `/api/v1/cloud-ai/ai-keys/{key_id}/entity-limits/{limit_id}`.  Не переданные поля не меняются. Если не передан ни `limit`, ни `money_limit` или `money_limit` снимается без `limit`, вернётся 400 с `error_code` `entity_keys_limit_value_required`. Если лимит относится к другому ключу, вернётся 403.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_ai_key_limit201_response import CreateAiKeyLimit201Response
from timeweb_cloud_api.models.update_ai_key_limit import UpdateAiKeyLimit
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
    api_instance = timeweb_cloud_api.AIGatewayApi(api_client)
    key_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID ключа AI Gateway (UUID)
    limit_id = 0f6b7d8e-1c2a-4b3d-9e8f-7a6b5c4d3e2f # object | ID лимита (UUID)
    update_ai_key_limit = timeweb_cloud_api.UpdateAiKeyLimit() # UpdateAiKeyLimit | 

    try:
        # Изменение лимита ключа AI Gateway
        api_response = api_instance.update_ai_key_limit(key_id, limit_id, update_ai_key_limit)
        print("The response of AIGatewayApi->update_ai_key_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayApi->update_ai_key_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | [**object**](.md)| ID ключа AI Gateway (UUID) | 
 **limit_id** | [**object**](.md)| ID лимита (UUID) | 
 **update_ai_key_limit** | [**UpdateAiKeyLimit**](UpdateAiKeyLimit.md)|  | 

### Return type

[**CreateAiKeyLimit201Response**](CreateAiKeyLimit201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ai_key_entity_limit&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

