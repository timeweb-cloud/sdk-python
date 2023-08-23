# timeweb_cloud_api.SSHApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_key_to_server**](SSHApi.md#add_key_to_server) | **POST** /api/v1/servers/{server_id}/ssh-keys | Добавление SSH-ключей на сервер
[**create_key**](SSHApi.md#create_key) | **POST** /api/v1/ssh-keys | Создание SSH-ключа
[**delete_key**](SSHApi.md#delete_key) | **DELETE** /api/v1/ssh-keys/{ssh_key_id} | Удаление SSH-ключа по уникальному идентификатору
[**delete_key_from_server**](SSHApi.md#delete_key_from_server) | **DELETE** /api/v1/servers/{server_id}/ssh-keys/{ssh_key_id} | Удаление SSH-ключей с сервера
[**get_key**](SSHApi.md#get_key) | **GET** /api/v1/ssh-keys/{ssh_key_id} | Получение SSH-ключа по уникальному идентификатору
[**get_keys**](SSHApi.md#get_keys) | **GET** /api/v1/ssh-keys | Получение списка SSH-ключей
[**update_key**](SSHApi.md#update_key) | **PATCH** /api/v1/ssh-keys/{ssh_key_id} | Изменение SSH-ключа по уникальному идентификатору


# **add_key_to_server**
> add_key_to_server(server_id, add_key_to_server_request)

Добавление SSH-ключей на сервер

Чтобы добавить SSH-ключи на сервер, отправьте POST-запрос на `/api/v1/servers/{server_id}/ssh-keys`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_key_to_server_request import AddKeyToServerRequest
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
    api_instance = timeweb_cloud_api.SSHApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    add_key_to_server_request = timeweb_cloud_api.AddKeyToServerRequest() # AddKeyToServerRequest | 

    try:
        # Добавление SSH-ключей на сервер
        api_instance.add_key_to_server(server_id, add_key_to_server_request)
    except Exception as e:
        print("Exception when calling SSHApi->add_key_to_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **add_key_to_server_request** | [**AddKeyToServerRequest**](AddKeyToServerRequest.md)|  | 

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
**204** | Успешное добавление SSH-ключей на сервер |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_key**
> CreateKey201Response create_key(create_key_request)

Создание SSH-ключа

Чтобы создать создать SSH-ключ, отправьте POST-запрос в `/api/v1/ssh-keys`, задав необходимые атрибуты.  

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_key201_response import CreateKey201Response
from timeweb_cloud_api.models.create_key_request import CreateKeyRequest
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
    api_instance = timeweb_cloud_api.SSHApi(api_client)
    create_key_request = timeweb_cloud_api.CreateKeyRequest() # CreateKeyRequest | 

    try:
        # Создание SSH-ключа
        api_response = api_instance.create_key(create_key_request)
        print("The response of SSHApi->create_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHApi->create_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_key_request** | [**CreateKeyRequest**](CreateKeyRequest.md)|  | 

### Return type

[**CreateKey201Response**](CreateKey201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;ssh-key&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key**
> delete_key(ssh_key_id)

Удаление SSH-ключа по уникальному идентификатору

Чтобы удалить SSH-ключ, отправьте DELETE-запрос на `/api/v1/ssh-keys/{ssh_key_id}`

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
    api_instance = timeweb_cloud_api.SSHApi(api_client)
    ssh_key_id = 1051 # object | Уникальный идентификатор SSH-ключа

    try:
        # Удаление SSH-ключа по уникальному идентификатору
        api_instance.delete_key(ssh_key_id)
    except Exception as e:
        print("Exception when calling SSHApi->delete_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_id** | [**object**](.md)| Уникальный идентификатор SSH-ключа | 

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
**204** | Успешное удаление SSH-ключа |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_key_from_server**
> delete_key_from_server(server_id, ssh_key_id)

Удаление SSH-ключей с сервера

Чтобы удалить SSH-ключ с сервера, отправьте DELETE-запрос на `/api/v1/servers/{server_id}/ssh-keys/{ssh_key_id}`

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
    api_instance = timeweb_cloud_api.SSHApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    ssh_key_id = 1051 # object | Уникальный идентификатор SSH-ключа

    try:
        # Удаление SSH-ключей с сервера
        api_instance.delete_key_from_server(server_id, ssh_key_id)
    except Exception as e:
        print("Exception when calling SSHApi->delete_key_from_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **ssh_key_id** | [**object**](.md)| Уникальный идентификатор SSH-ключа | 

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
**204** | Успешное удаление SSH-ключа с сервера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_key**
> GetKey200Response get_key(ssh_key_id)

Получение SSH-ключа по уникальному идентификатору

Чтобы получить SSH-ключ, отправьте GET-запрос на `/api/v1/ssh-keys/{ssh_key_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_key200_response import GetKey200Response
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
    api_instance = timeweb_cloud_api.SSHApi(api_client)
    ssh_key_id = 1051 # object | Уникальный идентификатор SSH-ключа

    try:
        # Получение SSH-ключа по уникальному идентификатору
        api_response = api_instance.get_key(ssh_key_id)
        print("The response of SSHApi->get_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHApi->get_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_id** | [**object**](.md)| Уникальный идентификатор SSH-ключа | 

### Return type

[**GetKey200Response**](GetKey200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ssh_key&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keys**
> GetKeys200Response get_keys()

Получение списка SSH-ключей

Чтобы получить список SSH-ключей, отправьте GET-запрос на `/api/v1/ssh-keys`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_keys200_response import GetKeys200Response
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
    api_instance = timeweb_cloud_api.SSHApi(api_client)

    try:
        # Получение списка SSH-ключей
        api_response = api_instance.get_keys()
        print("The response of SSHApi->get_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHApi->get_keys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetKeys200Response**](GetKeys200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ssh_keys&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_key**
> GetKey200Response update_key(ssh_key_id, update_key_request)

Изменение SSH-ключа по уникальному идентификатору

Чтобы изменить SSH-ключ, отправьте PATCH-запрос на `/api/v1/ssh-keys/{ssh_key_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_key200_response import GetKey200Response
from timeweb_cloud_api.models.update_key_request import UpdateKeyRequest
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
    api_instance = timeweb_cloud_api.SSHApi(api_client)
    ssh_key_id = 1051 # object | Уникальный идентификатор SSH-ключа
    update_key_request = timeweb_cloud_api.UpdateKeyRequest() # UpdateKeyRequest | 

    try:
        # Изменение SSH-ключа по уникальному идентификатору
        api_response = api_instance.update_key(ssh_key_id, update_key_request)
        print("The response of SSHApi->update_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SSHApi->update_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssh_key_id** | [**object**](.md)| Уникальный идентификатор SSH-ключа | 
 **update_key_request** | [**UpdateKeyRequest**](UpdateKeyRequest.md)|  | 

### Return type

[**GetKey200Response**](GetKey200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ssh_key&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

