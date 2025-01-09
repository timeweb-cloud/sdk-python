# timeweb_cloud_api.AccountApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_countries_to_allowed_list**](AccountApi.md#add_countries_to_allowed_list) | **POST** /api/v1/auth/access/countries | Добавление стран в список разрешенных
[**add_ips_to_allowed_list**](AccountApi.md#add_ips_to_allowed_list) | **POST** /api/v1/auth/access/ips | Добавление IP-адресов в список разрешенных
[**delete_countries_from_allowed_list**](AccountApi.md#delete_countries_from_allowed_list) | **DELETE** /api/v1/auth/access/countries | Удаление стран из списка разрешенных
[**delete_ips_from_allowed_list**](AccountApi.md#delete_ips_from_allowed_list) | **DELETE** /api/v1/auth/access/ips | Удаление IP-адресов из списка разрешенных
[**get_account_status**](AccountApi.md#get_account_status) | **GET** /api/v1/account/status | Получение статуса аккаунта
[**get_auth_access_settings**](AccountApi.md#get_auth_access_settings) | **GET** /api/v1/auth/access | Получить информацию о ограничениях авторизации пользователя
[**get_countries**](AccountApi.md#get_countries) | **GET** /api/v1/auth/access/countries | Получение списка стран
[**get_finances**](AccountApi.md#get_finances) | **GET** /api/v1/account/finances | Получение платежной информации
[**get_notification_settings**](AccountApi.md#get_notification_settings) | **GET** /api/v1/account/notification-settings | Получение настроек уведомлений аккаунта
[**update_auth_restrictions_by_countries**](AccountApi.md#update_auth_restrictions_by_countries) | **POST** /api/v1/auth/access/countries/enabled | Включение/отключение ограничений по стране
[**update_auth_restrictions_by_ip**](AccountApi.md#update_auth_restrictions_by_ip) | **POST** /api/v1/auth/access/ips/enabled | Включение/отключение ограничений по IP-адресу
[**update_notification_settings**](AccountApi.md#update_notification_settings) | **PATCH** /api/v1/account/notification-settings | Изменение настроек уведомлений аккаунта


# **add_countries_to_allowed_list**
> AddCountriesToAllowedList201Response add_countries_to_allowed_list(add_countries_to_allowed_list_request)

Добавление стран в список разрешенных

Чтобы добавить страны в список разрешенных, отправьте POST-запрос в `api/v1/access/countries`, передав в теле запроса параметр `countries` со списком стран.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_countries_to_allowed_list201_response import AddCountriesToAllowedList201Response
from timeweb_cloud_api.models.add_countries_to_allowed_list_request import AddCountriesToAllowedListRequest
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)
    add_countries_to_allowed_list_request = timeweb_cloud_api.AddCountriesToAllowedListRequest() # AddCountriesToAllowedListRequest | 

    try:
        # Добавление стран в список разрешенных
        api_response = api_instance.add_countries_to_allowed_list(add_countries_to_allowed_list_request)
        print("The response of AccountApi->add_countries_to_allowed_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->add_countries_to_allowed_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_countries_to_allowed_list_request** | [**AddCountriesToAllowedListRequest**](AddCountriesToAllowedListRequest.md)|  | 

### Return type

[**AddCountriesToAllowedList201Response**](AddCountriesToAllowedList201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;countries&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_ips_to_allowed_list**
> AddIPsToAllowedList201Response add_ips_to_allowed_list(add_ips_to_allowed_list_request)

Добавление IP-адресов в список разрешенных

Чтобы добавить IP-адреса в список разрешенных, отправьте POST-запрос в `api/v1/access/ips`, передав в теле запроса параметр `ips` со списком IP-адресов.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_ips_to_allowed_list201_response import AddIPsToAllowedList201Response
from timeweb_cloud_api.models.add_ips_to_allowed_list_request import AddIPsToAllowedListRequest
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)
    add_ips_to_allowed_list_request = timeweb_cloud_api.AddIPsToAllowedListRequest() # AddIPsToAllowedListRequest | 

    try:
        # Добавление IP-адресов в список разрешенных
        api_response = api_instance.add_ips_to_allowed_list(add_ips_to_allowed_list_request)
        print("The response of AccountApi->add_ips_to_allowed_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->add_ips_to_allowed_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_ips_to_allowed_list_request** | [**AddIPsToAllowedListRequest**](AddIPsToAllowedListRequest.md)|  | 

### Return type

[**AddIPsToAllowedList201Response**](AddIPsToAllowedList201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;ips&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_countries_from_allowed_list**
> DeleteCountriesFromAllowedList200Response delete_countries_from_allowed_list(delete_countries_from_allowed_list_request)

Удаление стран из списка разрешенных

Чтобы удалить страны из списка разрешенных, отправьте DELETE-запрос в `api/v1/access/countries`, передав в теле запроса параметр `countries` со списком стран.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.delete_countries_from_allowed_list200_response import DeleteCountriesFromAllowedList200Response
from timeweb_cloud_api.models.delete_countries_from_allowed_list_request import DeleteCountriesFromAllowedListRequest
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)
    delete_countries_from_allowed_list_request = timeweb_cloud_api.DeleteCountriesFromAllowedListRequest() # DeleteCountriesFromAllowedListRequest | 

    try:
        # Удаление стран из списка разрешенных
        api_response = api_instance.delete_countries_from_allowed_list(delete_countries_from_allowed_list_request)
        print("The response of AccountApi->delete_countries_from_allowed_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->delete_countries_from_allowed_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_countries_from_allowed_list_request** | [**DeleteCountriesFromAllowedListRequest**](DeleteCountriesFromAllowedListRequest.md)|  | 

### Return type

[**DeleteCountriesFromAllowedList200Response**](DeleteCountriesFromAllowedList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;countries&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ips_from_allowed_list**
> DeleteIPsFromAllowedList200Response delete_ips_from_allowed_list(delete_ips_from_allowed_list_request)

Удаление IP-адресов из списка разрешенных

Чтобы удалить IP-адреса из списка разрешенных, отправьте DELETE-запрос в `api/v1/access/ips`, передав в теле запроса параметр `ips` со списком IP-адресов.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.delete_ips_from_allowed_list200_response import DeleteIPsFromAllowedList200Response
from timeweb_cloud_api.models.delete_ips_from_allowed_list_request import DeleteIPsFromAllowedListRequest
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)
    delete_ips_from_allowed_list_request = timeweb_cloud_api.DeleteIPsFromAllowedListRequest() # DeleteIPsFromAllowedListRequest | 

    try:
        # Удаление IP-адресов из списка разрешенных
        api_response = api_instance.delete_ips_from_allowed_list(delete_ips_from_allowed_list_request)
        print("The response of AccountApi->delete_ips_from_allowed_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->delete_ips_from_allowed_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_ips_from_allowed_list_request** | [**DeleteIPsFromAllowedListRequest**](DeleteIPsFromAllowedListRequest.md)|  | 

### Return type

[**DeleteIPsFromAllowedList200Response**](DeleteIPsFromAllowedList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ips&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_status**
> GetAccountStatus200Response get_account_status()

Получение статуса аккаунта

Чтобы получить статус аккаунта, отправьте GET-запрос на `/api/v1/account/status`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_account_status200_response import GetAccountStatus200Response
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)

    try:
        # Получение статуса аккаунта
        api_response = api_instance.get_account_status()
        print("The response of AccountApi->get_account_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_account_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAccountStatus200Response**](GetAccountStatus200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;status&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_access_settings**
> GetAuthAccessSettings200Response get_auth_access_settings()

Получить информацию о ограничениях авторизации пользователя

Чтобы получить информацию о ограничениях авторизации пользователя, отправьте GET-запрос на `/api/v1/auth/access`.   Тело ответа будет представлять собой объект JSON с ключами `is_ip_restrictions_enabled`, `is_country_restrictions_enabled` и `white_list`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_auth_access_settings200_response import GetAuthAccessSettings200Response
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)

    try:
        # Получить информацию о ограничениях авторизации пользователя
        api_response = api_instance.get_auth_access_settings()
        print("The response of AccountApi->get_auth_access_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_auth_access_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAuthAccessSettings200Response**](GetAuthAccessSettings200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;is_ip_restrictions_enabled&#x60;, &#x60;is_country_restrictions_enabled&#x60; и &#x60;white_list&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_countries**
> GetCountries200Response get_countries()

Получение списка стран

Чтобы получить список стран, отправьте GET-запрос на `/api/v1/auth/access/countries`.   Тело ответа будет представлять собой объект JSON с ключом `countries`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_countries200_response import GetCountries200Response
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)

    try:
        # Получение списка стран
        api_response = api_instance.get_countries()
        print("The response of AccountApi->get_countries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_countries: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCountries200Response**](GetCountries200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;countries&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finances**
> GetFinances200Response get_finances()

Получение платежной информации

Чтобы получить платежную информацию, отправьте GET-запрос на `/api/v1/account/finances`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_finances200_response import GetFinances200Response
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)

    try:
        # Получение платежной информации
        api_response = api_instance.get_finances()
        print("The response of AccountApi->get_finances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_finances: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetFinances200Response**](GetFinances200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;finances&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_settings**
> GetNotificationSettings200Response get_notification_settings()

Получение настроек уведомлений аккаунта

Чтобы получить статус аккаунта, отправьте GET запрос на `/api/v1/account/notification-settings`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_notification_settings200_response import GetNotificationSettings200Response
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)

    try:
        # Получение настроек уведомлений аккаунта
        api_response = api_instance.get_notification_settings()
        print("The response of AccountApi->get_notification_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->get_notification_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetNotificationSettings200Response**](GetNotificationSettings200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;notification_settings&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auth_restrictions_by_countries**
> update_auth_restrictions_by_countries(update_auth_restrictions_by_countries_request)

Включение/отключение ограничений по стране

Чтобы включить/отключить ограничения по стране, отправьте POST-запрос в `api/v1/access/countries/enabled`, передав в теле запроса параметр `is_enabled`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.update_auth_restrictions_by_countries_request import UpdateAuthRestrictionsByCountriesRequest
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)
    update_auth_restrictions_by_countries_request = timeweb_cloud_api.UpdateAuthRestrictionsByCountriesRequest() # UpdateAuthRestrictionsByCountriesRequest | 

    try:
        # Включение/отключение ограничений по стране
        api_instance.update_auth_restrictions_by_countries(update_auth_restrictions_by_countries_request)
    except Exception as e:
        print("Exception when calling AccountApi->update_auth_restrictions_by_countries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_auth_restrictions_by_countries_request** | [**UpdateAuthRestrictionsByCountriesRequest**](UpdateAuthRestrictionsByCountriesRequest.md)|  | 

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
**204** | Ограничения по странам успешно изменены |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_auth_restrictions_by_ip**
> update_auth_restrictions_by_ip(update_auth_restrictions_by_countries_request)

Включение/отключение ограничений по IP-адресу

Чтобы включить/отключить ограничения по IP-адресу, отправьте POST-запрос в `api/v1/access/ips/enabled`, передав в теле запроса параметр `is_enabled`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.update_auth_restrictions_by_countries_request import UpdateAuthRestrictionsByCountriesRequest
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)
    update_auth_restrictions_by_countries_request = timeweb_cloud_api.UpdateAuthRestrictionsByCountriesRequest() # UpdateAuthRestrictionsByCountriesRequest | 

    try:
        # Включение/отключение ограничений по IP-адресу
        api_instance.update_auth_restrictions_by_ip(update_auth_restrictions_by_countries_request)
    except Exception as e:
        print("Exception when calling AccountApi->update_auth_restrictions_by_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_auth_restrictions_by_countries_request** | [**UpdateAuthRestrictionsByCountriesRequest**](UpdateAuthRestrictionsByCountriesRequest.md)|  | 

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
**204** | Ограничения по IP-адресу успешно изменены |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_notification_settings**
> GetNotificationSettings200Response update_notification_settings(update_notification_settings_request)

Изменение настроек уведомлений аккаунта

Чтобы изменить настройки уведомлений аккаунта, отправьте PATCH запрос на `/api/v1/account/notification-settings`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_notification_settings200_response import GetNotificationSettings200Response
from timeweb_cloud_api.models.update_notification_settings_request import UpdateNotificationSettingsRequest
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
    api_instance = timeweb_cloud_api.AccountApi(api_client)
    update_notification_settings_request = timeweb_cloud_api.UpdateNotificationSettingsRequest() # UpdateNotificationSettingsRequest | 

    try:
        # Изменение настроек уведомлений аккаунта
        api_response = api_instance.update_notification_settings(update_notification_settings_request)
        print("The response of AccountApi->update_notification_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AccountApi->update_notification_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_notification_settings_request** | [**UpdateNotificationSettingsRequest**](UpdateNotificationSettingsRequest.md)|  | 

### Return type

[**GetNotificationSettings200Response**](GetNotificationSettings200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;notification_settings&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

