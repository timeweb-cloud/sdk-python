# timeweb_cloud_api.AIAgentsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_additional_token_package**](AIAgentsApi.md#add_additional_token_package) | **POST** /api/v1/cloud-ai/agents/{id}/add-additional-token-package | Добавление дополнительного пакета токенов
[**create_agent**](AIAgentsApi.md#create_agent) | **POST** /api/v1/cloud-ai/agents | Создание AI агента
[**delete_agent**](AIAgentsApi.md#delete_agent) | **DELETE** /api/v1/cloud-ai/agents/{id} | Удаление AI агента
[**get_agent**](AIAgentsApi.md#get_agent) | **GET** /api/v1/cloud-ai/agents/{id} | Получение AI агента
[**get_agent_statistics**](AIAgentsApi.md#get_agent_statistics) | **GET** /api/v1/cloud-ai/agents/{id}/statistic | Получение статистики использования токенов агента
[**get_agents**](AIAgentsApi.md#get_agents) | **GET** /api/v1/cloud-ai/agents | Получение списка AI агентов
[**update_agent**](AIAgentsApi.md#update_agent) | **PATCH** /api/v1/cloud-ai/agents/{id} | Обновление AI агента


# **add_additional_token_package**
> add_additional_token_package(id, add_token_package=add_token_package)

Добавление дополнительного пакета токенов

Чтобы добавить дополнительный пакет токенов для AI агента, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{id}/add-additional-token-package`.

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

# **create_agent**
> CreateAgent201Response create_agent(create_agent)

Создание AI агента

Чтобы создать AI агента, отправьте POST-запрос на `/api/v1/cloud-ai/agents`, задав необходимые атрибуты.  Агент будет создан с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданном агенте.

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
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent**
> delete_agent(id)

Удаление AI агента

Чтобы удалить AI агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/agents/{id}`.

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

    try:
        # Удаление AI агента
        api_instance.delete_agent(id)
    except Exception as e:
        print("Exception when calling AIAgentsApi->delete_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID агента | 

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
**204** | AI агент успешно удален |  -  |
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

Чтобы получить информацию об AI агенте, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{id}`.

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

# **get_agent_statistics**
> GetAgentStatistics200Response get_agent_statistics(id, start_time=start_time, end_time=end_time, interval=interval)

Получение статистики использования токенов агента

Чтобы получить статистику использования токенов AI агента, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{id}/statistic`.  Можно указать временной диапазон и интервал агрегации.

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
    start_time = 2024-10-01T00:00:00.000Z # object | Начало временного диапазона (ISO 8601) (optional)
    end_time = 2024-10-16T23:59:59.999Z # object | Конец временного диапазона (ISO 8601) (optional)
    interval = 60 # object | Интервал в минутах (по умолчанию 60) (optional)

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
 **start_time** | [**object**](.md)| Начало временного диапазона (ISO 8601) | [optional] 
 **end_time** | [**object**](.md)| Конец временного диапазона (ISO 8601) | [optional] 
 **interval** | [**object**](.md)| Интервал в минутах (по умолчанию 60) | [optional] 

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

# **get_agents**
> GetAgents200Response get_agents()

Получение списка AI агентов

Чтобы получить список AI агентов, отправьте GET-запрос на `/api/v1/cloud-ai/agents`.  Тело ответа будет представлять собой объект JSON с ключом `agents`.

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
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent**
> CreateAgent201Response update_agent(id, update_agent)

Обновление AI агента

Чтобы обновить AI агента, отправьте PATCH-запрос на `/api/v1/cloud-ai/agents/{id}`.

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
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

