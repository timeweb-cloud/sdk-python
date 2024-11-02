# timeweb_cloud_api.KubernetesApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster**](KubernetesApi.md#create_cluster) | **POST** /api/v1/k8s/clusters | Создание кластера
[**create_cluster_node_group**](KubernetesApi.md#create_cluster_node_group) | **POST** /api/v1/k8s/clusters/{cluster_id}/groups | Создание группы нод
[**delete_cluster**](KubernetesApi.md#delete_cluster) | **DELETE** /api/v1/k8s/clusters/{cluster_id} | Удаление кластера
[**delete_cluster_node**](KubernetesApi.md#delete_cluster_node) | **DELETE** /api/v1/k8s/clusters/{cluster_id}/nodes/{node_id} | Удаление ноды
[**delete_cluster_node_group**](KubernetesApi.md#delete_cluster_node_group) | **DELETE** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id} | Удаление группы нод
[**get_cluster**](KubernetesApi.md#get_cluster) | **GET** /api/v1/k8s/clusters/{cluster_id} | Получение информации о кластере
[**get_cluster_kubeconfig**](KubernetesApi.md#get_cluster_kubeconfig) | **GET** /api/v1/k8s/clusters/{cluster_id}/kubeconfig | Получение файла kubeconfig
[**get_cluster_node_group**](KubernetesApi.md#get_cluster_node_group) | **GET** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id} | Получение информации о группе нод
[**get_cluster_node_groups**](KubernetesApi.md#get_cluster_node_groups) | **GET** /api/v1/k8s/clusters/{cluster_id}/groups | Получение групп нод кластера
[**get_cluster_nodes**](KubernetesApi.md#get_cluster_nodes) | **GET** /api/v1/k8s/clusters/{cluster_id}/nodes | Получение списка нод
[**get_cluster_nodes_from_group**](KubernetesApi.md#get_cluster_nodes_from_group) | **GET** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes | Получение списка нод, принадлежащих группе
[**get_cluster_resources**](KubernetesApi.md#get_cluster_resources) | **GET** /api/v1/k8s/clusters/{cluster_id}/resources | Получение ресурсов кластера
[**get_clusters**](KubernetesApi.md#get_clusters) | **GET** /api/v1/k8s/clusters | Получение списка кластеров
[**get_k8_s_network_drivers**](KubernetesApi.md#get_k8_s_network_drivers) | **GET** /api/v1/k8s/network_drivers | Получение списка сетевых драйверов k8s
[**get_k8_s_versions**](KubernetesApi.md#get_k8_s_versions) | **GET** /api/v1/k8s/k8s_versions | Получение списка версий k8s
[**get_kubernetes_presets**](KubernetesApi.md#get_kubernetes_presets) | **GET** /api/v1/presets/k8s | Получение списка тарифов
[**increase_count_of_nodes_in_group**](KubernetesApi.md#increase_count_of_nodes_in_group) | **POST** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes | Увеличение количества нод в группе на указанное количество
[**reduce_count_of_nodes_in_group**](KubernetesApi.md#reduce_count_of_nodes_in_group) | **DELETE** /api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes | Уменьшение количества нод в группе на указанное количество
[**update_cluster**](KubernetesApi.md#update_cluster) | **PATCH** /api/v1/k8s/clusters/{cluster_id} | Обновление информации о кластере


# **create_cluster**
> ClusterResponse create_cluster(cluster_in)

Создание кластера

Чтобы создать кластер, отправьте POST-запрос на `/api/v1/k8s/clusters`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.cluster_in import ClusterIn
from timeweb_cloud_api.models.cluster_response import ClusterResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_in = timeweb_cloud_api.ClusterIn() # ClusterIn | 

    try:
        # Создание кластера
        api_response = api_instance.create_cluster(cluster_in)
        print("The response of KubernetesApi->create_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->create_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_in** | [**ClusterIn**](ClusterIn.md)|  | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Информация о кластере |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_cluster_node_group**
> NodeGroupResponse create_cluster_node_group(cluster_id, node_group_in)

Создание группы нод

Чтобы создать группу нод кластера, отправьте POST-запрос в `/api/v1/k8s/clusters/{cluster_id}/groups`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.node_group_in import NodeGroupIn
from timeweb_cloud_api.models.node_group_response import NodeGroupResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера
    node_group_in = timeweb_cloud_api.NodeGroupIn() # NodeGroupIn | 

    try:
        # Создание группы нод
        api_response = api_instance.create_cluster_node_group(cluster_id, node_group_in)
        print("The response of KubernetesApi->create_cluster_node_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->create_cluster_node_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 
 **node_group_in** | [**NodeGroupIn**](NodeGroupIn.md)|  | 

### Return type

[**NodeGroupResponse**](NodeGroupResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Информация о группе нод |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster**
> DeleteCluster200Response delete_cluster(cluster_id, hash=hash, code=code)

Удаление кластера

Чтобы удалить кластер, отправьте DELETE-запрос в `/api/v1/k8s/clusters/{cluster_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.delete_cluster200_response import DeleteCluster200Response
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера
    hash = 15095f25-aac3-4d60-a788-96cb5136f186 # object | Хеш, который совместно с кодом авторизации надо отправить для удаления, если включено подтверждение удаления сервисов через Телеграм. (optional)
    code = 0000 # object | Код подтверждения, который придет к вам в Телеграм, после запроса удаления, если включено подтверждение удаления сервисов.  При помощи API токена сервисы можно удалять без подтверждения, если параметр токена `is_able_to_delete` установлен в значение `true` (optional)

    try:
        # Удаление кластера
        api_response = api_instance.delete_cluster(cluster_id, hash=hash, code=code)
        print("The response of KubernetesApi->delete_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 
 **hash** | [**object**](.md)| Хеш, который совместно с кодом авторизации надо отправить для удаления, если включено подтверждение удаления сервисов через Телеграм. | [optional] 
 **code** | [**object**](.md)| Код подтверждения, который придет к вам в Телеграм, после запроса удаления, если включено подтверждение удаления сервисов.  При помощи API токена сервисы можно удалять без подтверждения, если параметр токена &#x60;is_able_to_delete&#x60; установлен в значение &#x60;true&#x60; | [optional] 

### Return type

[**DeleteCluster200Response**](DeleteCluster200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;cluster_delete&#x60; |  -  |
**204** | Кластер удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_node**
> delete_cluster_node(cluster_id, node_id)

Удаление ноды

Чтобы удалить ноду, отправьте DELETE-запрос в `/api/v1/k8s/clusters/{cluster_id}/nodes/{node_id}`.

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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера
    node_id = None # object | Уникальный идентификатор группы нод

    try:
        # Удаление ноды
        api_instance.delete_cluster_node(cluster_id, node_id)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_cluster_node: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 
 **node_id** | [**object**](.md)| Уникальный идентификатор группы нод | 

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
**204** | Нода удалена |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cluster_node_group**
> delete_cluster_node_group(cluster_id, group_id)

Удаление группы нод

Чтобы удалить группу нод, отправьте DELETE-запрос в `/api/v1/k8s/clusters/{cluster_id}/groups/{group_id}`.

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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера
    group_id = None # object | Уникальный идентификатор группы

    try:
        # Удаление группы нод
        api_instance.delete_cluster_node_group(cluster_id, group_id)
    except Exception as e:
        print("Exception when calling KubernetesApi->delete_cluster_node_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 
 **group_id** | [**object**](.md)| Уникальный идентификатор группы | 

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
**204** | Группа нод удалена |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster**
> ClusterResponse get_cluster(cluster_id)

Получение информации о кластере

Чтобы получить информацию о кластере, отправьте GET-запрос в `/api/v1/k8s/clusters/{cluster_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.cluster_response import ClusterResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера

    try:
        # Получение информации о кластере
        api_response = api_instance.get_cluster(cluster_id)
        print("The response of KubernetesApi->get_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о кластере |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_kubeconfig**
> object get_cluster_kubeconfig(cluster_id)

Получение файла kubeconfig

Чтобы получить файл kubeconfig, отправьте GET-запрос в `/api/v1/k8s/clusters/{cluster_id}/kubeconfig`.

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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера

    try:
        # Получение файла kubeconfig
        api_response = api_instance.get_cluster_kubeconfig(cluster_id)
        print("The response of KubernetesApi->get_cluster_kubeconfig:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_cluster_kubeconfig: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/yaml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Загрузка конфигурации подключения к кластеру |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node_group**
> NodeGroupResponse get_cluster_node_group(cluster_id, group_id)

Получение информации о группе нод

Чтобы получить информацию о группе нод, отправьте GET-запрос в `/api/v1/k8s/clusters/{cluster_id}/groups/{group_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.node_group_response import NodeGroupResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера
    group_id = None # object | Уникальный идентификатор группы

    try:
        # Получение информации о группе нод
        api_response = api_instance.get_cluster_node_group(cluster_id, group_id)
        print("The response of KubernetesApi->get_cluster_node_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_cluster_node_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 
 **group_id** | [**object**](.md)| Уникальный идентификатор группы | 

### Return type

[**NodeGroupResponse**](NodeGroupResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о группе нод |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_node_groups**
> NodeGroupsResponse get_cluster_node_groups(cluster_id)

Получение групп нод кластера

Чтобы получить группы нод кластера, отправьте GET-запрос в `/api/v1/k8s/clusters/{cluster_id}/groups`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.node_groups_response import NodeGroupsResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера

    try:
        # Получение групп нод кластера
        api_response = api_instance.get_cluster_node_groups(cluster_id)
        print("The response of KubernetesApi->get_cluster_node_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_cluster_node_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 

### Return type

[**NodeGroupsResponse**](NodeGroupsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список групп нод |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_nodes**
> NodesResponse get_cluster_nodes(cluster_id)

Получение списка нод

Чтобы получить список нод, отправьте GET-запрос в `/api/v1/k8s/clusters/{cluster_id}/nodes`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.nodes_response import NodesResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера

    try:
        # Получение списка нод
        api_response = api_instance.get_cluster_nodes(cluster_id)
        print("The response of KubernetesApi->get_cluster_nodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_cluster_nodes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 

### Return type

[**NodesResponse**](NodesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список нод |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_nodes_from_group**
> NodesResponse get_cluster_nodes_from_group(cluster_id, group_id, limit=limit, offset=offset)

Получение списка нод, принадлежащих группе

Чтобы получить список нод принадлежащих группе, отправьте GET-запрос в `/api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.nodes_response import NodesResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера
    group_id = None # object | Уникальный идентификатор группы
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение, относительно начала списка. (optional)

    try:
        # Получение списка нод, принадлежащих группе
        api_response = api_instance.get_cluster_nodes_from_group(cluster_id, group_id, limit=limit, offset=offset)
        print("The response of KubernetesApi->get_cluster_nodes_from_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_cluster_nodes_from_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 
 **group_id** | [**object**](.md)| Уникальный идентификатор группы | 
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение, относительно начала списка. | [optional] 

### Return type

[**NodesResponse**](NodesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список нод |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cluster_resources**
> ResourcesResponse get_cluster_resources(cluster_id)

Получение ресурсов кластера

Устаревший метод, работает только для старых кластеров. \\  Чтобы получить ресурсы кластера, отправьте GET-запрос в `/api/v1/k8s/clusters/{cluster_id}/resources`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.resources_response import ResourcesResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера

    try:
        # Получение ресурсов кластера
        api_response = api_instance.get_cluster_resources(cluster_id)
        print("The response of KubernetesApi->get_cluster_resources:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_cluster_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 

### Return type

[**ResourcesResponse**](ResourcesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список ресурсов |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clusters**
> ClustersResponse get_clusters(limit=limit, offset=offset)

Получение списка кластеров

Чтобы получить список кластеров, отправьте GET-запрос на `/api/v1/k8s/clusters`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.clusters_response import ClustersResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)

    try:
        # Получение списка кластеров
        api_response = api_instance.get_clusters(limit=limit, offset=offset)
        print("The response of KubernetesApi->get_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 

### Return type

[**ClustersResponse**](ClustersResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список кластеров |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_k8_s_network_drivers**
> NetworkDriversResponse get_k8_s_network_drivers()

Получение списка сетевых драйверов k8s

Чтобы получить список сетевых драйверов k8s, отправьте GET-запрос в `/api/v1/k8s/network_drivers`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.network_drivers_response import NetworkDriversResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)

    try:
        # Получение списка сетевых драйверов k8s
        api_response = api_instance.get_k8_s_network_drivers()
        print("The response of KubernetesApi->get_k8_s_network_drivers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_k8_s_network_drivers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkDriversResponse**](NetworkDriversResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список сетевых драйверов k8s |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_k8_s_versions**
> K8SVersionsResponse get_k8_s_versions()

Получение списка версий k8s

Чтобы получить список версий k8s, отправьте GET-запрос в `/api/v1/k8s/k8s_versions`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.k8_s_versions_response import K8SVersionsResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)

    try:
        # Получение списка версий k8s
        api_response = api_instance.get_k8_s_versions()
        print("The response of KubernetesApi->get_k8_s_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_k8_s_versions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**K8SVersionsResponse**](K8SVersionsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список версий k8s |  -  |
**400** |  |  -  |
**401** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kubernetes_presets**
> PresetsResponse get_kubernetes_presets()

Получение списка тарифов

Чтобы получить список тарифов, отправьте GET-запрос в `/api/v1/presets/k8s`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.presets_response import PresetsResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)

    try:
        # Получение списка тарифов
        api_response = api_instance.get_kubernetes_presets()
        print("The response of KubernetesApi->get_kubernetes_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->get_kubernetes_presets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PresetsResponse**](PresetsResponse.md)

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

# **increase_count_of_nodes_in_group**
> NodesResponse increase_count_of_nodes_in_group(cluster_id, group_id, node_count)

Увеличение количества нод в группе на указанное количество

Чтобы увеличить количество нод в группе на указанное значение, отправьте POST-запрос на `/api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.node_count import NodeCount
from timeweb_cloud_api.models.nodes_response import NodesResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера
    group_id = None # object | Уникальный идентификатор группы
    node_count = timeweb_cloud_api.NodeCount() # NodeCount | 

    try:
        # Увеличение количества нод в группе на указанное количество
        api_response = api_instance.increase_count_of_nodes_in_group(cluster_id, group_id, node_count)
        print("The response of KubernetesApi->increase_count_of_nodes_in_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->increase_count_of_nodes_in_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 
 **group_id** | [**object**](.md)| Уникальный идентификатор группы | 
 **node_count** | [**NodeCount**](NodeCount.md)|  | 

### Return type

[**NodesResponse**](NodesResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Список нод |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reduce_count_of_nodes_in_group**
> reduce_count_of_nodes_in_group(cluster_id, group_id, node_count)

Уменьшение количества нод в группе на указанное количество

Чтобы уменьшить количество нод в группе на указанное значение, отправьте DELETE-запрос в `/api/v1/k8s/clusters/{cluster_id}/groups/{group_id}/nodes`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.node_count import NodeCount
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера
    group_id = None # object | Уникальный идентификатор группы
    node_count = timeweb_cloud_api.NodeCount() # NodeCount | 

    try:
        # Уменьшение количества нод в группе на указанное количество
        api_instance.reduce_count_of_nodes_in_group(cluster_id, group_id, node_count)
    except Exception as e:
        print("Exception when calling KubernetesApi->reduce_count_of_nodes_in_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 
 **group_id** | [**object**](.md)| Уникальный идентификатор группы | 
 **node_count** | [**NodeCount**](NodeCount.md)|  | 

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
**204** | Количество нод уменьшено |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cluster**
> ClusterResponse update_cluster(cluster_id, cluster_edit)

Обновление информации о кластере

Чтобы обновить информацию о кластере, отправьте PATCH-запрос в `/api/v1/k8s/clusters/{cluster_id}`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.cluster_edit import ClusterEdit
from timeweb_cloud_api.models.cluster_response import ClusterResponse
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
    api_instance = timeweb_cloud_api.KubernetesApi(api_client)
    cluster_id = None # object | Уникальный идентификатор кластера
    cluster_edit = timeweb_cloud_api.ClusterEdit() # ClusterEdit | 

    try:
        # Обновление информации о кластере
        api_response = api_instance.update_cluster(cluster_id, cluster_edit)
        print("The response of KubernetesApi->update_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KubernetesApi->update_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| Уникальный идентификатор кластера | 
 **cluster_edit** | [**ClusterEdit**](ClusterEdit.md)|  | 

### Return type

[**ClusterResponse**](ClusterResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Информация о кластере |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

