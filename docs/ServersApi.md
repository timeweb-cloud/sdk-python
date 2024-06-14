# timeweb_cloud_api.ServersApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_server_ip**](ServersApi.md#add_server_ip) | **POST** /api/v1/servers/{server_id}/ips | Добавление IP-адреса сервера
[**clone_server**](ServersApi.md#clone_server) | **POST** /api/v1/servers/{server_id}/clone | Клонирование сервера
[**create_server**](ServersApi.md#create_server) | **POST** /api/v1/servers | Создание сервера
[**create_server_disk**](ServersApi.md#create_server_disk) | **POST** /api/v1/servers/{server_id}/disks | Создание диска сервера
[**create_server_disk_backup**](ServersApi.md#create_server_disk_backup) | **POST** /api/v1/servers/{server_id}/disks/{disk_id}/backups | Создание бэкапа диска сервера
[**delete_server**](ServersApi.md#delete_server) | **DELETE** /api/v1/servers/{server_id} | Удаление сервера
[**delete_server_disk**](ServersApi.md#delete_server_disk) | **DELETE** /api/v1/servers/{server_id}/disks/{disk_id} | Удаление диска сервера
[**delete_server_disk_backup**](ServersApi.md#delete_server_disk_backup) | **DELETE** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id} | Удаление бэкапа диска сервера
[**delete_server_ip**](ServersApi.md#delete_server_ip) | **DELETE** /api/v1/servers/{server_id}/ips | Удаление IP-адреса сервера
[**get_configurators**](ServersApi.md#get_configurators) | **GET** /api/v1/configurator/servers | Получение списка конфигураторов серверов
[**get_os_list**](ServersApi.md#get_os_list) | **GET** /api/v1/os/servers | Получение списка операционных систем
[**get_server**](ServersApi.md#get_server) | **GET** /api/v1/servers/{server_id} | Получение сервера
[**get_server_disk**](ServersApi.md#get_server_disk) | **GET** /api/v1/servers/{server_id}/disks/{disk_id} | Получение диска сервера
[**get_server_disk_auto_backup_settings**](ServersApi.md#get_server_disk_auto_backup_settings) | **GET** /api/v1/servers/{server_id}/disks/{disk_id}/auto-backups | Получить настройки автобэкапов диска сервера
[**get_server_disk_backup**](ServersApi.md#get_server_disk_backup) | **GET** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id} | Получение бэкапа диска сервера
[**get_server_disk_backups**](ServersApi.md#get_server_disk_backups) | **GET** /api/v1/servers/{server_id}/disks/{disk_id}/backups | Получение списка бэкапов диска сервера
[**get_server_disks**](ServersApi.md#get_server_disks) | **GET** /api/v1/servers/{server_id}/disks | Получение списка дисков сервера
[**get_server_ips**](ServersApi.md#get_server_ips) | **GET** /api/v1/servers/{server_id}/ips | Получение списка IP-адресов сервера
[**get_server_logs**](ServersApi.md#get_server_logs) | **GET** /api/v1/servers/{server_id}/logs | Получение списка логов сервера
[**get_server_statistics**](ServersApi.md#get_server_statistics) | **GET** /api/v1/servers/{server_id}/statistics | Получение статистики сервера
[**get_servers**](ServersApi.md#get_servers) | **GET** /api/v1/servers | Получение списка серверов
[**get_servers_presets**](ServersApi.md#get_servers_presets) | **GET** /api/v1/presets/servers | Получение списка тарифов серверов
[**get_software**](ServersApi.md#get_software) | **GET** /api/v1/software/servers | Получение списка ПО из маркетплейса
[**hard_shutdown_server**](ServersApi.md#hard_shutdown_server) | **POST** /api/v1/servers/{server_id}/hard-shutdown | Принудительное выключение сервера
[**image_unmount_and_server_reload**](ServersApi.md#image_unmount_and_server_reload) | **POST** /api/v1/servers/{server_id}/image-unmount | Отмонтирование ISO образа и перезагрузка сервера
[**install_server**](ServersApi.md#install_server) | **POST** /api/v1/servers/{server_id}/install | Установка сервера
[**perform_action_on_backup**](ServersApi.md#perform_action_on_backup) | **POST** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id}/action | Выполнение действия над бэкапом диска сервера
[**perform_action_on_server**](ServersApi.md#perform_action_on_server) | **POST** /api/v1/servers/{server_id}/action | Выполнение действия над сервером
[**reboot_server**](ServersApi.md#reboot_server) | **POST** /api/v1/servers/{server_id}/reboot | Перезагрузка сервера
[**reset_server_password**](ServersApi.md#reset_server_password) | **POST** /api/v1/servers/{server_id}/reset-password | Сброс пароля сервера
[**shutdown_server**](ServersApi.md#shutdown_server) | **POST** /api/v1/servers/{server_id}/shutdown | Выключение сервера
[**start_server**](ServersApi.md#start_server) | **POST** /api/v1/servers/{server_id}/start | Запуск сервера
[**update_server**](ServersApi.md#update_server) | **PATCH** /api/v1/servers/{server_id} | Изменение сервера
[**update_server_disk**](ServersApi.md#update_server_disk) | **PATCH** /api/v1/servers/{server_id}/disks/{disk_id} | Изменение параметров диска сервера
[**update_server_disk_auto_backup_settings**](ServersApi.md#update_server_disk_auto_backup_settings) | **PATCH** /api/v1/servers/{server_id}/disks/{disk_id}/auto-backups | Изменение настроек автобэкапов диска сервера
[**update_server_disk_backup**](ServersApi.md#update_server_disk_backup) | **PATCH** /api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id} | Изменение бэкапа диска сервера
[**update_server_ip**](ServersApi.md#update_server_ip) | **PATCH** /api/v1/servers/{server_id}/ips | Изменение IP-адреса сервера
[**update_server_nat**](ServersApi.md#update_server_nat) | **PATCH** /api/v1/servers/{server_id}/local-networks/nat-mode | Изменение правил маршрутизации трафика сервера (NAT)
[**update_server_os_boot_mode**](ServersApi.md#update_server_os_boot_mode) | **POST** /api/v1/servers/{server_id}/boot-mode | Выбор типа загрузки операционной системы сервера


# **add_server_ip**
> AddServerIP201Response add_server_ip(server_id, add_server_ip_request)

Добавление IP-адреса сервера

Чтобы добавить IP-адрес сервера, отправьте POST-запрос на `/api/v1/servers/{server_id}/ips`. \\  На данный момент IPv6 доступны только для серверов с локацией `ru-1`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_server_ip201_response import AddServerIP201Response
from timeweb_cloud_api.models.add_server_ip_request import AddServerIPRequest
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    add_server_ip_request = timeweb_cloud_api.AddServerIPRequest() # AddServerIPRequest | 

    try:
        # Добавление IP-адреса сервера
        api_response = api_instance.add_server_ip(server_id, add_server_ip_request)
        print("The response of ServersApi->add_server_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->add_server_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **add_server_ip_request** | [**AddServerIPRequest**](AddServerIPRequest.md)|  | 

### Return type

[**AddServerIP201Response**](AddServerIP201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;server_ip&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clone_server**
> CreateServer201Response clone_server(server_id)

Клонирование сервера

Чтобы клонировать сервер, отправьте POST-запрос на `/api/v1/servers/{server_id}/clone`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_server201_response import CreateServer201Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.

    try:
        # Клонирование сервера
        api_response = api_instance.clone_server(server_id)
        print("The response of ServersApi->clone_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->clone_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 

### Return type

[**CreateServer201Response**](CreateServer201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;server&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_server**
> CreateServer201Response create_server(create_server)

Создание сервера

Чтобы создать сервер, отправьте POST-запрос в `api/v1/servers`, задав необходимые атрибуты. Обязательно должен присутствовать один из параметров `configuration` или `preset_id`, а также `image_id` или `os_id`.  Cервер будет создан с использованием предоставленной информации. Тело ответа будет содержать объект JSON с информацией о созданном сервере.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_server import CreateServer
from timeweb_cloud_api.models.create_server201_response import CreateServer201Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    create_server = timeweb_cloud_api.CreateServer() # CreateServer | 

    try:
        # Создание сервера
        api_response = api_instance.create_server(create_server)
        print("The response of ServersApi->create_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->create_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_server** | [**CreateServer**](CreateServer.md)|  | 

### Return type

[**CreateServer201Response**](CreateServer201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;server&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_server_disk**
> CreateServerDisk201Response create_server_disk(server_id, create_server_disk_request=create_server_disk_request)

Создание диска сервера

Чтобы создать диск сервера, отправьте POST-запрос на `/api/v1/servers/{server_id}/disks`. Системный диск создать нельзя.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_server_disk201_response import CreateServerDisk201Response
from timeweb_cloud_api.models.create_server_disk_request import CreateServerDiskRequest
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    create_server_disk_request = timeweb_cloud_api.CreateServerDiskRequest() # CreateServerDiskRequest |  (optional)

    try:
        # Создание диска сервера
        api_response = api_instance.create_server_disk(server_id, create_server_disk_request=create_server_disk_request)
        print("The response of ServersApi->create_server_disk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->create_server_disk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **create_server_disk_request** | [**CreateServerDiskRequest**](CreateServerDiskRequest.md)|  | [optional] 

### Return type

[**CreateServerDisk201Response**](CreateServerDisk201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Успешное создание диска сервера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_server_disk_backup**
> CreateServerDiskBackup201Response create_server_disk_backup(server_id, disk_id, create_server_disk_backup_request=create_server_disk_backup_request)

Создание бэкапа диска сервера

Чтобы создать бэкап диска сервера, отправьте POST-запрос на `/api/v1/servers/{server_id}/disks/{disk_id}/backups`.   Тело ответа будет представлять собой объект JSON с ключом `backup`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_server_disk_backup201_response import CreateServerDiskBackup201Response
from timeweb_cloud_api.models.create_server_disk_backup_request import CreateServerDiskBackupRequest
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    disk_id = 1051 # object | Уникальный идентификатор диска сервера.
    create_server_disk_backup_request = timeweb_cloud_api.CreateServerDiskBackupRequest() # CreateServerDiskBackupRequest |  (optional)

    try:
        # Создание бэкапа диска сервера
        api_response = api_instance.create_server_disk_backup(server_id, disk_id, create_server_disk_backup_request=create_server_disk_backup_request)
        print("The response of ServersApi->create_server_disk_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->create_server_disk_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **disk_id** | [**object**](.md)| Уникальный идентификатор диска сервера. | 
 **create_server_disk_backup_request** | [**CreateServerDiskBackupRequest**](CreateServerDiskBackupRequest.md)|  | [optional] 

### Return type

[**CreateServerDiskBackup201Response**](CreateServerDiskBackup201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;backup&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server**
> DeleteServer200Response delete_server(server_id, hash=hash, code=code)

Удаление сервера

Чтобы удалить сервер, отправьте запрос DELETE в `/api/v1/servers/{server_id}`.\\  Обратите внимание, если на аккаунте включено удаление серверов по смс, то вернется ошибка 423.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.delete_server200_response import DeleteServer200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    hash = 15095f25-aac3-4d60-a788-96cb5136f186 # object | Хеш, который совместно с кодом авторизации надо отправить для удаления, если включено подтверждение удаления сервисов через Телеграм. (optional)
    code = 0000 # object | Код подтверждения, который придет к вам в Телеграм, после запроса удаления, если включено подтверждение удаления сервисов.  При помощи API токена сервисы можно удалять без подтверждения, если параметр токена `is_able_to_delete` установлен в значение `true` (optional)

    try:
        # Удаление сервера
        api_response = api_instance.delete_server(server_id, hash=hash, code=code)
        print("The response of ServersApi->delete_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->delete_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **hash** | [**object**](.md)| Хеш, который совместно с кодом авторизации надо отправить для удаления, если включено подтверждение удаления сервисов через Телеграм. | [optional] 
 **code** | [**object**](.md)| Код подтверждения, который придет к вам в Телеграм, после запроса удаления, если включено подтверждение удаления сервисов.  При помощи API токена сервисы можно удалять без подтверждения, если параметр токена &#x60;is_able_to_delete&#x60; установлен в значение &#x60;true&#x60; | [optional] 

### Return type

[**DeleteServer200Response**](DeleteServer200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;server_delete&#x60; |  -  |
**204** | Успешное удаление сервера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server_disk**
> delete_server_disk(server_id, disk_id)

Удаление диска сервера

Чтобы удалить диск сервера, отправьте DELETE-запрос на `/api/v1/servers/{server_id}/disks/{disk_id}`. Нельзя удалять системный диск.

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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    disk_id = 1051 # object | Уникальный идентификатор диска сервера.

    try:
        # Удаление диска сервера
        api_instance.delete_server_disk(server_id, disk_id)
    except Exception as e:
        print("Exception when calling ServersApi->delete_server_disk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **disk_id** | [**object**](.md)| Уникальный идентификатор диска сервера. | 

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
**204** | Успешное удаление диска сервера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server_disk_backup**
> delete_server_disk_backup(server_id, disk_id, backup_id)

Удаление бэкапа диска сервера

Чтобы удалить бэкап диска сервера, отправьте DELETE-запрос на `/api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id}`.

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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    disk_id = 1051 # object | Уникальный идентификатор диска сервера.
    backup_id = 1051 # object | Уникальный идентификатор бэкапа сервера.

    try:
        # Удаление бэкапа диска сервера
        api_instance.delete_server_disk_backup(server_id, disk_id, backup_id)
    except Exception as e:
        print("Exception when calling ServersApi->delete_server_disk_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **disk_id** | [**object**](.md)| Уникальный идентификатор диска сервера. | 
 **backup_id** | [**object**](.md)| Уникальный идентификатор бэкапа сервера. | 

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
**204** | Успешное удаление бэкапа. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_server_ip**
> delete_server_ip(server_id, delete_server_ip_request)

Удаление IP-адреса сервера

Чтобы удалить IP-адрес сервера, отправьте DELETE-запрос на `/api/v1/servers/{server_id}/ips`. Нельзя удалить основной IP-адрес

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.delete_server_ip_request import DeleteServerIPRequest
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    delete_server_ip_request = timeweb_cloud_api.DeleteServerIPRequest() # DeleteServerIPRequest | 

    try:
        # Удаление IP-адреса сервера
        api_instance.delete_server_ip(server_id, delete_server_ip_request)
    except Exception as e:
        print("Exception when calling ServersApi->delete_server_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **delete_server_ip_request** | [**DeleteServerIPRequest**](DeleteServerIPRequest.md)|  | 

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
**204** | IP-адрес успешно удален |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configurators**
> GetConfigurators200Response get_configurators()

Получение списка конфигураторов серверов

Чтобы получить список всех конфигураторов серверов, отправьте GET-запрос на `/api/v1/configurator/servers`.   Тело ответа будет представлять собой объект JSON с ключом `server_configurators`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_configurators200_response import GetConfigurators200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)

    try:
        # Получение списка конфигураторов серверов
        api_response = api_instance.get_configurators()
        print("The response of ServersApi->get_configurators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_configurators: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetConfigurators200Response**](GetConfigurators200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;server_configurators&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_os_list**
> GetOsList200Response get_os_list()

Получение списка операционных систем

Чтобы получить список всех операционных систем, отправьте GET-запрос на `/api/v1/os/servers`.   Тело ответа будет представлять собой объект JSON с ключом `servers_os`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_os_list200_response import GetOsList200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)

    try:
        # Получение списка операционных систем
        api_response = api_instance.get_os_list()
        print("The response of ServersApi->get_os_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_os_list: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetOsList200Response**](GetOsList200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;servers_os&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server**
> CreateServer201Response get_server(server_id)

Получение сервера

Чтобы получить сервер, отправьте запрос GET в `/api/v1/servers/{server_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_server201_response import CreateServer201Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.

    try:
        # Получение сервера
        api_response = api_instance.get_server(server_id)
        print("The response of ServersApi->get_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 

### Return type

[**CreateServer201Response**](CreateServer201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;server&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_disk**
> CreateServerDisk201Response get_server_disk(server_id, disk_id)

Получение диска сервера

Чтобы получить диск сервера, отправьте GET-запрос на `/api/v1/servers/{server_id}/disks/{disk_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_server_disk201_response import CreateServerDisk201Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    disk_id = 1051 # object | Уникальный идентификатор диска сервера.

    try:
        # Получение диска сервера
        api_response = api_instance.get_server_disk(server_id, disk_id)
        print("The response of ServersApi->get_server_disk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_server_disk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **disk_id** | [**object**](.md)| Уникальный идентификатор диска сервера. | 

### Return type

[**CreateServerDisk201Response**](CreateServerDisk201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешное получение диска сервера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_disk_auto_backup_settings**
> GetServerDiskAutoBackupSettings200Response get_server_disk_auto_backup_settings(server_id, disk_id)

Получить настройки автобэкапов диска сервера

Чтобы полученить настройки автобэкапов диска сервера, отправьте GET-запрос на `/api/v1/servers/{server_id}/disks/{disk_id}/auto-backups`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_server_disk_auto_backup_settings200_response import GetServerDiskAutoBackupSettings200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    disk_id = 1051 # object | Уникальный идентификатор диска сервера.

    try:
        # Получить настройки автобэкапов диска сервера
        api_response = api_instance.get_server_disk_auto_backup_settings(server_id, disk_id)
        print("The response of ServersApi->get_server_disk_auto_backup_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_server_disk_auto_backup_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **disk_id** | [**object**](.md)| Уникальный идентификатор диска сервера. | 

### Return type

[**GetServerDiskAutoBackupSettings200Response**](GetServerDiskAutoBackupSettings200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;auto_backups_settings&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_disk_backup**
> GetServerDiskBackup200Response get_server_disk_backup(server_id, disk_id, backup_id)

Получение бэкапа диска сервера

Чтобы получить бэкап диска сервера, отправьте GET-запрос на `/api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id}`.   Тело ответа будет представлять собой объект JSON с ключом `backup`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_server_disk_backup200_response import GetServerDiskBackup200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    disk_id = 1051 # object | Уникальный идентификатор диска сервера.
    backup_id = 1051 # object | Уникальный идентификатор бэкапа сервера.

    try:
        # Получение бэкапа диска сервера
        api_response = api_instance.get_server_disk_backup(server_id, disk_id, backup_id)
        print("The response of ServersApi->get_server_disk_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_server_disk_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **disk_id** | [**object**](.md)| Уникальный идентификатор диска сервера. | 
 **backup_id** | [**object**](.md)| Уникальный идентификатор бэкапа сервера. | 

### Return type

[**GetServerDiskBackup200Response**](GetServerDiskBackup200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;backup&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_disk_backups**
> GetServerDiskBackups200Response get_server_disk_backups(server_id, disk_id)

Получение списка бэкапов диска сервера

Чтобы получить список бэкапов диска сервера, отправьте GET-запрос на `/api/v1/servers/{server_id}/disks/{disk_id}/backups`.   Тело ответа будет представлять собой объект JSON с ключом `backups`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_server_disk_backups200_response import GetServerDiskBackups200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    disk_id = 1051 # object | Уникальный идентификатор диска сервера.

    try:
        # Получение списка бэкапов диска сервера
        api_response = api_instance.get_server_disk_backups(server_id, disk_id)
        print("The response of ServersApi->get_server_disk_backups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_server_disk_backups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **disk_id** | [**object**](.md)| Уникальный идентификатор диска сервера. | 

### Return type

[**GetServerDiskBackups200Response**](GetServerDiskBackups200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;backups&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_disks**
> GetServerDisks200Response get_server_disks(server_id)

Получение списка дисков сервера

Чтобы получить список дисков сервера, отправьте GET-запрос на `/api/v1/servers/{server_id}/disks`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_server_disks200_response import GetServerDisks200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.

    try:
        # Получение списка дисков сервера
        api_response = api_instance.get_server_disks(server_id)
        print("The response of ServersApi->get_server_disks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_server_disks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 

### Return type

[**GetServerDisks200Response**](GetServerDisks200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;server_disks&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_ips**
> GetServerIPs200Response get_server_ips(server_id)

Получение списка IP-адресов сервера

Чтобы получить список IP-адресов сервера, отправьте GET-запрос на `/api/v1/servers/{server_id}/ips`. \\  На данный момент IPv6 доступны только для локации `ru-1`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_server_ips200_response import GetServerIPs200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.

    try:
        # Получение списка IP-адресов сервера
        api_response = api_instance.get_server_ips(server_id)
        print("The response of ServersApi->get_server_ips:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_server_ips: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 

### Return type

[**GetServerIPs200Response**](GetServerIPs200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;server_ips&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_logs**
> GetServerLogs200Response get_server_logs(server_id, limit=limit, offset=offset, order=order)

Получение списка логов сервера

Чтобы получить список логов сервера, отправьте GET-запрос на `/api/v1/servers/{server_id}/logs`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_server_logs200_response import GetServerLogs200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)
    order = None # object | Сортировка элементов по дате (optional)

    try:
        # Получение списка логов сервера
        api_response = api_instance.get_server_logs(server_id, limit=limit, offset=offset, order=order)
        print("The response of ServersApi->get_server_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_server_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 
 **order** | [**object**](.md)| Сортировка элементов по дате | [optional] 

### Return type

[**GetServerLogs200Response**](GetServerLogs200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;server_logs&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_server_statistics**
> GetServerStatistics200Response get_server_statistics(server_id, date_from, date_to)

Получение статистики сервера

Чтобы получить статистику сервера, отправьте GET-запрос на `/api/v1/servers/{server_id}/statistics`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_server_statistics200_response import GetServerStatistics200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    date_from = None # object | Дата начала сбора статистики. Строка в формате ISO 8061, закодированная в ASCII, пример: `2023-05-25%202023-05-25T14%3A35%3A38`
    date_to = None # object | Дата окончания сбора статистики. Строка в формате ISO 8061, закодированная в ASCII, пример: `2023-05-26%202023-05-25T14%3A35%3A38`

    try:
        # Получение статистики сервера
        api_response = api_instance.get_server_statistics(server_id, date_from, date_to)
        print("The response of ServersApi->get_server_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_server_statistics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **date_from** | [**object**](.md)| Дата начала сбора статистики. Строка в формате ISO 8061, закодированная в ASCII, пример: &#x60;2023-05-25%202023-05-25T14%3A35%3A38&#x60; | 
 **date_to** | [**object**](.md)| Дата окончания сбора статистики. Строка в формате ISO 8061, закодированная в ASCII, пример: &#x60;2023-05-26%202023-05-25T14%3A35%3A38&#x60; | 

### Return type

[**GetServerStatistics200Response**](GetServerStatistics200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;cpu&#x60;, &#x60;disk&#x60;, &#x60;network_traffic&#x60;, &#x60;ram&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_servers**
> GetServers200Response get_servers(limit=limit, offset=offset)

Получение списка серверов

Чтобы получить список серверов, отправьте GET-запрос на `/api/v1/servers`.   Тело ответа будет представлять собой объект JSON с ключом `servers`.

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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    limit = None # object | Обозначает количество записей, которое необходимо вернуть. (optional)
    offset = None # object | Указывает на смещение относительно начала списка. (optional)

    try:
        # Получение списка серверов
        api_response = api_instance.get_servers(limit=limit, offset=offset)
        print("The response of ServersApi->get_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)| Обозначает количество записей, которое необходимо вернуть. | [optional] 
 **offset** | [**object**](.md)| Указывает на смещение относительно начала списка. | [optional] 

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
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_servers_presets**
> GetServersPresets200Response get_servers_presets()

Получение списка тарифов серверов

Чтобы получить список всех тарифов серверов, отправьте GET-запрос на `/api/v1/presets/servers`.   Тело ответа будет представлять собой объект JSON с ключом `server_presets`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_servers_presets200_response import GetServersPresets200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)

    try:
        # Получение списка тарифов серверов
        api_response = api_instance.get_servers_presets()
        print("The response of ServersApi->get_servers_presets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_servers_presets: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetServersPresets200Response**](GetServersPresets200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;server_presets&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_software**
> GetSoftware200Response get_software()

Получение списка ПО из маркетплейса

Чтобы получить список ПО из маркетплейса, отправьте GET-запрос на `/api/v1/software/servers`.   Тело ответа будет представлять собой объект JSON с ключом `servers_software`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_software200_response import GetSoftware200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)

    try:
        # Получение списка ПО из маркетплейса
        api_response = api_instance.get_software()
        print("The response of ServersApi->get_software:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->get_software: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetSoftware200Response**](GetSoftware200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;servers_software&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hard_shutdown_server**
> hard_shutdown_server(server_id)

Принудительное выключение сервера

Чтобы выполнить принудительное выключение сервера, отправьте POST-запрос на `/api/v1/servers/{server_id}/hard-shutdown`.

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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.

    try:
        # Принудительное выключение сервера
        api_instance.hard_shutdown_server(server_id)
    except Exception as e:
        print("Exception when calling ServersApi->hard_shutdown_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 

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
**204** | Успешное выполнение действия |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **image_unmount_and_server_reload**
> image_unmount_and_server_reload(server_id)

Отмонтирование ISO образа и перезагрузка сервера

Чтобы отмонтировать ISO образ и перезагрузить сервер, отправьте POST-запрос на `/api/v1/servers/{server_id}/image-unmount`.

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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.

    try:
        # Отмонтирование ISO образа и перезагрузка сервера
        api_instance.image_unmount_and_server_reload(server_id)
    except Exception as e:
        print("Exception when calling ServersApi->image_unmount_and_server_reload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 

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
**200** | ISO образ в процессе отмонтирования |  -  |
**400** |  |  -  |
**401** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_server**
> install_server(server_id)

Установка сервера

Чтобы установить сервер, отправьте POST-запрос на `/api/v1/servers/{server_id}/install`.

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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.

    try:
        # Установка сервера
        api_instance.install_server(server_id)
    except Exception as e:
        print("Exception when calling ServersApi->install_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 

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
**204** | Успешное выполнение действия |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_action_on_backup**
> perform_action_on_backup(server_id, disk_id, backup_id, perform_action_on_backup_request=perform_action_on_backup_request)

Выполнение действия над бэкапом диска сервера

Чтобы выполнить действие над бэкапом диска сервера, отправьте POST-запрос на `/api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id}/action`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.perform_action_on_backup_request import PerformActionOnBackupRequest
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    disk_id = 1051 # object | Уникальный идентификатор диска сервера.
    backup_id = 1051 # object | Уникальный идентификатор бэкапа сервера.
    perform_action_on_backup_request = timeweb_cloud_api.PerformActionOnBackupRequest() # PerformActionOnBackupRequest |  (optional)

    try:
        # Выполнение действия над бэкапом диска сервера
        api_instance.perform_action_on_backup(server_id, disk_id, backup_id, perform_action_on_backup_request=perform_action_on_backup_request)
    except Exception as e:
        print("Exception when calling ServersApi->perform_action_on_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **disk_id** | [**object**](.md)| Уникальный идентификатор диска сервера. | 
 **backup_id** | [**object**](.md)| Уникальный идентификатор бэкапа сервера. | 
 **perform_action_on_backup_request** | [**PerformActionOnBackupRequest**](PerformActionOnBackupRequest.md)|  | [optional] 

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
**204** | Успешное выполнение действия |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **perform_action_on_server**
> perform_action_on_server(server_id, perform_action_on_server_request=perform_action_on_server_request)

Выполнение действия над сервером

Чтобы выполнить действие над сервером, отправьте POST-запрос на `/api/v1/servers/{server_id}/action`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.perform_action_on_server_request import PerformActionOnServerRequest
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    perform_action_on_server_request = timeweb_cloud_api.PerformActionOnServerRequest() # PerformActionOnServerRequest |  (optional)

    try:
        # Выполнение действия над сервером
        api_instance.perform_action_on_server(server_id, perform_action_on_server_request=perform_action_on_server_request)
    except Exception as e:
        print("Exception when calling ServersApi->perform_action_on_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **perform_action_on_server_request** | [**PerformActionOnServerRequest**](PerformActionOnServerRequest.md)|  | [optional] 

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
**204** | Успешное выполнение действия |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reboot_server**
> reboot_server(server_id)

Перезагрузка сервера

Чтобы перезагрузить сервер, отправьте POST-запрос на `/api/v1/servers/{server_id}/reboot`.

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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.

    try:
        # Перезагрузка сервера
        api_instance.reboot_server(server_id)
    except Exception as e:
        print("Exception when calling ServersApi->reboot_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 

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
**204** | Успешное выполнение действия |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_server_password**
> reset_server_password(server_id)

Сброс пароля сервера

Чтобы сбросить пароль сервера, отправьте POST-запрос на `/api/v1/servers/{server_id}/reset-password`.

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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.

    try:
        # Сброс пароля сервера
        api_instance.reset_server_password(server_id)
    except Exception as e:
        print("Exception when calling ServersApi->reset_server_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 

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
**204** | Успешное выполнение действия |  -  |
**400** |  |  -  |
**401** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_server**
> shutdown_server(server_id)

Выключение сервера

Чтобы выключить сервер, отправьте POST-запрос на `/api/v1/servers/{server_id}/shutdown`.

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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.

    try:
        # Выключение сервера
        api_instance.shutdown_server(server_id)
    except Exception as e:
        print("Exception when calling ServersApi->shutdown_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 

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
**204** | Успешное выполнение действия |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_server**
> start_server(server_id)

Запуск сервера

Чтобы запустить сервер, отправьте POST-запрос на `/api/v1/servers/{server_id}/start`.

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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.

    try:
        # Запуск сервера
        api_instance.start_server(server_id)
    except Exception as e:
        print("Exception when calling ServersApi->start_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 

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
**204** | Успешное выполнение действия |  -  |
**400** |  |  -  |
**401** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server**
> CreateServer201Response update_server(server_id, update_server)

Изменение сервера

Чтобы обновить только определенные атрибуты сервера, отправьте запрос PATCH в `/api/v1/servers/{server_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_server201_response import CreateServer201Response
from timeweb_cloud_api.models.update_server import UpdateServer
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    update_server = timeweb_cloud_api.UpdateServer() # UpdateServer | 

    try:
        # Изменение сервера
        api_response = api_instance.update_server(server_id, update_server)
        print("The response of ServersApi->update_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->update_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **update_server** | [**UpdateServer**](UpdateServer.md)|  | 

### Return type

[**CreateServer201Response**](CreateServer201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;server&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server_disk**
> CreateServerDisk201Response update_server_disk(server_id, disk_id, update_server_disk_request=update_server_disk_request)

Изменение параметров диска сервера

Чтобы изменить параметры диска сервера, отправьте PATCH-запрос на `/api/v1/servers/{server_id}/disks/{disk_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_server_disk201_response import CreateServerDisk201Response
from timeweb_cloud_api.models.update_server_disk_request import UpdateServerDiskRequest
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    disk_id = 1051 # object | Уникальный идентификатор диска сервера.
    update_server_disk_request = timeweb_cloud_api.UpdateServerDiskRequest() # UpdateServerDiskRequest |  (optional)

    try:
        # Изменение параметров диска сервера
        api_response = api_instance.update_server_disk(server_id, disk_id, update_server_disk_request=update_server_disk_request)
        print("The response of ServersApi->update_server_disk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->update_server_disk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **disk_id** | [**object**](.md)| Уникальный идентификатор диска сервера. | 
 **update_server_disk_request** | [**UpdateServerDiskRequest**](UpdateServerDiskRequest.md)|  | [optional] 

### Return type

[**CreateServerDisk201Response**](CreateServerDisk201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Успешное изменение параметров диска сервера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server_disk_auto_backup_settings**
> GetServerDiskAutoBackupSettings200Response update_server_disk_auto_backup_settings(server_id, disk_id, auto_backup=auto_backup)

Изменение настроек автобэкапов диска сервера

Чтобы изменить настройки автобэкапов диска сервера, отправьте PATCH-запрос на `/api/v1/servers/{server_id}/disks/{disk_id}/auto-backups`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.auto_backup import AutoBackup
from timeweb_cloud_api.models.get_server_disk_auto_backup_settings200_response import GetServerDiskAutoBackupSettings200Response
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    disk_id = 1051 # object | Уникальный идентификатор диска сервера.
    auto_backup = timeweb_cloud_api.AutoBackup() # AutoBackup | При значении `is_enabled`: `true`, поля `copy_count`, `creation_start_at`, `interval` являются обязательными (optional)

    try:
        # Изменение настроек автобэкапов диска сервера
        api_response = api_instance.update_server_disk_auto_backup_settings(server_id, disk_id, auto_backup=auto_backup)
        print("The response of ServersApi->update_server_disk_auto_backup_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->update_server_disk_auto_backup_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **disk_id** | [**object**](.md)| Уникальный идентификатор диска сервера. | 
 **auto_backup** | [**AutoBackup**](AutoBackup.md)| При значении &#x60;is_enabled&#x60;: &#x60;true&#x60;, поля &#x60;copy_count&#x60;, &#x60;creation_start_at&#x60;, &#x60;interval&#x60; являются обязательными | [optional] 

### Return type

[**GetServerDiskAutoBackupSettings200Response**](GetServerDiskAutoBackupSettings200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;auto_backups_settings&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server_disk_backup**
> GetServerDiskBackup200Response update_server_disk_backup(server_id, disk_id, backup_id, update_server_disk_backup_request=update_server_disk_backup_request)

Изменение бэкапа диска сервера

Чтобы изменить бэкап диска сервера, отправьте PATCH-запрос на `/api/v1/servers/{server_id}/disks/{disk_id}/backups/{backup_id}`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_server_disk_backup200_response import GetServerDiskBackup200Response
from timeweb_cloud_api.models.update_server_disk_backup_request import UpdateServerDiskBackupRequest
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    disk_id = 1051 # object | Уникальный идентификатор диска сервера.
    backup_id = 1051 # object | Уникальный идентификатор бэкапа сервера.
    update_server_disk_backup_request = timeweb_cloud_api.UpdateServerDiskBackupRequest() # UpdateServerDiskBackupRequest |  (optional)

    try:
        # Изменение бэкапа диска сервера
        api_response = api_instance.update_server_disk_backup(server_id, disk_id, backup_id, update_server_disk_backup_request=update_server_disk_backup_request)
        print("The response of ServersApi->update_server_disk_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->update_server_disk_backup: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **disk_id** | [**object**](.md)| Уникальный идентификатор диска сервера. | 
 **backup_id** | [**object**](.md)| Уникальный идентификатор бэкапа сервера. | 
 **update_server_disk_backup_request** | [**UpdateServerDiskBackupRequest**](UpdateServerDiskBackupRequest.md)|  | [optional] 

### Return type

[**GetServerDiskBackup200Response**](GetServerDiskBackup200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;backup&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server_ip**
> AddServerIP201Response update_server_ip(server_id, update_server_ip_request)

Изменение IP-адреса сервера

Чтобы изменить IP-адрес сервера, отправьте POST-запрос на `/api/v1/servers/{server_id}/ips`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_server_ip201_response import AddServerIP201Response
from timeweb_cloud_api.models.update_server_ip_request import UpdateServerIPRequest
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    update_server_ip_request = timeweb_cloud_api.UpdateServerIPRequest() # UpdateServerIPRequest | 

    try:
        # Изменение IP-адреса сервера
        api_response = api_instance.update_server_ip(server_id, update_server_ip_request)
        print("The response of ServersApi->update_server_ip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServersApi->update_server_ip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **update_server_ip_request** | [**UpdateServerIPRequest**](UpdateServerIPRequest.md)|  | 

### Return type

[**AddServerIP201Response**](AddServerIP201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;server_ip&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server_nat**
> update_server_nat(server_id, update_server_nat_request=update_server_nat_request)

Изменение правил маршрутизации трафика сервера (NAT)

Чтобы измененить правила маршрутизации трафика сервера (NAT), отправьте PATCH-запрос на `/api/v1/servers/{server_id}/local-networks/nat-mode`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.update_server_nat_request import UpdateServerNATRequest
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    update_server_nat_request = timeweb_cloud_api.UpdateServerNATRequest() # UpdateServerNATRequest |  (optional)

    try:
        # Изменение правил маршрутизации трафика сервера (NAT)
        api_instance.update_server_nat(server_id, update_server_nat_request=update_server_nat_request)
    except Exception as e:
        print("Exception when calling ServersApi->update_server_nat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **update_server_nat_request** | [**UpdateServerNATRequest**](UpdateServerNATRequest.md)|  | [optional] 

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
**204** | Успешна смена правила маршрутизации трафика |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_server_os_boot_mode**
> update_server_os_boot_mode(server_id, update_server_os_boot_mode_request=update_server_os_boot_mode_request)

Выбор типа загрузки операционной системы сервера

Чтобы изменить тип загрузки операционной системы сервера, отправьте POST-запрос на `/api/v1/servers/{server_id}/boot-mode`. \\  После смены типа загрузки сервер будет перезапущен.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.update_server_os_boot_mode_request import UpdateServerOSBootModeRequest
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
    api_instance = timeweb_cloud_api.ServersApi(api_client)
    server_id = 1051 # object | Уникальный идентификатор облачного сервера.
    update_server_os_boot_mode_request = timeweb_cloud_api.UpdateServerOSBootModeRequest() # UpdateServerOSBootModeRequest |  (optional)

    try:
        # Выбор типа загрузки операционной системы сервера
        api_instance.update_server_os_boot_mode(server_id, update_server_os_boot_mode_request=update_server_os_boot_mode_request)
    except Exception as e:
        print("Exception when calling ServersApi->update_server_os_boot_mode: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **server_id** | [**object**](.md)| Уникальный идентификатор облачного сервера. | 
 **update_server_os_boot_mode_request** | [**UpdateServerOSBootModeRequest**](UpdateServerOSBootModeRequest.md)|  | [optional] 

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
**204** | Успешная смена загрузки операционной системы сервера |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

