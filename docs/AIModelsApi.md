# timeweb_cloud_api.AIModelsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agents_token_packages**](AIModelsApi.md#get_agents_token_packages) | **GET** /api/v1/cloud-ai/token-packages/agents | Получение списка пакетов токенов для агентов
[**get_knowledgebases_token_packages**](AIModelsApi.md#get_knowledgebases_token_packages) | **GET** /api/v1/cloud-ai/token-packages/knowledge-bases | Получение списка пакетов токенов для баз знаний
[**get_models**](AIModelsApi.md#get_models) | **GET** /api/v1/cloud-ai/models | Получение списка моделей


# **get_agents_token_packages**
> GetAgentsTokenPackages200Response get_agents_token_packages()

Получение списка пакетов токенов для агентов

Чтобы получить список доступных пакетов токенов для AI агентов, отправьте GET-запрос на `/api/v1/cloud-ai/token-packages/agents`.  Тело ответа будет представлять собой объект JSON с ключом `token_packages`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agents_token_packages200_response import GetAgentsTokenPackages200Response
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
    api_instance = timeweb_cloud_api.AIModelsApi(api_client)

    try:
        # Получение списка пакетов токенов для агентов
        api_response = api_instance.get_agents_token_packages()
        print("The response of AIModelsApi->get_agents_token_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIModelsApi->get_agents_token_packages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAgentsTokenPackages200Response**](GetAgentsTokenPackages200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;token_packages&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledgebases_token_packages**
> GetAgentsTokenPackages200Response get_knowledgebases_token_packages()

Получение списка пакетов токенов для баз знаний

Чтобы получить список доступных пакетов токенов для баз знаний, отправьте GET-запрос на `/api/v1/cloud-ai/token-packages/knowledge-bases`.  Тело ответа будет представлять собой объект JSON с ключом `token_packages`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agents_token_packages200_response import GetAgentsTokenPackages200Response
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
    api_instance = timeweb_cloud_api.AIModelsApi(api_client)

    try:
        # Получение списка пакетов токенов для баз знаний
        api_response = api_instance.get_knowledgebases_token_packages()
        print("The response of AIModelsApi->get_knowledgebases_token_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIModelsApi->get_knowledgebases_token_packages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAgentsTokenPackages200Response**](GetAgentsTokenPackages200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;token_packages&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> GetModels200Response get_models()

Получение списка моделей

Чтобы получить список доступных AI моделей, отправьте GET-запрос на `/api/v1/cloud-ai/models`.  Тело ответа будет представлять собой объект JSON с ключом `models`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_models200_response import GetModels200Response
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
    api_instance = timeweb_cloud_api.AIModelsApi(api_client)

    try:
        # Получение списка моделей
        api_response = api_instance.get_models()
        print("The response of AIModelsApi->get_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIModelsApi->get_models: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetModels200Response**](GetModels200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;models&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

