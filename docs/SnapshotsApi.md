# timeweb_cloud_api.SnapshotsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_restore_point**](SnapshotsApi.md#commit_restore_point) | **POST** /api/v1/restore-points/{vds_id}/commit | Фиксация снапшота
[**create_restore_point**](SnapshotsApi.md#create_restore_point) | **POST** /api/v1/restore-points/{vds_id}/create | Создание снапшота
[**get_restore_point**](SnapshotsApi.md#get_restore_point) | **GET** /api/v1/restore-points/{vds_id} | Получение снапшота сервера
[**get_restore_points**](SnapshotsApi.md#get_restore_points) | **GET** /api/v1/restore-points | Получение списка снапшотов
[**rollback_restore_point**](SnapshotsApi.md#rollback_restore_point) | **POST** /api/v1/restore-points/{vds_id}/rollback | Откат к снапшоту


# **commit_restore_point**
> commit_restore_point(vds_id)

Фиксация снапшота

Чтобы зафиксировать (применить) снапшот облачного сервера (VDS), отправьте POST-запрос на `/api/v1/restore-points/{vds_id}/commit`.  Фиксация подтверждает текущее состояние сервера. Действие выполняется асинхронно, ответ не содержит тела.  Для выполнения действия сервер должен быть включён, иначе вернётся ошибка `403`.

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
    api_instance = timeweb_cloud_api.SnapshotsApi(api_client)
    vds_id = 1051 # object | ID облачного сервера (VDS).

    try:
        # Фиксация снапшота
        api_instance.commit_restore_point(vds_id)
    except Exception as e:
        print("Exception when calling SnapshotsApi->commit_restore_point: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vds_id** | [**object**](.md)| ID облачного сервера (VDS). | 

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
**204** | Действие над снапшотом запущено |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_restore_point**
> GetRestorePoint200Response create_restore_point(vds_id)

Создание снапшота

Чтобы создать снапшот облачного сервера (VDS), отправьте POST-запрос на `/api/v1/restore-points/{vds_id}/create`.  Тело ответа будет содержать объект JSON с ключом `restore_point` и информацией о созданном снапшоте. Сразу после создания снапшот может находиться в статусе `creating`.  Для создания снапшота сервер должен быть включён, иначе вернётся ошибка `403`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_restore_point200_response import GetRestorePoint200Response
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
    api_instance = timeweb_cloud_api.SnapshotsApi(api_client)
    vds_id = 1051 # object | ID облачного сервера (VDS).

    try:
        # Создание снапшота
        api_response = api_instance.create_restore_point(vds_id)
        print("The response of SnapshotsApi->create_restore_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->create_restore_point: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vds_id** | [**object**](.md)| ID облачного сервера (VDS). | 

### Return type

[**GetRestorePoint200Response**](GetRestorePoint200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;restore_point&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_restore_point**
> GetRestorePoint200Response get_restore_point(vds_id)

Получение снапшота сервера

Чтобы получить снапшот облачного сервера (VDS), отправьте GET-запрос на `/api/v1/restore-points/{vds_id}`.  Тело ответа будет представлять собой объект JSON с ключом `restore_point`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_restore_point200_response import GetRestorePoint200Response
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
    api_instance = timeweb_cloud_api.SnapshotsApi(api_client)
    vds_id = 1051 # object | ID облачного сервера (VDS).

    try:
        # Получение снапшота сервера
        api_response = api_instance.get_restore_point(vds_id)
        print("The response of SnapshotsApi->get_restore_point:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->get_restore_point: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vds_id** | [**object**](.md)| ID облачного сервера (VDS). | 

### Return type

[**GetRestorePoint200Response**](GetRestorePoint200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;restore_point&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_restore_points**
> GetRestorePoints200Response get_restore_points()

Получение списка снапшотов

Чтобы получить список снапшотов аккаунта, отправьте GET-запрос на `/api/v1/restore-points`.  Тело ответа будет представлять собой объект JSON с ключом `restore_points`.  Снапшот — это снимок состояния облачного сервера (VDS), к которому можно вернуться. Каждому снапшоту соответствует один сервер.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_restore_points200_response import GetRestorePoints200Response
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
    api_instance = timeweb_cloud_api.SnapshotsApi(api_client)

    try:
        # Получение списка снапшотов
        api_response = api_instance.get_restore_points()
        print("The response of SnapshotsApi->get_restore_points:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnapshotsApi->get_restore_points: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetRestorePoints200Response**](GetRestorePoints200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;restore_points&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_restore_point**
> rollback_restore_point(vds_id)

Откат к снапшоту

Чтобы откатить облачный сервер (VDS) к снапшоту, отправьте POST-запрос на `/api/v1/restore-points/{vds_id}/rollback`.  Откат возвращает сервер к состоянию, сохранённому в снапшоте. Действие выполняется асинхронно, ответ не содержит тела.  Для выполнения действия сервер должен быть включён, иначе вернётся ошибка `403`.

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
    api_instance = timeweb_cloud_api.SnapshotsApi(api_client)
    vds_id = 1051 # object | ID облачного сервера (VDS).

    try:
        # Откат к снапшоту
        api_instance.rollback_restore_point(vds_id)
    except Exception as e:
        print("Exception when calling SnapshotsApi->rollback_restore_point: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vds_id** | [**object**](.md)| ID облачного сервера (VDS). | 

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
**204** | Действие над снапшотом запущено |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

