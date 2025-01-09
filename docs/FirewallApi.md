# timeweb_cloud_api.FirewallApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_resource_to_group**](FirewallApi.md#add_resource_to_group) | **POST** /api/v1/firewall/groups/{group_id}/resources/{resource_id} | Линковка ресурса в firewall group
[**create_group**](FirewallApi.md#create_group) | **POST** /api/v1/firewall/groups | Создание группы правил
[**create_group_rule**](FirewallApi.md#create_group_rule) | **POST** /api/v1/firewall/groups/{group_id}/rules | Создание firewall правила
[**delete_group**](FirewallApi.md#delete_group) | **DELETE** /api/v1/firewall/groups/{group_id} | Удаление группы правил
[**delete_group_rule**](FirewallApi.md#delete_group_rule) | **DELETE** /api/v1/firewall/groups/{group_id}/rules/{rule_id} | Удаление firewall правила
[**delete_resource_from_group**](FirewallApi.md#delete_resource_from_group) | **DELETE** /api/v1/firewall/groups/{group_id}/resources/{resource_id} | Отлинковка ресурса из firewall group
[**get_group**](FirewallApi.md#get_group) | **GET** /api/v1/firewall/groups/{group_id} | Получение информации о группе правил
[**get_group_resources**](FirewallApi.md#get_group_resources) | **GET** /api/v1/firewall/groups/{group_id}/resources | Получение слинкованных ресурсов
[**get_group_rule**](FirewallApi.md#get_group_rule) | **GET** /api/v1/firewall/groups/{group_id}/rules/{rule_id} | Получение информации о правиле
[**get_group_rules**](FirewallApi.md#get_group_rules) | **GET** /api/v1/firewall/groups/{group_id}/rules | Получение списка правил
[**get_groups**](FirewallApi.md#get_groups) | **GET** /api/v1/firewall/groups | Получение групп правил
[**get_rules_for_resource**](FirewallApi.md#get_rules_for_resource) | **GET** /api/v1/firewall/service/{resource_type}/{resource_id} | Получение групп правил для ресурса
[**update_group**](FirewallApi.md#update_group) | **PATCH** /api/v1/firewall/groups/{group_id} | Обновление группы правил
[**update_group_rule**](FirewallApi.md#update_group_rule) | **PATCH** /api/v1/firewall/groups/{group_id}/rules/{rule_id} | Обновление firewall правила


# **add_resource_to_group**
> FirewallGroupResourceOutResponse add_resource_to_group(group_id, resource_id, resource_type=resource_type)

Линковка ресурса в firewall group

Чтобы слинковать ресурс с группой правил, отправьте POST запрос на `/api/v1/firewall/groups/{group_id}/resources/{resource_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.firewall_group_resource_out_response import FirewallGroupResourceOutResponse
from timeweb_cloud_api.models.resource_type import ResourceType
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    group_id = None # object | ID группы правил
    resource_id = None # object | ID ресурса
    resource_type = timeweb_cloud_api.ResourceType() # ResourceType |  (optional)

    try:
        # Линковка ресурса в firewall group
        api_response = api_instance.add_resource_to_group(group_id, resource_id, resource_type=resource_type)
        print("The response of FirewallApi->add_resource_to_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->add_resource_to_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| ID группы правил | 
 **resource_id** | [**object**](.md)| ID ресурса | 
 **resource_type** | [**ResourceType**](.md)|  | [optional] 

### Return type

[**FirewallGroupResourceOutResponse**](FirewallGroupResourceOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ресурс добавлен к группе |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group**
> FirewallGroupOutResponse create_group(firewall_group_in_api, policy=policy)

Создание группы правил

Чтобы создать группу правил, отправьте POST запрос на `/api/v1/firewall/groups`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.firewall_group_in_api import FirewallGroupInAPI
from timeweb_cloud_api.models.firewall_group_out_response import FirewallGroupOutResponse
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    firewall_group_in_api = timeweb_cloud_api.FirewallGroupInAPI() # FirewallGroupInAPI | 
    policy = None # object | Тип группы правил (optional)

    try:
        # Создание группы правил
        api_response = api_instance.create_group(firewall_group_in_api, policy=policy)
        print("The response of FirewallApi->create_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->create_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_group_in_api** | [**FirewallGroupInAPI**](FirewallGroupInAPI.md)|  | 
 **policy** | [**object**](.md)| Тип группы правил | [optional] 

### Return type

[**FirewallGroupOutResponse**](FirewallGroupOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Группа правил создана |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_rule**
> FirewallRuleOutResponse create_group_rule(group_id, firewall_rule_in_api)

Создание firewall правила

Чтобы создать правило в группе, отправьте POST запрос на `/api/v1/firewall/groups/{group_id}/rules`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.firewall_rule_in_api import FirewallRuleInAPI
from timeweb_cloud_api.models.firewall_rule_out_response import FirewallRuleOutResponse
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    group_id = None # object | ID группы правил
    firewall_rule_in_api = timeweb_cloud_api.FirewallRuleInAPI() # FirewallRuleInAPI | 

    try:
        # Создание firewall правила
        api_response = api_instance.create_group_rule(group_id, firewall_rule_in_api)
        print("The response of FirewallApi->create_group_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->create_group_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| ID группы правил | 
 **firewall_rule_in_api** | [**FirewallRuleInAPI**](FirewallRuleInAPI.md)|  | 

### Return type

[**FirewallRuleOutResponse**](FirewallRuleOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Правило создано |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id)

Удаление группы правил

Чтобы удалить группу правил, отправьте DELETE запрос на `/api/v1/firewall/groups/{group_id}`

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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    group_id = None # object | ID группы правил

    try:
        # Удаление группы правил
        api_instance.delete_group(group_id)
    except Exception as e:
        print("Exception when calling FirewallApi->delete_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| ID группы правил | 

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
**204** | Группа удалена |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_rule**
> delete_group_rule(group_id, rule_id)

Удаление firewall правила

Чтобы удалить правило, отправьте DELETE запрос на `/api/v1/firewall/groups/{group_id}/rules/{rule_id}`

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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    group_id = None # object | ID группы правил
    rule_id = None # object | ID правила

    try:
        # Удаление firewall правила
        api_instance.delete_group_rule(group_id, rule_id)
    except Exception as e:
        print("Exception when calling FirewallApi->delete_group_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| ID группы правил | 
 **rule_id** | [**object**](.md)| ID правила | 

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
**204** | Правило удалено |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_resource_from_group**
> delete_resource_from_group(group_id, resource_id, resource_type=resource_type)

Отлинковка ресурса из firewall group

Чтобы отлинковать ресурс от группы правил, отправьте DELETE запрос на `/api/v1/firewall/groups/{group_id}/resources/{resource_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.resource_type import ResourceType
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    group_id = None # object | ID группы правил
    resource_id = None # object | ID ресурса
    resource_type = timeweb_cloud_api.ResourceType() # ResourceType |  (optional)

    try:
        # Отлинковка ресурса из firewall group
        api_instance.delete_resource_from_group(group_id, resource_id, resource_type=resource_type)
    except Exception as e:
        print("Exception when calling FirewallApi->delete_resource_from_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| ID группы правил | 
 **resource_id** | [**object**](.md)| ID ресурса | 
 **resource_type** | [**ResourceType**](.md)|  | [optional] 

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
**204** | Ресурс удален из Группы правил |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> FirewallGroupOutResponse get_group(group_id)

Получение информации о группе правил

Чтобы получить информацию о группе правил, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.firewall_group_out_response import FirewallGroupOutResponse
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    group_id = None # object | ID группы правил

    try:
        # Получение информации о группе правил
        api_response = api_instance.get_group(group_id)
        print("The response of FirewallApi->get_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->get_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| ID группы правил | 

### Return type

[**FirewallGroupOutResponse**](FirewallGroupOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о группе правил |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_resources**
> FirewallGroupResourcesOutResponse get_group_resources(group_id, limit=limit, offset=offset)

Получение слинкованных ресурсов

Чтобы получить слинкованных ресурсов для группы правил, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}/resources`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.firewall_group_resources_out_response import FirewallGroupResourcesOutResponse
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    group_id = None # object | ID группы правил
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)

    try:
        # Получение слинкованных ресурсов
        api_response = api_instance.get_group_resources(group_id, limit=limit, offset=offset)
        print("The response of FirewallApi->get_group_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->get_group_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| ID группы правил | 
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 

### Return type

[**FirewallGroupResourcesOutResponse**](FirewallGroupResourcesOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список слинкованных ресурсов |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_rule**
> FirewallRuleOutResponse get_group_rule(rule_id, group_id)

Получение информации о правиле

Чтобы получить инфомрацию о правиле, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}/rules/{rule_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.firewall_rule_out_response import FirewallRuleOutResponse
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    rule_id = None # object | ID правила
    group_id = None # object | ID группы правил

    try:
        # Получение информации о правиле
        api_response = api_instance.get_group_rule(rule_id, group_id)
        print("The response of FirewallApi->get_group_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->get_group_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | [**object**](.md)| ID правила | 
 **group_id** | [**object**](.md)| ID группы правил | 

### Return type

[**FirewallRuleOutResponse**](FirewallRuleOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о правиле |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group_rules**
> FirewallRulesOutResponse get_group_rules(group_id, limit=limit, offset=offset)

Получение списка правил

Чтобы получить список правил в группе, отправьте GET запрос на `/api/v1/firewall/groups/{group_id}/rules`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.firewall_rules_out_response import FirewallRulesOutResponse
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    group_id = None # object | ID группы правил
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)

    try:
        # Получение списка правил
        api_response = api_instance.get_group_rules(group_id, limit=limit, offset=offset)
        print("The response of FirewallApi->get_group_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->get_group_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| ID группы правил | 
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 

### Return type

[**FirewallRulesOutResponse**](FirewallRulesOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список правил |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_groups**
> FirewallGroupsOutResponse get_groups(limit=limit, offset=offset)

Получение групп правил

Чтобы получить групп правил для аккаунта, отправьте GET запрос на `/api/v1/firewall/groups`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.firewall_groups_out_response import FirewallGroupsOutResponse
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)

    try:
        # Получение групп правил
        api_response = api_instance.get_groups(limit=limit, offset=offset)
        print("The response of FirewallApi->get_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->get_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 

### Return type

[**FirewallGroupsOutResponse**](FirewallGroupsOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список групп правил |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rules_for_resource**
> FirewallGroupsOutResponse get_rules_for_resource(resource_id, resource_type, limit=limit, offset=offset)

Получение групп правил для ресурса

Чтобы получить список групп правил, с которыми слинкован ресурс, отправьте GET запрос на `/api/v1/firewall/service/{resource_type}/{resource_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.firewall_groups_out_response import FirewallGroupsOutResponse
from timeweb_cloud_api.models.resource_type import ResourceType
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    resource_id = None # object | Идентификатор ресурса
    resource_type = timeweb_cloud_api.ResourceType() # ResourceType | 
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)

    try:
        # Получение групп правил для ресурса
        api_response = api_instance.get_rules_for_resource(resource_id, resource_type, limit=limit, offset=offset)
        print("The response of FirewallApi->get_rules_for_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->get_rules_for_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| Идентификатор ресурса | 
 **resource_type** | [**ResourceType**](.md)|  | 
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 

### Return type

[**FirewallGroupsOutResponse**](FirewallGroupsOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список групп правил |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> FirewallGroupOutResponse update_group(group_id, firewall_group_in_api)

Обновление группы правил

Чтобы изменить группу правил, отправьте PATCH запрос на `/api/v1/firewall/groups/{group_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.firewall_group_in_api import FirewallGroupInAPI
from timeweb_cloud_api.models.firewall_group_out_response import FirewallGroupOutResponse
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    group_id = None # object | ID группы правил
    firewall_group_in_api = timeweb_cloud_api.FirewallGroupInAPI() # FirewallGroupInAPI | 

    try:
        # Обновление группы правил
        api_response = api_instance.update_group(group_id, firewall_group_in_api)
        print("The response of FirewallApi->update_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->update_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| ID группы правил | 
 **firewall_group_in_api** | [**FirewallGroupInAPI**](FirewallGroupInAPI.md)|  | 

### Return type

[**FirewallGroupOutResponse**](FirewallGroupOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Группа правил обновлена |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group_rule**
> FirewallRuleOutResponse update_group_rule(group_id, rule_id, firewall_rule_in_api)

Обновление firewall правила

Чтобы изменить правило, отправьте PATCH запрос на `/api/v1/firewall/groups/{group_id}/rules/{rule_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.firewall_rule_in_api import FirewallRuleInAPI
from timeweb_cloud_api.models.firewall_rule_out_response import FirewallRuleOutResponse
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
    api_instance = timeweb_cloud_api.FirewallApi(api_client)
    group_id = None # object | ID группы правил
    rule_id = None # object | ID правила
    firewall_rule_in_api = timeweb_cloud_api.FirewallRuleInAPI() # FirewallRuleInAPI | 

    try:
        # Обновление firewall правила
        api_response = api_instance.update_group_rule(group_id, rule_id, firewall_rule_in_api)
        print("The response of FirewallApi->update_group_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirewallApi->update_group_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | [**object**](.md)| ID группы правил | 
 **rule_id** | [**object**](.md)| ID правила | 
 **firewall_rule_in_api** | [**FirewallRuleInAPI**](FirewallRuleInAPI.md)|  | 

### Return type

[**FirewallRuleOutResponse**](FirewallRuleOutResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Правило обновлено |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

