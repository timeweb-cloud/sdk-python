# timeweb_cloud_api.AIModelsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agents_token_packages**](AIModelsApi.md#get_agents_token_packages) | **GET** /api/v1/cloud-ai/token-packages/agents | Получение списка пакетов токенов для агентов
[**get_ai_model_parameters**](AIModelsApi.md#get_ai_model_parameters) | **GET** /api/v3/cloud-ai/model-parameters | Получение справочника характеристик моделей
[**get_ai_model_token_packages**](AIModelsApi.md#get_ai_model_token_packages) | **GET** /api/v1/cloud-ai/models/{id}/token-packages | Получение пакетов токенов модели
[**get_ai_provider**](AIModelsApi.md#get_ai_provider) | **GET** /api/v1/cloud-ai/providers/{id} | Получение провайдера моделей
[**get_ai_providers**](AIModelsApi.md#get_ai_providers) | **GET** /api/v1/cloud-ai/providers | Получение списка провайдеров моделей
[**get_knowledgebases_token_packages**](AIModelsApi.md#get_knowledgebases_token_packages) | **GET** /api/v1/cloud-ai/token-packages/knowledge-bases | Получение списка пакетов токенов для баз знаний
[**get_models**](AIModelsApi.md#get_models) | **GET** /api/v1/cloud-ai/models | Получение списка моделей (v1)
[**get_models_v3**](AIModelsApi.md#get_models_v3) | **GET** /api/v3/cloud-ai/models | Получение списка моделей


# **get_agents_token_packages**
> GetAgentsTokenPackages200Response get_agents_token_packages()

Получение списка пакетов токенов для агентов

Метод устарел.  Чтобы получить список пакетов токенов для AI агентов всех моделей, отправьте GET-запрос на `/api/v1/cloud-ai/token-packages/agents`.  Тело ответа будет представлять собой объект JSON с ключами `token_packages` и `meta`.

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
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_model_parameters**
> GetAiModelParameters200Response get_ai_model_parameters()

Получение справочника характеристик моделей

Чтобы получить справочник характеристик, которые возвращаются в `parameter_values` моделей, отправьте GET-запрос на `/api/v3/cloud-ai/model-parameters`.  Справочник описывает название, тип, единицу измерения и направление сравнения каждой характеристики. Цены кэша (`cost_cache_read`, `cost_cache_write`) в справочник не входят.  Тело ответа будет представлять собой объект JSON с ключами `model_parameters` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_model_parameters200_response import GetAiModelParameters200Response
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
        # Получение справочника характеристик моделей
        api_response = api_instance.get_ai_model_parameters()
        print("The response of AIModelsApi->get_ai_model_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIModelsApi->get_ai_model_parameters: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAiModelParameters200Response**](GetAiModelParameters200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;model_parameters&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_model_token_packages**
> GetAiModelTokenPackages200Response get_ai_model_token_packages(id)

Получение пакетов токенов модели

Чтобы получить пакеты токенов, доступные для AI модели, отправьте GET-запрос на `/api/v1/cloud-ai/models/{id}/token-packages`.  Тело ответа будет представлять собой объект JSON с ключами `token_packages` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_model_token_packages200_response import GetAiModelTokenPackages200Response
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
    id = 17 # object | ID модели

    try:
        # Получение пакетов токенов модели
        api_response = api_instance.get_ai_model_token_packages(id)
        print("The response of AIModelsApi->get_ai_model_token_packages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIModelsApi->get_ai_model_token_packages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID модели | 

### Return type

[**GetAiModelTokenPackages200Response**](GetAiModelTokenPackages200Response.md)

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
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_provider**
> GetAiProvider200Response get_ai_provider(id)

Получение провайдера моделей

Чтобы получить информацию о провайдере AI моделей, отправьте GET-запрос на `/api/v1/cloud-ai/providers/{id}`.  Тело ответа будет представлять собой объект JSON с ключом `provider`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_provider200_response import GetAiProvider200Response
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
    id = 1 # object | ID провайдера

    try:
        # Получение провайдера моделей
        api_response = api_instance.get_ai_provider(id)
        print("The response of AIModelsApi->get_ai_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIModelsApi->get_ai_provider: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID провайдера | 

### Return type

[**GetAiProvider200Response**](GetAiProvider200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;provider&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_providers**
> GetAiProviders200Response get_ai_providers()

Получение списка провайдеров моделей

Чтобы получить список провайдеров AI моделей, отправьте GET-запрос на `/api/v1/cloud-ai/providers`.  Провайдер модели — поле `provider_id` модели.  Тело ответа будет представлять собой объект JSON с ключами `providers` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_providers200_response import GetAiProviders200Response
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
        # Получение списка провайдеров моделей
        api_response = api_instance.get_ai_providers()
        print("The response of AIModelsApi->get_ai_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIModelsApi->get_ai_providers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAiProviders200Response**](GetAiProviders200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;providers&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledgebases_token_packages**
> GetKnowledgebasesTokenPackages200Response get_knowledgebases_token_packages()

Получение списка пакетов токенов для баз знаний

Чтобы получить список пакетов токенов для баз знаний, отправьте GET-запрос на `/api/v1/cloud-ai/token-packages/knowledge-bases`.  Базовый пакет (`package_type: base`) указывается при создании базы знаний, дополнительный (`package_type: additional`) покупается через `POST /api/v1/cloud-ai/knowledge-bases/{id}/add-additional-token-package`.  Тело ответа будет представлять собой объект JSON с ключами `token_packages` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_knowledgebases_token_packages200_response import GetKnowledgebasesTokenPackages200Response
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

[**GetKnowledgebasesTokenPackages200Response**](GetKnowledgebasesTokenPackages200Response.md)

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
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models**
> GetModels200Response get_models()

Получение списка моделей (v1)

Метод устарел — используйте `GET /api/v3/cloud-ai/models`.  Чтобы получить список AI моделей, отправьте GET-запрос на `/api/v1/cloud-ai/models`.  Тело ответа будет представлять собой объект JSON с ключами `models` и `meta`.

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
        # Получение списка моделей (v1)
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
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models_v3**
> GetModelsV3200Response get_models_v3()

Получение списка моделей

Чтобы получить список AI моделей с ценами и характеристиками, отправьте GET-запрос на `/api/v3/cloud-ai/models`.  Цены и характеристики (контекст, модальности, индексы качества) возвращаются в словаре `parameter_values`, их названия и единицы — в справочнике `GET /api/v3/cloud-ai/model-parameters`. В списке есть и устаревшие модели — проверяйте `is_deprecated` и `is_stopped`.  Тело ответа будет представлять собой объект JSON с ключами `models` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_models_v3200_response import GetModelsV3200Response
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
        api_response = api_instance.get_models_v3()
        print("The response of AIModelsApi->get_models_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIModelsApi->get_models_v3: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetModelsV3200Response**](GetModelsV3200Response.md)

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
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

