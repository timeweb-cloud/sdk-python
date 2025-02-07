# timeweb_cloud_api.NetworkDrivesApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_drive**](NetworkDrivesApi.md#create_network_drive) | **POST** /api/v1/network-drives | Создание сетевого диска
[**delete_network_drive**](NetworkDrivesApi.md#delete_network_drive) | **DELETE** /api/v1/network-drives/{network_drive_id} | Удаление сетевого диска по идентификатору
[**get_network_drive**](NetworkDrivesApi.md#get_network_drive) | **GET** /api/v1/network-drives/{network_drive_id} | Получение сетевого диска
[**get_network_drives**](NetworkDrivesApi.md#get_network_drives) | **GET** /api/v1/network-drives | Получение списка cетевых дисков
[**get_network_drives_available_resources**](NetworkDrivesApi.md#get_network_drives_available_resources) | **GET** /api/v1/network-drives/available-resources | Получение списка сервисов доступных для подключения диска
[**get_network_drives_presets**](NetworkDrivesApi.md#get_network_drives_presets) | **GET** /api/v1/presets/network-drives | Получение списка доступных тарифов для сетевого диска
[**mount_network_drive**](NetworkDrivesApi.md#mount_network_drive) | **POST** /api/v1/network-drives/{network_drive_id}/mount | Подключить сетевой диск к сервису
[**unmount_network_drive**](NetworkDrivesApi.md#unmount_network_drive) | **POST** /api/v1/network-drives/{network_drive_id}/unmount | Отключить сетевой диск от сервиса
[**update_network_drive**](NetworkDrivesApi.md#update_network_drive) | **PATCH** /api/v1/network-drives/{network_drive_id} | Изменение сетевого диска по ID


# **create_network_drive**
> CreateNetworkDrive201Response create_network_drive(create_network_drive)

Создание сетевого диска

Чтобы создать создать сетевой диск, отправьте POST-запрос в `/api/v1/network-drives`, задав необходимые атрибуты.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_network_drive import CreateNetworkDrive
from timeweb_cloud_api.models.create_network_drive201_response import CreateNetworkDrive201Response
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
    api_instance = timeweb_cloud_api.NetworkDrivesApi(api_client)
    create_network_drive = timeweb_cloud_api.CreateNetworkDrive() # CreateNetworkDrive | 

    try:
        # Создание сетевого диска
        api_response = api_instance.create_network_drive(create_network_drive)
        print("The response of NetworkDrivesApi->create_network_drive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkDrivesApi->create_network_drive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_network_drive** | [**CreateNetworkDrive**](CreateNetworkDrive.md)|  | 

### Return type

[**CreateNetworkDrive201Response**](CreateNetworkDrive201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;network_drive&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_drive**
> delete_network_drive(network_drive_id)

Удаление сетевого диска по идентификатору

Чтобы удалить сетевой диск, отправьте DELETE-запрос на `/api/v1/network-drives/{network_drive_id}`

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
    api_instance = timeweb_cloud_api.NetworkDrivesApi(api_client)
    network_drive_id = 87fa289f-1513-4c4d-8d49-5707f411f14b # object | ID сетевого диска

    try:
        # Удаление сетевого диска по идентификатору
        api_instance.delete_network_drive(network_drive_id)
    except Exception as e:
        print("Exception when calling NetworkDrivesApi->delete_network_drive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_drive_id** | [**object**](.md)| ID сетевого диска | 

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
**204** | Сетевой диск успешно удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_drive**
> CreateNetworkDrive201Response get_network_drive(network_drive_id)

Получение сетевого диска

Чтобы отобразить информацию об отдельном сетевом диске, отправьте запрос GET на `api/v1/network-drives/{network_drive_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_network_drive201_response import CreateNetworkDrive201Response
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
    api_instance = timeweb_cloud_api.NetworkDrivesApi(api_client)
    network_drive_id = 87fa289f-1513-4c4d-8d49-5707f411f14b # object | ID сетевого диска

    try:
        # Получение сетевого диска
        api_response = api_instance.get_network_drive(network_drive_id)
        print("The response of NetworkDrivesApi->get_network_drive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkDrivesApi->get_network_drive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_drive_id** | [**object**](.md)| ID сетевого диска | 

### Return type

[**CreateNetworkDrive201Response**](CreateNetworkDrive201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;network_drive&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_drives**
> GetNetworkDrives200Response get_network_drives()

Получение списка cетевых дисков

Чтобы получить список сетевых дисков, отправьте GET-запрос на `/api/v1/network-drives`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_network_drives200_response import GetNetworkDrives200Response
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
    api_instance = timeweb_cloud_api.NetworkDrivesApi(api_client)

    try:
        # Получение списка cетевых дисков
        api_response = api_instance.get_network_drives()
        print("The response of NetworkDrivesApi->get_network_drives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkDrivesApi->get_network_drives: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNetworkDrives200Response**](GetNetworkDrives200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;network_drives&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_drives_available_resources**
> GetNetworkDrivesAvailableResources200Response get_network_drives_available_resources()

Получение списка сервисов доступных для подключения диска

Чтобы получить список сервисов, отправьте GET-запрос на `/api/v1/network-drives/available-resources`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_network_drives_available_resources200_response import GetNetworkDrivesAvailableResources200Response
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
    api_instance = timeweb_cloud_api.NetworkDrivesApi(api_client)

    try:
        # Получение списка сервисов доступных для подключения диска
        api_response = api_instance.get_network_drives_available_resources()
        print("The response of NetworkDrivesApi->get_network_drives_available_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkDrivesApi->get_network_drives_available_resources: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNetworkDrivesAvailableResources200Response**](GetNetworkDrivesAvailableResources200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;available_resources&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_drives_presets**
> GetNetworkDrivesPresets200Response get_network_drives_presets()

Получение списка доступных тарифов для сетевого диска

Чтобы получить список тарифов, отправьте GET-запрос на `/api/v1/presets/network-drives`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_network_drives_presets200_response import GetNetworkDrivesPresets200Response
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
    api_instance = timeweb_cloud_api.NetworkDrivesApi(api_client)

    try:
        # Получение списка доступных тарифов для сетевого диска
        api_response = api_instance.get_network_drives_presets()
        print("The response of NetworkDrivesApi->get_network_drives_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkDrivesApi->get_network_drives_presets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNetworkDrivesPresets200Response**](GetNetworkDrivesPresets200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;network_drive_presets&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mount_network_drive**
> mount_network_drive(network_drive_id, mount_network_drive)

Подключить сетевой диск к сервису

Чтобы подключить сетевой диск к сервису, отправьте POST-запрос на `/api/v1/network-drives/{network_drive_id}/mount`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.mount_network_drive import MountNetworkDrive
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
    api_instance = timeweb_cloud_api.NetworkDrivesApi(api_client)
    network_drive_id = 87fa289f-1513-4c4d-8d49-5707f411f14b # object | ID сетевого диска
    mount_network_drive = timeweb_cloud_api.MountNetworkDrive() # MountNetworkDrive | 

    try:
        # Подключить сетевой диск к сервису
        api_instance.mount_network_drive(network_drive_id, mount_network_drive)
    except Exception as e:
        print("Exception when calling NetworkDrivesApi->mount_network_drive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_drive_id** | [**object**](.md)| ID сетевого диска | 
 **mount_network_drive** | [**MountNetworkDrive**](MountNetworkDrive.md)|  | 

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
**204** | Сетевой диск успешно подключен |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unmount_network_drive**
> unmount_network_drive(network_drive_id)

Отключить сетевой диск от сервиса

Чтобы отключить сетевой диск от сервиса, отправьте POST-запрос на `/api/v1/network-drives/{network_drive_id}/unmount`.

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
    api_instance = timeweb_cloud_api.NetworkDrivesApi(api_client)
    network_drive_id = 87fa289f-1513-4c4d-8d49-5707f411f14b # object | ID сетевого диска

    try:
        # Отключить сетевой диск от сервиса
        api_instance.unmount_network_drive(network_drive_id)
    except Exception as e:
        print("Exception when calling NetworkDrivesApi->unmount_network_drive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_drive_id** | [**object**](.md)| ID сетевого диска | 

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
**204** | Сетевой диск успешно отключен |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_drive**
> CreateNetworkDrive201Response update_network_drive(network_drive_id, update_network_drive)

Изменение сетевого диска по ID

Чтобы изменить сетевой диск, отправьте PATCH-запрос на `/api/v1/network-drives/{network_drive_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_network_drive201_response import CreateNetworkDrive201Response
from timeweb_cloud_api.models.update_network_drive import UpdateNetworkDrive
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
    api_instance = timeweb_cloud_api.NetworkDrivesApi(api_client)
    network_drive_id = 87fa289f-1513-4c4d-8d49-5707f411f14b # object | ID сетевого диска
    update_network_drive = timeweb_cloud_api.UpdateNetworkDrive() # UpdateNetworkDrive | 

    try:
        # Изменение сетевого диска по ID
        api_response = api_instance.update_network_drive(network_drive_id, update_network_drive)
        print("The response of NetworkDrivesApi->update_network_drive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkDrivesApi->update_network_drive: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_drive_id** | [**object**](.md)| ID сетевого диска | 
 **update_network_drive** | [**UpdateNetworkDrive**](UpdateNetworkDrive.md)|  | 

### Return type

[**CreateNetworkDrive201Response**](CreateNetworkDrive201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;network_drive&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

