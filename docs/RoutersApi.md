# timeweb_cloud_api.RoutersApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_networks**](RoutersApi.md#add_networks) | **POST** /api/v1/routers/{router_id}/networks | Подключение сетей к роутеру
[**create_router**](RoutersApi.md#create_router) | **POST** /api/v1/routers | Создание роутера
[**delete_dnat**](RoutersApi.md#delete_dnat) | **DELETE** /api/v1/routers/{router_id}/dnat-rules/{dnat_id} | Удаление правила проброса портов
[**delete_router**](RoutersApi.md#delete_router) | **DELETE** /api/v1/routers/{router_id} | Удаление роутера
[**delete_router_nat**](RoutersApi.md#delete_router_nat) | **DELETE** /api/v1/routers/{router_id}/networks/{network_name}/nat | Выключение NAT для сети
[**delete_router_network**](RoutersApi.md#delete_router_network) | **DELETE** /api/v1/routers/{router_id}/networks/{network_name} | Удаление сети из роутера
[**delete_static_route**](RoutersApi.md#delete_static_route) | **DELETE** /api/v1/routers/{router_id}/static-routes/{static_route_id} | Удаление статического маршрута
[**get_available_static_routes**](RoutersApi.md#get_available_static_routes) | **GET** /api/v1/routers/{router_id}/static-routes/available | Получение доступных подсетей для статических маршрутов
[**get_dnat**](RoutersApi.md#get_dnat) | **GET** /api/v1/routers/{router_id}/dnat-rules | Получение списка правил проброса портов
[**get_dnat_rule**](RoutersApi.md#get_dnat_rule) | **GET** /api/v1/routers/{router_id}/dnat-rules/{dnat_id} | Получение правила проброса портов
[**get_networks**](RoutersApi.md#get_networks) | **GET** /api/v1/routers/{router_id}/networks | Получение списка сетей роутера
[**get_router**](RoutersApi.md#get_router) | **GET** /api/v1/routers/{router_id} | Получение информации о роутере
[**get_router_available_networks**](RoutersApi.md#get_router_available_networks) | **GET** /api/v1/routers/networks/available | Получение списка доступных сетей
[**get_router_presets**](RoutersApi.md#get_router_presets) | **GET** /api/v1/presets/routers | Получение списка тарифов роутеров
[**get_router_statistics**](RoutersApi.md#get_router_statistics) | **GET** /api/v1/routers/{router_id}/statistics/{time_from}/{period}/{keys} | Получение статистики роутера
[**get_routers**](RoutersApi.md#get_routers) | **GET** /api/v1/routers | Получение списка роутеров
[**get_static_routes**](RoutersApi.md#get_static_routes) | **GET** /api/v1/routers/{router_id}/static-routes | Получение списка статических маршрутов
[**patch_network**](RoutersApi.md#patch_network) | **PATCH** /api/v1/routers/{router_id}/networks/{network_name} | Обновление информации о сети
[**patch_networks**](RoutersApi.md#patch_networks) | **PATCH** /api/v1/routers/{router_id}/networks | Обновление сетей роутера
[**post_dnat**](RoutersApi.md#post_dnat) | **POST** /api/v1/routers/{router_id}/dnat-rules | Добавление правила проброса портов
[**post_static_route**](RoutersApi.md#post_static_route) | **POST** /api/v1/routers/{router_id}/static-routes | Добавление статического маршрута
[**update_router**](RoutersApi.md#update_router) | **PATCH** /api/v1/routers/{router_id} | Обновление информации о роутере
[**update_router_nat**](RoutersApi.md#update_router_nat) | **PATCH** /api/v1/routers/{router_id}/networks/{network_name}/nat | Включение NAT для сети


# **add_networks**
> NetworksResponse add_networks(router_id, network_in)

Подключение сетей к роутеру

Чтобы подключить сети к роутеру, отправьте POST-запрос на `/api/v1/routers/{router_id}/networks`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.network_in import NetworkIn
from timeweb_cloud_api.models.networks_response import NetworksResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    network_in = timeweb_cloud_api.NetworkIn() # NetworkIn | 

    try:
        # Подключение сетей к роутеру
        api_response = api_instance.add_networks(router_id, network_in)
        print("The response of RoutersApi->add_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->add_networks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **network_in** | [**NetworkIn**](NetworkIn.md)|  | 

### Return type

[**NetworksResponse**](NetworksResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Список сетей роутера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_router**
> RouterResponse create_router(router_in)

Создание роутера

Чтобы создать роутер, отправьте POST-запрос на `/api/v1/routers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.router_in import RouterIn
from timeweb_cloud_api.models.router_response import RouterResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_in = timeweb_cloud_api.RouterIn() # RouterIn | 

    try:
        # Создание роутера
        api_response = api_instance.create_router(router_in)
        print("The response of RoutersApi->create_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->create_router: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_in** | [**RouterIn**](RouterIn.md)|  | 

### Return type

[**RouterResponse**](RouterResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Информация о роутере |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dnat**
> delete_dnat(router_id, dnat_id)

Удаление правила проброса портов

Чтобы удалить правило проброса портов (DNAT), отправьте DELETE-запрос на `/api/v1/routers/{router_id}/dnat-rules/{dnat_id}`.

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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    dnat_id = None # object | ID правила

    try:
        # Удаление правила проброса портов
        api_instance.delete_dnat(router_id, dnat_id)
    except Exception as e:
        print("Exception when calling RoutersApi->delete_dnat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **dnat_id** | [**object**](.md)| ID правила | 

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
**200** | Правило удалено |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_router**
> delete_router(router_id)

Удаление роутера

Чтобы удалить роутер, отправьте DELETE-запрос на `/api/v1/routers/{router_id}`.

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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера

    try:
        # Удаление роутера
        api_instance.delete_router(router_id)
    except Exception as e:
        print("Exception when calling RoutersApi->delete_router: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 

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
**200** | Роутер удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_router_nat**
> RouterResponse delete_router_nat(router_id, network_name)

Выключение NAT для сети

Чтобы выключить NAT для сети роутера, отправьте DELETE-запрос на `/api/v1/routers/{router_id}/networks/{network_name}/nat`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.router_response import RouterResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    network_name = None # object | Имя сети

    try:
        # Выключение NAT для сети
        api_response = api_instance.delete_router_nat(router_id, network_name)
        print("The response of RoutersApi->delete_router_nat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->delete_router_nat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **network_name** | [**object**](.md)| Имя сети | 

### Return type

[**RouterResponse**](RouterResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о роутере |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_router_network**
> delete_router_network(router_id, network_name)

Удаление сети из роутера

Чтобы отключить сеть от роутера, отправьте DELETE-запрос на `/api/v1/routers/{router_id}/networks/{network_name}`.

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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    network_name = None # object | Имя сети

    try:
        # Удаление сети из роутера
        api_instance.delete_router_network(router_id, network_name)
    except Exception as e:
        print("Exception when calling RoutersApi->delete_router_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **network_name** | [**object**](.md)| Имя сети | 

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
**200** | Сеть отключена от роутера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_static_route**
> delete_static_route(router_id, static_route_id)

Удаление статического маршрута

Чтобы удалить статический маршрут, отправьте DELETE-запрос на `/api/v1/routers/{router_id}/static-routes/{static_route_id}`.

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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    static_route_id = None # object | ID статического маршрута

    try:
        # Удаление статического маршрута
        api_instance.delete_static_route(router_id, static_route_id)
    except Exception as e:
        print("Exception when calling RoutersApi->delete_static_route: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **static_route_id** | [**object**](.md)| ID статического маршрута | 

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
**200** | Статический маршрут удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_static_routes**
> AvailableStaticRoutesResponse get_available_static_routes(router_id)

Получение доступных подсетей для статических маршрутов

Чтобы получить список подсетей, доступных для добавления статических маршрутов, отправьте GET-запрос на `/api/v1/routers/{router_id}/static-routes/available`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.available_static_routes_response import AvailableStaticRoutesResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера

    try:
        # Получение доступных подсетей для статических маршрутов
        api_response = api_instance.get_available_static_routes(router_id)
        print("The response of RoutersApi->get_available_static_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->get_available_static_routes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 

### Return type

[**AvailableStaticRoutesResponse**](AvailableStaticRoutesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Доступные подсети |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dnat**
> DnatRulesResponse get_dnat(router_id)

Получение списка правил проброса портов

Чтобы получить список правил проброса портов (DNAT), отправьте GET-запрос на `/api/v1/routers/{router_id}/dnat-rules`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.dnat_rules_response import DnatRulesResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера

    try:
        # Получение списка правил проброса портов
        api_response = api_instance.get_dnat(router_id)
        print("The response of RoutersApi->get_dnat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->get_dnat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 

### Return type

[**DnatRulesResponse**](DnatRulesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список правил проброса портов |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dnat_rule**
> DnatRuleResponse get_dnat_rule(router_id, dnat_id)

Получение правила проброса портов

Чтобы получить информацию о правиле проброса портов (DNAT), отправьте GET-запрос на `/api/v1/routers/{router_id}/dnat-rules/{dnat_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.dnat_rule_response import DnatRuleResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    dnat_id = None # object | ID правила

    try:
        # Получение правила проброса портов
        api_response = api_instance.get_dnat_rule(router_id, dnat_id)
        print("The response of RoutersApi->get_dnat_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->get_dnat_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **dnat_id** | [**object**](.md)| ID правила | 

### Return type

[**DnatRuleResponse**](DnatRuleResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Правило проброса портов |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_networks**
> NetworksResponse get_networks(router_id)

Получение списка сетей роутера

Чтобы получить список сетей роутера, отправьте GET-запрос на `/api/v1/routers/{router_id}/networks`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.networks_response import NetworksResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера

    try:
        # Получение списка сетей роутера
        api_response = api_instance.get_networks(router_id)
        print("The response of RoutersApi->get_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->get_networks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 

### Return type

[**NetworksResponse**](NetworksResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список сетей роутера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_router**
> RouterResponse get_router(router_id)

Получение информации о роутере

Чтобы получить информацию о роутере, отправьте GET-запрос на `/api/v1/routers/{router_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.router_response import RouterResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера

    try:
        # Получение информации о роутере
        api_response = api_instance.get_router(router_id)
        print("The response of RoutersApi->get_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->get_router: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 

### Return type

[**RouterResponse**](RouterResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о роутере |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_router_available_networks**
> AvailableNetworksResponse get_router_available_networks()

Получение списка доступных сетей

Чтобы получить список локальных сетей, доступных для подключения к роутеру, отправьте GET-запрос на `/api/v1/routers/networks/available`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.available_networks_response import AvailableNetworksResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)

    try:
        # Получение списка доступных сетей
        api_response = api_instance.get_router_available_networks()
        print("The response of RoutersApi->get_router_available_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->get_router_available_networks: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AvailableNetworksResponse**](AvailableNetworksResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список доступных сетей |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_router_presets**
> RouterPresetsResponse get_router_presets()

Получение списка тарифов роутеров

Чтобы получить список доступных тарифов роутеров, отправьте GET-запрос на `/api/v1/presets/routers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.router_presets_response import RouterPresetsResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)

    try:
        # Получение списка тарифов роутеров
        api_response = api_instance.get_router_presets()
        print("The response of RoutersApi->get_router_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->get_router_presets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RouterPresetsResponse**](RouterPresetsResponse.md)

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

# **get_router_statistics**
> RouterStatisticsResponse get_router_statistics(router_id, time_from, period, keys, node_id=node_id)

Получение статистики роутера

Чтобы получить статистику роутера, отправьте GET-запрос на `/api/v1/routers/{router_id}/statistics/{time_from}/{period}/{keys}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.router_statistics_response import RouterStatisticsResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    time_from = None # object | Начало периода
    period = None # object | Период агрегации
    keys = None # object | Ключи метрик
    node_id = None # object | ID ноды (optional)

    try:
        # Получение статистики роутера
        api_response = api_instance.get_router_statistics(router_id, time_from, period, keys, node_id=node_id)
        print("The response of RoutersApi->get_router_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->get_router_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **time_from** | [**object**](.md)| Начало периода | 
 **period** | [**object**](.md)| Период агрегации | 
 **keys** | [**object**](.md)| Ключи метрик | 
 **node_id** | [**object**](.md)| ID ноды | [optional] 

### Return type

[**RouterStatisticsResponse**](RouterStatisticsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Статистика роутера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_routers**
> RoutersResponse get_routers()

Получение списка роутеров

Чтобы получить список роутеров, отправьте GET-запрос на `/api/v1/routers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.routers_response import RoutersResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)

    try:
        # Получение списка роутеров
        api_response = api_instance.get_routers()
        print("The response of RoutersApi->get_routers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->get_routers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RoutersResponse**](RoutersResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список роутеров |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_static_routes**
> StaticRoutesResponse get_static_routes(router_id)

Получение списка статических маршрутов

Чтобы получить список статических маршрутов роутера, отправьте GET-запрос на `/api/v1/routers/{router_id}/static-routes`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.static_routes_response import StaticRoutesResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера

    try:
        # Получение списка статических маршрутов
        api_response = api_instance.get_static_routes(router_id)
        print("The response of RoutersApi->get_static_routes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->get_static_routes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 

### Return type

[**StaticRoutesResponse**](StaticRoutesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список статических маршрутов |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_network**
> NetworkResponse patch_network(router_id, network_name, network_edit)

Обновление информации о сети

Чтобы включить или выключить DHCP в сети роутера, отправьте PATCH-запрос на `/api/v1/routers/{router_id}/networks/{network_name}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.network_edit import NetworkEdit
from timeweb_cloud_api.models.network_response import NetworkResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    network_name = None # object | Имя сети
    network_edit = timeweb_cloud_api.NetworkEdit() # NetworkEdit | 

    try:
        # Обновление информации о сети
        api_response = api_instance.patch_network(router_id, network_name, network_edit)
        print("The response of RoutersApi->patch_network:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->patch_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **network_name** | [**object**](.md)| Имя сети | 
 **network_edit** | [**NetworkEdit**](NetworkEdit.md)|  | 

### Return type

[**NetworkResponse**](NetworkResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о сети |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_networks**
> NetworksResponse patch_networks(router_id, network_in)

Обновление сетей роутера

Чтобы обновить набор сетей роутера, отправьте PATCH-запрос на `/api/v1/routers/{router_id}/networks`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.network_in import NetworkIn
from timeweb_cloud_api.models.networks_response import NetworksResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    network_in = timeweb_cloud_api.NetworkIn() # NetworkIn | 

    try:
        # Обновление сетей роутера
        api_response = api_instance.patch_networks(router_id, network_in)
        print("The response of RoutersApi->patch_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->patch_networks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **network_in** | [**NetworkIn**](NetworkIn.md)|  | 

### Return type

[**NetworksResponse**](NetworksResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список сетей роутера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dnat**
> DnatRuleResponse post_dnat(router_id, dnat_in)

Добавление правила проброса портов

Чтобы добавить правило проброса портов (DNAT), отправьте POST-запрос на `/api/v1/routers/{router_id}/dnat-rules`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.dnat_in import DnatIn
from timeweb_cloud_api.models.dnat_rule_response import DnatRuleResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    dnat_in = timeweb_cloud_api.DnatIn() # DnatIn | 

    try:
        # Добавление правила проброса портов
        api_response = api_instance.post_dnat(router_id, dnat_in)
        print("The response of RoutersApi->post_dnat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->post_dnat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **dnat_in** | [**DnatIn**](DnatIn.md)|  | 

### Return type

[**DnatRuleResponse**](DnatRuleResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Правило проброса портов |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_static_route**
> StaticRouteResponse post_static_route(router_id, static_route_in)

Добавление статического маршрута

Чтобы добавить статический маршрут, отправьте POST-запрос на `/api/v1/routers/{router_id}/static-routes`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.static_route_in import StaticRouteIn
from timeweb_cloud_api.models.static_route_response import StaticRouteResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    static_route_in = timeweb_cloud_api.StaticRouteIn() # StaticRouteIn | 

    try:
        # Добавление статического маршрута
        api_response = api_instance.post_static_route(router_id, static_route_in)
        print("The response of RoutersApi->post_static_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->post_static_route: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **static_route_in** | [**StaticRouteIn**](StaticRouteIn.md)|  | 

### Return type

[**StaticRouteResponse**](StaticRouteResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Статический маршрут |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_router**
> RouterResponse update_router(router_id, router_edit)

Обновление информации о роутере

Чтобы обновить информацию о роутере, отправьте PATCH-запрос на `/api/v1/routers/{router_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.router_edit import RouterEdit
from timeweb_cloud_api.models.router_response import RouterResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    router_edit = timeweb_cloud_api.RouterEdit() # RouterEdit | 

    try:
        # Обновление информации о роутере
        api_response = api_instance.update_router(router_id, router_edit)
        print("The response of RoutersApi->update_router:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->update_router: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **router_edit** | [**RouterEdit**](RouterEdit.md)|  | 

### Return type

[**RouterResponse**](RouterResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о роутере |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_router_nat**
> RouterResponse update_router_nat(router_id, network_name, nat_in)

Включение NAT для сети

Чтобы включить NAT для сети роутера, отправьте PATCH-запрос на `/api/v1/routers/{router_id}/networks/{network_name}/nat`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.nat_in import NatIn
from timeweb_cloud_api.models.router_response import RouterResponse
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
    api_instance = timeweb_cloud_api.RoutersApi(api_client)
    router_id = None # object | ID роутера
    network_name = None # object | Имя сети
    nat_in = timeweb_cloud_api.NatIn() # NatIn | 

    try:
        # Включение NAT для сети
        api_response = api_instance.update_router_nat(router_id, network_name, nat_in)
        print("The response of RoutersApi->update_router_nat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutersApi->update_router_nat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **router_id** | [**object**](.md)| ID роутера | 
 **network_name** | [**object**](.md)| Имя сети | 
 **nat_in** | [**NatIn**](NatIn.md)|  | 

### Return type

[**RouterResponse**](RouterResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о роутере |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

