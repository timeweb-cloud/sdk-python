# timeweb_cloud_api.CDNApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cdn_certificate**](CDNApi.md#add_cdn_certificate) | **POST** /api/v1/cdn/certificates | Загрузка собственного сертификата CDN
[**archive_cdn_certificate_task**](CDNApi.md#archive_cdn_certificate_task) | **POST** /api/v1/cdn/certificates/tasks/{task_id}/archive | Архивация задачи на выпуск сертификата
[**clear_cdn_resource_cache**](CDNApi.md#clear_cdn_resource_cache) | **POST** /api/v1/cdn/http-resources/{resource_id}/clear-cache | Очистка кэша CDN-ресурса
[**create_cdn_resource**](CDNApi.md#create_cdn_resource) | **POST** /api/v1/cdn/http-resources | Создание CDN-ресурса
[**delete_cdn_certificate**](CDNApi.md#delete_cdn_certificate) | **DELETE** /api/v1/cdn/certificates/{certificate_id} | Удаление сертификата CDN
[**delete_cdn_resource**](CDNApi.md#delete_cdn_resource) | **DELETE** /api/v1/cdn/http-resources/{resource_id} | Удаление CDN-ресурса
[**get_cdn_certificate_tasks**](CDNApi.md#get_cdn_certificate_tasks) | **GET** /api/v1/cdn/certificates/tasks | Получение списка задач на выпуск сертификатов
[**get_cdn_certificates**](CDNApi.md#get_cdn_certificates) | **GET** /api/v1/cdn/certificates | Получение списка сертификатов CDN
[**get_cdn_origin_nodes**](CDNApi.md#get_cdn_origin_nodes) | **GET** /api/v1/cdn/nodes/origin | Получение списка подсетей узлов CDN
[**get_cdn_presets**](CDNApi.md#get_cdn_presets) | **GET** /api/v1/cdn/presets | Получение списка тарифов CDN
[**get_cdn_resource**](CDNApi.md#get_cdn_resource) | **GET** /api/v1/cdn/http-resources/{resource_id} | Получение CDN-ресурса
[**get_cdn_resource_configuration**](CDNApi.md#get_cdn_resource_configuration) | **GET** /api/v1/cdn/http-resources/{resource_id}/configuration | Получение конфигурации CDN-ресурса
[**get_cdn_resource_nodes**](CDNApi.md#get_cdn_resource_nodes) | **GET** /api/v1/cdn/nodes/http-resources/{resource_id} | Получение списка раздающих узлов CDN-ресурса
[**get_cdn_resource_statistics**](CDNApi.md#get_cdn_resource_statistics) | **GET** /api/v1/cdn/http-resources/{resource_id}/statistics | Получение статистики CDN-ресурса
[**get_cdn_resources**](CDNApi.md#get_cdn_resources) | **GET** /api/v1/cdn/http-resources | Получение списка CDN-ресурсов
[**issue_cdn_certificate**](CDNApi.md#issue_cdn_certificate) | **POST** /api/v1/cdn/certificates/issue | Выпуск сертификата Let&#39;s Encrypt для CDN-ресурса
[**preload_cdn_resource_cache**](CDNApi.md#preload_cdn_resource_cache) | **POST** /api/v1/cdn/http-resources/{resource_id}/preload-cache | Предварительная загрузка кэша CDN-ресурса
[**resume_cdn_resource**](CDNApi.md#resume_cdn_resource) | **POST** /api/v1/cdn/http-resources/{resource_id}/resume | Возобновление раздачи CDN-ресурса
[**suspend_cdn_resource**](CDNApi.md#suspend_cdn_resource) | **POST** /api/v1/cdn/http-resources/{resource_id}/suspend | Приостановка раздачи CDN-ресурса
[**update_cdn_resource**](CDNApi.md#update_cdn_resource) | **PATCH** /api/v1/cdn/http-resources/{resource_id} | Изменение CDN-ресурса


# **add_cdn_certificate**
> add_cdn_certificate(add_certificate)

Загрузка собственного сертификата CDN

Чтобы загрузить собственный SSL-сертификат, отправьте POST-запрос на `/api/v1/cdn/certificates`.  После загрузки сертификат появится в списке `/api/v1/cdn/certificates` — привязать его к ресурсу можно, передав его ID в поле `config.security.certificate_id` PATCH-запроса на `/api/v1/cdn/http-resources/{resource_id}`.  Если сертификат или приватный ключ не проходят проверку — например, истек срок действия или ключ не соответствует сертификату — вернется ошибка `422`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_certificate import AddCertificate
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    add_certificate = timeweb_cloud_api.AddCertificate() # AddCertificate | 

    try:
        # Загрузка собственного сертификата CDN
        api_instance.add_cdn_certificate(add_certificate)
    except Exception as e:
        print("Exception when calling CDNApi->add_cdn_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_certificate** | [**AddCertificate**](AddCertificate.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Сертификат успешно добавлен |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**422** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **archive_cdn_certificate_task**
> archive_cdn_certificate_task(task_id)

Архивация задачи на выпуск сертификата

Чтобы убрать из списка задачу на выпуск сертификата, отправьте POST-запрос на `/api/v1/cdn/certificates/tasks/{task_id}/archive`.

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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    task_id = 42 # object | ID задачи на выпуск сертификата

    try:
        # Архивация задачи на выпуск сертификата
        api_instance.archive_cdn_certificate_task(task_id)
    except Exception as e:
        print("Exception when calling CDNApi->archive_cdn_certificate_task: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | [**object**](.md)| ID задачи на выпуск сертификата | 

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
**204** | Задача на выпуск сертификата успешно архивирована |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_cdn_resource_cache**
> clear_cdn_resource_cache(resource_id, clear_cache)

Очистка кэша CDN-ресурса

Чтобы очистить кэш на узлах CDN, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/clear-cache`.  При `purge_type` = `full` очищается весь кэш ресурса, при `purge_type` = `partial` — только файлы из списка `paths`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.clear_cache import ClearCache
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | ID CDN-ресурса
    clear_cache = timeweb_cloud_api.ClearCache() # ClearCache | 

    try:
        # Очистка кэша CDN-ресурса
        api_instance.clear_cdn_resource_cache(resource_id, clear_cache)
    except Exception as e:
        print("Exception when calling CDNApi->clear_cdn_resource_cache: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| ID CDN-ресурса | 
 **clear_cache** | [**ClearCache**](ClearCache.md)|  | 

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
**204** | Запрос на очистку кэша принят |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cdn_resource**
> CreateCdnResource201Response create_cdn_resource(create_http_resource)

Создание CDN-ресурса

Чтобы создать CDN-ресурс, отправьте POST-запрос на `/api/v1/cdn/http-resources`.  Источник контента задается ровно одним из полей: `storage_id` для S3-хранилища или `server` для произвольного origin-сервера. Если ни одно из них не передано, вернется ошибка `400`.  Сразу после создания ресурсу выдается технический домен `cdn_domain`, а сам ресурс какое-то время находится в статусе `processing`, пока конфигурация применяется на узлах CDN.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_cdn_resource201_response import CreateCdnResource201Response
from timeweb_cloud_api.models.create_http_resource import CreateHttpResource
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    create_http_resource = timeweb_cloud_api.CreateHttpResource() # CreateHttpResource | 

    try:
        # Создание CDN-ресурса
        api_response = api_instance.create_cdn_resource(create_http_resource)
        print("The response of CDNApi->create_cdn_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->create_cdn_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_http_resource** | [**CreateHttpResource**](CreateHttpResource.md)|  | 

### Return type

[**CreateCdnResource201Response**](CreateCdnResource201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;http_resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cdn_certificate**
> delete_cdn_certificate(certificate_id)

Удаление сертификата CDN

Чтобы удалить SSL-сертификат, отправьте DELETE-запрос на `/api/v1/cdn/certificates/{certificate_id}`.  Если сертификат привязан к CDN-ресурсу, вернется ошибка `409` — сначала отвяжите его, передав `config.security.certificate_id` = `null` в PATCH-запросе на `/api/v1/cdn/http-resources/{resource_id}`.

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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    certificate_id = 5678 # object | ID сертификата

    try:
        # Удаление сертификата CDN
        api_instance.delete_cdn_certificate(certificate_id)
    except Exception as e:
        print("Exception when calling CDNApi->delete_cdn_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | [**object**](.md)| ID сертификата | 

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
**204** | Сертификат успешно удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cdn_resource**
> delete_cdn_resource(resource_id)

Удаление CDN-ресурса

Чтобы удалить CDN-ресурс, отправьте DELETE-запрос на `/api/v1/cdn/http-resources/{resource_id}`. Вместе с ресурсом освобождается его технический домен, а привязанный сертификат отвязывается.

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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | ID CDN-ресурса

    try:
        # Удаление CDN-ресурса
        api_instance.delete_cdn_resource(resource_id)
    except Exception as e:
        print("Exception when calling CDNApi->delete_cdn_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| ID CDN-ресурса | 

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
**204** | CDN-ресурс успешно удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_certificate_tasks**
> GetCdnCertificateTasks200Response get_cdn_certificate_tasks(resource_id=resource_id)

Получение списка задач на выпуск сертификатов

Чтобы получить список задач на выпуск сертификатов Let's Encrypt, отправьте GET-запрос на `/api/v1/cdn/certificates/tasks`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_cdn_certificate_tasks200_response import GetCdnCertificateTasks200Response
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | Оставить в выдаче только задачи указанного CDN-ресурса. (optional)

    try:
        # Получение списка задач на выпуск сертификатов
        api_response = api_instance.get_cdn_certificate_tasks(resource_id=resource_id)
        print("The response of CDNApi->get_cdn_certificate_tasks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->get_cdn_certificate_tasks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| Оставить в выдаче только задачи указанного CDN-ресурса. | [optional] 

### Return type

[**GetCdnCertificateTasks200Response**](GetCdnCertificateTasks200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;certificate_tasks&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_certificates**
> GetCdnCertificates200Response get_cdn_certificates(resource_id=resource_id)

Получение списка сертификатов CDN

Чтобы получить список SSL-сертификатов, доступных для доменов CDN-ресурсов, отправьте GET-запрос на `/api/v1/cdn/certificates`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_cdn_certificates200_response import GetCdnCertificates200Response
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | Оставить в выдаче только сертификаты, подходящие для доменов указанного CDN-ресурса. (optional)

    try:
        # Получение списка сертификатов CDN
        api_response = api_instance.get_cdn_certificates(resource_id=resource_id)
        print("The response of CDNApi->get_cdn_certificates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->get_cdn_certificates: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| Оставить в выдаче только сертификаты, подходящие для доменов указанного CDN-ресурса. | [optional] 

### Return type

[**GetCdnCertificates200Response**](GetCdnCertificates200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;certificates&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_origin_nodes**
> GetCdnOriginNodes200Response get_cdn_origin_nodes(with_extra_zones=with_extra_zones)

Получение списка подсетей узлов CDN

Чтобы получить список IP-адресов и подсетей, с которых узлы CDN обращаются к источнику контента, отправьте GET-запрос на `/api/v1/cdn/nodes/origin`. Этот список удобно использовать, чтобы разрешить доступ к origin-серверу только для узлов CDN.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_cdn_origin_nodes200_response import GetCdnOriginNodes200Response
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    with_extra_zones = true # object | Добавить в выдачу узлы дополнительных зон раздачи. (optional)

    try:
        # Получение списка подсетей узлов CDN
        api_response = api_instance.get_cdn_origin_nodes(with_extra_zones=with_extra_zones)
        print("The response of CDNApi->get_cdn_origin_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->get_cdn_origin_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **with_extra_zones** | [**object**](.md)| Добавить в выдачу узлы дополнительных зон раздачи. | [optional] 

### Return type

[**GetCdnOriginNodes200Response**](GetCdnOriginNodes200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;origin_nodes&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_presets**
> GetCdnPresets200Response get_cdn_presets()

Получение списка тарифов CDN

Чтобы получить список доступных тарифов CDN, отправьте GET-запрос на `/api/v1/cdn/presets`. ID тарифа из этого списка указывается в поле `preset_id` при создании и изменении ресурса.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_cdn_presets200_response import GetCdnPresets200Response
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)

    try:
        # Получение списка тарифов CDN
        api_response = api_instance.get_cdn_presets()
        print("The response of CDNApi->get_cdn_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->get_cdn_presets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCdnPresets200Response**](GetCdnPresets200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;http_resource_presets&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_resource**
> CreateCdnResource201Response get_cdn_resource(resource_id)

Получение CDN-ресурса

Чтобы получить информацию об отдельном CDN-ресурсе, отправьте GET-запрос на `/api/v1/cdn/http-resources/{resource_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_cdn_resource201_response import CreateCdnResource201Response
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | ID CDN-ресурса

    try:
        # Получение CDN-ресурса
        api_response = api_instance.get_cdn_resource(resource_id)
        print("The response of CDNApi->get_cdn_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->get_cdn_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| ID CDN-ресурса | 

### Return type

[**CreateCdnResource201Response**](CreateCdnResource201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;http_resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_resource_configuration**
> GetCdnResourceConfiguration200Response get_cdn_resource_configuration(resource_id)

Получение конфигурации CDN-ресурса

Чтобы получить текущую конфигурацию CDN-ресурса, отправьте GET-запрос на `/api/v1/cdn/http-resources/{resource_id}/configuration`.  Изменить конфигурацию можно в поле `config` PATCH-запроса на `/api/v1/cdn/http-resources/{resource_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_cdn_resource_configuration200_response import GetCdnResourceConfiguration200Response
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | ID CDN-ресурса

    try:
        # Получение конфигурации CDN-ресурса
        api_response = api_instance.get_cdn_resource_configuration(resource_id)
        print("The response of CDNApi->get_cdn_resource_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->get_cdn_resource_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| ID CDN-ресурса | 

### Return type

[**GetCdnResourceConfiguration200Response**](GetCdnResourceConfiguration200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;http_resource_configuration&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_resource_nodes**
> GetCdnResourceNodes200Response get_cdn_resource_nodes(resource_id, with_extra_zones=with_extra_zones, country=country)

Получение списка раздающих узлов CDN-ресурса

Чтобы получить список узлов, которые раздают контент доменов ресурса, отправьте GET-запрос на `/api/v1/cdn/nodes/http-resources/{resource_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_cdn_resource_nodes200_response import GetCdnResourceNodes200Response
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | ID CDN-ресурса
    with_extra_zones = true # object | Добавить в выдачу узлы дополнительных зон раздачи. (optional)
    country = ["RU","KZ"] # object | Оставить в выдаче только основные зоны раздачи в указанных странах. Коды стран в формате ISO 3166-1 alpha-2. (optional)

    try:
        # Получение списка раздающих узлов CDN-ресурса
        api_response = api_instance.get_cdn_resource_nodes(resource_id, with_extra_zones=with_extra_zones, country=country)
        print("The response of CDNApi->get_cdn_resource_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->get_cdn_resource_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| ID CDN-ресурса | 
 **with_extra_zones** | [**object**](.md)| Добавить в выдачу узлы дополнительных зон раздачи. | [optional] 
 **country** | [**object**](.md)| Оставить в выдаче только основные зоны раздачи в указанных странах. Коды стран в формате ISO 3166-1 alpha-2. | [optional] 

### Return type

[**GetCdnResourceNodes200Response**](GetCdnResourceNodes200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;user_nodes&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_resource_statistics**
> GetCdnResourceStatistics200Response get_cdn_resource_statistics(resource_id, var_from=var_from, to=to)

Получение статистики CDN-ресурса

Чтобы получить статистику трафика и запросов CDN-ресурса, отправьте GET-запрос на `/api/v1/cdn/http-resources/{resource_id}/statistics`.  Данные возвращаются с разбивкой по часовым интервалам. Если период не указан, вернется статистика за последние 6 часов.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_cdn_resource_statistics200_response import GetCdnResourceStatistics200Response
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | ID CDN-ресурса
    var_from = 2026-04-16T00:00:00Z # object | Начало периода в формате ISO 8601. По умолчанию — 6 часов назад. (optional)
    to = 2026-04-16T23:59:59Z # object | Конец периода в формате ISO 8601. По умолчанию — текущий момент. Должен быть не раньше `from`. (optional)

    try:
        # Получение статистики CDN-ресурса
        api_response = api_instance.get_cdn_resource_statistics(resource_id, var_from=var_from, to=to)
        print("The response of CDNApi->get_cdn_resource_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->get_cdn_resource_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| ID CDN-ресурса | 
 **var_from** | [**object**](.md)| Начало периода в формате ISO 8601. По умолчанию — 6 часов назад. | [optional] 
 **to** | [**object**](.md)| Конец периода в формате ISO 8601. По умолчанию — текущий момент. Должен быть не раньше &#x60;from&#x60;. | [optional] 

### Return type

[**GetCdnResourceStatistics200Response**](GetCdnResourceStatistics200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;statistics&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cdn_resources**
> GetCdnResources200Response get_cdn_resources(bucket_id=bucket_id)

Получение списка CDN-ресурсов

Чтобы получить список CDN-ресурсов, отправьте GET-запрос на `/api/v1/cdn/http-resources`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_cdn_resources200_response import GetCdnResources200Response
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    bucket_id = 4210 # object | Оставить в выдаче только ресурсы, источником контента которых является указанное S3-хранилище. (optional)

    try:
        # Получение списка CDN-ресурсов
        api_response = api_instance.get_cdn_resources(bucket_id=bucket_id)
        print("The response of CDNApi->get_cdn_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->get_cdn_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucket_id** | [**object**](.md)| Оставить в выдаче только ресурсы, источником контента которых является указанное S3-хранилище. | [optional] 

### Return type

[**GetCdnResources200Response**](GetCdnResources200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;http_resources&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_cdn_certificate**
> issue_cdn_certificate(issue_certificate)

Выпуск сертификата Let's Encrypt для CDN-ресурса

Чтобы выпустить бесплатный сертификат Let's Encrypt для доменов CDN-ресурса, отправьте POST-запрос на `/api/v1/cdn/certificates/issue`.  Выпуск выполняется асинхронно: в ответ возвращается код `202`, а следить за ходом выпуска можно по списку задач `/api/v1/cdn/certificates/tasks`. Готовый сертификат привязывается к ресурсу автоматически.  Перед выпуском убедитесь, что домены ресурса указывают на его технический домен `cdn_domain` — иначе вернется ошибка `422`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.issue_certificate import IssueCertificate
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    issue_certificate = timeweb_cloud_api.IssueCertificate() # IssueCertificate | 

    try:
        # Выпуск сертификата Let's Encrypt для CDN-ресурса
        api_instance.issue_cdn_certificate(issue_certificate)
    except Exception as e:
        print("Exception when calling CDNApi->issue_cdn_certificate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_certificate** | [**IssueCertificate**](IssueCertificate.md)|  | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Запрос на выпуск сертификата принят |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**422** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preload_cdn_resource_cache**
> preload_cdn_resource_cache(resource_id, preload_cache)

Предварительная загрузка кэша CDN-ресурса

Чтобы заранее загрузить файлы в кэш узлов CDN, не дожидаясь первого обращения пользователей, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/preload-cache`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.preload_cache import PreloadCache
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | ID CDN-ресурса
    preload_cache = timeweb_cloud_api.PreloadCache() # PreloadCache | 

    try:
        # Предварительная загрузка кэша CDN-ресурса
        api_instance.preload_cdn_resource_cache(resource_id, preload_cache)
    except Exception as e:
        print("Exception when calling CDNApi->preload_cdn_resource_cache: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| ID CDN-ресурса | 
 **preload_cache** | [**PreloadCache**](PreloadCache.md)|  | 

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
**204** | Запрос на загрузку файлов в кэш принят |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resume_cdn_resource**
> CreateCdnResource201Response resume_cdn_resource(resource_id)

Возобновление раздачи CDN-ресурса

Чтобы возобновить раздачу контента после приостановки, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/resume`.  Если ресурс заблокирован, вернется ошибка `409`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_cdn_resource201_response import CreateCdnResource201Response
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | ID CDN-ресурса

    try:
        # Возобновление раздачи CDN-ресурса
        api_response = api_instance.resume_cdn_resource(resource_id)
        print("The response of CDNApi->resume_cdn_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->resume_cdn_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| ID CDN-ресурса | 

### Return type

[**CreateCdnResource201Response**](CreateCdnResource201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;http_resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_cdn_resource**
> CreateCdnResource201Response suspend_cdn_resource(resource_id)

Приостановка раздачи CDN-ресурса

Чтобы приостановить раздачу контента, отправьте POST-запрос на `/api/v1/cdn/http-resources/{resource_id}/suspend`. Ресурс перейдет в статус `stopped`, его настройки и домены сохранятся.  Если ресурс заблокирован, вернется ошибка `409`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_cdn_resource201_response import CreateCdnResource201Response
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | ID CDN-ресурса

    try:
        # Приостановка раздачи CDN-ресурса
        api_response = api_instance.suspend_cdn_resource(resource_id)
        print("The response of CDNApi->suspend_cdn_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->suspend_cdn_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| ID CDN-ресурса | 

### Return type

[**CreateCdnResource201Response**](CreateCdnResource201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;http_resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cdn_resource**
> CreateCdnResource201Response update_cdn_resource(resource_id, update_http_resource)

Изменение CDN-ресурса

Чтобы изменить CDN-ресурс, отправьте PATCH-запрос на `/api/v1/cdn/http-resources/{resource_id}`.  Передавайте только те поля, которые нужно изменить: переданные значения накладываются на текущую конфигурацию, а непереданные остаются без изменений. Чтобы сбросить настройку, передайте в соответствующем поле `null`.  Поля `storage_id` и `config.origin.servers` нельзя передавать вместе — источник контента может быть только один.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_cdn_resource201_response import CreateCdnResource201Response
from timeweb_cloud_api.models.update_http_resource import UpdateHttpResource
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
    api_instance = timeweb_cloud_api.CDNApi(api_client)
    resource_id = 1234 # object | ID CDN-ресурса
    update_http_resource = timeweb_cloud_api.UpdateHttpResource() # UpdateHttpResource | 

    try:
        # Изменение CDN-ресурса
        api_response = api_instance.update_cdn_resource(resource_id, update_http_resource)
        print("The response of CDNApi->update_cdn_resource:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CDNApi->update_cdn_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_id** | [**object**](.md)| ID CDN-ресурса | 
 **update_http_resource** | [**UpdateHttpResource**](UpdateHttpResource.md)|  | 

### Return type

[**CreateCdnResource201Response**](CreateCdnResource201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;http_resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

