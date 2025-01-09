# timeweb_cloud_api.VPCApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vpc**](VPCApi.md#create_vpc) | **POST** /api/v2/vpcs | Создание VPC
[**delete_vpc**](VPCApi.md#delete_vpc) | **DELETE** /api/v1/vpcs/{vpc_id} | Удаление VPC по ID сети
[**get_vpc**](VPCApi.md#get_vpc) | **GET** /api/v2/vpcs/{vpc_id} | Получение VPC
[**get_vpc_ports**](VPCApi.md#get_vpc_ports) | **GET** /api/v1/vpcs/{vpc_id}/ports | Получение списка портов для VPC
[**get_vpc_services**](VPCApi.md#get_vpc_services) | **GET** /api/v2/vpcs/{vpc_id}/services | Получение списка сервисов в VPC
[**get_vpcs**](VPCApi.md#get_vpcs) | **GET** /api/v2/vpcs | Получение списка VPCs
[**update_vpcs**](VPCApi.md#update_vpcs) | **PATCH** /api/v2/vpcs/{vpc_id} | Изменение VPC по ID сети


# **create_vpc**
> CreateVPC201Response create_vpc(create_vpc)

Создание VPC

Чтобы создать создать VPC, отправьте POST-запрос в `/api/v2/vpcs`, задав необходимые атрибуты.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_vpc201_response import CreateVPC201Response
from timeweb_cloud_api.models.create_vpc import CreateVpc
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
    api_instance = timeweb_cloud_api.VPCApi(api_client)
    create_vpc = timeweb_cloud_api.CreateVpc() # CreateVpc | 

    try:
        # Создание VPC
        api_response = api_instance.create_vpc(create_vpc)
        print("The response of VPCApi->create_vpc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCApi->create_vpc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_vpc** | [**CreateVpc**](CreateVpc.md)|  | 

### Return type

[**CreateVPC201Response**](CreateVPC201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;vpc&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vpc**
> delete_vpc(vpc_id)

Удаление VPC по ID сети

Чтобы удалить VPC, отправьте DELETE-запрос на `/api/v1/vpcs/{vpc_id}`

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
    api_instance = timeweb_cloud_api.VPCApi(api_client)
    vpc_id = network-1234567890 # object | ID сети

    try:
        # Удаление VPC по ID сети
        api_instance.delete_vpc(vpc_id)
    except Exception as e:
        print("Exception when calling VPCApi->delete_vpc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc_id** | [**object**](.md)| ID сети | 

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
**204** | Успешное выполнение действия |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpc**
> CreateVPC201Response get_vpc(vpc_id)

Получение VPC

Чтобы отобразить информацию об отдельном VPC, отправьте запрос GET на `api/v2/vpcs/{vpc_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_vpc201_response import CreateVPC201Response
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
    api_instance = timeweb_cloud_api.VPCApi(api_client)
    vpc_id = network-1234567890 # object | ID сети

    try:
        # Получение VPC
        api_response = api_instance.get_vpc(vpc_id)
        print("The response of VPCApi->get_vpc:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCApi->get_vpc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc_id** | [**object**](.md)| ID сети | 

### Return type

[**CreateVPC201Response**](CreateVPC201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;vpc&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpc_ports**
> GetVPCPorts200Response get_vpc_ports(vpc_id)

Получение списка портов для VPC

Чтобы получить список портов для VPC, отправьте GET-запрос на `/api/v1/vpcs/{vpc_id}/ports`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_vpc_ports200_response import GetVPCPorts200Response
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
    api_instance = timeweb_cloud_api.VPCApi(api_client)
    vpc_id = network-1234567890 # object | ID сети

    try:
        # Получение списка портов для VPC
        api_response = api_instance.get_vpc_ports(vpc_id)
        print("The response of VPCApi->get_vpc_ports:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCApi->get_vpc_ports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc_id** | [**object**](.md)| ID сети | 

### Return type

[**GetVPCPorts200Response**](GetVPCPorts200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;vpc_ports&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpc_services**
> GetVPCServices200Response get_vpc_services(vpc_id)

Получение списка сервисов в VPC

Чтобы получить список сервисов, отправьте GET-запрос на `/api/v2/vpcs/{vpc_id}/services`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_vpc_services200_response import GetVPCServices200Response
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
    api_instance = timeweb_cloud_api.VPCApi(api_client)
    vpc_id = network-1234567890 # object | ID сети

    try:
        # Получение списка сервисов в VPC
        api_response = api_instance.get_vpc_services(vpc_id)
        print("The response of VPCApi->get_vpc_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCApi->get_vpc_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc_id** | [**object**](.md)| ID сети | 

### Return type

[**GetVPCServices200Response**](GetVPCServices200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;services&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vpcs**
> GetVPCs200Response get_vpcs()

Получение списка VPCs

Чтобы получить список VPCs, отправьте GET-запрос на `/api/v2/vpcs`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_vpcs200_response import GetVPCs200Response
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
    api_instance = timeweb_cloud_api.VPCApi(api_client)

    try:
        # Получение списка VPCs
        api_response = api_instance.get_vpcs()
        print("The response of VPCApi->get_vpcs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCApi->get_vpcs: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetVPCs200Response**](GetVPCs200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;vpcs&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_vpcs**
> CreateVPC201Response update_vpcs(vpc_id, update_vpc)

Изменение VPC по ID сети

Чтобы изменить VPC, отправьте PATCH-запрос на `/api/v2/vpcs/{vpc_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_vpc201_response import CreateVPC201Response
from timeweb_cloud_api.models.update_vpc import UpdateVpc
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
    api_instance = timeweb_cloud_api.VPCApi(api_client)
    vpc_id = network-1234567890 # object | ID сети
    update_vpc = timeweb_cloud_api.UpdateVpc() # UpdateVpc | 

    try:
        # Изменение VPC по ID сети
        api_response = api_instance.update_vpcs(vpc_id, update_vpc)
        print("The response of VPCApi->update_vpcs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPCApi->update_vpcs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpc_id** | [**object**](.md)| ID сети | 
 **update_vpc** | [**UpdateVpc**](UpdateVpc.md)|  | 

### Return type

[**CreateVPC201Response**](CreateVPC201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;vpc&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

