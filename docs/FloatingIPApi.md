# timeweb_cloud_api.FloatingIPApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bind_floating_ip**](FloatingIPApi.md#bind_floating_ip) | **POST** /api/v1/floating-ips/{floating_ip_id}/bind | Привязать IP к сервису
[**create_floating_ip**](FloatingIPApi.md#create_floating_ip) | **POST** /api/v1/floating-ips | Создание плавающего IP
[**delete_floating_ip**](FloatingIPApi.md#delete_floating_ip) | **DELETE** /api/v1/floating-ips/{floating_ip_id} | Удаление плавающего IP по идентификатору
[**get_floating_ip**](FloatingIPApi.md#get_floating_ip) | **GET** /api/v1/floating-ips/{floating_ip_id} | Получение плавающего IP
[**get_floating_ips**](FloatingIPApi.md#get_floating_ips) | **GET** /api/v1/floating-ips | Получение списка плавающих IP
[**unbind_floating_ip**](FloatingIPApi.md#unbind_floating_ip) | **POST** /api/v1/floating-ips/{floating_ip_id}/unbind | Отвязать IP от сервиса
[**update_floating_ip**](FloatingIPApi.md#update_floating_ip) | **PATCH** /api/v1/floating-ips/{floating_ip_id} | Изменение плавающего IP по идентификатору


# **bind_floating_ip**
> bind_floating_ip(floating_ip_id, bind_floating_ip)

Привязать IP к сервису

Чтобы привязать IP к сервису, отправьте POST-запрос на `/api/v1/floating-ip/{floating_ip_id}/bind`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.bind_floating_ip import BindFloatingIp
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
    api_instance = timeweb_cloud_api.FloatingIPApi(api_client)
    floating_ip_id = 87fa289f-1513-4c4d-8d49-5707f411f14b # object | Идентификатор плавающего IP
    bind_floating_ip = timeweb_cloud_api.BindFloatingIp() # BindFloatingIp | 

    try:
        # Привязать IP к сервису
        api_instance.bind_floating_ip(floating_ip_id, bind_floating_ip)
    except Exception as e:
        print("Exception when calling FloatingIPApi->bind_floating_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip_id** | [**object**](.md)| Идентификатор плавающего IP | 
 **bind_floating_ip** | [**BindFloatingIp**](BindFloatingIp.md)|  | 

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
**204** | Плавающий IP успешно привязан |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_floating_ip**
> CreateFloatingIp201Response create_floating_ip(create_floating_ip)

Создание плавающего IP

Чтобы создать создать плавающий IP, отправьте POST-запрос в `/api/v1/floating-ip`, задав необходимые атрибуты.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_floating_ip import CreateFloatingIp
from timeweb_cloud_api.models.create_floating_ip201_response import CreateFloatingIp201Response
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
    api_instance = timeweb_cloud_api.FloatingIPApi(api_client)
    create_floating_ip = timeweb_cloud_api.CreateFloatingIp() # CreateFloatingIp | 

    try:
        # Создание плавающего IP
        api_response = api_instance.create_floating_ip(create_floating_ip)
        print("The response of FloatingIPApi->create_floating_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIPApi->create_floating_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_floating_ip** | [**CreateFloatingIp**](CreateFloatingIp.md)|  | 

### Return type

[**CreateFloatingIp201Response**](CreateFloatingIp201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;ip&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_floating_ip**
> delete_floating_ip(floating_ip_id)

Удаление плавающего IP по идентификатору

Чтобы удалить плавающий IP, отправьте DELETE-запрос на `/api/v1/floating-ips/{floating_ip_id}`

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
    api_instance = timeweb_cloud_api.FloatingIPApi(api_client)
    floating_ip_id = 87fa289f-1513-4c4d-8d49-5707f411f14b # object | Идентификатор плавающего IP

    try:
        # Удаление плавающего IP по идентификатору
        api_instance.delete_floating_ip(floating_ip_id)
    except Exception as e:
        print("Exception when calling FloatingIPApi->delete_floating_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip_id** | [**object**](.md)| Идентификатор плавающего IP | 

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
**201** | Плавающий IP успешно удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_floating_ip**
> CreateFloatingIp201Response get_floating_ip(floating_ip_id)

Получение плавающего IP

Чтобы отобразить информацию об отдельном плавающем IP, отправьте запрос GET на `api/v1/floating-ips/{floating_ip_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_floating_ip201_response import CreateFloatingIp201Response
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
    api_instance = timeweb_cloud_api.FloatingIPApi(api_client)
    floating_ip_id = 87fa289f-1513-4c4d-8d49-5707f411f14b # object | Идентификатор плавающего IP

    try:
        # Получение плавающего IP
        api_response = api_instance.get_floating_ip(floating_ip_id)
        print("The response of FloatingIPApi->get_floating_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIPApi->get_floating_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip_id** | [**object**](.md)| Идентификатор плавающего IP | 

### Return type

[**CreateFloatingIp201Response**](CreateFloatingIp201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;ip&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_floating_ips**
> GetFloatingIps200Response get_floating_ips()

Получение списка плавающих IP

Чтобы получить список плавающих IP, отправьте GET-запрос на `/api/v1/floating-ips`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_floating_ips200_response import GetFloatingIps200Response
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
    api_instance = timeweb_cloud_api.FloatingIPApi(api_client)

    try:
        # Получение списка плавающих IP
        api_response = api_instance.get_floating_ips()
        print("The response of FloatingIPApi->get_floating_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIPApi->get_floating_ips: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetFloatingIps200Response**](GetFloatingIps200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ips&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unbind_floating_ip**
> unbind_floating_ip(floating_ip_id)

Отвязать IP от сервиса

Чтобы отвязать IP от сервиса, отправьте POST-запрос на `/api/v1/floating-ip/{floating_ip_id}/unbind`.

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
    api_instance = timeweb_cloud_api.FloatingIPApi(api_client)
    floating_ip_id = 87fa289f-1513-4c4d-8d49-5707f411f14b # object | Идентификатор плавающего IP

    try:
        # Отвязать IP от сервиса
        api_instance.unbind_floating_ip(floating_ip_id)
    except Exception as e:
        print("Exception when calling FloatingIPApi->unbind_floating_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip_id** | [**object**](.md)| Идентификатор плавающего IP | 

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
**204** | Плавающий IP успешно отвязан |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_floating_ip**
> CreateFloatingIp201Response update_floating_ip(floating_ip_id, update_floating_ip)

Изменение плавающего IP по идентификатору

Чтобы изменить плавающий IP, отправьте PATCH-запрос на `/api/v1/floating-ips/{floating_ip_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_floating_ip201_response import CreateFloatingIp201Response
from timeweb_cloud_api.models.update_floating_ip import UpdateFloatingIp
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
    api_instance = timeweb_cloud_api.FloatingIPApi(api_client)
    floating_ip_id = 87fa289f-1513-4c4d-8d49-5707f411f14b # object | Идентификатор плавающего IP
    update_floating_ip = timeweb_cloud_api.UpdateFloatingIp() # UpdateFloatingIp | 

    try:
        # Изменение плавающего IP по идентификатору
        api_response = api_instance.update_floating_ip(floating_ip_id, update_floating_ip)
        print("The response of FloatingIPApi->update_floating_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FloatingIPApi->update_floating_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **floating_ip_id** | [**object**](.md)| Идентификатор плавающего IP | 
 **update_floating_ip** | [**UpdateFloatingIp**](UpdateFloatingIp.md)|  | 

### Return type

[**CreateFloatingIp201Response**](CreateFloatingIp201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ip&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

