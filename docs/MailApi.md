# timeweb_cloud_api.MailApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_domain_mailbox**](MailApi.md#create_domain_mailbox) | **POST** /api/v1/mail/domains/{domain} | Создание почтового ящика
[**create_multiple_domain_mailboxes**](MailApi.md#create_multiple_domain_mailboxes) | **POST** /api/v1/mail/domains/{domain}/batch | Множественное создание почтовых ящиков
[**delete_mailbox**](MailApi.md#delete_mailbox) | **DELETE** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Удаление почтового ящика
[**get_domain_mail_info**](MailApi.md#get_domain_mail_info) | **GET** /api/v1/mail/domains/{domain}/info | Получение почтовой информации о домене
[**get_domain_mailboxes**](MailApi.md#get_domain_mailboxes) | **GET** /api/v1/mail/domains/{domain} | Получение списка почтовых ящиков домена
[**get_mail_quota**](MailApi.md#get_mail_quota) | **GET** /api/v1/mail/quota | Получение квоты почты аккаунта
[**get_mailbox**](MailApi.md#get_mailbox) | **GET** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Получение почтового ящика
[**get_mailboxes**](MailApi.md#get_mailboxes) | **GET** /api/v1/mail | Получение списка почтовых ящиков аккаунта
[**update_domain_mail_info**](MailApi.md#update_domain_mail_info) | **PATCH** /api/v1/mail/domains/{domain}/info | Изменение почтовой информации о домене
[**update_mail_quota**](MailApi.md#update_mail_quota) | **PATCH** /api/v1/mail/quota | Изменение квоты почты аккаунта
[**update_mailbox**](MailApi.md#update_mailbox) | **PATCH** /api/v1/mail/domains/{domain}/mailboxes/{mailbox} | Изменение почтового ящика


# **create_domain_mailbox**
> CreateDomainMailbox201Response create_domain_mailbox(domain, create_domain_mailbox_request)

Создание почтового ящика

Чтобы создать почтовый ящик, отправьте POST-запрос на `/api/v1/mail/domains/{domain}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_domain_mailbox201_response import CreateDomainMailbox201Response
from timeweb_cloud_api.models.create_domain_mailbox_request import CreateDomainMailboxRequest
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
    api_instance = timeweb_cloud_api.MailApi(api_client)
    domain = somedomain.ru # object | Полное имя домена
    create_domain_mailbox_request = timeweb_cloud_api.CreateDomainMailboxRequest() # CreateDomainMailboxRequest | 

    try:
        # Создание почтового ящика
        api_response = api_instance.create_domain_mailbox(domain, create_domain_mailbox_request)
        print("The response of MailApi->create_domain_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->create_domain_mailbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**object**](.md)| Полное имя домена | 
 **create_domain_mailbox_request** | [**CreateDomainMailboxRequest**](CreateDomainMailboxRequest.md)|  | 

### Return type

[**CreateDomainMailbox201Response**](CreateDomainMailbox201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON c ключом &#x60;mailbox&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_multiple_domain_mailboxes**
> CreateMultipleDomainMailboxes201Response create_multiple_domain_mailboxes(domain, create_multiple_domain_mailboxes_request)

Множественное создание почтовых ящиков

Чтобы создать почтовый ящики, отправьте POST-запрос на `/api/v1/mail/domains/{domain}/batch`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_multiple_domain_mailboxes201_response import CreateMultipleDomainMailboxes201Response
from timeweb_cloud_api.models.create_multiple_domain_mailboxes_request import CreateMultipleDomainMailboxesRequest
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
    api_instance = timeweb_cloud_api.MailApi(api_client)
    domain = somedomain.ru # object | Полное имя домена
    create_multiple_domain_mailboxes_request = timeweb_cloud_api.CreateMultipleDomainMailboxesRequest() # CreateMultipleDomainMailboxesRequest | 

    try:
        # Множественное создание почтовых ящиков
        api_response = api_instance.create_multiple_domain_mailboxes(domain, create_multiple_domain_mailboxes_request)
        print("The response of MailApi->create_multiple_domain_mailboxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->create_multiple_domain_mailboxes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**object**](.md)| Полное имя домена | 
 **create_multiple_domain_mailboxes_request** | [**CreateMultipleDomainMailboxesRequest**](CreateMultipleDomainMailboxesRequest.md)|  | 

### Return type

[**CreateMultipleDomainMailboxes201Response**](CreateMultipleDomainMailboxes201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON c ключом &#x60;mailboxes&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mailbox**
> delete_mailbox(domain, mailbox)

Удаление почтового ящика

Чтобы удалить почтовый ящик, отправьте DELETE-запрос на `/api/v1/mail/domains/{domain}/mailboxes/{mailbox}`.

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
    api_instance = timeweb_cloud_api.MailApi(api_client)
    domain = somedomain.ru # object | Полное имя домена
    mailbox = mailbox # object | Название почтового ящика

    try:
        # Удаление почтового ящика
        api_instance.delete_mailbox(domain, mailbox)
    except Exception as e:
        print("Exception when calling MailApi->delete_mailbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**object**](.md)| Полное имя домена | 
 **mailbox** | [**object**](.md)| Название почтового ящика | 

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
**204** | Успешное удаление почтового ящика |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_mail_info**
> GetDomainMailInfo200Response get_domain_mail_info(domain)

Получение почтовой информации о домене

Чтобы получить почтовую информацию о домене, отправьте GET-запрос на `/api/v1/mail/domains/{domain}/info`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_domain_mail_info200_response import GetDomainMailInfo200Response
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
    api_instance = timeweb_cloud_api.MailApi(api_client)
    domain = somedomain.ru # object | Полное имя домена

    try:
        # Получение почтовой информации о домене
        api_response = api_instance.get_domain_mail_info(domain)
        print("The response of MailApi->get_domain_mail_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->get_domain_mail_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**object**](.md)| Полное имя домена | 

### Return type

[**GetDomainMailInfo200Response**](GetDomainMailInfo200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;domain_info&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_mailboxes**
> GetMailboxes200Response get_domain_mailboxes(domain, limit=limit, offset=offset, search=search)

Получение списка почтовых ящиков домена

Чтобы получить список почтовых ящиков домена, отправьте GET-запрос на `/api/v1/mail/domains/{domain}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_mailboxes200_response import GetMailboxes200Response
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
    api_instance = timeweb_cloud_api.MailApi(api_client)
    domain = somedomain.ru # object | Полное имя домена
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)
    search = None # object | Поиск почтового ящика по названию (optional)

    try:
        # Получение списка почтовых ящиков домена
        api_response = api_instance.get_domain_mailboxes(domain, limit=limit, offset=offset, search=search)
        print("The response of MailApi->get_domain_mailboxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->get_domain_mailboxes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**object**](.md)| Полное имя домена | 
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 
 **search** | [**object**](.md)| Поиск почтового ящика по названию | [optional] 

### Return type

[**GetMailboxes200Response**](GetMailboxes200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;mailboxes&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mail_quota**
> GetMailQuota200Response get_mail_quota()

Получение квоты почты аккаунта

Чтобы получить квоту почты аккаунта, отправьте GET-запрос на `/api/v1/mail/quota`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_mail_quota200_response import GetMailQuota200Response
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
    api_instance = timeweb_cloud_api.MailApi(api_client)

    try:
        # Получение квоты почты аккаунта
        api_response = api_instance.get_mail_quota()
        print("The response of MailApi->get_mail_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->get_mail_quota: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetMailQuota200Response**](GetMailQuota200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;quota&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mailbox**
> CreateDomainMailbox201Response get_mailbox(domain, mailbox)

Получение почтового ящика

Чтобы получить почтовый ящик, отправьте GET-запрос на `/api/v1/mail/domains/{domain}/mailboxes/{mailbox}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_domain_mailbox201_response import CreateDomainMailbox201Response
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
    api_instance = timeweb_cloud_api.MailApi(api_client)
    domain = somedomain.ru # object | Полное имя домена
    mailbox = mailbox # object | Название почтового ящика

    try:
        # Получение почтового ящика
        api_response = api_instance.get_mailbox(domain, mailbox)
        print("The response of MailApi->get_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->get_mailbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**object**](.md)| Полное имя домена | 
 **mailbox** | [**object**](.md)| Название почтового ящика | 

### Return type

[**CreateDomainMailbox201Response**](CreateDomainMailbox201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;mailbox&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mailboxes**
> GetMailboxes200Response get_mailboxes(limit=limit, offset=offset, search=search)

Получение списка почтовых ящиков аккаунта

Чтобы получить список почтовых ящиков аккаунта, отправьте GET-запрос на `/api/v1/mail`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_mailboxes200_response import GetMailboxes200Response
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
    api_instance = timeweb_cloud_api.MailApi(api_client)
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)
    search = None # object | Поиск почтового ящика по названию (optional)

    try:
        # Получение списка почтовых ящиков аккаунта
        api_response = api_instance.get_mailboxes(limit=limit, offset=offset, search=search)
        print("The response of MailApi->get_mailboxes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->get_mailboxes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 
 **search** | [**object**](.md)| Поиск почтового ящика по названию | [optional] 

### Return type

[**GetMailboxes200Response**](GetMailboxes200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;mailboxes&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_domain_mail_info**
> GetDomainMailInfo200Response update_domain_mail_info(domain, update_domain_mail_info_request)

Изменение почтовой информации о домене

Чтобы изменить почтовую информацию о домене, отправьте PATCH-запрос на `/api/v1/mail/domains/{domain}/info`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_domain_mail_info200_response import GetDomainMailInfo200Response
from timeweb_cloud_api.models.update_domain_mail_info_request import UpdateDomainMailInfoRequest
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
    api_instance = timeweb_cloud_api.MailApi(api_client)
    domain = somedomain.ru # object | Полное имя домена
    update_domain_mail_info_request = timeweb_cloud_api.UpdateDomainMailInfoRequest() # UpdateDomainMailInfoRequest | 

    try:
        # Изменение почтовой информации о домене
        api_response = api_instance.update_domain_mail_info(domain, update_domain_mail_info_request)
        print("The response of MailApi->update_domain_mail_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->update_domain_mail_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**object**](.md)| Полное имя домена | 
 **update_domain_mail_info_request** | [**UpdateDomainMailInfoRequest**](UpdateDomainMailInfoRequest.md)|  | 

### Return type

[**GetDomainMailInfo200Response**](GetDomainMailInfo200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;domain_info&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mail_quota**
> GetMailQuota200Response update_mail_quota(update_mail_quota_request)

Изменение квоты почты аккаунта

Чтобы получить инфомацию по квоте почты аккаунта, отправьте GET-запрос на `/api/v1/mail/quota`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_mail_quota200_response import GetMailQuota200Response
from timeweb_cloud_api.models.update_mail_quota_request import UpdateMailQuotaRequest
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
    api_instance = timeweb_cloud_api.MailApi(api_client)
    update_mail_quota_request = timeweb_cloud_api.UpdateMailQuotaRequest() # UpdateMailQuotaRequest | 

    try:
        # Изменение квоты почты аккаунта
        api_response = api_instance.update_mail_quota(update_mail_quota_request)
        print("The response of MailApi->update_mail_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->update_mail_quota: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_mail_quota_request** | [**UpdateMailQuotaRequest**](UpdateMailQuotaRequest.md)|  | 

### Return type

[**GetMailQuota200Response**](GetMailQuota200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;quota&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mailbox**
> CreateDomainMailbox201Response update_mailbox(domain, mailbox, update_mailbox)

Изменение почтового ящика

Чтобы изменить почтовый ящик, отправьте PATCH-запрос на `/api/v1/mail/domains/{domain}/mailboxes/{mailbox}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_domain_mailbox201_response import CreateDomainMailbox201Response
from timeweb_cloud_api.models.update_mailbox import UpdateMailbox
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
    api_instance = timeweb_cloud_api.MailApi(api_client)
    domain = somedomain.ru # object | Полное имя домена
    mailbox = mailbox # object | Название почтового ящика
    update_mailbox = timeweb_cloud_api.UpdateMailbox() # UpdateMailbox | 

    try:
        # Изменение почтового ящика
        api_response = api_instance.update_mailbox(domain, mailbox, update_mailbox)
        print("The response of MailApi->update_mailbox:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MailApi->update_mailbox: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain** | [**object**](.md)| Полное имя домена | 
 **mailbox** | [**object**](.md)| Название почтового ящика | 
 **update_mailbox** | [**UpdateMailbox**](UpdateMailbox.md)|  | 

### Return type

[**CreateDomainMailbox201Response**](CreateDomainMailbox201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;mailbox&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

