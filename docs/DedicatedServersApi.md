# openapi_client.DedicatedServersApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dedicated_server**](DedicatedServersApi.md#create_dedicated_server) | **POST** /api/v1/dedicated-servers | Создание выделенного сервера
[**delete_dedicated_server**](DedicatedServersApi.md#delete_dedicated_server) | **DELETE** /api/v1/dedicated-servers/{dedicated_id} | Удаление выделенного сервера
[**get_dedicated_server**](DedicatedServersApi.md#get_dedicated_server) | **GET** /api/v1/dedicated-servers/{dedicated_id} | Получение выделенного сервера
[**get_dedicated_server_preset_additional_services**](DedicatedServersApi.md#get_dedicated_server_preset_additional_services) | **GET** /api/v1/presets/dedicated-servers/{preset_id}/additional-services | Получение дополнительных услуг для выделенного сервера
[**get_dedicated_servers**](DedicatedServersApi.md#get_dedicated_servers) | **GET** /api/v1/dedicated-servers | Получение списка выделенных серверов
[**get_dedicated_servers_presets**](DedicatedServersApi.md#get_dedicated_servers_presets) | **GET** /api/v1/presets/dedicated-servers | Получение списка тарифов для выделенного сервера
[**update_dedicated_server**](DedicatedServersApi.md#update_dedicated_server) | **PATCH** /api/v1/dedicated-servers/{dedicated_id} | Обновление выделенного сервера


# **create_dedicated_server**
> CreateDedicatedServer201Response create_dedicated_server(create_dedicated_server)

Создание выделенного сервера

Чтобы создать выделенный сервер, отправьте POST-запрос в `api/v1/dedicated-servers`, задав необходимые атрибуты.  Выделенный сервер будет создан с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданном выделенном сервере.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.create_dedicated_server import CreateDedicatedServer
from openapi_client.models.create_dedicated_server201_response import CreateDedicatedServer201Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DedicatedServersApi(api_client)
    create_dedicated_server = openapi_client.CreateDedicatedServer() # CreateDedicatedServer | 

    try:
        # Создание выделенного сервера
        api_response = api_instance.create_dedicated_server(create_dedicated_server)
        print("The response of DedicatedServersApi->create_dedicated_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DedicatedServersApi->create_dedicated_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dedicated_server** | [**CreateDedicatedServer**](CreateDedicatedServer.md)|  | 

### Return type

[**CreateDedicatedServer201Response**](CreateDedicatedServer201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dedicated_server**
> delete_dedicated_server(dedicated_id)

Удаление выделенного сервера

Чтобы удалить выделенный сервер, отправьте запрос DELETE в `api/v1/dedicated-servers/{dedicated_id}`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DedicatedServersApi(api_client)
    dedicated_id = 1051 # object | Уникальный идентификатор выделенного сервера.

    try:
        # Удаление выделенного сервера
        api_instance.delete_dedicated_server(dedicated_id)
    except Exception as e:
        print("Exception when calling DedicatedServersApi->delete_dedicated_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dedicated_id** | [**object**](.md)| Уникальный идентификатор выделенного сервера. | 

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
**204** | Выделенный сервер успешно удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dedicated_server**
> CreateDedicatedServer201Response get_dedicated_server(dedicated_id)

Получение выделенного сервера

Чтобы отобразить информацию об отдельном выделенном сервере, отправьте запрос GET на `api/v1/dedicated-servers/{dedicated_id}`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.create_dedicated_server201_response import CreateDedicatedServer201Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DedicatedServersApi(api_client)
    dedicated_id = 1051 # object | Уникальный идентификатор выделенного сервера.

    try:
        # Получение выделенного сервера
        api_response = api_instance.get_dedicated_server(dedicated_id)
        print("The response of DedicatedServersApi->get_dedicated_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DedicatedServersApi->get_dedicated_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dedicated_id** | [**object**](.md)| Уникальный идентификатор выделенного сервера. | 

### Return type

[**CreateDedicatedServer201Response**](CreateDedicatedServer201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;dedicated_server&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dedicated_server_preset_additional_services**
> GetDedicatedServerPresetAdditionalServices200Response get_dedicated_server_preset_additional_services(preset_id)

Получение дополнительных услуг для выделенного сервера

Чтобы получить список всех дополнительных услуг для выделенных серверов, отправьте GET-запрос на `/api/v1/presets/dedicated-servers/{preset_id}/additional-services`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.get_dedicated_server_preset_additional_services200_response import GetDedicatedServerPresetAdditionalServices200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DedicatedServersApi(api_client)
    preset_id = 1051 # object | Уникальный идентификатор тарифа выделенного сервера.

    try:
        # Получение дополнительных услуг для выделенного сервера
        api_response = api_instance.get_dedicated_server_preset_additional_services(preset_id)
        print("The response of DedicatedServersApi->get_dedicated_server_preset_additional_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DedicatedServersApi->get_dedicated_server_preset_additional_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preset_id** | [**object**](.md)| Уникальный идентификатор тарифа выделенного сервера. | 

### Return type

[**GetDedicatedServerPresetAdditionalServices200Response**](GetDedicatedServerPresetAdditionalServices200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключем &#x60;dedicated_server_additional_services&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dedicated_servers**
> GetDedicatedServers200Response get_dedicated_servers()

Получение списка выделенных серверов

Чтобы получить список всех выделенных серверов на вашем аккаунте, отправьте GET-запрос на `/api/v1/dedicated-servers`.   Тело ответа будет представлять собой объект JSON с ключом `dedicated_servers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.get_dedicated_servers200_response import GetDedicatedServers200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DedicatedServersApi(api_client)

    try:
        # Получение списка выделенных серверов
        api_response = api_instance.get_dedicated_servers()
        print("The response of DedicatedServersApi->get_dedicated_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DedicatedServersApi->get_dedicated_servers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDedicatedServers200Response**](GetDedicatedServers200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;dedicated_servers&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dedicated_servers_presets**
> GetDedicatedServersPresets200Response get_dedicated_servers_presets(location=location)

Получение списка тарифов для выделенного сервера

Чтобы получить список всех тарифов выделенных серверов, отправьте GET-запрос на `/api/v1/presets/dedicated-servers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.get_dedicated_servers_presets200_response import GetDedicatedServersPresets200Response
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DedicatedServersApi(api_client)
    location = None # object | Получение тарифов определенной локации. (optional)

    try:
        # Получение списка тарифов для выделенного сервера
        api_response = api_instance.get_dedicated_servers_presets(location=location)
        print("The response of DedicatedServersApi->get_dedicated_servers_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DedicatedServersApi->get_dedicated_servers_presets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | [**object**](.md)| Получение тарифов определенной локации. | [optional] 

### Return type

[**GetDedicatedServersPresets200Response**](GetDedicatedServersPresets200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключем &#x60;dedicated_servers_presets&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dedicated_server**
> CreateDedicatedServer201Response update_dedicated_server(dedicated_id, update_dedicated_server_request=update_dedicated_server_request)

Обновление выделенного сервера

Чтобы обновить только определенные атрибуты выделенного сервера, отправьте запрос PATCH в `api/v1/dedicated-servers/{dedicated_id}`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.create_dedicated_server201_response import CreateDedicatedServer201Response
from openapi_client.models.update_dedicated_server_request import UpdateDedicatedServerRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.timeweb.cloud
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.timeweb.cloud"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DedicatedServersApi(api_client)
    dedicated_id = 1051 # object | Уникальный идентификатор выделенного сервера.
    update_dedicated_server_request = openapi_client.UpdateDedicatedServerRequest() # UpdateDedicatedServerRequest |  (optional)

    try:
        # Обновление выделенного сервера
        api_response = api_instance.update_dedicated_server(dedicated_id, update_dedicated_server_request=update_dedicated_server_request)
        print("The response of DedicatedServersApi->update_dedicated_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DedicatedServersApi->update_dedicated_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dedicated_id** | [**object**](.md)| Уникальный идентификатор выделенного сервера. | 
 **update_dedicated_server_request** | [**UpdateDedicatedServerRequest**](UpdateDedicatedServerRequest.md)|  | [optional] 

### Return type

[**CreateDedicatedServer201Response**](CreateDedicatedServer201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;dedicated_server&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

