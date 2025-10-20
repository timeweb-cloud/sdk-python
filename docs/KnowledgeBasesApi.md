# timeweb_cloud_api.KnowledgeBasesApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_additional_token_package_to_knowledgebase**](KnowledgeBasesApi.md#add_additional_token_package_to_knowledgebase) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/add-additional-token-package | Добавление дополнительного пакета токенов
[**create_knowledgebase**](KnowledgeBasesApi.md#create_knowledgebase) | **POST** /api/v1/cloud-ai/knowledge-bases | Создание базы знаний
[**delete_document**](KnowledgeBasesApi.md#delete_document) | **DELETE** /api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id} | Удаление документа из базы знаний
[**delete_knowledgebase**](KnowledgeBasesApi.md#delete_knowledgebase) | **DELETE** /api/v1/cloud-ai/knowledge-bases/{id} | Удаление базы знаний
[**download_document**](KnowledgeBasesApi.md#download_document) | **GET** /api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/download | Скачивание документа из базы знаний
[**get_knowledgebase**](KnowledgeBasesApi.md#get_knowledgebase) | **GET** /api/v1/cloud-ai/knowledge-bases/{id} | Получение базы знаний
[**get_knowledgebase_statistics**](KnowledgeBasesApi.md#get_knowledgebase_statistics) | **GET** /api/v1/cloud-ai/knowledge-bases/{id}/statistic | Получение статистики использования токенов базы знаний
[**get_knowledgebases**](KnowledgeBasesApi.md#get_knowledgebases) | **GET** /api/v1/cloud-ai/knowledge-bases | Получение списка баз знаний
[**link_knowledgebase_to_agent**](KnowledgeBasesApi.md#link_knowledgebase_to_agent) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id} | Привязка базы знаний к агенту
[**reindex_document**](KnowledgeBasesApi.md#reindex_document) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/reindex | Переиндексация документа
[**unlink_knowledgebase_from_agent**](KnowledgeBasesApi.md#unlink_knowledgebase_from_agent) | **DELETE** /api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id} | Отвязка базы знаний от агента
[**update_knowledgebase**](KnowledgeBasesApi.md#update_knowledgebase) | **PATCH** /api/v1/cloud-ai/knowledge-bases/{id} | Обновление базы знаний
[**upload_files_to_knowledgebase**](KnowledgeBasesApi.md#upload_files_to_knowledgebase) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/upload | Загрузка файлов в базу знаний


# **add_additional_token_package_to_knowledgebase**
> add_additional_token_package_to_knowledgebase(id, add_token_package=add_token_package)

Добавление дополнительного пакета токенов

Чтобы добавить дополнительный пакет токенов для базы знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/add-additional-token-package`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_token_package import AddTokenPackage
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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    id = 1 # object | ID базы знаний
    add_token_package = timeweb_cloud_api.AddTokenPackage() # AddTokenPackage |  (optional)

    try:
        # Добавление дополнительного пакета токенов
        api_instance.add_additional_token_package_to_knowledgebase(id, add_token_package=add_token_package)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->add_additional_token_package_to_knowledgebase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **add_token_package** | [**AddTokenPackage**](AddTokenPackage.md)|  | [optional] 

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
**204** | Дополнительный пакет токенов успешно добавлен |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_knowledgebase**
> CreateKnowledgebase201Response create_knowledgebase(create_knowledgebase)

Создание базы знаний

Чтобы создать базу знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases`, задав необходимые атрибуты.  База знаний будет создана с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданной базе знаний.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_knowledgebase import CreateKnowledgebase
from timeweb_cloud_api.models.create_knowledgebase201_response import CreateKnowledgebase201Response
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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    create_knowledgebase = timeweb_cloud_api.CreateKnowledgebase() # CreateKnowledgebase | 

    try:
        # Создание базы знаний
        api_response = api_instance.create_knowledgebase(create_knowledgebase)
        print("The response of KnowledgeBasesApi->create_knowledgebase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->create_knowledgebase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_knowledgebase** | [**CreateKnowledgebase**](CreateKnowledgebase.md)|  | 

### Return type

[**CreateKnowledgebase201Response**](CreateKnowledgebase201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;knowledgebase&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(id, document_id)

Удаление документа из базы знаний

Чтобы удалить документ из базы знаний, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}`.

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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    id = 1 # object | ID базы знаний
    document_id = 1 # object | ID документа

    try:
        # Удаление документа из базы знаний
        api_instance.delete_document(id, document_id)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->delete_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **document_id** | [**object**](.md)| ID документа | 

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
**204** | Документ успешно удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_knowledgebase**
> delete_knowledgebase(id)

Удаление базы знаний

Чтобы удалить базу знаний, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.

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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    id = 1 # object | ID базы знаний

    try:
        # Удаление базы знаний
        api_instance.delete_knowledgebase(id)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->delete_knowledgebase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 

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
**204** | База знаний успешно удалена |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_document**
> object download_document(id, document_id)

Скачивание документа из базы знаний

Чтобы скачать документ из базы знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/download`.

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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    id = 1 # object | ID базы знаний
    document_id = 1 # object | ID документа

    try:
        # Скачивание документа из базы знаний
        api_response = api_instance.download_document(id, document_id)
        print("The response of KnowledgeBasesApi->download_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->download_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **document_id** | [**object**](.md)| ID документа | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Файл документа |  * Content-Type - MIME тип файла <br>  * Content-Disposition - Attachment с именем файла <br>  * Content-Length - Размер файла в байтах <br>  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledgebase**
> CreateKnowledgebase201Response get_knowledgebase(id)

Получение базы знаний

Чтобы получить информацию о базе знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_knowledgebase201_response import CreateKnowledgebase201Response
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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    id = 1 # object | ID базы знаний

    try:
        # Получение базы знаний
        api_response = api_instance.get_knowledgebase(id)
        print("The response of KnowledgeBasesApi->get_knowledgebase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->get_knowledgebase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 

### Return type

[**CreateKnowledgebase201Response**](CreateKnowledgebase201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;knowledgebase&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledgebase_statistics**
> GetKnowledgebaseStatistics200Response get_knowledgebase_statistics(id, start_time=start_time, end_time=end_time, interval=interval)

Получение статистики использования токенов базы знаний

Чтобы получить статистику использования токенов базы знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/statistic`.  Можно указать временной диапазон и интервал агрегации.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_knowledgebase_statistics200_response import GetKnowledgebaseStatistics200Response
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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    id = 1 # object | ID базы знаний
    start_time = 2024-10-01T00:00:00.000Z # object | Начало временного диапазона (ISO 8601) (optional)
    end_time = 2024-10-16T23:59:59.999Z # object | Конец временного диапазона (ISO 8601) (optional)
    interval = 60 # object | Интервал в минутах (по умолчанию 60) (optional)

    try:
        # Получение статистики использования токенов базы знаний
        api_response = api_instance.get_knowledgebase_statistics(id, start_time=start_time, end_time=end_time, interval=interval)
        print("The response of KnowledgeBasesApi->get_knowledgebase_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->get_knowledgebase_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **start_time** | [**object**](.md)| Начало временного диапазона (ISO 8601) | [optional] 
 **end_time** | [**object**](.md)| Конец временного диапазона (ISO 8601) | [optional] 
 **interval** | [**object**](.md)| Интервал в минутах (по умолчанию 60) | [optional] 

### Return type

[**GetKnowledgebaseStatistics200Response**](GetKnowledgebaseStatistics200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;knowledgebase_statistics&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledgebases**
> GetKnowledgebases200Response get_knowledgebases()

Получение списка баз знаний

Чтобы получить список баз знаний, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases`.  Тело ответа будет представлять собой объект JSON с ключом `knowledgebases`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_knowledgebases200_response import GetKnowledgebases200Response
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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)

    try:
        # Получение списка баз знаний
        api_response = api_instance.get_knowledgebases()
        print("The response of KnowledgeBasesApi->get_knowledgebases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->get_knowledgebases: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetKnowledgebases200Response**](GetKnowledgebases200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;knowledgebases&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_knowledgebase_to_agent**
> link_knowledgebase_to_agent(id, agent_id)

Привязка базы знаний к агенту

Чтобы привязать базу знаний к AI агенту, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id}`.

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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    id = 1 # object | ID базы знаний
    agent_id = 1 # object | ID агента

    try:
        # Привязка базы знаний к агенту
        api_instance.link_knowledgebase_to_agent(id, agent_id)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->link_knowledgebase_to_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **agent_id** | [**object**](.md)| ID агента | 

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
**204** | База знаний успешно привязана к агенту |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reindex_document**
> reindex_document(id, document_id)

Переиндексация документа

Чтобы переиндексировать документ в базе знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/reindex`.

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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    id = 1 # object | ID базы знаний
    document_id = 1 # object | ID документа

    try:
        # Переиндексация документа
        api_instance.reindex_document(id, document_id)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->reindex_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **document_id** | [**object**](.md)| ID документа | 

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
**204** | Переиндексация документа начата |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_knowledgebase_from_agent**
> unlink_knowledgebase_from_agent(id, agent_id)

Отвязка базы знаний от агента

Чтобы отвязать базу знаний от AI агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id}`.

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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    id = 1 # object | ID базы знаний
    agent_id = 1 # object | ID агента

    try:
        # Отвязка базы знаний от агента
        api_instance.unlink_knowledgebase_from_agent(id, agent_id)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->unlink_knowledgebase_from_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **agent_id** | [**object**](.md)| ID агента | 

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
**200** | База знаний успешно отвязана от агента |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_knowledgebase**
> CreateKnowledgebase201Response update_knowledgebase(id, update_knowledgebase)

Обновление базы знаний

Чтобы обновить базу знаний, отправьте PATCH-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_knowledgebase201_response import CreateKnowledgebase201Response
from timeweb_cloud_api.models.update_knowledgebase import UpdateKnowledgebase
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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    id = 1 # object | ID базы знаний
    update_knowledgebase = timeweb_cloud_api.UpdateKnowledgebase() # UpdateKnowledgebase | 

    try:
        # Обновление базы знаний
        api_response = api_instance.update_knowledgebase(id, update_knowledgebase)
        print("The response of KnowledgeBasesApi->update_knowledgebase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->update_knowledgebase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **update_knowledgebase** | [**UpdateKnowledgebase**](UpdateKnowledgebase.md)|  | 

### Return type

[**CreateKnowledgebase201Response**](CreateKnowledgebase201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;knowledgebase&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_files_to_knowledgebase**
> UploadFilesToKnowledgebase200Response upload_files_to_knowledgebase(id, files)

Загрузка файлов в базу знаний

Чтобы загрузить файлы в базу знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/upload` с файлами в формате multipart/form-data.  Поддерживаемые форматы: CSV, XML, Markdown (md), HTML, TXT. JSON не поддерживается. Максимум 10 файлов, до 10 МБ каждый.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.upload_files_to_knowledgebase200_response import UploadFilesToKnowledgebase200Response
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
    api_instance = timeweb_cloud_api.KnowledgeBasesApi(api_client)
    id = 1 # object | ID базы знаний
    files = None # object | Файлы для загрузки (максимум 10 файлов, 10 МБ каждый)

    try:
        # Загрузка файлов в базу знаний
        api_response = api_instance.upload_files_to_knowledgebase(id, files)
        print("The response of KnowledgeBasesApi->upload_files_to_knowledgebase:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->upload_files_to_knowledgebase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **files** | [**object**](object.md)| Файлы для загрузки (максимум 10 файлов, 10 МБ каждый) | 

### Return type

[**UploadFilesToKnowledgebase200Response**](UploadFilesToKnowledgebase200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;uploaded_files&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

