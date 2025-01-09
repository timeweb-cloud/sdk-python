# timeweb_cloud_api.DomainsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain**](DomainsApi.md#add_domain) | **POST** /api/v1/add-domain/{fqdn} | Добавление домена на аккаунт
[**add_subdomain**](DomainsApi.md#add_subdomain) | **POST** /api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn} | Добавление поддомена
[**check_domain**](DomainsApi.md#check_domain) | **GET** /api/v1/check-domain/{fqdn} | Проверить, доступен ли домен для регистрации
[**create_domain_dns_record**](DomainsApi.md#create_domain_dns_record) | **POST** /api/v1/domains/{fqdn}/dns-records | Добавить информацию о DNS-записи для домена или поддомена
[**create_domain_request**](DomainsApi.md#create_domain_request) | **POST** /api/v1/domains-requests | Создание заявки на регистрацию/продление/трансфер домена
[**delete_domain**](DomainsApi.md#delete_domain) | **DELETE** /api/v1/domains/{fqdn} | Удаление домена
[**delete_domain_dns_record**](DomainsApi.md#delete_domain_dns_record) | **DELETE** /api/v1/domains/{fqdn}/dns-records/{record_id} | Удалить информацию о DNS-записи для домена или поддомена
[**delete_subdomain**](DomainsApi.md#delete_subdomain) | **DELETE** /api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn} | Удаление поддомена
[**get_domain**](DomainsApi.md#get_domain) | **GET** /api/v1/domains/{fqdn} | Получение информации о домене
[**get_domain_default_dns_records**](DomainsApi.md#get_domain_default_dns_records) | **GET** /api/v1/domains/{fqdn}/default-dns-records | Получить информацию обо всех DNS-записях по умолчанию домена или поддомена
[**get_domain_dns_records**](DomainsApi.md#get_domain_dns_records) | **GET** /api/v1/domains/{fqdn}/dns-records | Получить информацию обо всех пользовательских DNS-записях домена или поддомена
[**get_domain_name_servers**](DomainsApi.md#get_domain_name_servers) | **GET** /api/v1/domains/{fqdn}/name-servers | Получение списка name-серверов домена
[**get_domain_request**](DomainsApi.md#get_domain_request) | **GET** /api/v1/domains-requests/{request_id} | Получение заявки на регистрацию/продление/трансфер домена
[**get_domain_requests**](DomainsApi.md#get_domain_requests) | **GET** /api/v1/domains-requests | Получение списка заявок на регистрацию/продление/трансфер домена
[**get_domains**](DomainsApi.md#get_domains) | **GET** /api/v1/domains | Получение списка всех доменов
[**get_tld**](DomainsApi.md#get_tld) | **GET** /api/v1/tlds/{tld_id} | Получить информацию о доменной зоне по ID
[**get_tlds**](DomainsApi.md#get_tlds) | **GET** /api/v1/tlds | Получить информацию о доменных зонах
[**update_domain_auto_prolongation**](DomainsApi.md#update_domain_auto_prolongation) | **PATCH** /api/v1/domains/{fqdn} | Включение/выключение автопродления домена
[**update_domain_dns_record**](DomainsApi.md#update_domain_dns_record) | **PATCH** /api/v1/domains/{fqdn}/dns-records/{record_id} | Обновить информацию о DNS-записи домена или поддомена
[**update_domain_name_servers**](DomainsApi.md#update_domain_name_servers) | **PUT** /api/v1/domains/{fqdn}/name-servers | Изменение name-серверов домена
[**update_domain_request**](DomainsApi.md#update_domain_request) | **PATCH** /api/v1/domains-requests/{request_id} | Оплата/обновление заявки на регистрацию/продление/трансфер домена


# **add_domain**
> add_domain(fqdn)

Добавление домена на аккаунт

Чтобы добавить домен на свой аккаунт, отправьте запрос POST на `/api/v1/add-domain/{fqdn}`.

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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена.

    try:
        # Добавление домена на аккаунт
        api_instance.add_domain(fqdn)
    except Exception as e:
        print("Exception when calling DomainsApi->add_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Домен успешно добавлен на ваш аккаунт. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_subdomain**
> AddSubdomain201Response add_subdomain(fqdn, subdomain_fqdn)

Добавление поддомена

Чтобы добавить поддомен, отправьте запрос POST на `/api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn}`, задав необходимые атрибуты.  Поддомен будет добавлен с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о добавленном поддомене.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_subdomain201_response import AddSubdomain201Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена.
    subdomain_fqdn = sub.somedomain.ru # object | Полное имя поддомена.

    try:
        # Добавление поддомена
        api_response = api_instance.add_subdomain(fqdn, subdomain_fqdn)
        print("The response of DomainsApi->add_subdomain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->add_subdomain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена. | 
 **subdomain_fqdn** | [**object**](.md)| Полное имя поддомена. | 

### Return type

[**AddSubdomain201Response**](AddSubdomain201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON c ключом &#x60;subdomain&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_domain**
> CheckDomain200Response check_domain(fqdn)

Проверить, доступен ли домен для регистрации

Чтобы проверить, доступен ли домен для регистрации, отправьте запрос GET на `/api/v1/check-domain/{fqdn}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.check_domain200_response import CheckDomain200Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена.

    try:
        # Проверить, доступен ли домен для регистрации
        api_response = api_instance.check_domain(fqdn)
        print("The response of DomainsApi->check_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->check_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена. | 

### Return type

[**CheckDomain200Response**](CheckDomain200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;is_domain_available&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_domain_dns_record**
> CreateDomainDNSRecord201Response create_domain_dns_record(fqdn, create_dns)

Добавить информацию о DNS-записи для домена или поддомена

Чтобы добавить информацию о DNS-записи для домена или поддомена, отправьте запрос POST на `/api/v1/domains/{fqdn}/dns-records`, задав необходимые атрибуты.  DNS-запись будет добавлена с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о добавленной DNS-записи.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_dns import CreateDns
from timeweb_cloud_api.models.create_domain_dns_record201_response import CreateDomainDNSRecord201Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена или поддомена.
    create_dns = timeweb_cloud_api.CreateDns() # CreateDns | 

    try:
        # Добавить информацию о DNS-записи для домена или поддомена
        api_response = api_instance.create_domain_dns_record(fqdn, create_dns)
        print("The response of DomainsApi->create_domain_dns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->create_domain_dns_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена или поддомена. | 
 **create_dns** | [**CreateDns**](CreateDns.md)|  | 

### Return type

[**CreateDomainDNSRecord201Response**](CreateDomainDNSRecord201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON c ключом &#x60;dns_record&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_domain_request**
> CreateDomainRequest201Response create_domain_request(domain_register)

Создание заявки на регистрацию/продление/трансфер домена

Чтобы создать заявку на регистрацию/продление/трансфер домена, отправьте POST-запрос в `api/v1/domains-requests`, задав необходимые атрибуты.  Заявка будет создана с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданной заявке.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_domain_request201_response import CreateDomainRequest201Response
from timeweb_cloud_api.models.domain_register import DomainRegister
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    domain_register = timeweb_cloud_api.DomainRegister() # DomainRegister | 

    try:
        # Создание заявки на регистрацию/продление/трансфер домена
        api_response = api_instance.create_domain_request(domain_register)
        print("The response of DomainsApi->create_domain_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->create_domain_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_register** | [**DomainRegister**](DomainRegister.md)|  | 

### Return type

[**CreateDomainRequest201Response**](CreateDomainRequest201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON c ключом &#x60;request&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain**
> delete_domain(fqdn)

Удаление домена

Чтобы удалить домен, отправьте запрос DELETE на `/api/v1/domains/{fqdn}`.

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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена.

    try:
        # Удаление домена
        api_instance.delete_domain(fqdn)
    except Exception as e:
        print("Exception when calling DomainsApi->delete_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Домен успешно удален. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_domain_dns_record**
> delete_domain_dns_record(fqdn, record_id)

Удалить информацию о DNS-записи для домена или поддомена

Чтобы удалить информацию о DNS-записи для домена или поддомена, отправьте запрос DELETE на `/api/v1/domains/{fqdn}/dns-records/{record_id}`.

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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена или поддомена.
    record_id = 123 # object | ID DNS-записи домена или поддомена.

    try:
        # Удалить информацию о DNS-записи для домена или поддомена
        api_instance.delete_domain_dns_record(fqdn, record_id)
    except Exception as e:
        print("Exception when calling DomainsApi->delete_domain_dns_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена или поддомена. | 
 **record_id** | [**object**](.md)| ID DNS-записи домена или поддомена. | 

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
**204** | Информация о DNS-записи успешно удалена. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subdomain**
> delete_subdomain(fqdn, subdomain_fqdn)

Удаление поддомена

Чтобы удалить поддомен, отправьте запрос DELETE на `/api/v1/domains/{fqdn}/subdomains/{subdomain_fqdn}`.

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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена.
    subdomain_fqdn = sub.somedomain.ru # object | Полное имя поддомена.

    try:
        # Удаление поддомена
        api_instance.delete_subdomain(fqdn, subdomain_fqdn)
    except Exception as e:
        print("Exception when calling DomainsApi->delete_subdomain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена. | 
 **subdomain_fqdn** | [**object**](.md)| Полное имя поддомена. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Поддомен успешно удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain**
> GetDomain200Response get_domain(fqdn)

Получение информации о домене

Чтобы отобразить информацию об отдельном домене, отправьте запрос GET на `/api/v1/domains/{fqdn}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_domain200_response import GetDomain200Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена.

    try:
        # Получение информации о домене
        api_response = api_instance.get_domain(fqdn)
        print("The response of DomainsApi->get_domain:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена. | 

### Return type

[**GetDomain200Response**](GetDomain200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;domain&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_default_dns_records**
> GetDomainDNSRecords200Response get_domain_default_dns_records(fqdn, limit=limit, offset=offset)

Получить информацию обо всех DNS-записях по умолчанию домена или поддомена

Чтобы получить информацию обо всех DNS-записях по умолчанию домена или поддомена, отправьте запрос GET на `/api/v1/domains/{fqdn}/default-dns-records`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_domain_dns_records200_response import GetDomainDNSRecords200Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена или поддомена.
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)

    try:
        # Получить информацию обо всех DNS-записях по умолчанию домена или поддомена
        api_response = api_instance.get_domain_default_dns_records(fqdn, limit=limit, offset=offset)
        print("The response of DomainsApi->get_domain_default_dns_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain_default_dns_records: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена или поддомена. | 
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 

### Return type

[**GetDomainDNSRecords200Response**](GetDomainDNSRecords200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;dns_records&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_dns_records**
> GetDomainDNSRecords200Response get_domain_dns_records(fqdn, limit=limit, offset=offset)

Получить информацию обо всех пользовательских DNS-записях домена или поддомена

Чтобы получить информацию обо всех пользовательских DNS-записях домена или поддомена, отправьте запрос GET на `/api/v1/domains/{fqdn}/dns-records`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_domain_dns_records200_response import GetDomainDNSRecords200Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена или поддомена.
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)

    try:
        # Получить информацию обо всех пользовательских DNS-записях домена или поддомена
        api_response = api_instance.get_domain_dns_records(fqdn, limit=limit, offset=offset)
        print("The response of DomainsApi->get_domain_dns_records:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain_dns_records: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена или поддомена. | 
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 

### Return type

[**GetDomainDNSRecords200Response**](GetDomainDNSRecords200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;dns_records&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_name_servers**
> GetDomainNameServers200Response get_domain_name_servers(fqdn)

Получение списка name-серверов домена

Чтобы получить список name-серверов домена, отправьте запрос GET на `/api/v1/domains/{fqdn}/name-servers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_domain_name_servers200_response import GetDomainNameServers200Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена.

    try:
        # Получение списка name-серверов домена
        api_response = api_instance.get_domain_name_servers(fqdn)
        print("The response of DomainsApi->get_domain_name_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain_name_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена. | 

### Return type

[**GetDomainNameServers200Response**](GetDomainNameServers200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;name_servers&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_request**
> CreateDomainRequest201Response get_domain_request(request_id)

Получение заявки на регистрацию/продление/трансфер домена

Чтобы получить заявку на регистрацию/продление/трансфер домена, отправьте запрос GET на `/api/v1/domains-requests/{request_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_domain_request201_response import CreateDomainRequest201Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    request_id = 123 # object | ID заявки на регистрацию/продление/трансфер домена.

    try:
        # Получение заявки на регистрацию/продление/трансфер домена
        api_response = api_instance.get_domain_request(request_id)
        print("The response of DomainsApi->get_domain_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | [**object**](.md)| ID заявки на регистрацию/продление/трансфер домена. | 

### Return type

[**CreateDomainRequest201Response**](CreateDomainRequest201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;request&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_requests**
> GetDomainRequests200Response get_domain_requests(person_id=person_id)

Получение списка заявок на регистрацию/продление/трансфер домена

Чтобы получить список заявок на регистрацию/продление/трансфер домена, отправьте запрос GET на `/api/v1/domains-requests`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_domain_requests200_response import GetDomainRequests200Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    person_id = 123 # object | ID администратора, на которого зарегистрирован домен. (optional)

    try:
        # Получение списка заявок на регистрацию/продление/трансфер домена
        api_response = api_instance.get_domain_requests(person_id=person_id)
        print("The response of DomainsApi->get_domain_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domain_requests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | [**object**](.md)| ID администратора, на которого зарегистрирован домен. | [optional] 

### Return type

[**GetDomainRequests200Response**](GetDomainRequests200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;requests&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domains**
> GetDomains200Response get_domains(limit=limit, offset=offset, idn_name=idn_name, linked_ip=linked_ip, order=order, sort=sort)

Получение списка всех доменов

Чтобы получить список всех доменов на вашем аккаунте, отправьте GET-запрос на `/api/v1/domains`.   Тело ответа будет представлять собой объект JSON с ключом `domains`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_domains200_response import GetDomains200Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)
    idn_name = xn--e1afmkfd.xn--p1ai # object | Интернационализированное доменное имя. (optional)
    linked_ip = 192.168.1.1 # object | Привязанный к домену IP-адрес. (optional)
    order = asc # object | Порядок доменов. (optional)
    sort = idn_name # object | Сортировка доменов. (optional)

    try:
        # Получение списка всех доменов
        api_response = api_instance.get_domains(limit=limit, offset=offset, idn_name=idn_name, linked_ip=linked_ip, order=order, sort=sort)
        print("The response of DomainsApi->get_domains:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 
 **idn_name** | [**object**](.md)| Интернационализированное доменное имя. | [optional] 
 **linked_ip** | [**object**](.md)| Привязанный к домену IP-адрес. | [optional] 
 **order** | [**object**](.md)| Порядок доменов. | [optional] 
 **sort** | [**object**](.md)| Сортировка доменов. | [optional] 

### Return type

[**GetDomains200Response**](GetDomains200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;domains&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tld**
> GetTLD200Response get_tld(tld_id)

Получить информацию о доменной зоне по ID

Чтобы получить информацию о доменной зоне по ID, отправьте запрос GET на `/api/v1/tlds/{tld_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_tld200_response import GetTLD200Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    tld_id = 123 # object | ID доменной зоны.

    try:
        # Получить информацию о доменной зоне по ID
        api_response = api_instance.get_tld(tld_id)
        print("The response of DomainsApi->get_tld:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_tld: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tld_id** | [**object**](.md)| ID доменной зоны. | 

### Return type

[**GetTLD200Response**](GetTLD200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;top_level_domain&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tlds**
> GetTLDs200Response get_tlds(is_published=is_published, is_registered=is_registered)

Получить информацию о доменных зонах

Чтобы получить информацию о доменных зонах, отправьте запрос GET на `/api/v1/tlds`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_tlds200_response import GetTLDs200Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    is_published = true # object | Это логическое значение, которое показывает, опубликована ли доменная зона. (optional)
    is_registered = true # object | Это логическое значение, которое показывает, зарегистрирована ли доменная зона. (optional)

    try:
        # Получить информацию о доменных зонах
        api_response = api_instance.get_tlds(is_published=is_published, is_registered=is_registered)
        print("The response of DomainsApi->get_tlds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->get_tlds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_published** | [**object**](.md)| Это логическое значение, которое показывает, опубликована ли доменная зона. | [optional] 
 **is_registered** | [**object**](.md)| Это логическое значение, которое показывает, зарегистрирована ли доменная зона. | [optional] 

### Return type

[**GetTLDs200Response**](GetTLDs200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;top_level_domains&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_auto_prolongation**
> UpdateDomainAutoProlongation200Response update_domain_auto_prolongation(fqdn, update_domain)

Включение/выключение автопродления домена

Чтобы включить/выключить автопродление домена, отправьте запрос PATCH на `/api/v1/domains/{fqdn}`, передав в теле запроса параметр `is_autoprolong_enabled`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.update_domain import UpdateDomain
from timeweb_cloud_api.models.update_domain_auto_prolongation200_response import UpdateDomainAutoProlongation200Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена.
    update_domain = timeweb_cloud_api.UpdateDomain() # UpdateDomain | 

    try:
        # Включение/выключение автопродления домена
        api_response = api_instance.update_domain_auto_prolongation(fqdn, update_domain)
        print("The response of DomainsApi->update_domain_auto_prolongation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain_auto_prolongation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена. | 
 **update_domain** | [**UpdateDomain**](UpdateDomain.md)|  | 

### Return type

[**UpdateDomainAutoProlongation200Response**](UpdateDomainAutoProlongation200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;domain&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_dns_record**
> CreateDomainDNSRecord201Response update_domain_dns_record(fqdn, record_id, create_dns)

Обновить информацию о DNS-записи домена или поддомена

Чтобы обновить информацию о DNS-записи для домена или поддомена, отправьте запрос PATCH на `/api/v1/domains/{fqdn}/dns-records/{record_id}`, задав необходимые атрибуты.  DNS-запись будет обновлена с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией об добавленной DNS-записи.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_dns import CreateDns
from timeweb_cloud_api.models.create_domain_dns_record201_response import CreateDomainDNSRecord201Response
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена или поддомена.
    record_id = 123 # object | ID DNS-записи домена или поддомена.
    create_dns = timeweb_cloud_api.CreateDns() # CreateDns | 

    try:
        # Обновить информацию о DNS-записи домена или поддомена
        api_response = api_instance.update_domain_dns_record(fqdn, record_id, create_dns)
        print("The response of DomainsApi->update_domain_dns_record:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain_dns_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена или поддомена. | 
 **record_id** | [**object**](.md)| ID DNS-записи домена или поддомена. | 
 **create_dns** | [**CreateDns**](CreateDns.md)|  | 

### Return type

[**CreateDomainDNSRecord201Response**](CreateDomainDNSRecord201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;dns_record&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_name_servers**
> GetDomainNameServers200Response update_domain_name_servers(fqdn, update_domain_name_servers)

Изменение name-серверов домена

Чтобы изменить name-серверы домена, отправьте запрос PUT на `/api/v1/domains/{fqdn}/name-servers`, задав необходимые атрибуты.  Name-серверы будут изменены с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о name-серверах домена.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_domain_name_servers200_response import GetDomainNameServers200Response
from timeweb_cloud_api.models.update_domain_name_servers import UpdateDomainNameServers
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    fqdn = somedomain.ru # object | Полное имя домена.
    update_domain_name_servers = timeweb_cloud_api.UpdateDomainNameServers() # UpdateDomainNameServers | 

    try:
        # Изменение name-серверов домена
        api_response = api_instance.update_domain_name_servers(fqdn, update_domain_name_servers)
        print("The response of DomainsApi->update_domain_name_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain_name_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | [**object**](.md)| Полное имя домена. | 
 **update_domain_name_servers** | [**UpdateDomainNameServers**](UpdateDomainNameServers.md)|  | 

### Return type

[**GetDomainNameServers200Response**](GetDomainNameServers200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;name_servers&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_request**
> CreateDomainRequest201Response update_domain_request(request_id, use)

Оплата/обновление заявки на регистрацию/продление/трансфер домена

Чтобы оплатить/обновить заявку на регистрацию/продление/трансфер домена, отправьте запрос PATCH на `/api/v1/domains-requests/{request_id}`, задав необходимые атрибуты.  Заявка будет обновлена с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о обновленной заявке.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_domain_request201_response import CreateDomainRequest201Response
from timeweb_cloud_api.models.use import Use
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
    api_instance = timeweb_cloud_api.DomainsApi(api_client)
    request_id = 123 # object | ID заявки на регистрацию/продление/трансфер домена.
    use = timeweb_cloud_api.Use() # Use | 

    try:
        # Оплата/обновление заявки на регистрацию/продление/трансфер домена
        api_response = api_instance.update_domain_request(request_id, use)
        print("The response of DomainsApi->update_domain_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DomainsApi->update_domain_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | [**object**](.md)| ID заявки на регистрацию/продление/трансфер домена. | 
 **use** | [**Use**](Use.md)|  | 

### Return type

[**CreateDomainRequest201Response**](CreateDomainRequest201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;request&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

