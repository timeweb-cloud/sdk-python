# timeweb_cloud_api.ProjectsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_balancer_to_project**](ProjectsApi.md#add_balancer_to_project) | **POST** /api/v1/projects/{project_id}/resources/balancers | Добавление балансировщика в проект
[**add_cluster_to_project**](ProjectsApi.md#add_cluster_to_project) | **POST** /api/v1/projects/{project_id}/resources/clusters | Добавление кластера в проект
[**add_database_to_project**](ProjectsApi.md#add_database_to_project) | **POST** /api/v1/projects/{project_id}/resources/databases | Добавление базы данных в проект
[**add_dedicated_server_to_project**](ProjectsApi.md#add_dedicated_server_to_project) | **POST** /api/v1/projects/{project_id}/resources/dedicated | Добавление выделенного сервера в проект
[**add_server_to_project**](ProjectsApi.md#add_server_to_project) | **POST** /api/v1/projects/{project_id}/resources/servers | Добавление сервера в проект
[**add_storage_to_project**](ProjectsApi.md#add_storage_to_project) | **POST** /api/v1/projects/{project_id}/resources/buckets | Добавление хранилища в проект
[**create_project**](ProjectsApi.md#create_project) | **POST** /api/v1/projects | Создание проекта
[**delete_project**](ProjectsApi.md#delete_project) | **DELETE** /api/v1/projects/{project_id} | Удаление проекта
[**get_account_balancers**](ProjectsApi.md#get_account_balancers) | **GET** /api/v1/projects/resources/balancers | Получение списка всех балансировщиков на аккаунте
[**get_account_clusters**](ProjectsApi.md#get_account_clusters) | **GET** /api/v1/projects/resources/clusters | Получение списка всех кластеров на аккаунте
[**get_account_databases**](ProjectsApi.md#get_account_databases) | **GET** /api/v1/projects/resources/databases | Получение списка всех баз данных на аккаунте
[**get_account_dedicated_servers**](ProjectsApi.md#get_account_dedicated_servers) | **GET** /api/v1/projects/resources/dedicated | Получение списка всех выделенных серверов на аккаунте
[**get_account_servers**](ProjectsApi.md#get_account_servers) | **GET** /api/v1/projects/resources/servers | Получение списка всех серверов на аккаунте
[**get_account_storages**](ProjectsApi.md#get_account_storages) | **GET** /api/v1/projects/resources/buckets | Получение списка всех хранилищ на аккаунте
[**get_all_project_resources**](ProjectsApi.md#get_all_project_resources) | **GET** /api/v1/projects/{project_id}/resources | Получение всех ресурсов проекта
[**get_project**](ProjectsApi.md#get_project) | **GET** /api/v1/projects/{project_id} | Получение проекта по идентификатору
[**get_project_balancers**](ProjectsApi.md#get_project_balancers) | **GET** /api/v1/projects/{project_id}/resources/balancers | Получение списка балансировщиков проекта
[**get_project_clusters**](ProjectsApi.md#get_project_clusters) | **GET** /api/v1/projects/{project_id}/resources/clusters | Получение списка кластеров проекта
[**get_project_databases**](ProjectsApi.md#get_project_databases) | **GET** /api/v1/projects/{project_id}/resources/databases | Получение списка баз данных проекта
[**get_project_dedicated_servers**](ProjectsApi.md#get_project_dedicated_servers) | **GET** /api/v1/projects/{project_id}/resources/dedicated | Получение списка выделенных серверов проекта
[**get_project_servers**](ProjectsApi.md#get_project_servers) | **GET** /api/v1/projects/{project_id}/resources/servers | Получение списка серверов проекта
[**get_project_storages**](ProjectsApi.md#get_project_storages) | **GET** /api/v1/projects/{project_id}/resources/buckets | Получение списка хранилищ проекта
[**get_projects**](ProjectsApi.md#get_projects) | **GET** /api/v1/projects | Получение списка проектов
[**transfer_resource_to_another_project**](ProjectsApi.md#transfer_resource_to_another_project) | **PUT** /api/v1/projects/{project_id}/resources/transfer | Перенести ресурс в другой проект
[**update_project**](ProjectsApi.md#update_project) | **PUT** /api/v1/projects/{project_id} | Изменение проекта


# **add_balancer_to_project**
> AddBalancerToProject200Response add_balancer_to_project(project_id, add_balancer_to_project_request)

Добавление балансировщика в проект

Чтобы добавить балансировщик в проект, отправьте POST-запрос на `/api/v1/projects/{project_id}/resources/balancers`, задав необходимые атрибуты.  Балансировщик будет добавлен в указанный проект. Тело ответа будет содержать объект JSON с информацией о добавленном балансировщике.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_balancer_to_project200_response import AddBalancerToProject200Response
from timeweb_cloud_api.models.add_balancer_to_project_request import AddBalancerToProjectRequest
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.
    add_balancer_to_project_request = timeweb_cloud_api.AddBalancerToProjectRequest() # AddBalancerToProjectRequest | 

    try:
        # Добавление балансировщика в проект
        api_response = api_instance.add_balancer_to_project(project_id, add_balancer_to_project_request)
        print("The response of ProjectsApi->add_balancer_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_balancer_to_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 
 **add_balancer_to_project_request** | [**AddBalancerToProjectRequest**](AddBalancerToProjectRequest.md)|  | 

### Return type

[**AddBalancerToProject200Response**](AddBalancerToProject200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_cluster_to_project**
> AddBalancerToProject200Response add_cluster_to_project(project_id, add_cluster_to_project_request)

Добавление кластера в проект

Чтобы добавить кластер в проект, отправьте POST-запрос на `/api/v1/projects/{project_id}/resources/clusters`, задав необходимые атрибуты.  Кластер будет добавлен в указанный проект. Тело ответа будет содержать объект JSON с информацией о добавленном кластере.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_balancer_to_project200_response import AddBalancerToProject200Response
from timeweb_cloud_api.models.add_cluster_to_project_request import AddClusterToProjectRequest
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.
    add_cluster_to_project_request = timeweb_cloud_api.AddClusterToProjectRequest() # AddClusterToProjectRequest | 

    try:
        # Добавление кластера в проект
        api_response = api_instance.add_cluster_to_project(project_id, add_cluster_to_project_request)
        print("The response of ProjectsApi->add_cluster_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_cluster_to_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 
 **add_cluster_to_project_request** | [**AddClusterToProjectRequest**](AddClusterToProjectRequest.md)|  | 

### Return type

[**AddBalancerToProject200Response**](AddBalancerToProject200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_database_to_project**
> AddBalancerToProject200Response add_database_to_project(project_id, add_database_to_project_request)

Добавление базы данных в проект

Чтобы добавить базу данных в проект, отправьте POST-запрос на `/api/v1/projects/{project_id}/resources/databases`, задав необходимые атрибуты.  База данных будет добавлена в указанный проект. Тело ответа будет содержать объект JSON с информацией о добавленной базе данных.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_balancer_to_project200_response import AddBalancerToProject200Response
from timeweb_cloud_api.models.add_database_to_project_request import AddDatabaseToProjectRequest
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.
    add_database_to_project_request = timeweb_cloud_api.AddDatabaseToProjectRequest() # AddDatabaseToProjectRequest | 

    try:
        # Добавление базы данных в проект
        api_response = api_instance.add_database_to_project(project_id, add_database_to_project_request)
        print("The response of ProjectsApi->add_database_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_database_to_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 
 **add_database_to_project_request** | [**AddDatabaseToProjectRequest**](AddDatabaseToProjectRequest.md)|  | 

### Return type

[**AddBalancerToProject200Response**](AddBalancerToProject200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_dedicated_server_to_project**
> AddBalancerToProject200Response add_dedicated_server_to_project(project_id, add_dedicated_server_to_project_request)

Добавление выделенного сервера в проект

Чтобы добавить выделенный сервер в проект, отправьте POST-запрос на `/api/v1/projects/{project_id}/resources/dedicated`, задав необходимые атрибуты.  Выделенный сервер будет добавлен в указанный проект. Тело ответа будет содержать объект JSON с информацией о добавленном выделенном сервере.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_balancer_to_project200_response import AddBalancerToProject200Response
from timeweb_cloud_api.models.add_dedicated_server_to_project_request import AddDedicatedServerToProjectRequest
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.
    add_dedicated_server_to_project_request = timeweb_cloud_api.AddDedicatedServerToProjectRequest() # AddDedicatedServerToProjectRequest | 

    try:
        # Добавление выделенного сервера в проект
        api_response = api_instance.add_dedicated_server_to_project(project_id, add_dedicated_server_to_project_request)
        print("The response of ProjectsApi->add_dedicated_server_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_dedicated_server_to_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 
 **add_dedicated_server_to_project_request** | [**AddDedicatedServerToProjectRequest**](AddDedicatedServerToProjectRequest.md)|  | 

### Return type

[**AddBalancerToProject200Response**](AddBalancerToProject200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_server_to_project**
> AddBalancerToProject200Response add_server_to_project(project_id, add_server_to_project_request)

Добавление сервера в проект

Чтобы добавить сервер в проект, отправьте POST-запрос на `/api/v1/projects/{project_id}/resources/servers`, задав необходимые атрибуты.  Сервер будет добавлен в указанный проект. Тело ответа будет содержать объект JSON с информацией о добавленном сервере.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_balancer_to_project200_response import AddBalancerToProject200Response
from timeweb_cloud_api.models.add_server_to_project_request import AddServerToProjectRequest
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.
    add_server_to_project_request = timeweb_cloud_api.AddServerToProjectRequest() # AddServerToProjectRequest | 

    try:
        # Добавление сервера в проект
        api_response = api_instance.add_server_to_project(project_id, add_server_to_project_request)
        print("The response of ProjectsApi->add_server_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_server_to_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 
 **add_server_to_project_request** | [**AddServerToProjectRequest**](AddServerToProjectRequest.md)|  | 

### Return type

[**AddBalancerToProject200Response**](AddBalancerToProject200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_storage_to_project**
> AddBalancerToProject200Response add_storage_to_project(project_id, add_storage_to_project_request)

Добавление хранилища в проект

Чтобы добавить хранилище в проект, отправьте POST-запрос на `/api/v1/projects/{project_id}/resources/buckets`, задав необходимые атрибуты.  Хранилище будет добавлено в указанный проект. Тело ответа будет содержать объект JSON с информацией о добавленном хранилище.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_balancer_to_project200_response import AddBalancerToProject200Response
from timeweb_cloud_api.models.add_storage_to_project_request import AddStorageToProjectRequest
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.
    add_storage_to_project_request = timeweb_cloud_api.AddStorageToProjectRequest() # AddStorageToProjectRequest | 

    try:
        # Добавление хранилища в проект
        api_response = api_instance.add_storage_to_project(project_id, add_storage_to_project_request)
        print("The response of ProjectsApi->add_storage_to_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->add_storage_to_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 
 **add_storage_to_project_request** | [**AddStorageToProjectRequest**](AddStorageToProjectRequest.md)|  | 

### Return type

[**AddBalancerToProject200Response**](AddBalancerToProject200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> CreateProject201Response create_project(create_project)

Создание проекта

Чтобы создать проект, отправьте POST-запрос в `api/v1/projects`, задав необходимые атрибуты.  Проект будет создан с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданном проекте.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_project import CreateProject
from timeweb_cloud_api.models.create_project201_response import CreateProject201Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    create_project = timeweb_cloud_api.CreateProject() # CreateProject | 

    try:
        # Создание проекта
        api_response = api_instance.create_project(create_project)
        print("The response of ProjectsApi->create_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->create_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_project** | [**CreateProject**](CreateProject.md)|  | 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;project&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> delete_project(project_id)

Удаление проекта

Чтобы удалить проект, отправьте запрос DELETE в `api/v1/projects/{project_id}`.

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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.

    try:
        # Удаление проекта
        api_instance.delete_project(project_id)
    except Exception as e:
        print("Exception when calling ProjectsApi->delete_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 

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
**204** | Проект успешно удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_balancers**
> GetBalancers200Response get_account_balancers()

Получение списка всех балансировщиков на аккаунте

Чтобы получить список всех балансировщиков на аккаунте, отправьте GET-запрос на `/api/v1/projects/resources/balancers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_balancers200_response import GetBalancers200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)

    try:
        # Получение списка всех балансировщиков на аккаунте
        api_response = api_instance.get_account_balancers()
        print("The response of ProjectsApi->get_account_balancers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_account_balancers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | Объект JSON c ключом &#x60;balancers&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_clusters**
> GetProjectClusters200Response get_account_clusters()

Получение списка всех кластеров на аккаунте

Чтобы получить список всех кластеров на аккаунте, отправьте GET-запрос на `/api/v1/projects/resources/clusters`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_project_clusters200_response import GetProjectClusters200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)

    try:
        # Получение списка всех кластеров на аккаунте
        api_response = api_instance.get_account_clusters()
        print("The response of ProjectsApi->get_account_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_account_clusters: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetProjectClusters200Response**](GetProjectClusters200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;clusters&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_databases**
> GetProjectDatabases200Response get_account_databases()

Получение списка всех баз данных на аккаунте

Чтобы получить список всех баз данных на аккаунте, отправьте GET-запрос на `/api/v1/projects/resources/databases`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_project_databases200_response import GetProjectDatabases200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)

    try:
        # Получение списка всех баз данных на аккаунте
        api_response = api_instance.get_account_databases()
        print("The response of ProjectsApi->get_account_databases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_account_databases: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetProjectDatabases200Response**](GetProjectDatabases200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;databases&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_dedicated_servers**
> GetDedicatedServers200Response get_account_dedicated_servers()

Получение списка всех выделенных серверов на аккаунте

Чтобы получить список всех выделенных серверов на аккаунте, отправьте GET-запрос на `/api/v1/projects/resources/dedicated`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_dedicated_servers200_response import GetDedicatedServers200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)

    try:
        # Получение списка всех выделенных серверов на аккаунте
        api_response = api_instance.get_account_dedicated_servers()
        print("The response of ProjectsApi->get_account_dedicated_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_account_dedicated_servers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDedicatedServers200Response**](GetDedicatedServers200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;dedicated_servers&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_servers**
> GetServers200Response get_account_servers()

Получение списка всех серверов на аккаунте

Чтобы получить список всех серверов на аккаунте, отправьте GET-запрос на `/api/v1/projects/resources/servers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_servers200_response import GetServers200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)

    try:
        # Получение списка всех серверов на аккаунте
        api_response = api_instance.get_account_servers()
        print("The response of ProjectsApi->get_account_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_account_servers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetServers200Response**](GetServers200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;servers&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_storages**
> GetProjectStorages200Response get_account_storages()

Получение списка всех хранилищ на аккаунте

Чтобы получить список всех хранилищ на аккаунте, отправьте GET-запрос на `/api/v1/projects/resources/buckets`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_project_storages200_response import GetProjectStorages200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)

    try:
        # Получение списка всех хранилищ на аккаунте
        api_response = api_instance.get_account_storages()
        print("The response of ProjectsApi->get_account_storages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_account_storages: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetProjectStorages200Response**](GetProjectStorages200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;buckets&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_project_resources**
> GetAllProjectResources200Response get_all_project_resources(project_id)

Получение всех ресурсов проекта

Чтобы получить все ресурсы проекта, отправьте GET-запрос на `/api/v1/projects/{project_id}/resources`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_all_project_resources200_response import GetAllProjectResources200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.

    try:
        # Получение всех ресурсов проекта
        api_response = api_instance.get_all_project_resources(project_id)
        print("The response of ProjectsApi->get_all_project_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_all_project_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 

### Return type

[**GetAllProjectResources200Response**](GetAllProjectResources200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами: &#x60;servers&#x60;, &#x60;balancers&#x60;, &#x60;buckets&#x60;, &#x60;clusters&#x60;, &#x60;databases&#x60;, &#x60;dedicated_servers&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project**
> CreateProject201Response get_project(project_id)

Получение проекта по идентификатору

Чтобы получить проект по идентификатору, отправьте GET-запрос на `/api/v1/projects/{project_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_project201_response import CreateProject201Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.

    try:
        # Получение проекта по идентификатору
        api_response = api_instance.get_project(project_id)
        print("The response of ProjectsApi->get_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;project&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_balancers**
> GetBalancers200Response get_project_balancers(project_id)

Получение списка балансировщиков проекта

Чтобы получить список балансировщиков проекта, отправьте GET-запрос на `/api/v1/projects/{project_id}/resources/balancers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_balancers200_response import GetBalancers200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.

    try:
        # Получение списка балансировщиков проекта
        api_response = api_instance.get_project_balancers(project_id)
        print("The response of ProjectsApi->get_project_balancers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_balancers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 

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
**200** | Объект JSON c ключом &#x60;balancers&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_clusters**
> GetProjectClusters200Response get_project_clusters(project_id)

Получение списка кластеров проекта

Чтобы получить список кластеров проекта, отправьте GET-запрос на `/api/v1/projects/{project_id}/resources/clusters`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_project_clusters200_response import GetProjectClusters200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.

    try:
        # Получение списка кластеров проекта
        api_response = api_instance.get_project_clusters(project_id)
        print("The response of ProjectsApi->get_project_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 

### Return type

[**GetProjectClusters200Response**](GetProjectClusters200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;clusters&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_databases**
> GetProjectDatabases200Response get_project_databases(project_id)

Получение списка баз данных проекта

Чтобы получить список баз данных проекта, отправьте GET-запрос на `/api/v1/projects/{project_id}/resources/databases`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_project_databases200_response import GetProjectDatabases200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.

    try:
        # Получение списка баз данных проекта
        api_response = api_instance.get_project_databases(project_id)
        print("The response of ProjectsApi->get_project_databases:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_databases: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 

### Return type

[**GetProjectDatabases200Response**](GetProjectDatabases200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;databases&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_dedicated_servers**
> GetDedicatedServers200Response get_project_dedicated_servers(project_id)

Получение списка выделенных серверов проекта

Чтобы получить список выделенных серверов проекта, отправьте GET-запрос на `/api/v1/projects/{project_id}/resources/dedicated`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_dedicated_servers200_response import GetDedicatedServers200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.

    try:
        # Получение списка выделенных серверов проекта
        api_response = api_instance.get_project_dedicated_servers(project_id)
        print("The response of ProjectsApi->get_project_dedicated_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_dedicated_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 

### Return type

[**GetDedicatedServers200Response**](GetDedicatedServers200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;dedicated_servers&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_servers**
> GetServers200Response get_project_servers(project_id)

Получение списка серверов проекта

Чтобы получить список серверов проекта, отправьте GET-запрос на `/api/v1/projects/{project_id}/resources/servers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_servers200_response import GetServers200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.

    try:
        # Получение списка серверов проекта
        api_response = api_instance.get_project_servers(project_id)
        print("The response of ProjectsApi->get_project_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 

### Return type

[**GetServers200Response**](GetServers200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;servers&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_storages**
> GetProjectStorages200Response get_project_storages(project_id)

Получение списка хранилищ проекта

Чтобы получить список хранилищ проекта, отправьте GET-запрос на `/api/v1/projects/{project_id}/resources/buckets`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_project_storages200_response import GetProjectStorages200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.

    try:
        # Получение списка хранилищ проекта
        api_response = api_instance.get_project_storages(project_id)
        print("The response of ProjectsApi->get_project_storages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_project_storages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 

### Return type

[**GetProjectStorages200Response**](GetProjectStorages200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;buckets&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects**
> GetProjects200Response get_projects()

Получение списка проектов

Чтобы получить список всех проектов на вашем аккаунте, отправьте GET-запрос на `/api/v1/dedicated-servers`.   Тело ответа будет представлять собой объект JSON с ключом `projects`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_projects200_response import GetProjects200Response
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)

    try:
        # Получение списка проектов
        api_response = api_instance.get_projects()
        print("The response of ProjectsApi->get_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->get_projects: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetProjects200Response**](GetProjects200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;projects&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transfer_resource_to_another_project**
> AddBalancerToProject200Response transfer_resource_to_another_project(project_id, resource_transfer)

Перенести ресурс в другой проект

Чтобы перенести ресурс в другой проект, отправьте запрос PUT в `api/v1/projects/{project_id}/resources/transfer`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_balancer_to_project200_response import AddBalancerToProject200Response
from timeweb_cloud_api.models.resource_transfer import ResourceTransfer
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.
    resource_transfer = timeweb_cloud_api.ResourceTransfer() # ResourceTransfer | 

    try:
        # Перенести ресурс в другой проект
        api_response = api_instance.transfer_resource_to_another_project(project_id, resource_transfer)
        print("The response of ProjectsApi->transfer_resource_to_another_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->transfer_resource_to_another_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 
 **resource_transfer** | [**ResourceTransfer**](ResourceTransfer.md)|  | 

### Return type

[**AddBalancerToProject200Response**](AddBalancerToProject200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;resource&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> CreateProject201Response update_project(project_id, update_project)

Изменение проекта

Чтобы изменить проект, отправьте запрос PUT в `api/v1/projects/{project_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_project201_response import CreateProject201Response
from timeweb_cloud_api.models.update_project import UpdateProject
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
    api_instance = timeweb_cloud_api.ProjectsApi(api_client)
    project_id = 99 # object | Уникальный идентификатор проекта.
    update_project = timeweb_cloud_api.UpdateProject() # UpdateProject | 

    try:
        # Изменение проекта
        api_response = api_instance.update_project(project_id, update_project)
        print("The response of ProjectsApi->update_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectsApi->update_project: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | [**object**](.md)| Уникальный идентификатор проекта. | 
 **update_project** | [**UpdateProject**](UpdateProject.md)|  | 

### Return type

[**CreateProject201Response**](CreateProject201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;project&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

