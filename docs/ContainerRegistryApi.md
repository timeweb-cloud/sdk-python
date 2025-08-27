# timeweb_cloud_api.ContainerRegistryApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_registry**](ContainerRegistryApi.md#create_registry) | **POST** /api/v1/container-registry | Создание реестра
[**delete_registry**](ContainerRegistryApi.md#delete_registry) | **DELETE** /api/v1/container-registry/{registry_id} | Удаление реестра
[**get_registries**](ContainerRegistryApi.md#get_registries) | **GET** /api/v1/container-registry | Получение списка реестров контейнеров
[**get_registry**](ContainerRegistryApi.md#get_registry) | **GET** /api/v1/container-registry/{registry_id} | Получение информации о реестре
[**get_registry_presets**](ContainerRegistryApi.md#get_registry_presets) | **GET** /api/v1/container-registry/presets | Получение списка тарифов
[**get_registry_repositories**](ContainerRegistryApi.md#get_registry_repositories) | **GET** /api/v1/container-registry/{registry_id}/repositories | Получение списка репозиториев
[**update_registry**](ContainerRegistryApi.md#update_registry) | **PATCH** /api/v1/container-registry/{registry_id} | Обновление информации о реестре


# **create_registry**
> RegistryResponse create_registry(registry_in)

Создание реестра

Чтобы создать реестр, отправьте POST-запрос на `/api/v1/container-registry`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.registry_in import RegistryIn
from timeweb_cloud_api.models.registry_response import RegistryResponse
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
    api_instance = timeweb_cloud_api.ContainerRegistryApi(api_client)
    registry_in = timeweb_cloud_api.RegistryIn() # RegistryIn | 

    try:
        # Создание реестра
        api_response = api_instance.create_registry(registry_in)
        print("The response of ContainerRegistryApi->create_registry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerRegistryApi->create_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_in** | [**RegistryIn**](RegistryIn.md)|  | 

### Return type

[**RegistryResponse**](RegistryResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Информация о реестре |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_registry**
> delete_registry(registry_id)

Удаление реестра

Чтобы удалить реестр, отправьте DELETE-запрос в `/api/v1/container-registry/{registry_id}`

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
    api_instance = timeweb_cloud_api.ContainerRegistryApi(api_client)
    registry_id = None # object | ID реестра

    try:
        # Удаление реестра
        api_instance.delete_registry(registry_id)
    except Exception as e:
        print("Exception when calling ContainerRegistryApi->delete_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | [**object**](.md)| ID реестра | 

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
**204** | Реестр удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registries**
> RegistriesResponse get_registries()

Получение списка реестров контейнеров

Чтобы получить список реестров, отправьте GET-запрос на `/api/v1/container-registry`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.registries_response import RegistriesResponse
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
    api_instance = timeweb_cloud_api.ContainerRegistryApi(api_client)

    try:
        # Получение списка реестров контейнеров
        api_response = api_instance.get_registries()
        print("The response of ContainerRegistryApi->get_registries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerRegistryApi->get_registries: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RegistriesResponse**](RegistriesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список реестров |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry**
> RegistryResponse get_registry(registry_id)

Получение информации о реестре

Чтобы получить информацию о реестре, отправьте GET-запрос в `/api/v1/container-registry/{registry_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.registry_response import RegistryResponse
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
    api_instance = timeweb_cloud_api.ContainerRegistryApi(api_client)
    registry_id = None # object | ID реестра

    try:
        # Получение информации о реестре
        api_response = api_instance.get_registry(registry_id)
        print("The response of ContainerRegistryApi->get_registry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerRegistryApi->get_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | [**object**](.md)| ID реестра | 

### Return type

[**RegistryResponse**](RegistryResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о реестре |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_presets**
> SchemasPresetsResponse get_registry_presets()

Получение списка тарифов

Чтобы получить список тарифов, отправьте GET-запрос в `/api/v1/container-registry/presets`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.schemas_presets_response import SchemasPresetsResponse
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
    api_instance = timeweb_cloud_api.ContainerRegistryApi(api_client)

    try:
        # Получение списка тарифов
        api_response = api_instance.get_registry_presets()
        print("The response of ContainerRegistryApi->get_registry_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerRegistryApi->get_registry_presets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SchemasPresetsResponse**](SchemasPresetsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список тарифов |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registry_repositories**
> RepositoriesResponse get_registry_repositories(registry_id)

Получение списка репозиториев

Чтобы получить список репозиториев, отправьте GET-запрос в `/api/v1/container-registry/{registry_id}/repositories`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.repositories_response import RepositoriesResponse
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
    api_instance = timeweb_cloud_api.ContainerRegistryApi(api_client)
    registry_id = None # object | ID реестра

    try:
        # Получение списка репозиториев
        api_response = api_instance.get_registry_repositories(registry_id)
        print("The response of ContainerRegistryApi->get_registry_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerRegistryApi->get_registry_repositories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | [**object**](.md)| ID реестра | 

### Return type

[**RepositoriesResponse**](RepositoriesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список репозиториев |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_registry**
> RegistryResponse update_registry(registry_id, registry_edit)

Обновление информации о реестре

Чтобы обновить информацию о реестре, отправьте PATCH-запрос в `/api/v1/container-registry/{registry_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.registry_edit import RegistryEdit
from timeweb_cloud_api.models.registry_response import RegistryResponse
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
    api_instance = timeweb_cloud_api.ContainerRegistryApi(api_client)
    registry_id = None # object | ID реестра
    registry_edit = timeweb_cloud_api.RegistryEdit() # RegistryEdit | 

    try:
        # Обновление информации о реестре
        api_response = api_instance.update_registry(registry_id, registry_edit)
        print("The response of ContainerRegistryApi->update_registry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ContainerRegistryApi->update_registry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **registry_id** | [**object**](.md)| ID реестра | 
 **registry_edit** | [**RegistryEdit**](RegistryEdit.md)|  | 

### Return type

[**RegistryResponse**](RegistryResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о реестре |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

