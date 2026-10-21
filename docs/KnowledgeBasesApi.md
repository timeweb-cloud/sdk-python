# timeweb_cloud_api.KnowledgeBasesApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_additional_token_package_to_knowledgebase**](KnowledgeBasesApi.md#add_additional_token_package_to_knowledgebase) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/add-additional-token-package | Покупка дополнительных пакетов токенов
[**create_knowledgebase**](KnowledgeBasesApi.md#create_knowledgebase) | **POST** /api/v1/cloud-ai/knowledge-bases | Создание базы знаний
[**create_knowledgebase_document**](KnowledgeBasesApi.md#create_knowledgebase_document) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/documents | Добавление документа по ссылке
[**delete_document**](KnowledgeBasesApi.md#delete_document) | **DELETE** /api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id} | Удаление документа из базы знаний
[**delete_knowledgebase**](KnowledgeBasesApi.md#delete_knowledgebase) | **DELETE** /api/v1/cloud-ai/knowledge-bases/{id} | Удаление базы знаний
[**download_document**](KnowledgeBasesApi.md#download_document) | **GET** /api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/download | Скачивание файла документа
[**get_knowledgebase**](KnowledgeBasesApi.md#get_knowledgebase) | **GET** /api/v1/cloud-ai/knowledge-bases/{id} | Получение базы знаний со списком документов
[**get_knowledgebase_documents_v2**](KnowledgeBasesApi.md#get_knowledgebase_documents_v2) | **GET** /api/v2/cloud-ai/knowledge-bases/{id}/documents | Получение списка документов базы знаний
[**get_knowledgebase_v3**](KnowledgeBasesApi.md#get_knowledgebase_v3) | **GET** /api/v3/cloud-ai/knowledge-bases/{id} | Получение базы знаний
[**get_knowledgebases**](KnowledgeBasesApi.md#get_knowledgebases) | **GET** /api/v1/cloud-ai/knowledge-bases | Получение списка баз знаний (v1)
[**get_knowledgebases_v2**](KnowledgeBasesApi.md#get_knowledgebases_v2) | **GET** /api/v2/cloud-ai/knowledge-bases | Получение списка баз знаний (v2)
[**get_knowledgebases_v3**](KnowledgeBasesApi.md#get_knowledgebases_v3) | **GET** /api/v3/cloud-ai/knowledge-bases | Получение списка баз знаний
[**link_knowledgebase_to_agent**](KnowledgeBasesApi.md#link_knowledgebase_to_agent) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id} | Привязка базы знаний к агенту
[**reindex_document**](KnowledgeBasesApi.md#reindex_document) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/reindex | Переиндексация документа
[**unlink_knowledgebase_from_agent**](KnowledgeBasesApi.md#unlink_knowledgebase_from_agent) | **DELETE** /api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id} | Отвязка базы знаний от агента
[**update_knowledgebase**](KnowledgeBasesApi.md#update_knowledgebase) | **PATCH** /api/v1/cloud-ai/knowledge-bases/{id} | Изменение базы знаний
[**update_knowledgebase_agent_link**](KnowledgeBasesApi.md#update_knowledgebase_agent_link) | **PATCH** /api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id} | Изменение режима поиска по базе знаний для агента
[**update_knowledgebase_document**](KnowledgeBasesApi.md#update_knowledgebase_document) | **PATCH** /api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id} | Изменение документа
[**upload_files_to_knowledgebase**](KnowledgeBasesApi.md#upload_files_to_knowledgebase) | **POST** /api/v1/cloud-ai/knowledge-bases/{id}/upload | Загрузка файлов в базу знаний


# **add_additional_token_package_to_knowledgebase**
> add_additional_token_package_to_knowledgebase(id, knowledgebase_add_token_package=knowledgebase_add_token_package)

Покупка дополнительных пакетов токенов

Чтобы докупить токены для базы знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/add-additional-token-package`.  Покупается дополнительный пакет (`package_type: additional`) из `GET /api/v1/cloud-ai/token-packages/knowledge-bases` в количестве `count`. Стоимость списывается с баланса, токены добавляются к текущему периоду подписки, заблокированная база знаний разблокируется.  Возможные ошибки: - `400 insufficient_balance` — на балансе недостаточно средств - `400 subscription_expired` — база знаний заблокирована и дата продления подписки прошла: продлите подписку в панели управления - `404 additional_token_package_not_found` — дополнительный пакет недоступен

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.knowledgebase_add_token_package import KnowledgebaseAddTokenPackage
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
    knowledgebase_add_token_package = timeweb_cloud_api.KnowledgebaseAddTokenPackage() # KnowledgebaseAddTokenPackage |  (optional)

    try:
        # Покупка дополнительных пакетов токенов
        api_instance.add_additional_token_package_to_knowledgebase(id, knowledgebase_add_token_package=knowledgebase_add_token_package)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->add_additional_token_package_to_knowledgebase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **knowledgebase_add_token_package** | [**KnowledgebaseAddTokenPackage**](KnowledgebaseAddTokenPackage.md)|  | [optional] 

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
**204** | Пакеты токенов куплены |  -  |
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

Чтобы создать базу знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases`, задав необходимые атрибуты.  Для базы знаний в вашем аккаунте создаётся кластер базы данных OpenSearch по выбранному тарифу в указанной приватной сети, а с баланса сразу списывается стоимость пакета токенов. Подписка продлевается автоматически раз в период пакета.  Пока кластер создаётся, база знаний находится в статусе `creating`; документы, добавленные в это время, будут проиндексированы после перехода в `active`.  Возможные ошибки: - `404 token_package_not_found` — пакет токенов не найден или недоступен - `400 invalid_token_package_type` — пакет не является базовым пакетом для баз знаний - `400 insufficient_balance` — на балансе недостаточно средств для оплаты пакета  Тело ответа будет представлять собой объект JSON с ключом `knowledge_base`.

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
**201** | Объект JSON c ключом &#x60;knowledge_base&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_knowledgebase_document**
> CreateKnowledgebaseDocument201Response create_knowledgebase_document(id, create_document)

Добавление документа по ссылке

Чтобы добавить в базу знаний документ по ссылке, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents`.  Перед добавлением выполняется HEAD-запрос к `url`: адрес должен быть публично доступен, а ответ — содержать заголовок `Content-Type` одного из поддерживаемых форматов (текст, Markdown, HTML, XML, CSV, PDF, DOC, DOCX, XLS, XLSX; JSON не поддерживается). Документ сразу ставится в очередь на индексацию. Чтобы содержимое по ссылке переиндексировалось автоматически, задайте `indexing_schedule`.  Возможные ошибки: - `400 url_is_not_accessible` — адрес недоступен или вернул ошибку - `400 unsupported_file_type` — неподдерживаемый `Content-Type`  Тело ответа будет представлять собой объект JSON с ключом `document`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_document import CreateDocument
from timeweb_cloud_api.models.create_knowledgebase_document201_response import CreateKnowledgebaseDocument201Response
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
    create_document = timeweb_cloud_api.CreateDocument() # CreateDocument | 

    try:
        # Добавление документа по ссылке
        api_response = api_instance.create_knowledgebase_document(id, create_document)
        print("The response of KnowledgeBasesApi->create_knowledgebase_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->create_knowledgebase_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **create_document** | [**CreateDocument**](CreateDocument.md)|  | 

### Return type

[**CreateKnowledgebaseDocument201Response**](CreateKnowledgebaseDocument201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;document&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document**
> delete_document(id, document_id)

Удаление документа из базы знаний

Чтобы удалить документ из базы знаний, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}`.  Документ удаляется вместе с его фрагментами в поисковом индексе.

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
    document_id = 286071 # object | ID документа

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
**204** | Документ удалён |  -  |
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

Чтобы удалить базу знаний, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.  База знаний отвязывается от всех агентов, её кластер базы данных OpenSearch удаляется, подписка закрывается.

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
**204** | База знаний удалена |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_document**
> object download_document(id, document_id)

Скачивание файла документа

Чтобы скачать загруженный файл документа, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/download`.  Доступно только для документов типа `file`. Файл возвращается потоком с исходным MIME-типом в заголовке `Content-Type` и именем в `Content-Disposition`.

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
    document_id = 286071 # object | ID документа

    try:
        # Скачивание файла документа
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
**200** | Содержимое файла |  * Content-Type - MIME-тип файла <br>  * Content-Disposition - &#x60;attachment&#x60; с именем файла (URL-кодированным) <br>  * Content-Length - Размер файла в байтах <br>  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledgebase**
> CreateKnowledgebase201Response get_knowledgebase(id)

Получение базы знаний со списком документов

Чтобы получить информацию о базе знаний вместе со всеми её документами, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.  Тело ответа будет представлять собой объект JSON с ключом `knowledge_base`.

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
        # Получение базы знаний со списком документов
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
**200** | Объект JSON c ключом &#x60;knowledge_base&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledgebase_documents_v2**
> GetKnowledgebaseDocumentsV2200Response get_knowledgebase_documents_v2(id, limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, search=search)

Получение списка документов базы знаний

Чтобы получить список документов базы знаний с пагинацией, отправьте GET-запрос на `/api/v2/cloud-ai/knowledge-bases/{id}/documents`.  Некорректные значения параметров пагинации и сортировки не приводят к ошибке — вместо них применяются значения по умолчанию.  Тело ответа будет представлять собой объект JSON с ключами `knowledgebase_documents` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_knowledgebase_documents_v2200_response import GetKnowledgebaseDocumentsV2200Response
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
    limit = 20 # object | Количество документов на странице. Значения больше 100 уменьшаются до 100 (optional)
    offset = 0 # object | Количество документов, которые нужно пропустить (optional)
    sort_by = name # object | Поле сортировки. `indexing_timestamp` — время последнего изменения документа (optional)
    sort_order = ASC # object | Порядок сортировки (optional)
    search = faq # object | Фильтр по подстроке в названии документа (optional)

    try:
        # Получение списка документов базы знаний
        api_response = api_instance.get_knowledgebase_documents_v2(id, limit=limit, offset=offset, sort_by=sort_by, sort_order=sort_order, search=search)
        print("The response of KnowledgeBasesApi->get_knowledgebase_documents_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->get_knowledgebase_documents_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **limit** | [**object**](.md)| Количество документов на странице. Значения больше 100 уменьшаются до 100 | [optional] 
 **offset** | [**object**](.md)| Количество документов, которые нужно пропустить | [optional] 
 **sort_by** | [**object**](.md)| Поле сортировки. &#x60;indexing_timestamp&#x60; — время последнего изменения документа | [optional] 
 **sort_order** | [**object**](.md)| Порядок сортировки | [optional] 
 **search** | [**object**](.md)| Фильтр по подстроке в названии документа | [optional] 

### Return type

[**GetKnowledgebaseDocumentsV2200Response**](GetKnowledgebaseDocumentsV2200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;knowledgebase_documents&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledgebase_v3**
> GetKnowledgebaseV3200Response get_knowledgebase_v3(id)

Получение базы знаний

Чтобы получить информацию о базе знаний, отправьте GET-запрос на `/api/v3/cloud-ai/knowledge-bases/{id}`.  Тело ответа будет представлять собой объект JSON с ключом `knowledge_base`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_knowledgebase_v3200_response import GetKnowledgebaseV3200Response
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
        api_response = api_instance.get_knowledgebase_v3(id)
        print("The response of KnowledgeBasesApi->get_knowledgebase_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->get_knowledgebase_v3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 

### Return type

[**GetKnowledgebaseV3200Response**](GetKnowledgebaseV3200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;knowledge_base&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledgebases**
> GetKnowledgebases200Response get_knowledgebases()

Получение списка баз знаний (v1)

Метод устарел — используйте `GET /api/v3/cloud-ai/knowledge-bases`.  Чтобы получить список баз знаний вместе со всеми их документами, отправьте GET-запрос на `/api/v1/cloud-ai/knowledge-bases`.  Тело ответа будет представлять собой объект JSON с ключами `knowledge_bases` и `meta`.

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
        # Получение списка баз знаний (v1)
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
**200** | Объект JSON c ключами &#x60;knowledge_bases&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledgebases_v2**
> GetKnowledgebasesV2200Response get_knowledgebases_v2()

Получение списка баз знаний (v2)

Чтобы получить список баз знаний, отправьте GET-запрос на `/api/v2/cloud-ai/knowledge-bases`.  Вместо списка документов возвращается их количество, привязанные агенты — списком ID. Режим поиска для каждого агента возвращает `GET /api/v3/cloud-ai/knowledge-bases`.  Тело ответа будет представлять собой объект JSON с ключами `knowledge_bases` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_knowledgebases_v2200_response import GetKnowledgebasesV2200Response
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
        # Получение списка баз знаний (v2)
        api_response = api_instance.get_knowledgebases_v2()
        print("The response of KnowledgeBasesApi->get_knowledgebases_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->get_knowledgebases_v2: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetKnowledgebasesV2200Response**](GetKnowledgebasesV2200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;knowledge_bases&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledgebases_v3**
> GetKnowledgebasesV3200Response get_knowledgebases_v3()

Получение списка баз знаний

Чтобы получить список баз знаний, отправьте GET-запрос на `/api/v3/cloud-ai/knowledge-bases`.  Ответ содержит количество документов и привязанных агентов с режимом поиска. Документы базы знаний запрашивайте отдельно — `GET /api/v2/cloud-ai/knowledge-bases/{id}/documents`.  Тело ответа будет представлять собой объект JSON с ключами `knowledge_bases` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_knowledgebases_v3200_response import GetKnowledgebasesV3200Response
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
        api_response = api_instance.get_knowledgebases_v3()
        print("The response of KnowledgeBasesApi->get_knowledgebases_v3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->get_knowledgebases_v3: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetKnowledgebasesV3200Response**](GetKnowledgebasesV3200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;knowledge_bases&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_knowledgebase_to_agent**
> link_knowledgebase_to_agent(id, agent_id, link_knowledgebase=link_knowledgebase)

Привязка базы знаний к агенту

Чтобы привязать базу знаний к AI агенту, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id}`.  Тело запроса необязательно: в нём можно выбрать режим поиска `retrievalMode` (по умолчанию `agentic`). Изменить режим для существующей привязки можно запросом PATCH на тот же адрес.  Возможные ошибки: `404 knowledgebase_not_found`, `404 agent_not_found`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.link_knowledgebase import LinkKnowledgebase
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
    agent_id = 101 # object | ID AI агента
    link_knowledgebase = timeweb_cloud_api.LinkKnowledgebase() # LinkKnowledgebase |  (optional)

    try:
        # Привязка базы знаний к агенту
        api_instance.link_knowledgebase_to_agent(id, agent_id, link_knowledgebase=link_knowledgebase)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->link_knowledgebase_to_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **agent_id** | [**object**](.md)| ID AI агента | 
 **link_knowledgebase** | [**LinkKnowledgebase**](LinkKnowledgebase.md)|  | [optional] 

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
**204** | База знаний привязана к агенту |  -  |
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

Чтобы переиндексировать документ, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}/reindex`.  Документ ставится в очередь на индексацию; следите за полем `status` документа. Для документа по ссылке содержимое скачивается заново. Если база знаний не в статусе `active`, документ будет проиндексирован после активации.  Возможные ошибки: `404 knowledgebase_not_found`, `404 document_not_found`.

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
    document_id = 286071 # object | ID документа

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
**204** | Документ поставлен в очередь на индексацию |  -  |
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

Чтобы отвязать базу знаний от AI агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id}`.  Возможные ошибки: `404 knowledgebase_not_found`, `404 agent_not_found`.

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
    agent_id = 101 # object | ID AI агента

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
 **agent_id** | [**object**](.md)| ID AI агента | 

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
**204** | База знаний отвязана от агента |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_knowledgebase**
> CreateKnowledgebase201Response update_knowledgebase(id, update_knowledgebase)

Изменение базы знаний

Чтобы изменить название или описание базы знаний, отправьте PATCH-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}`.  Тело ответа будет представлять собой объект JSON с ключом `knowledge_base`.

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
        # Изменение базы знаний
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
**200** | Объект JSON c ключом &#x60;knowledge_base&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_knowledgebase_agent_link**
> update_knowledgebase_agent_link(id, agent_id, link_knowledgebase=link_knowledgebase)

Изменение режима поиска по базе знаний для агента

Чтобы изменить режим поиска по привязанной базе знаний для AI агента, отправьте PATCH-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/link/{agent_id}`.  Если `retrievalMode` не передан, устанавливается `agentic`. Если база знаний не привязана к агенту, запрос ничего не меняет и также возвращает `204`.  Возможные ошибки: `404 knowledgebase_not_found`, `404 agent_not_found`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.link_knowledgebase import LinkKnowledgebase
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
    agent_id = 101 # object | ID AI агента
    link_knowledgebase = timeweb_cloud_api.LinkKnowledgebase() # LinkKnowledgebase |  (optional)

    try:
        # Изменение режима поиска по базе знаний для агента
        api_instance.update_knowledgebase_agent_link(id, agent_id, link_knowledgebase=link_knowledgebase)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->update_knowledgebase_agent_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **agent_id** | [**object**](.md)| ID AI агента | 
 **link_knowledgebase** | [**LinkKnowledgebase**](LinkKnowledgebase.md)|  | [optional] 

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
**204** | Режим поиска изменён |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_knowledgebase_document**
> CreateKnowledgebaseDocument201Response update_knowledgebase_document(id, document_id, update_document)

Изменение документа

Чтобы изменить документ базы знаний, отправьте PATCH-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/documents/{document_id}`.  Можно изменить название, расписание переиндексации и — только для документов типа `link` — адрес. После смены адреса документ переиндексируется; изменение названия и расписания переиндексацию не запускает. Новый адрес проверяется так же, как при добавлении документа.  Тело ответа будет представлять собой объект JSON с ключом `document`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_knowledgebase_document201_response import CreateKnowledgebaseDocument201Response
from timeweb_cloud_api.models.update_document import UpdateDocument
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
    document_id = 286071 # object | ID документа
    update_document = timeweb_cloud_api.UpdateDocument() # UpdateDocument | 

    try:
        # Изменение документа
        api_response = api_instance.update_knowledgebase_document(id, document_id, update_document)
        print("The response of KnowledgeBasesApi->update_knowledgebase_document:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBasesApi->update_knowledgebase_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID базы знаний | 
 **document_id** | [**object**](.md)| ID документа | 
 **update_document** | [**UpdateDocument**](UpdateDocument.md)|  | 

### Return type

[**CreateKnowledgebaseDocument201Response**](CreateKnowledgebaseDocument201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;document&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_files_to_knowledgebase**
> UploadResult upload_files_to_knowledgebase(id, files)

Загрузка файлов в базу знаний

Чтобы загрузить файлы в базу знаний, отправьте POST-запрос на `/api/v1/cloud-ai/knowledge-bases/{id}/upload` с файлами в поле `files` формата `multipart/form-data`. Для каждого файла создаётся документ типа `file`, после загрузки документы ставятся в очередь на индексацию (если база знаний в статусе `active`; иначе — после активации).  Поддерживаемые форматы: TXT, Markdown (`md`, `markdown`), HTML (`html`, `htm`), XML, CSV, PDF, DOC, DOCX, XLS, XLSX, а также другие файлы с MIME-типом `text/*`. JSON (`json`, `jsonl`, `ndjson`) не поддерживается. Размер одного файла — не более 50 МБ.  Если хотя бы один файл неподдерживаемого формата, запрос завершается ошибкой.  Тело ответа будет представлять собой объект JSON с ключами `uploadedFiles` и `documents`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.upload_result import UploadResult
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
    files = None # object | Файлы для загрузки

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
 **files** | [**object**](object.md)| Файлы для загрузки | 

### Return type

[**UploadResult**](UploadResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;uploadedFiles&#x60; и &#x60;documents&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

