# timeweb_cloud_api.DatabasesApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_database_backup**](DatabasesApi.md#create_database_backup) | **POST** /api/v1/dbs/{db_id}/backups | Создание бэкапа базы данных
[**create_database_backup_download_url**](DatabasesApi.md#create_database_backup_download_url) | **POST** /api/v1/dbs/{db_id}/backups/{backup_id}/download-url | Получение ссылки для скачивания бэкапа базы данных
[**create_database_cluster**](DatabasesApi.md#create_database_cluster) | **POST** /api/v1/databases | Создание кластера базы данных
[**create_database_instance**](DatabasesApi.md#create_database_instance) | **POST** /api/v1/databases/{db_cluster_id}/instances | Создание инстанса базы данных
[**create_database_s3_backup**](DatabasesApi.md#create_database_s3_backup) | **POST** /api/v2/databases/{db_id}/backups | Создание S3-бэкапа базы данных
[**create_database_user**](DatabasesApi.md#create_database_user) | **POST** /api/v1/databases/{db_cluster_id}/admins | Создание пользователя базы данных
[**delete_database_backup**](DatabasesApi.md#delete_database_backup) | **DELETE** /api/v1/dbs/{db_id}/backups/{backup_id} | Удаление бэкапа базы данных
[**delete_database_cluster**](DatabasesApi.md#delete_database_cluster) | **DELETE** /api/v1/databases/{db_cluster_id} | Удаление кластера базы данных
[**delete_database_instance**](DatabasesApi.md#delete_database_instance) | **DELETE** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Удаление инстанса базы данных
[**delete_database_s3_backup**](DatabasesApi.md#delete_database_s3_backup) | **DELETE** /api/v2/databases/{db_id}/backups/{backup_id} | Удаление S3-бэкапа базы данных
[**delete_database_user**](DatabasesApi.md#delete_database_user) | **DELETE** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Удаление пользователя базы данных
[**get_database_auto_backups_settings**](DatabasesApi.md#get_database_auto_backups_settings) | **GET** /api/v1/dbs/{db_id}/auto-backups | Получение настроек автобэкапов базы данных
[**get_database_backup**](DatabasesApi.md#get_database_backup) | **GET** /api/v1/dbs/{db_id}/backups/{backup_id} | Получение бэкапа базы данных
[**get_database_backups**](DatabasesApi.md#get_database_backups) | **GET** /api/v1/dbs/{db_id}/backups | Список бэкапов базы данных
[**get_database_cluster**](DatabasesApi.md#get_database_cluster) | **GET** /api/v1/databases/{db_cluster_id} | Получение кластера базы данных
[**get_database_cluster_replicas**](DatabasesApi.md#get_database_cluster_replicas) | **GET** /api/v1/databases/{db_cluster_id}/replicas | Получение списка реплик кластера базы данных
[**get_database_cluster_types**](DatabasesApi.md#get_database_cluster_types) | **GET** /api/v1/database-types | Получение списка типов кластеров баз данных
[**get_database_clusters**](DatabasesApi.md#get_database_clusters) | **GET** /api/v1/databases | Получение списка кластеров баз данных
[**get_database_configurators**](DatabasesApi.md#get_database_configurators) | **GET** /api/v1/configurator/databases | Получение списка конфигураторов баз данных
[**get_database_default_parameters**](DatabasesApi.md#get_database_default_parameters) | **GET** /api/v1/dbs/default-parameters | Получение рекомендуемых значений параметров баз данных
[**get_database_instance**](DatabasesApi.md#get_database_instance) | **GET** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Получение инстанса базы данных
[**get_database_instances**](DatabasesApi.md#get_database_instances) | **GET** /api/v1/databases/{db_cluster_id}/instances | Получение списка инстансов баз данных
[**get_database_parameters**](DatabasesApi.md#get_database_parameters) | **GET** /api/v1/dbs/parameters | Получение списка параметров баз данных
[**get_database_preset**](DatabasesApi.md#get_database_preset) | **GET** /api/v2/dbs/presets/{preset_id} | Получение тарифа для базы данных
[**get_database_privileges**](DatabasesApi.md#get_database_privileges) | **GET** /api/v1/databases/{db_cluster_id}/privileges | Получение привилегий кластера базы данных
[**get_database_s3_backup**](DatabasesApi.md#get_database_s3_backup) | **GET** /api/v2/databases/{db_id}/backups/{backup_id} | Получение S3-бэкапа базы данных
[**get_database_s3_backups**](DatabasesApi.md#get_database_s3_backups) | **GET** /api/v2/databases/{db_id}/backups | Список S3-бэкапов базы данных
[**get_database_user**](DatabasesApi.md#get_database_user) | **GET** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Получение пользователя базы данных
[**get_database_users**](DatabasesApi.md#get_database_users) | **GET** /api/v1/databases/{db_cluster_id}/admins | Получение списка пользователей базы данных
[**get_databases_presets**](DatabasesApi.md#get_databases_presets) | **GET** /api/v2/presets/dbs | Получение списка тарифов для баз данных
[**perform_database_cluster_action**](DatabasesApi.md#perform_database_cluster_action) | **POST** /api/v1/databases/{db_cluster_id}/action | Выполнение действия над кластером базы данных
[**restore_database_from_backup**](DatabasesApi.md#restore_database_from_backup) | **PUT** /api/v1/dbs/{db_id}/backups/{backup_id} | Восстановление базы данных из бэкапа
[**restore_database_from_s3_backup**](DatabasesApi.md#restore_database_from_s3_backup) | **POST** /api/v2/databases/{db_id}/backups/{backup_id}/restore | Восстановление базы данных из S3-бэкапа
[**update_database_auto_backups_settings**](DatabasesApi.md#update_database_auto_backups_settings) | **PATCH** /api/v1/dbs/{db_id}/auto-backups | Изменение настроек автобэкапов базы данных
[**update_database_backup**](DatabasesApi.md#update_database_backup) | **PATCH** /api/v1/dbs/{db_id}/backups/{backup_id} | Изменение комментария к бэкапу базы данных
[**update_database_cluster**](DatabasesApi.md#update_database_cluster) | **PATCH** /api/v1/databases/{db_cluster_id} | Изменение кластера базы данных
[**update_database_cluster_v2**](DatabasesApi.md#update_database_cluster_v2) | **PATCH** /api/v2/databases/{db_cluster_id} | Изменение кластера базы данных (v2)
[**update_database_instance**](DatabasesApi.md#update_database_instance) | **PATCH** /api/v1/databases/{db_cluster_id}/instances/{instance_id} | Изменение инстанса базы данных
[**update_database_s3_backup**](DatabasesApi.md#update_database_s3_backup) | **PATCH** /api/v2/databases/{db_id}/backups/{backup_id} | Изменение комментария S3-бэкапа базы данных
[**update_database_user**](DatabasesApi.md#update_database_user) | **PATCH** /api/v1/databases/{db_cluster_id}/admins/{admin_id} | Изменение пользователя базы данных


# **create_database_backup**
> CreateDatabaseBackup201Response create_database_backup(db_id, dbs_create_backup=dbs_create_backup)

Создание бэкапа базы данных

Чтобы создать бэкап базы данных, отправьте запрос POST в `api/v1/dbs/{db_id}/backups`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_database_backup201_response import CreateDatabaseBackup201Response
from timeweb_cloud_api.models.dbs_create_backup import DbsCreateBackup
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    dbs_create_backup = timeweb_cloud_api.DbsCreateBackup() # DbsCreateBackup |  (optional)

    try:
        # Создание бэкапа базы данных
        api_response = api_instance.create_database_backup(db_id, dbs_create_backup=dbs_create_backup)
        print("The response of DatabasesApi->create_database_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->create_database_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **dbs_create_backup** | [**DbsCreateBackup**](DbsCreateBackup.md)|  | [optional] 

### Return type

[**CreateDatabaseBackup201Response**](CreateDatabaseBackup201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON с ключом &#x60;backup&#x60;. Для кластеров PostgreSQL из нескольких нод значение ключа &#x60;backup&#x60; будет равно &#x60;null&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_database_backup_download_url**
> CreateDatabaseBackupDownloadUrl201Response create_database_backup_download_url(db_id, backup_id, backup_download_url_request)

Получение ссылки для скачивания бэкапа базы данных

Чтобы получить ссылку для скачивания резервной копии базы данных, отправьте POST-запрос на `/api/v1/dbs/{db_id}/backups/{backup_id}/download-url`.   Скачивание резервных копий доступно не для всех кластеров. Если для вашего кластера оно недоступно, метод вернет ошибку со статусом `400`.   Тело ответа будет представлять собой объект JSON с ключом `backup_url`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.backup_download_url_request import BackupDownloadUrlRequest
from timeweb_cloud_api.models.create_database_backup_download_url201_response import CreateDatabaseBackupDownloadUrl201Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    backup_id = None # object | ID резервной копии
    backup_download_url_request = timeweb_cloud_api.BackupDownloadUrlRequest() # BackupDownloadUrlRequest | 

    try:
        # Получение ссылки для скачивания бэкапа базы данных
        api_response = api_instance.create_database_backup_download_url(db_id, backup_id, backup_download_url_request)
        print("The response of DatabasesApi->create_database_backup_download_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->create_database_backup_download_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **backup_id** | [**object**](.md)| ID резервной копии | 
 **backup_download_url_request** | [**BackupDownloadUrlRequest**](BackupDownloadUrlRequest.md)|  | 

### Return type

[**CreateDatabaseBackupDownloadUrl201Response**](CreateDatabaseBackupDownloadUrl201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON с ключом &#x60;backup_url&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_database_cluster**
> CreateDatabaseCluster201Response create_database_cluster(create_cluster)

Создание кластера базы данных

Чтобы создать кластер базы данных на вашем аккаунте, отправьте POST-запрос на `/api/v1/databases`.   Вместе с кластером будет создан один инстанс базы данных и один пользователь.   Размер кластера задается либо тарифом (`preset_id`), либо конфигуратором (`configuration`). Эти поля взаимоисключающие, но одно из них передать обязательно — запрос без обоих вернется с ошибкой.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_cluster import CreateCluster
from timeweb_cloud_api.models.create_database_cluster201_response import CreateDatabaseCluster201Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    create_cluster = timeweb_cloud_api.CreateCluster() # CreateCluster | 

    try:
        # Создание кластера базы данных
        api_response = api_instance.create_database_cluster(create_cluster)
        print("The response of DatabasesApi->create_database_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->create_database_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_cluster** | [**CreateCluster**](CreateCluster.md)|  | 

### Return type

[**CreateDatabaseCluster201Response**](CreateDatabaseCluster201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON c ключом &#x60;db&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_database_instance**
> CreateDatabaseInstance201Response create_database_instance(db_cluster_id, create_instance)

Создание инстанса базы данных

Чтобы создать инстанс базы данных, отправьте POST-запрос на `/api/v1/databases/{db_cluster_id}/instances`.\\    Существующие пользователи не будут иметь доступа к новой базе данных после создания. Вы можете изменить привилегии для пользователя через <a href='#tag/Bazy-dannyh/operation/updateDatabaseUser'>метод изменения пользователя</a> 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_database_instance201_response import CreateDatabaseInstance201Response
from timeweb_cloud_api.models.create_instance import CreateInstance
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных
    create_instance = timeweb_cloud_api.CreateInstance() # CreateInstance | 

    try:
        # Создание инстанса базы данных
        api_response = api_instance.create_database_instance(db_cluster_id, create_instance)
        print("The response of DatabasesApi->create_database_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->create_database_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 
 **create_instance** | [**CreateInstance**](CreateInstance.md)|  | 

### Return type

[**CreateDatabaseInstance201Response**](CreateDatabaseInstance201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON c ключом &#x60;instance&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_database_s3_backup**
> CreateDatabaseS3Backup201Response create_database_s3_backup(db_id, create_s3_backup=create_s3_backup)

Создание S3-бэкапа базы данных

Чтобы создать резервную копию кластера базы данных в объектном хранилище, отправьте POST-запрос на `/api/v2/databases/{db_id}/backups`.   Тело запроса необязательно: единственное поле `comment` можно не передавать. Тело ответа будет представлять собой объект JSON с ключом `backup`.   Копия создается асинхронно. Пока она создается, ее статус — `running`, и восстановиться из нее нельзя. Дождитесь статуса `success`, опрашивая `/api/v2/databases/{db_id}/backups/{backup_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_database_s3_backup201_response import CreateDatabaseS3Backup201Response
from timeweb_cloud_api.models.create_s3_backup import CreateS3Backup
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    create_s3_backup = timeweb_cloud_api.CreateS3Backup() # CreateS3Backup |  (optional)

    try:
        # Создание S3-бэкапа базы данных
        api_response = api_instance.create_database_s3_backup(db_id, create_s3_backup=create_s3_backup)
        print("The response of DatabasesApi->create_database_s3_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->create_database_s3_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **create_s3_backup** | [**CreateS3Backup**](CreateS3Backup.md)|  | [optional] 

### Return type

[**CreateDatabaseS3Backup201Response**](CreateDatabaseS3Backup201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON с ключом &#x60;backup&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_database_user**
> CreateDatabaseUser201Response create_database_user(db_cluster_id, create_admin)

Создание пользователя базы данных

Чтобы создать пользователя базы данных, отправьте POST-запрос на `/api/v1/databases/{db_cluster_id}/admins`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_admin import CreateAdmin
from timeweb_cloud_api.models.create_database_user201_response import CreateDatabaseUser201Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных
    create_admin = timeweb_cloud_api.CreateAdmin() # CreateAdmin | 

    try:
        # Создание пользователя базы данных
        api_response = api_instance.create_database_user(db_cluster_id, create_admin)
        print("The response of DatabasesApi->create_database_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->create_database_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 
 **create_admin** | [**CreateAdmin**](CreateAdmin.md)|  | 

### Return type

[**CreateDatabaseUser201Response**](CreateDatabaseUser201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Ответ будет представлять собой объект JSON c ключом &#x60;admin&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database_backup**
> delete_database_backup(db_id, backup_id)

Удаление бэкапа базы данных

Чтобы удалить бэкап базы данных, отправьте запрос DELETE в `api/v1/dbs/{db_id}/backups/{backup_id}`. 

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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    backup_id = None # object | ID резервной копии

    try:
        # Удаление бэкапа базы данных
        api_instance.delete_database_backup(db_id, backup_id)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_database_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **backup_id** | [**object**](.md)| ID резервной копии | 

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
**204** | Бэкап успешно удален. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database_cluster**
> DeleteDatabaseCluster200Response delete_database_cluster(db_cluster_id)

Удаление кластера базы данных

Чтобы удалить кластер базы данных, отправьте DELETE-запрос на `/api/v1/databases/{db_cluster_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.delete_database_cluster200_response import DeleteDatabaseCluster200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных

    try:
        # Удаление кластера базы данных
        api_response = api_instance.delete_database_cluster(db_cluster_id)
        print("The response of DatabasesApi->delete_database_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_database_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 

### Return type

[**DeleteDatabaseCluster200Response**](DeleteDatabaseCluster200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Если для удаления кластера требуется подтверждение, кластер не удаляется сразу: ответ будет представлять собой объект JSON c ключом &#x60;database_delete&#x60;. |  -  |
**204** | Кластер базы данных удален. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database_instance**
> delete_database_instance(db_cluster_id, instance_id)

Удаление инстанса базы данных

Чтобы удалить инстанс базы данных, отправьте DELETE-запрос на `/api/v1/databases/{db_cluster_id}/instances/{instance_id}`.

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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных
    instance_id = None # object | ID инстанса базы данных

    try:
        # Удаление инстанса базы данных
        api_instance.delete_database_instance(db_cluster_id, instance_id)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_database_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 
 **instance_id** | [**object**](.md)| ID инстанса базы данных | 

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
**204** | Инстанс базы данных удален. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database_s3_backup**
> delete_database_s3_backup(db_id, backup_id)

Удаление S3-бэкапа базы данных

Чтобы удалить резервную копию кластера базы данных из объектного хранилища, отправьте DELETE-запрос на `/api/v2/databases/{db_id}/backups/{backup_id}`.   Копия удаляется безвозвратно, тело ответа пустое. На резервные копии из `/api/v1/dbs/{db_id}/backups/{backup_id}` этот метод не действует — они удаляются отдельным запросом.

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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    backup_id = None # object | ID резервной копии в формате UUID

    try:
        # Удаление S3-бэкапа базы данных
        api_instance.delete_database_s3_backup(db_id, backup_id)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_database_s3_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **backup_id** | [**object**](.md)| ID резервной копии в формате UUID | 

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
**204** | Резервная копия успешно удалена. Тело ответа пустое. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_database_user**
> delete_database_user(db_cluster_id, admin_id)

Удаление пользователя базы данных

Чтобы удалить пользователя базы данных на вашем аккаунте, отправьте DELETE-запрос на `/api/v1/databases/{db_cluster_id}/admins/{admin_id}`.

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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных
    admin_id = None # object | ID пользователя базы данных

    try:
        # Удаление пользователя базы данных
        api_instance.delete_database_user(db_cluster_id, admin_id)
    except Exception as e:
        print("Exception when calling DatabasesApi->delete_database_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 
 **admin_id** | [**object**](.md)| ID пользователя базы данных | 

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
**204** | Пользователь базы данных удален. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_auto_backups_settings**
> GetDatabaseAutoBackupsSettings200Response get_database_auto_backups_settings(db_id)

Получение настроек автобэкапов базы данных

Чтобы получить список настроек автобэкапов базы данных, отправьте запрос GET в `api/v1/dbs/{db_id}/auto-backups`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_auto_backups_settings200_response import GetDatabaseAutoBackupsSettings200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных

    try:
        # Получение настроек автобэкапов базы данных
        api_response = api_instance.get_database_auto_backups_settings(db_id)
        print("The response of DatabasesApi->get_database_auto_backups_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_auto_backups_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 

### Return type

[**GetDatabaseAutoBackupsSettings200Response**](GetDatabaseAutoBackupsSettings200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;auto_backups_settings&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_backup**
> GetDatabaseBackup200Response get_database_backup(db_id, backup_id)

Получение бэкапа базы данных

Чтобы получить бэкап базы данных, отправьте запрос GET в `api/v1/dbs/{db_id}/backups/{backup_id}`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_backup200_response import GetDatabaseBackup200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    backup_id = None # object | ID резервной копии

    try:
        # Получение бэкапа базы данных
        api_response = api_instance.get_database_backup(db_id, backup_id)
        print("The response of DatabasesApi->get_database_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **backup_id** | [**object**](.md)| ID резервной копии | 

### Return type

[**GetDatabaseBackup200Response**](GetDatabaseBackup200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;backup&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_backups**
> GetDatabaseBackups200Response get_database_backups(db_id, limit=limit, offset=offset)

Список бэкапов базы данных

Чтобы получить список бэкапов базы данных, отправьте запрос GET в `api/v1/dbs/{db_id}/backups`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_backups200_response import GetDatabaseBackups200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)

    try:
        # Список бэкапов базы данных
        api_response = api_instance.get_database_backups(db_id, limit=limit, offset=offset)
        print("The response of DatabasesApi->get_database_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_backups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 

### Return type

[**GetDatabaseBackups200Response**](GetDatabaseBackups200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;backups&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_cluster**
> CreateDatabaseCluster201Response get_database_cluster(db_cluster_id)

Получение кластера базы данных

Чтобы получить кластер базы данных на вашем аккаунте, отправьте GET-запрос на `/api/v1/databases/{db_cluster_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_database_cluster201_response import CreateDatabaseCluster201Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных

    try:
        # Получение кластера базы данных
        api_response = api_instance.get_database_cluster(db_cluster_id)
        print("The response of DatabasesApi->get_database_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 

### Return type

[**CreateDatabaseCluster201Response**](CreateDatabaseCluster201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;db&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_cluster_replicas**
> GetDatabaseClusterReplicas200Response get_database_cluster_replicas(db_cluster_id)

Получение списка реплик кластера базы данных

Чтобы получить список реплик кластера базы данных, отправьте GET-запрос на `/api/v1/databases/{db_cluster_id}/replicas`.   Тело ответа будет представлять собой объект JSON с ключом `replicas`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_cluster_replicas200_response import GetDatabaseClusterReplicas200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных

    try:
        # Получение списка реплик кластера базы данных
        api_response = api_instance.get_database_cluster_replicas(db_cluster_id)
        print("The response of DatabasesApi->get_database_cluster_replicas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_cluster_replicas: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 

### Return type

[**GetDatabaseClusterReplicas200Response**](GetDatabaseClusterReplicas200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;replicas&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_cluster_types**
> GetDatabaseClusterTypes200Response get_database_cluster_types()

Получение списка типов кластеров баз данных

Чтобы получить список типов баз данных на вашем аккаунте, отправьте GET-запрос на `/api/v1/database-types`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_cluster_types200_response import GetDatabaseClusterTypes200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)

    try:
        # Получение списка типов кластеров баз данных
        api_response = api_instance.get_database_cluster_types()
        print("The response of DatabasesApi->get_database_cluster_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_cluster_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetDatabaseClusterTypes200Response**](GetDatabaseClusterTypes200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;types&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_clusters**
> GetDatabaseClusters200Response get_database_clusters(limit=limit, offset=offset)

Получение списка кластеров баз данных

Чтобы получить список кластеров баз данных, отправьте GET-запрос на `/api/v1/databases`.   Тело ответа будет представлять собой объект JSON с ключом `dbs`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_clusters200_response import GetDatabaseClusters200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)

    try:
        # Получение списка кластеров баз данных
        api_response = api_instance.get_database_clusters(limit=limit, offset=offset)
        print("The response of DatabasesApi->get_database_clusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_clusters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 

### Return type

[**GetDatabaseClusters200Response**](GetDatabaseClusters200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;dbs&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_configurators**
> GetDatabaseConfigurators200Response get_database_configurators(cluster_id=cluster_id, with_unavailable=with_unavailable)

Получение списка конфигураторов баз данных

Чтобы получить список конфигураторов баз данных, отправьте GET-запрос на `/api/v1/configurator/databases`.   Конфигуратор позволяет создать кластер с произвольным количеством ресурсов вместо готового тарифа: его ID передается при создании кластера в поле `configuration.configurator_id`, а допустимые значения ресурсов ограничены объектом `requirements`.   Тело ответа будет представлять собой объект JSON с ключом `database_configurators`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_configurators200_response import GetDatabaseConfigurators200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    cluster_id = None # object | ID кластера базы данных. Возвращает конфигураторы группы, в пределах которой доступна смена конфигурации этого кластера (сценарий изменения кластера). (optional)
    with_unavailable = None # object | Включить в ответ конфигураторы, недоступные к заказу из-за нехватки свободных ресурсов. Учитывается только при запросе без `cluster_id`. (optional)

    try:
        # Получение списка конфигураторов баз данных
        api_response = api_instance.get_database_configurators(cluster_id=cluster_id, with_unavailable=with_unavailable)
        print("The response of DatabasesApi->get_database_configurators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_configurators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| ID кластера базы данных. Возвращает конфигураторы группы, в пределах которой доступна смена конфигурации этого кластера (сценарий изменения кластера). | [optional] 
 **with_unavailable** | [**object**](.md)| Включить в ответ конфигураторы, недоступные к заказу из-за нехватки свободных ресурсов. Учитывается только при запросе без &#x60;cluster_id&#x60;. | [optional] 

### Return type

[**GetDatabaseConfigurators200Response**](GetDatabaseConfigurators200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Конфигураторы успешно получены. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_default_parameters**
> GetDatabaseDefaultParameters200Response get_database_default_parameters(type, ram, replica_count=replica_count)

Получение рекомендуемых значений параметров баз данных

Чтобы получить рекомендуемые значения параметров базы данных, отправьте GET-запрос на `/api/v1/dbs/default-parameters`.   Значения рассчитываются для указанного типа кластера, объема оперативной памяти и количества реплик — их можно передать при создании кластера в поле `config_parameters`. Список имен параметров, доступных для каждого типа кластера, возвращает `GET /api/v1/dbs/parameters`.   Тело ответа будет представлять собой объект JSON с ключом `config_params`. Рекомендуемые значения рассчитываются только для кластеров MySQL, PostgreSQL и Valkey — для остальных типов возвращается пустой объект.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_default_parameters200_response import GetDatabaseDefaultParameters200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    type = postgres17 # object | Тип кластера базы данных.
    ram = 2048 # object | Объём оперативной памяти кластера (в Мб).
    replica_count = 1 # object | Количество нод (реплик) кластера. (optional)

    try:
        # Получение рекомендуемых значений параметров баз данных
        api_response = api_instance.get_database_default_parameters(type, ram, replica_count=replica_count)
        print("The response of DatabasesApi->get_database_default_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_default_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**object**](.md)| Тип кластера базы данных. | 
 **ram** | [**object**](.md)| Объём оперативной памяти кластера (в Мб). | 
 **replica_count** | [**object**](.md)| Количество нод (реплик) кластера. | [optional] 

### Return type

[**GetDatabaseDefaultParameters200Response**](GetDatabaseDefaultParameters200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Рекомендуемые значения параметров успешно получены. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_instance**
> CreateDatabaseInstance201Response get_database_instance(db_cluster_id, instance_id)

Получение инстанса базы данных

Чтобы получить инстанс базы данных, отправьте GET-запрос на `/api/v1/databases/{db_cluster_id}/instances/{instance_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_database_instance201_response import CreateDatabaseInstance201Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных
    instance_id = None # object | ID инстанса базы данных

    try:
        # Получение инстанса базы данных
        api_response = api_instance.get_database_instance(db_cluster_id, instance_id)
        print("The response of DatabasesApi->get_database_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 
 **instance_id** | [**object**](.md)| ID инстанса базы данных | 

### Return type

[**CreateDatabaseInstance201Response**](CreateDatabaseInstance201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;instance&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_instances**
> GetDatabaseInstances200Response get_database_instances(db_cluster_id)

Получение списка инстансов баз данных

Чтобы получить список баз данных на вашем аккаунте, отправьте GET-запрос на `/api/v1/databases/{db_cluster_id}/instances`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_instances200_response import GetDatabaseInstances200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных

    try:
        # Получение списка инстансов баз данных
        api_response = api_instance.get_database_instances(db_cluster_id)
        print("The response of DatabasesApi->get_database_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_instances: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 

### Return type

[**GetDatabaseInstances200Response**](GetDatabaseInstances200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;instances&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_parameters**
> DbParametersByType get_database_parameters()

Получение списка параметров баз данных

Чтобы получить список параметров баз данных, отправьте GET-запрос на `/api/v1/dbs/parameters`.   Ответ содержит только имена параметров, доступных для каждого типа кластера. Рекомендуемые значения этих параметров для конкретной конфигурации возвращает `GET /api/v1/dbs/default-parameters`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.db_parameters_by_type import DbParametersByType
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)

    try:
        # Получение списка параметров баз данных
        api_response = api_instance.get_database_parameters()
        print("The response of DatabasesApi->get_database_parameters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_parameters: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**DbParametersByType**](DbParametersByType.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON, ключи которого — типы кластеров баз данных, а значения — массивы имён доступных параметров. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_preset**
> GetDatabasePreset200Response get_database_preset(preset_id)

Получение тарифа для базы данных

Чтобы получить тариф для базы данных, отправьте GET-запрос на `/api/v2/dbs/presets/{preset_id}`.   Тело ответа будет представлять собой объект JSON с ключом `databases_preset`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_preset200_response import GetDatabasePreset200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    preset_id = None # object | ID тарифа

    try:
        # Получение тарифа для базы данных
        api_response = api_instance.get_database_preset(preset_id)
        print("The response of DatabasesApi->get_database_preset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_preset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **preset_id** | [**object**](.md)| ID тарифа | 

### Return type

[**GetDatabasePreset200Response**](GetDatabasePreset200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Тариф успешно получен. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_privileges**
> GetDatabasePrivileges200Response get_database_privileges(db_cluster_id)

Получение привилегий кластера базы данных

Чтобы получить список привилегий, которые можно выдать пользователям кластера базы данных, отправьте GET-запрос на `/api/v1/databases/{db_cluster_id}/privileges`.\\    Список зависит от типа СУБД кластера и определяется сервером автоматически: возвращаются только те привилегии, которые допустимы для этого кластера. Используйте его, чтобы заполнить поле `privileges` при <a href='#tag/Bazy-dannyh/operation/createDatabaseUser'>создании</a> или <a href='#tag/Bazy-dannyh/operation/updateDatabaseUser'>изменении</a> пользователя базы данных.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_privileges200_response import GetDatabasePrivileges200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных

    try:
        # Получение привилегий кластера базы данных
        api_response = api_instance.get_database_privileges(db_cluster_id)
        print("The response of DatabasesApi->get_database_privileges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_privileges: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 

### Return type

[**GetDatabasePrivileges200Response**](GetDatabasePrivileges200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;privileges&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_s3_backup**
> CreateDatabaseS3Backup201Response get_database_s3_backup(db_id, backup_id)

Получение S3-бэкапа базы данных

Чтобы получить информацию о резервной копии кластера базы данных в объектном хранилище, отправьте GET-запрос на `/api/v2/databases/{db_id}/backups/{backup_id}`.   Тело ответа будет представлять собой объект JSON с ключом `backup`. Обратите внимание, что `backup_id` здесь — строка в формате UUID, а не число, как в `/api/v1/dbs/{db_id}/backups/{backup_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_database_s3_backup201_response import CreateDatabaseS3Backup201Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    backup_id = None # object | ID резервной копии в формате UUID

    try:
        # Получение S3-бэкапа базы данных
        api_response = api_instance.get_database_s3_backup(db_id, backup_id)
        print("The response of DatabasesApi->get_database_s3_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_s3_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **backup_id** | [**object**](.md)| ID резервной копии в формате UUID | 

### Return type

[**CreateDatabaseS3Backup201Response**](CreateDatabaseS3Backup201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;backup&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_s3_backups**
> GetDatabaseS3Backups200Response get_database_s3_backups(db_id)

Список S3-бэкапов базы данных

Чтобы получить список резервных копий кластера базы данных в объектном хранилище, отправьте GET-запрос на `/api/v2/databases/{db_id}/backups`.   Тело ответа будет представлять собой объект JSON с ключом `backups`. Копии отсортированы по дате создания по убыванию — сначала самые свежие.   Резервное копирование в объектное хранилище доступно для кластеров MySQL и PostgreSQL. Идентификатор такой копии — строка в формате UUID; это отдельный от `/api/v1/dbs/{db_id}/backups` механизм, и идентификаторы копий между ними не взаимозаменяемы.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_s3_backups200_response import GetDatabaseS3Backups200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных

    try:
        # Список S3-бэкапов базы данных
        api_response = api_instance.get_database_s3_backups(db_id)
        print("The response of DatabasesApi->get_database_s3_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_s3_backups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 

### Return type

[**GetDatabaseS3Backups200Response**](GetDatabaseS3Backups200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;backups&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_user**
> CreateDatabaseUser201Response get_database_user(db_cluster_id, admin_id)

Получение пользователя базы данных

Чтобы получить пользователя базы данных на вашем аккаунте, отправьте GET-запрос на `/api/v1/databases/{db_cluster_id}/admins/{admin_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_database_user201_response import CreateDatabaseUser201Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных
    admin_id = None # object | ID пользователя базы данных

    try:
        # Получение пользователя базы данных
        api_response = api_instance.get_database_user(db_cluster_id, admin_id)
        print("The response of DatabasesApi->get_database_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 
 **admin_id** | [**object**](.md)| ID пользователя базы данных | 

### Return type

[**CreateDatabaseUser201Response**](CreateDatabaseUser201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;admin&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_database_users**
> GetDatabaseUsers200Response get_database_users(db_cluster_id)

Получение списка пользователей базы данных

Чтобы получить список пользователей базы данных на вашем аккаунте, отправьте GET-запрос на `/api/v1/databases/{db_cluster_id}/admins`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_users200_response import GetDatabaseUsers200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных

    try:
        # Получение списка пользователей базы данных
        api_response = api_instance.get_database_users(db_cluster_id)
        print("The response of DatabasesApi->get_database_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_database_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 

### Return type

[**GetDatabaseUsers200Response**](GetDatabaseUsers200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;admins&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_databases_presets**
> GetDatabasesPresets200Response get_databases_presets(cluster_id=cluster_id, with_unavailable=with_unavailable)

Получение списка тарифов для баз данных

Чтобы получить список тарифов для баз данных, отправьте GET-запрос на `/api/v2/presets/dbs`.   Без параметров возвращаются тарифы, доступные к заказу — этот список используется при создании кластера. Если передать `cluster_id`, вернутся тарифы группы, в пределах которой можно сменить тариф указанного кластера.   Тело ответа будет представлять собой объект JSON с ключом `databases_presets`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_databases_presets200_response import GetDatabasesPresets200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    cluster_id = None # object | ID кластера базы данных. Возвращает тарифы группы, в пределах которой доступна смена тарифа этого кластера (сценарий изменения кластера). (optional)
    with_unavailable = None # object | Включить в ответ тарифы, недоступные к заказу из-за нехватки свободных ресурсов. Учитывается только при запросе без `cluster_id`: вместе с `cluster_id` фильтр по свободным ресурсам и так не применяется. (optional)

    try:
        # Получение списка тарифов для баз данных
        api_response = api_instance.get_databases_presets(cluster_id=cluster_id, with_unavailable=with_unavailable)
        print("The response of DatabasesApi->get_databases_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->get_databases_presets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | [**object**](.md)| ID кластера базы данных. Возвращает тарифы группы, в пределах которой доступна смена тарифа этого кластера (сценарий изменения кластера). | [optional] 
 **with_unavailable** | [**object**](.md)| Включить в ответ тарифы, недоступные к заказу из-за нехватки свободных ресурсов. Учитывается только при запросе без &#x60;cluster_id&#x60;: вместе с &#x60;cluster_id&#x60; фильтр по свободным ресурсам и так не применяется. | [optional] 

### Return type

[**GetDatabasesPresets200Response**](GetDatabasesPresets200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Тарифы успешно получены. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_database_cluster_action**
> perform_database_cluster_action(db_cluster_id, cluster_action)

Выполнение действия над кластером базы данных

Чтобы выполнить действие над кластером базы данных, отправьте POST-запрос на `/api/v1/databases/{db_cluster_id}/action`.   Доступные действия: `reboot` — перезагрузка кластера, `shutdown` — выключение кластера, `start` — включение кластера.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.cluster_action import ClusterAction
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных
    cluster_action = timeweb_cloud_api.ClusterAction() # ClusterAction | 

    try:
        # Выполнение действия над кластером базы данных
        api_instance.perform_database_cluster_action(db_cluster_id, cluster_action)
    except Exception as e:
        print("Exception when calling DatabasesApi->perform_database_cluster_action: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 
 **cluster_action** | [**ClusterAction**](ClusterAction.md)|  | 

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
**201** | Действие принято к выполнению. Тело ответа пустое. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_database_from_backup**
> restore_database_from_backup(db_id, backup_id)

Восстановление базы данных из бэкапа

Чтобы восстановить базу данных из бэкапа, отправьте запрос PUT в `api/v1/dbs/{db_id}/backups/{backup_id}`. 

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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    backup_id = None # object | ID резервной копии

    try:
        # Восстановление базы данных из бэкапа
        api_instance.restore_database_from_backup(db_id, backup_id)
    except Exception as e:
        print("Exception when calling DatabasesApi->restore_database_from_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **backup_id** | [**object**](.md)| ID резервной копии | 

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
**204** | База данных из бэкапа успешно восстановлена. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_database_from_s3_backup**
> restore_database_from_s3_backup(db_id, backup_id)

Восстановление базы данных из S3-бэкапа

Чтобы восстановить кластер базы данных из резервной копии в объектном хранилище, отправьте POST-запрос на `/api/v2/databases/{db_id}/backups/{backup_id}/restore`.   Тела запроса нет, тело ответа пустое. Восстановиться можно только из копии со статусом `success`.   Сразу после запуска кластер переходит в статус `backup_recovery`. Пока восстановление не завершится, создание, изменение и удаление резервных копий, а также повторный запуск восстановления недоступны.

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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    backup_id = None # object | ID резервной копии в формате UUID

    try:
        # Восстановление базы данных из S3-бэкапа
        api_instance.restore_database_from_s3_backup(db_id, backup_id)
    except Exception as e:
        print("Exception when calling DatabasesApi->restore_database_from_s3_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **backup_id** | [**object**](.md)| ID резервной копии в формате UUID | 

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
**204** | Восстановление успешно запущено. Тело ответа пустое. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database_auto_backups_settings**
> GetDatabaseAutoBackupsSettings200Response update_database_auto_backups_settings(db_id, update_auto_backup)

Изменение настроек автобэкапов базы данных

Чтобы изменить список настроек автобэкапов базы данных, отправьте запрос PATCH в `api/v1/dbs/{db_id}/auto-backups`

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_database_auto_backups_settings200_response import GetDatabaseAutoBackupsSettings200Response
from timeweb_cloud_api.models.update_auto_backup import UpdateAutoBackup
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    update_auto_backup = timeweb_cloud_api.UpdateAutoBackup() # UpdateAutoBackup | При значении `is_enabled`: `true`, поля `copy_count`, `creation_start_at`, `interval` являются обязательными

    try:
        # Изменение настроек автобэкапов базы данных
        api_response = api_instance.update_database_auto_backups_settings(db_id, update_auto_backup)
        print("The response of DatabasesApi->update_database_auto_backups_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->update_database_auto_backups_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **update_auto_backup** | [**UpdateAutoBackup**](UpdateAutoBackup.md)| При значении &#x60;is_enabled&#x60;: &#x60;true&#x60;, поля &#x60;copy_count&#x60;, &#x60;creation_start_at&#x60;, &#x60;interval&#x60; являются обязательными | 

### Return type

[**GetDatabaseAutoBackupsSettings200Response**](GetDatabaseAutoBackupsSettings200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;auto_backups_settings&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database_backup**
> GetDatabaseBackup200Response update_database_backup(db_id, backup_id, dbs_update_backup)

Изменение комментария к бэкапу базы данных

Чтобы изменить комментарий к бэкапу базы данных, отправьте PATCH-запрос на `/api/v1/dbs/{db_id}/backups/{backup_id}`.  Тело ответа будет представлять собой объект JSON с ключом `backup`. 

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.dbs_update_backup import DbsUpdateBackup
from timeweb_cloud_api.models.get_database_backup200_response import GetDatabaseBackup200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    backup_id = None # object | ID резервной копии
    dbs_update_backup = timeweb_cloud_api.DbsUpdateBackup() # DbsUpdateBackup | 

    try:
        # Изменение комментария к бэкапу базы данных
        api_response = api_instance.update_database_backup(db_id, backup_id, dbs_update_backup)
        print("The response of DatabasesApi->update_database_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->update_database_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **backup_id** | [**object**](.md)| ID резервной копии | 
 **dbs_update_backup** | [**DbsUpdateBackup**](DbsUpdateBackup.md)|  | 

### Return type

[**GetDatabaseBackup200Response**](GetDatabaseBackup200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;backup&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database_cluster**
> UpdateDatabaseCluster200Response update_database_cluster(db_cluster_id, update_cluster)

Изменение кластера базы данных

Чтобы изменить кластер базы данных на вашем аккаунте, отправьте PATCH-запрос на `/api/v1/databases/{db_cluster_id}`.   Размер кластера задается либо тарифом (`preset_id`), либо конфигуратором (`configuration`) — эти поля взаимоисключающие.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.update_cluster import UpdateCluster
from timeweb_cloud_api.models.update_database_cluster200_response import UpdateDatabaseCluster200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных
    update_cluster = timeweb_cloud_api.UpdateCluster() # UpdateCluster | 

    try:
        # Изменение кластера базы данных
        api_response = api_instance.update_database_cluster(db_cluster_id, update_cluster)
        print("The response of DatabasesApi->update_database_cluster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->update_database_cluster: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 
 **update_cluster** | [**UpdateCluster**](UpdateCluster.md)|  | 

### Return type

[**UpdateDatabaseCluster200Response**](UpdateDatabaseCluster200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;db&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database_cluster_v2**
> UpdateDatabaseCluster200Response update_database_cluster_v2(db_cluster_id, update_cluster_v2)

Изменение кластера базы данных (v2)

Чтобы изменить кластер базы данных на вашем аккаунте, отправьте PATCH-запрос на `/api/v2/databases/{db_cluster_id}`.   В отличие от `/api/v1/databases/{db_cluster_id}`, эта версия дополнительно позволяет привязать плавающий IP-адрес (`floating_ip`).   Размер кластера задается либо тарифом (`preset_id`), либо конфигуратором (`configuration`) — эти поля взаимоисключающие.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.update_cluster_v2 import UpdateClusterV2
from timeweb_cloud_api.models.update_database_cluster200_response import UpdateDatabaseCluster200Response
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных
    update_cluster_v2 = timeweb_cloud_api.UpdateClusterV2() # UpdateClusterV2 | 

    try:
        # Изменение кластера базы данных (v2)
        api_response = api_instance.update_database_cluster_v2(db_cluster_id, update_cluster_v2)
        print("The response of DatabasesApi->update_database_cluster_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->update_database_cluster_v2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 
 **update_cluster_v2** | [**UpdateClusterV2**](UpdateClusterV2.md)|  | 

### Return type

[**UpdateDatabaseCluster200Response**](UpdateDatabaseCluster200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;db&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database_instance**
> CreateDatabaseInstance201Response update_database_instance(db_cluster_id, instance_id, update_instance)

Изменение инстанса базы данных

Чтобы изменить инстанс базы данных, отправьте PATCH-запрос на `/api/v1/databases/{db_cluster_id}/instances/{instance_id}`.   Изменить название базы данных (`name`) и ее владельца (`owner_id`) можно только в кластере PostgreSQL, а настройки топика (`config_parameters`) — только в кластере Kafka. Если один из этих трех параметров передан для неподходящего типа кластера, запрос вернется с ошибкой 409.   Расширения (`extensions`) применимы к кластерам PostgreSQL и RabbitMQ.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_database_instance201_response import CreateDatabaseInstance201Response
from timeweb_cloud_api.models.update_instance import UpdateInstance
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных
    instance_id = None # object | ID инстанса базы данных
    update_instance = timeweb_cloud_api.UpdateInstance() # UpdateInstance | 

    try:
        # Изменение инстанса базы данных
        api_response = api_instance.update_database_instance(db_cluster_id, instance_id, update_instance)
        print("The response of DatabasesApi->update_database_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->update_database_instance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 
 **instance_id** | [**object**](.md)| ID инстанса базы данных | 
 **update_instance** | [**UpdateInstance**](UpdateInstance.md)|  | 

### Return type

[**CreateDatabaseInstance201Response**](CreateDatabaseInstance201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;instance&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database_s3_backup**
> CreateDatabaseS3Backup201Response update_database_s3_backup(db_id, backup_id, update_s3_backup=update_s3_backup)

Изменение комментария S3-бэкапа базы данных

Чтобы изменить комментарий к резервной копии кластера базы данных, отправьте PATCH-запрос на `/api/v2/databases/{db_id}/backups/{backup_id}`.   Изменить можно только комментарий: других полей метод не принимает, сама резервная копия при этом не пересоздается. Тело ответа будет представлять собой объект JSON с ключом `backup`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_database_s3_backup201_response import CreateDatabaseS3Backup201Response
from timeweb_cloud_api.models.update_s3_backup import UpdateS3Backup
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_id = None # object | ID базы данных
    backup_id = None # object | ID резервной копии в формате UUID
    update_s3_backup = timeweb_cloud_api.UpdateS3Backup() # UpdateS3Backup |  (optional)

    try:
        # Изменение комментария S3-бэкапа базы данных
        api_response = api_instance.update_database_s3_backup(db_id, backup_id, update_s3_backup=update_s3_backup)
        print("The response of DatabasesApi->update_database_s3_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->update_database_s3_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_id** | [**object**](.md)| ID базы данных | 
 **backup_id** | [**object**](.md)| ID резервной копии в формате UUID | 
 **update_s3_backup** | [**UpdateS3Backup**](UpdateS3Backup.md)|  | [optional] 

### Return type

[**CreateDatabaseS3Backup201Response**](CreateDatabaseS3Backup201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON с ключом &#x60;backup&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_database_user**
> CreateDatabaseUser201Response update_database_user(db_cluster_id, admin_id, update_admin)

Изменение пользователя базы данных

Чтобы изменить пользователя базы данных на вашем аккаунте, отправьте PATCH-запрос на `/api/v1/databases/{db_cluster_id}/admins/{admin_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_database_user201_response import CreateDatabaseUser201Response
from timeweb_cloud_api.models.update_admin import UpdateAdmin
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
    api_instance = timeweb_cloud_api.DatabasesApi(api_client)
    db_cluster_id = None # object | ID кластера базы данных
    admin_id = None # object | ID пользователя базы данных
    update_admin = timeweb_cloud_api.UpdateAdmin() # UpdateAdmin | 

    try:
        # Изменение пользователя базы данных
        api_response = api_instance.update_database_user(db_cluster_id, admin_id, update_admin)
        print("The response of DatabasesApi->update_database_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DatabasesApi->update_database_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **db_cluster_id** | [**object**](.md)| ID кластера базы данных | 
 **admin_id** | [**object**](.md)| ID пользователя базы данных | 
 **update_admin** | [**UpdateAdmin**](UpdateAdmin.md)|  | 

### Return type

[**CreateDatabaseUser201Response**](CreateDatabaseUser201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ будет представлять собой объект JSON c ключом &#x60;admin&#x60;. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

