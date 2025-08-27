# timeweb_cloud_api.S3Api

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_storage_subdomain_certificate**](S3Api.md#add_storage_subdomain_certificate) | **POST** /api/v1/storages/certificates/generate | Добавление сертификата для поддомена хранилища
[**add_storage_subdomains**](S3Api.md#add_storage_subdomains) | **POST** /api/v1/storages/buckets/{bucket_id}/subdomains | Добавление поддоменов для хранилища
[**create_storage**](S3Api.md#create_storage) | **POST** /api/v1/storages/buckets | Создание хранилища
[**delete_storage**](S3Api.md#delete_storage) | **DELETE** /api/v1/storages/buckets/{bucket_id} | Удаление хранилища на аккаунте
[**delete_storage_subdomains**](S3Api.md#delete_storage_subdomains) | **DELETE** /api/v1/storages/buckets/{bucket_id}/subdomains | Удаление поддоменов хранилища
[**get_storage_subdomains**](S3Api.md#get_storage_subdomains) | **GET** /api/v1/storages/buckets/{bucket_id}/subdomains | Получение списка поддоменов хранилища
[**get_storage_transfer_status**](S3Api.md#get_storage_transfer_status) | **GET** /api/v1/storages/buckets/{bucket_id}/transfer-status | Получение статуса переноса хранилища от стороннего S3 в Timeweb Cloud
[**get_storage_users**](S3Api.md#get_storage_users) | **GET** /api/v1/storages/users | Получение списка пользователей хранилищ аккаунта
[**get_storages**](S3Api.md#get_storages) | **GET** /api/v1/storages/buckets | Получение списка хранилищ аккаунта
[**get_storages_presets**](S3Api.md#get_storages_presets) | **GET** /api/v1/presets/storages | Получение списка тарифов для хранилищ
[**transfer_storage**](S3Api.md#transfer_storage) | **POST** /api/v1/storages/transfer | Перенос хранилища от стороннего провайдера S3 в Timeweb Cloud
[**update_storage**](S3Api.md#update_storage) | **PATCH** /api/v1/storages/buckets/{bucket_id} | Изменение хранилища на аккаунте
[**update_storage_user**](S3Api.md#update_storage_user) | **PATCH** /api/v1/storages/users/{user_id} | Изменение пароля пользователя-администратора хранилища


# **add_storage_subdomain_certificate**
> add_storage_subdomain_certificate(add_storage_subdomain_certificate_request)

Добавление сертификата для поддомена хранилища

Чтобы добавить сертификат для поддомена хранилища, отправьте POST-запрос на `/api/v1/storages/certificates/generate`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_storage_subdomain_certificate_request import AddStorageSubdomainCertificateRequest
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
    api_instance = timeweb_cloud_api.S3Api(api_client)
    add_storage_subdomain_certificate_request = timeweb_cloud_api.AddStorageSubdomainCertificateRequest() # AddStorageSubdomainCertificateRequest | 

    try:
        # Добавление сертификата для поддомена хранилища
        api_instance.add_storage_subdomain_certificate(add_storage_subdomain_certificate_request)
    except Exception as e:
        print("Exception when calling S3Api->add_storage_subdomain_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_storage_subdomain_certificate_request** | [**AddStorageSubdomainCertificateRequest**](AddStorageSubdomainCertificateRequest.md)|  | 

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
**204** | Сертификат добавлен |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_storage_subdomains**
> AddStorageSubdomains200Response add_storage_subdomains(bucket_id, add_storage_subdomains_request)

Добавление поддоменов для хранилища

Чтобы добавить поддомены для хранилища, отправьте POST-запрос на `/api/v1/storages/buckets/{bucket_id}/subdomains`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_storage_subdomains200_response import AddStorageSubdomains200Response
from timeweb_cloud_api.models.add_storage_subdomains_request import AddStorageSubdomainsRequest
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
    api_instance = timeweb_cloud_api.S3Api(api_client)
    bucket_id = 1051 # object | ID хранилища.
    add_storage_subdomains_request = timeweb_cloud_api.AddStorageSubdomainsRequest() # AddStorageSubdomainsRequest | 

    try:
        # Добавление поддоменов для хранилища
        api_response = api_instance.add_storage_subdomains(bucket_id, add_storage_subdomains_request)
        print("The response of S3Api->add_storage_subdomains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3Api->add_storage_subdomains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | [**object**](.md)| ID хранилища. | 
 **add_storage_subdomains_request** | [**AddStorageSubdomainsRequest**](AddStorageSubdomainsRequest.md)|  | 

### Return type

[**AddStorageSubdomains200Response**](AddStorageSubdomains200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;subdomains&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_storage**
> CreateStorage201Response create_storage(create_storage_request)

Создание хранилища

Чтобы создать хранилище, отправьте POST-запрос на `/api/v1/storages/buckets`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_storage201_response import CreateStorage201Response
from timeweb_cloud_api.models.create_storage_request import CreateStorageRequest
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
    api_instance = timeweb_cloud_api.S3Api(api_client)
    create_storage_request = timeweb_cloud_api.CreateStorageRequest() # CreateStorageRequest | 

    try:
        # Создание хранилища
        api_response = api_instance.create_storage(create_storage_request)
        print("The response of S3Api->create_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3Api->create_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_storage_request** | [**CreateStorageRequest**](CreateStorageRequest.md)|  | 

### Return type

[**CreateStorage201Response**](CreateStorage201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;bucket&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage**
> DeleteStorage200Response delete_storage(bucket_id, hash=hash, code=code)

Удаление хранилища на аккаунте

Чтобы удалить хранилище, отправьте DELETE-запрос на `/api/v1/storages/buckets/{bucket_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.delete_storage200_response import DeleteStorage200Response
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
    api_instance = timeweb_cloud_api.S3Api(api_client)
    bucket_id = 1051 # object | ID хранилища.
    hash = 15095f25-aac3-4d60-a788-96cb5136f186 # object | Хеш, который совместно с кодом авторизации надо отправить для удаления, если включено подтверждение удаления сервисов через Телеграм. (optional)
    code = 0000 # object | Код подтверждения, который придет к вам в Телеграм, после запроса удаления, если включено подтверждение удаления сервисов.  При помощи API токена сервисы можно удалять без подтверждения, если параметр токена `is_able_to_delete` установлен в значение `true` (optional)

    try:
        # Удаление хранилища на аккаунте
        api_response = api_instance.delete_storage(bucket_id, hash=hash, code=code)
        print("The response of S3Api->delete_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3Api->delete_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | [**object**](.md)| ID хранилища. | 
 **hash** | [**object**](.md)| Хеш, который совместно с кодом авторизации надо отправить для удаления, если включено подтверждение удаления сервисов через Телеграм. | [optional] 
 **code** | [**object**](.md)| Код подтверждения, который придет к вам в Телеграм, после запроса удаления, если включено подтверждение удаления сервисов.  При помощи API токена сервисы можно удалять без подтверждения, если параметр токена &#x60;is_able_to_delete&#x60; установлен в значение &#x60;true&#x60; | [optional] 

### Return type

[**DeleteStorage200Response**](DeleteStorage200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;bucket_delete&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_storage_subdomains**
> AddStorageSubdomains200Response delete_storage_subdomains(bucket_id, add_storage_subdomains_request)

Удаление поддоменов хранилища

Чтобы удалить поддомены хранилища, отправьте DELETE-запрос на `/api/v1/storages/buckets/{bucket_id}/subdomains`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_storage_subdomains200_response import AddStorageSubdomains200Response
from timeweb_cloud_api.models.add_storage_subdomains_request import AddStorageSubdomainsRequest
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
    api_instance = timeweb_cloud_api.S3Api(api_client)
    bucket_id = 1051 # object | ID хранилища.
    add_storage_subdomains_request = timeweb_cloud_api.AddStorageSubdomainsRequest() # AddStorageSubdomainsRequest | 

    try:
        # Удаление поддоменов хранилища
        api_response = api_instance.delete_storage_subdomains(bucket_id, add_storage_subdomains_request)
        print("The response of S3Api->delete_storage_subdomains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3Api->delete_storage_subdomains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | [**object**](.md)| ID хранилища. | 
 **add_storage_subdomains_request** | [**AddStorageSubdomainsRequest**](AddStorageSubdomainsRequest.md)|  | 

### Return type

[**AddStorageSubdomains200Response**](AddStorageSubdomains200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;subdomains&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_subdomains**
> GetStorageSubdomains200Response get_storage_subdomains(bucket_id)

Получение списка поддоменов хранилища

Чтобы получить список поддоменов хранилища, отправьте GET-запрос на `/api/v1/storages/buckets/{bucket_id}/subdomains`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_storage_subdomains200_response import GetStorageSubdomains200Response
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
    api_instance = timeweb_cloud_api.S3Api(api_client)
    bucket_id = 1051 # object | ID хранилища.

    try:
        # Получение списка поддоменов хранилища
        api_response = api_instance.get_storage_subdomains(bucket_id)
        print("The response of S3Api->get_storage_subdomains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3Api->get_storage_subdomains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | [**object**](.md)| ID хранилища. | 

### Return type

[**GetStorageSubdomains200Response**](GetStorageSubdomains200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;subdomains&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_transfer_status**
> GetStorageTransferStatus200Response get_storage_transfer_status(bucket_id)

Получение статуса переноса хранилища от стороннего S3 в Timeweb Cloud

Чтобы получить статус переноса хранилища от стороннего S3 в Timeweb Cloud, отправьте GET-запрос на `/api/v1/storages/buckets/{bucket_id}/transfer-status`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_storage_transfer_status200_response import GetStorageTransferStatus200Response
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
    api_instance = timeweb_cloud_api.S3Api(api_client)
    bucket_id = 1051 # object | ID хранилища.

    try:
        # Получение статуса переноса хранилища от стороннего S3 в Timeweb Cloud
        api_response = api_instance.get_storage_transfer_status(bucket_id)
        print("The response of S3Api->get_storage_transfer_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3Api->get_storage_transfer_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | [**object**](.md)| ID хранилища. | 

### Return type

[**GetStorageTransferStatus200Response**](GetStorageTransferStatus200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;transfer_status&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_users**
> GetStorageUsers200Response get_storage_users()

Получение списка пользователей хранилищ аккаунта

Чтобы получить список пользователей хранилищ аккаунта, отправьте GET-запрос на `/api/v1/storages/users`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_storage_users200_response import GetStorageUsers200Response
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
    api_instance = timeweb_cloud_api.S3Api(api_client)

    try:
        # Получение списка пользователей хранилищ аккаунта
        api_response = api_instance.get_storage_users()
        print("The response of S3Api->get_storage_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3Api->get_storage_users: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetStorageUsers200Response**](GetStorageUsers200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;users&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storages**
> GetProjectStorages200Response get_storages()

Получение списка хранилищ аккаунта

Чтобы получить список хранилищ аккаунта, отправьте GET-запрос на `/api/v1/storages/buckets`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_project_storages200_response import GetProjectStorages200Response
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
    api_instance = timeweb_cloud_api.S3Api(api_client)

    try:
        # Получение списка хранилищ аккаунта
        api_response = api_instance.get_storages()
        print("The response of S3Api->get_storages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3Api->get_storages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetProjectStorages200Response**](GetProjectStorages200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;buckets&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storages_presets**
> GetStoragesPresets200Response get_storages_presets()

Получение списка тарифов для хранилищ

Чтобы получить список тарифов для хранилищ, отправьте GET-запрос на `/api/v1/presets/storages`.   Тело ответа будет представлять собой объект JSON с ключом `storages_presets`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_storages_presets200_response import GetStoragesPresets200Response
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
    api_instance = timeweb_cloud_api.S3Api(api_client)

    try:
        # Получение списка тарифов для хранилищ
        api_response = api_instance.get_storages_presets()
        print("The response of S3Api->get_storages_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3Api->get_storages_presets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetStoragesPresets200Response**](GetStoragesPresets200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON с ключом &#x60;storages_presets&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_storage**
> transfer_storage(transfer_storage_request)

Перенос хранилища от стороннего провайдера S3 в Timeweb Cloud

Чтобы перенести хранилище от стороннего провайдера S3 в Timeweb Cloud, отправьте POST-запрос на `/api/v1/storages/transfer`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.transfer_storage_request import TransferStorageRequest
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
    api_instance = timeweb_cloud_api.S3Api(api_client)
    transfer_storage_request = timeweb_cloud_api.TransferStorageRequest() # TransferStorageRequest | 

    try:
        # Перенос хранилища от стороннего провайдера S3 в Timeweb Cloud
        api_instance.transfer_storage(transfer_storage_request)
    except Exception as e:
        print("Exception when calling S3Api->transfer_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transfer_storage_request** | [**TransferStorageRequest**](TransferStorageRequest.md)|  | 

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
**204** | Задание на перенос отправлено |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage**
> CreateStorage201Response update_storage(bucket_id, update_storage_request)

Изменение хранилища на аккаунте

Чтобы изменить хранилище, отправьте PATCH-запрос на `/api/v1/storages/buckets/{bucket_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_storage201_response import CreateStorage201Response
from timeweb_cloud_api.models.update_storage_request import UpdateStorageRequest
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
    api_instance = timeweb_cloud_api.S3Api(api_client)
    bucket_id = 1051 # object | ID хранилища.
    update_storage_request = timeweb_cloud_api.UpdateStorageRequest() # UpdateStorageRequest | 

    try:
        # Изменение хранилища на аккаунте
        api_response = api_instance.update_storage(bucket_id, update_storage_request)
        print("The response of S3Api->update_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3Api->update_storage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | [**object**](.md)| ID хранилища. | 
 **update_storage_request** | [**UpdateStorageRequest**](UpdateStorageRequest.md)|  | 

### Return type

[**CreateStorage201Response**](CreateStorage201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;bucket&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage_user**
> UpdateStorageUser200Response update_storage_user(user_id, update_storage_user_request)

Изменение пароля пользователя-администратора хранилища

Чтобы изменить пароль пользователя-администратора хранилища, отправьте POST-запрос на `/api/v1/storages/users/{user_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.update_storage_user200_response import UpdateStorageUser200Response
from timeweb_cloud_api.models.update_storage_user_request import UpdateStorageUserRequest
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
    api_instance = timeweb_cloud_api.S3Api(api_client)
    user_id = 1051 # object | ID пользователя хранилища.
    update_storage_user_request = timeweb_cloud_api.UpdateStorageUserRequest() # UpdateStorageUserRequest | 

    try:
        # Изменение пароля пользователя-администратора хранилища
        api_response = api_instance.update_storage_user(user_id, update_storage_user_request)
        print("The response of S3Api->update_storage_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling S3Api->update_storage_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)| ID пользователя хранилища. | 
 **update_storage_user_request** | [**UpdateStorageUserRequest**](UpdateStorageUserRequest.md)|  | 

### Return type

[**UpdateStorageUser200Response**](UpdateStorageUser200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;user&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

