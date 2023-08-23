# openapi_client.BalancersApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ips_to_balancer**](BalancersApi.md#add_ips_to_balancer) | **POST** /api/v1/balancers/{balancer_id}/ips | Добавление IP-адресов к балансировщику
[**create_balancer**](BalancersApi.md#create_balancer) | **POST** /api/v1/balancers | Создание бaлансировщика
[**create_balancer_rule**](BalancersApi.md#create_balancer_rule) | **POST** /api/v1/balancers/{balancer_id}/rules | Создание правила для балансировщика
[**delete_balancer**](BalancersApi.md#delete_balancer) | **DELETE** /api/v1/balancers/{balancer_id} | Удаление балансировщика
[**delete_balancer_rule**](BalancersApi.md#delete_balancer_rule) | **DELETE** /api/v1/balancers/{balancer_id}/rules/{rule_id} | Удаление правила для балансировщика
[**delete_ips_from_balancer**](BalancersApi.md#delete_ips_from_balancer) | **DELETE** /api/v1/balancers/{balancer_id}/ips | Удаление IP-адресов из балансировщика
[**get_balancer**](BalancersApi.md#get_balancer) | **GET** /api/v1/balancers/{balancer_id} | Получение бaлансировщика
[**get_balancer_ips**](BalancersApi.md#get_balancer_ips) | **GET** /api/v1/balancers/{balancer_id}/ips | Получение списка IP-адресов балансировщика
[**get_balancer_rules**](BalancersApi.md#get_balancer_rules) | **GET** /api/v1/balancers/{balancer_id}/rules | Получение правил балансировщика
[**get_balancers**](BalancersApi.md#get_balancers) | **GET** /api/v1/balancers | Получение списка всех бaлансировщиков
[**get_balancers_presets**](BalancersApi.md#get_balancers_presets) | **GET** /api/v1/presets/balancers | Получение списка тарифов для балансировщика
[**update_balancer**](BalancersApi.md#update_balancer) | **PATCH** /api/v1/balancers/{balancer_id} | Обновление балансировщика
[**update_balancer_rule**](BalancersApi.md#update_balancer_rule) | **PATCH** /api/v1/balancers/{balancer_id}/rules/{rule_id} | Обновление правила для балансировщика


# **add_ips_to_balancer**
> add_ips_to_balancer(balancer_id, add_ips_to_balancer_request)

Добавление IP-адресов к балансировщику

Чтобы добавить `IP`-адреса к балансировщику, отправьте запрос POST в `api/v1/balancers/{balancer_id}/ips`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.add_ips_to_balancer_request import AddIPsToBalancerRequest
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
    api_instance = openapi_client.BalancersApi(api_client)
    balancer_id = None # object | Идентификатор балансировщика
    add_ips_to_balancer_request = openapi_client.AddIPsToBalancerRequest() # AddIPsToBalancerRequest | 

    try:
        # Добавление IP-адресов к балансировщику
        api_instance.add_ips_to_balancer(balancer_id, add_ips_to_balancer_request)
    except Exception as e:
        print("Exception when calling BalancersApi->add_ips_to_balancer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balancer_id** | [**object**](.md)| Идентификатор балансировщика | 
 **add_ips_to_balancer_request** | [**AddIPsToBalancerRequest**](AddIPsToBalancerRequest.md)|  | 

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
**204** | &#x60;Ip&#x60; адреса добавлены к балансировщику |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_balancer**
> CreateBalancer200Response create_balancer(create_balancer)

Создание бaлансировщика

Чтобы создать бaлансировщик на вашем аккаунте, отправьте POST-запрос на `/api/v1/balancers`, задав необходимые атрибуты.  Балансировщик будет создан с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданном балансировщике.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.create_balancer import CreateBalancer
from openapi_client.models.create_balancer200_response import CreateBalancer200Response
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
    api_instance = openapi_client.BalancersApi(api_client)
    create_balancer = openapi_client.CreateBalancer() # CreateBalancer | 

    try:
        # Создание бaлансировщика
        api_response = api_instance.create_balancer(create_balancer)
        print("The response of BalancersApi->create_balancer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancersApi->create_balancer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_balancer** | [**CreateBalancer**](CreateBalancer.md)|  | 

### Return type

[**CreateBalancer200Response**](CreateBalancer200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;balancer&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_balancer_rule**
> CreateBalancerRule200Response create_balancer_rule(balancer_id, create_rule)

Создание правила для балансировщика

Чтобы создать правило для балансировщика, отправьте запрос POST в `api/v1/balancers/{balancer_id}/rules`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.create_balancer_rule200_response import CreateBalancerRule200Response
from openapi_client.models.create_rule import CreateRule
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
    api_instance = openapi_client.BalancersApi(api_client)
    balancer_id = None # object | Идентификатор балансировщика
    create_rule = openapi_client.CreateRule() # CreateRule | 

    try:
        # Создание правила для балансировщика
        api_response = api_instance.create_balancer_rule(balancer_id, create_rule)
        print("The response of BalancersApi->create_balancer_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancersApi->create_balancer_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balancer_id** | [**object**](.md)| Идентификатор балансировщика | 
 **create_rule** | [**CreateRule**](CreateRule.md)|  | 

### Return type

[**CreateBalancerRule200Response**](CreateBalancerRule200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;rule&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_balancer**
> DeleteBalancer200Response delete_balancer(balancer_id, hash=hash, code=code)

Удаление балансировщика

Чтобы удалить балансировщик, отправьте запрос DELETE в `api/v1/balancers/{balancer_id}`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.delete_balancer200_response import DeleteBalancer200Response
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
    api_instance = openapi_client.BalancersApi(api_client)
    balancer_id = None # object | Идентификатор балансировщика
    hash = 15095f25-aac3-4d60-a788-96cb5136f186 # object | Хеш, который совместно с кодом авторизации надо отправить для удаления, если включено подтверждение удаления сервисов через Телеграм. (optional)
    code = 0000 # object | Код подтверждения, который придет к вам в Телеграм, после запроса удаления, если включено подтверждение удаления сервисов.  При помощи API токена сервисы можно удалять без подтверждения, если параметр токена `is_able_to_delete` установлен в значение `true` (optional)

    try:
        # Удаление балансировщика
        api_response = api_instance.delete_balancer(balancer_id, hash=hash, code=code)
        print("The response of BalancersApi->delete_balancer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancersApi->delete_balancer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balancer_id** | [**object**](.md)| Идентификатор балансировщика | 
 **hash** | [**object**](.md)| Хеш, который совместно с кодом авторизации надо отправить для удаления, если включено подтверждение удаления сервисов через Телеграм. | [optional] 
 **code** | [**object**](.md)| Код подтверждения, который придет к вам в Телеграм, после запроса удаления, если включено подтверждение удаления сервисов.  При помощи API токена сервисы можно удалять без подтверждения, если параметр токена &#x60;is_able_to_delete&#x60; установлен в значение &#x60;true&#x60; | [optional] 

### Return type

[**DeleteBalancer200Response**](DeleteBalancer200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;balancer_delete&#x60; |  -  |
**204** | Балансировщик успешно удален. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_balancer_rule**
> delete_balancer_rule(balancer_id, rule_id)

Удаление правила для балансировщика

Чтобы удалить правило для балансировщика, отправьте запрос DELETE в `api/v1/balancers/{balancer_id}/rules/{rule_id}`. 

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
    api_instance = openapi_client.BalancersApi(api_client)
    balancer_id = None # object | Идентификатор балансировщика
    rule_id = None # object | Идентификатор правила для балансировщика

    try:
        # Удаление правила для балансировщика
        api_instance.delete_balancer_rule(balancer_id, rule_id)
    except Exception as e:
        print("Exception when calling BalancersApi->delete_balancer_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balancer_id** | [**object**](.md)| Идентификатор балансировщика | 
 **rule_id** | [**object**](.md)| Идентификатор правила для балансировщика | 

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
**204** | Правило удалено из балансировщика |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ips_from_balancer**
> delete_ips_from_balancer(balancer_id, add_ips_to_balancer_request)

Удаление IP-адресов из балансировщика

Чтобы удалить `IP`-адреса из балансировщика, отправьте запрос DELETE в `api/v1/balancers/{balancer_id}/ips`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.add_ips_to_balancer_request import AddIPsToBalancerRequest
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
    api_instance = openapi_client.BalancersApi(api_client)
    balancer_id = None # object | Идентификатор балансировщика
    add_ips_to_balancer_request = openapi_client.AddIPsToBalancerRequest() # AddIPsToBalancerRequest | 

    try:
        # Удаление IP-адресов из балансировщика
        api_instance.delete_ips_from_balancer(balancer_id, add_ips_to_balancer_request)
    except Exception as e:
        print("Exception when calling BalancersApi->delete_ips_from_balancer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balancer_id** | [**object**](.md)| Идентификатор балансировщика | 
 **add_ips_to_balancer_request** | [**AddIPsToBalancerRequest**](AddIPsToBalancerRequest.md)|  | 

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
**204** | &#x60;Ip&#x60; адрес удален из балансировщика |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancer**
> CreateBalancer200Response get_balancer(balancer_id)

Получение бaлансировщика

Чтобы отобразить информацию об отдельном балансировщике, отправьте запрос GET на `api/v1/balancers/{balancer_id}`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.create_balancer200_response import CreateBalancer200Response
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
    api_instance = openapi_client.BalancersApi(api_client)
    balancer_id = None # object | Идентификатор балансировщика

    try:
        # Получение бaлансировщика
        api_response = api_instance.get_balancer(balancer_id)
        print("The response of BalancersApi->get_balancer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancersApi->get_balancer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balancer_id** | [**object**](.md)| Идентификатор балансировщика | 

### Return type

[**CreateBalancer200Response**](CreateBalancer200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;balancer&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancer_ips**
> GetBalancerIPs200Response get_balancer_ips(balancer_id)

Получение списка IP-адресов балансировщика

Чтобы добавить `IP`-адреса к балансировщику, отправьте запрос GET в `api/v1/balancers/{balancer_id}/ips`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.get_balancer_ips200_response import GetBalancerIPs200Response
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
    api_instance = openapi_client.BalancersApi(api_client)
    balancer_id = None # object | Идентификатор балансировщика

    try:
        # Получение списка IP-адресов балансировщика
        api_response = api_instance.get_balancer_ips(balancer_id)
        print("The response of BalancersApi->get_balancer_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancersApi->get_balancer_ips: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balancer_id** | [**object**](.md)| Идентификатор балансировщика | 

### Return type

[**GetBalancerIPs200Response**](GetBalancerIPs200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;ips&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancer_rules**
> GetBalancerRules200Response get_balancer_rules(balancer_id)

Получение правил балансировщика

Чтобы получить правила балансировщика, отправьте запрос GET в `api/v1/balancers/{balancer_id}/rules`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.get_balancer_rules200_response import GetBalancerRules200Response
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
    api_instance = openapi_client.BalancersApi(api_client)
    balancer_id = None # object | Идентификатор балансировщика

    try:
        # Получение правил балансировщика
        api_response = api_instance.get_balancer_rules(balancer_id)
        print("The response of BalancersApi->get_balancer_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancersApi->get_balancer_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balancer_id** | [**object**](.md)| Идентификатор балансировщика | 

### Return type

[**GetBalancerRules200Response**](GetBalancerRules200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;rules&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancers**
> GetBalancers200Response get_balancers(limit=limit, offset=offset)

Получение списка всех бaлансировщиков

Чтобы получить список всех бaлансировщиков на вашем аккаунте, отправьте GET-запрос на `/api/v1/balancers`.   Тело ответа будет представлять собой объект JSON с ключом `balancers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.get_balancers200_response import GetBalancers200Response
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
    api_instance = openapi_client.BalancersApi(api_client)
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)

    try:
        # Получение списка всех бaлансировщиков
        api_response = api_instance.get_balancers(limit=limit, offset=offset)
        print("The response of BalancersApi->get_balancers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancersApi->get_balancers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 

### Return type

[**GetBalancers200Response**](GetBalancers200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;balancers&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_balancers_presets**
> GetBalancersPresets200Response get_balancers_presets()

Получение списка тарифов для балансировщика

Чтобы получить список тарифов для балансировщика, отправьте GET-запрос на `/api/v1/presets/balancers`.   Тело ответа будет представлять собой объект JSON с ключом `balancers_presets`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.get_balancers_presets200_response import GetBalancersPresets200Response
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
    api_instance = openapi_client.BalancersApi(api_client)

    try:
        # Получение списка тарифов для балансировщика
        api_response = api_instance.get_balancers_presets()
        print("The response of BalancersApi->get_balancers_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancersApi->get_balancers_presets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBalancersPresets200Response**](GetBalancersPresets200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Тарифы успешно получены |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_balancer**
> CreateBalancer200Response update_balancer(balancer_id, update_balancer)

Обновление балансировщика

Чтобы обновить только определенные атрибуты балансировщика, отправьте запрос PATCH в `api/v1/balancers/{balancer_id}`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.create_balancer200_response import CreateBalancer200Response
from openapi_client.models.update_balancer import UpdateBalancer
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
    api_instance = openapi_client.BalancersApi(api_client)
    balancer_id = None # object | Идентификатор балансировщика
    update_balancer = openapi_client.UpdateBalancer() # UpdateBalancer | 

    try:
        # Обновление балансировщика
        api_response = api_instance.update_balancer(balancer_id, update_balancer)
        print("The response of BalancersApi->update_balancer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancersApi->update_balancer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balancer_id** | [**object**](.md)| Идентификатор балансировщика | 
 **update_balancer** | [**UpdateBalancer**](UpdateBalancer.md)|  | 

### Return type

[**CreateBalancer200Response**](CreateBalancer200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;balancer&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_balancer_rule**
> CreateBalancerRule200Response update_balancer_rule(balancer_id, rule_id, update_rule)

Обновление правила для балансировщика

Чтобы обновить правило для балансировщика, отправьте запрос PATCH в `api/v1/balancers/{balancer_id}/rules/{rule_id}`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import openapi_client
from openapi_client.models.create_balancer_rule200_response import CreateBalancerRule200Response
from openapi_client.models.update_rule import UpdateRule
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
    api_instance = openapi_client.BalancersApi(api_client)
    balancer_id = None # object | Идентификатор балансировщика
    rule_id = None # object | Идентификатор правила для балансировщика
    update_rule = openapi_client.UpdateRule() # UpdateRule | 

    try:
        # Обновление правила для балансировщика
        api_response = api_instance.update_balancer_rule(balancer_id, rule_id, update_rule)
        print("The response of BalancersApi->update_balancer_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BalancersApi->update_balancer_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **balancer_id** | [**object**](.md)| Идентификатор балансировщика | 
 **rule_id** | [**object**](.md)| Идентификатор правила для балансировщика | 
 **update_rule** | [**UpdateRule**](UpdateRule.md)|  | 

### Return type

[**CreateBalancerRule200Response**](CreateBalancerRule200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;rule&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

