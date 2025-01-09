# timeweb_cloud_api.APIKeysApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token**](APIKeysApi.md#create_token) | **POST** /api/v1/auth/api-keys | Создание токена
[**delete_token**](APIKeysApi.md#delete_token) | **DELETE** /api/v1/auth/api-keys/{token_id} | Удалить токен
[**get_tokens**](APIKeysApi.md#get_tokens) | **GET** /api/v1/auth/api-keys | Получение списка выпущенных токенов
[**reissue_token**](APIKeysApi.md#reissue_token) | **PUT** /api/v1/auth/api-keys/{token_id} | Перевыпустить токен
[**update_token**](APIKeysApi.md#update_token) | **PATCH** /api/v1/auth/api-keys/{token_id} | Изменить токен


# **create_token**
> CreateToken201Response create_token(create_api_key)

Создание токена

Чтобы создать токен, отправьте POST-запрос на `/api/v1/auth/api-keys`, задав необходимые атрибуты.  Токен будет создан с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданном токене.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_api_key import CreateApiKey
from timeweb_cloud_api.models.create_token201_response import CreateToken201Response
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
    except Exception as e:
        print("Exception when calling APIKeysApi->create_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_api_key** | [**CreateApiKey**](CreateApiKey.md)|  | 

### Return type

[**CreateToken201Response**](CreateToken201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON c ключом &#x60;api_key&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_token**
> delete_token(token_id)

Удалить токен

Чтобы удалить токен, отправьте DELETE-запрос на `/api/v1/auth/api-keys/{token_id}`.

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
    api_instance = timeweb_cloud_api.APIKeysApi(api_client)
    token_id = None # object | ID токена

    try:
        # Удалить токен
        api_instance.delete_token(token_id)
    except Exception as e:
        print("Exception when calling APIKeysApi->delete_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | [**object**](.md)| ID токена | 

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
**204** | Токен успешно удален. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tokens**
> GetTokens200Response get_tokens()

Получение списка выпущенных токенов

Чтобы получить список выпущенных токенов, отправьте GET-запрос на `/api/v1/auth/api-keys`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_tokens200_response import GetTokens200Response
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

    try:
        # Получение списка выпущенных токенов
        api_response = api_instance.get_tokens()
        print("The response of APIKeysApi->get_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->get_tokens: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetTokens200Response**](GetTokens200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;api_keys&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reissue_token**
> CreateToken201Response reissue_token(token_id, refresh_api_key)

Перевыпустить токен

Чтобы перевыпустить токен, отправьте PUT-запрос на `/api/v1/auth/api-keys/{token_id}`, задав необходимые атрибуты.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_token201_response import CreateToken201Response
from timeweb_cloud_api.models.refresh_api_key import RefreshApiKey
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
    token_id = None # object | ID токена
    refresh_api_key = timeweb_cloud_api.RefreshApiKey() # RefreshApiKey | 

    try:
        # Перевыпустить токен
        api_response = api_instance.reissue_token(token_id, refresh_api_key)
        print("The response of APIKeysApi->reissue_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->reissue_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | [**object**](.md)| ID токена | 
 **refresh_api_key** | [**RefreshApiKey**](RefreshApiKey.md)|  | 

### Return type

[**CreateToken201Response**](CreateToken201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;api_key&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_token**
> UpdateToken200Response update_token(token_id, edit_api_key)

Изменить токен

Чтобы изменить токен, отправьте PATCH-запрос на `/api/v1/auth/api-keys/{token_id}`, задав необходимые атрибуты.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.edit_api_key import EditApiKey
from timeweb_cloud_api.models.update_token200_response import UpdateToken200Response
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
    token_id = None # object | ID токена
    edit_api_key = timeweb_cloud_api.EditApiKey() # EditApiKey | 

    try:
        # Изменить токен
        api_response = api_instance.update_token(token_id, edit_api_key)
        print("The response of APIKeysApi->update_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIKeysApi->update_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | [**object**](.md)| ID токена | 
 **edit_api_key** | [**EditApiKey**](EditApiKey.md)|  | 

### Return type

[**UpdateToken200Response**](UpdateToken200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;api_key&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

