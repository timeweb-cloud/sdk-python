# timeweb_cloud_api.AIAgentSkillsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_agent_skill_catalog_update**](AIAgentSkillsApi.md#apply_agent_skill_catalog_update) | **POST** /api/v1/cloud-ai/skills/{skill_id}/apply-catalog-update | Применение обновления навыка из каталога
[**connect_agent_skills_to_agent**](AIAgentSkillsApi.md#connect_agent_skills_to_agent) | **POST** /api/v1/cloud-ai/agents/{agent_id}/skills/connect | Подключение нескольких навыков к агенту
[**create_agent_skill**](AIAgentSkillsApi.md#create_agent_skill) | **POST** /api/v1/cloud-ai/skills | Создание навыка
[**delete_agent_skill**](AIAgentSkillsApi.md#delete_agent_skill) | **DELETE** /api/v1/cloud-ai/skills/{skill_id} | Удаление навыка
[**disconnect_agent_skill_from_agent**](AIAgentSkillsApi.md#disconnect_agent_skill_from_agent) | **DELETE** /api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id} | Отключение навыка от агента
[**duplicate_agent_skill**](AIAgentSkillsApi.md#duplicate_agent_skill) | **POST** /api/v1/cloud-ai/skills/{skill_id}/duplicate | Копирование навыка
[**get_agent_skill**](AIAgentSkillsApi.md#get_agent_skill) | **GET** /api/v1/cloud-ai/skills/{skill_id} | Получение навыка
[**get_agent_skill_catalog**](AIAgentSkillsApi.md#get_agent_skill_catalog) | **GET** /api/v1/cloud-ai/skill-catalog | Получение каталога навыков
[**get_agent_skill_library**](AIAgentSkillsApi.md#get_agent_skill_library) | **GET** /api/v1/cloud-ai/skills | Получение списка навыков
[**get_agent_skill_version**](AIAgentSkillsApi.md#get_agent_skill_version) | **GET** /api/v1/cloud-ai/skills/{skill_id}/versions/{version} | Получение версии навыка
[**get_agent_skill_versions**](AIAgentSkillsApi.md#get_agent_skill_versions) | **GET** /api/v1/cloud-ai/skills/{skill_id}/versions | Получение истории версий навыка
[**get_agent_skills_for_agent**](AIAgentSkillsApi.md#get_agent_skills_for_agent) | **GET** /api/v1/cloud-ai/agents/{agent_id}/skills | Получение навыков агента
[**install_agent_skill_from_catalog**](AIAgentSkillsApi.md#install_agent_skill_from_catalog) | **POST** /api/v1/cloud-ai/skill-catalog/{catalog_item_id}/install | Установка навыка из каталога
[**install_and_connect_agent_skill**](AIAgentSkillsApi.md#install_and_connect_agent_skill) | **POST** /api/v1/cloud-ai/agents/{agent_id}/skills/install-and-connect | Установка навыка из каталога и включение у агента
[**rollback_agent_skill_version**](AIAgentSkillsApi.md#rollback_agent_skill_version) | **POST** /api/v1/cloud-ai/skills/{skill_id}/versions/{version}/rollback | Переключение навыка на версию из истории
[**set_agent_skill_for_agent**](AIAgentSkillsApi.md#set_agent_skill_for_agent) | **PUT** /api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id} | Включение и выключение навыка у агента
[**sync_agent_skill_agents_versions**](AIAgentSkillsApi.md#sync_agent_skill_agents_versions) | **POST** /api/v1/cloud-ai/skills/{skill_id}/agents/sync-versions | Перевод всех агентов навыка на текущую версию
[**sync_agent_skill_versions_for_agent**](AIAgentSkillsApi.md#sync_agent_skill_versions_for_agent) | **POST** /api/v1/cloud-ai/agents/{agent_id}/skills/sync-versions | Перевод всех навыков агента на текущие версии
[**update_agent_skill**](AIAgentSkillsApi.md#update_agent_skill) | **PATCH** /api/v1/cloud-ai/skills/{skill_id} | Изменение навыка
[**update_agent_skill_version_for_agent**](AIAgentSkillsApi.md#update_agent_skill_version_for_agent) | **POST** /api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}/update-version | Перевод агента на текущую версию навыка


# **apply_agent_skill_catalog_update**
> CreateAgentSkill201Response apply_agent_skill_catalog_update(skill_id)

Применение обновления навыка из каталога

Чтобы применить к установленному навыку новую версию из каталога, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/apply-catalog-update`.  Текст «когда применять» и инструкция заменяются каталожными, при этом создаётся новая версия: прежний текст, в том числе ваши правки, остаётся в истории. Название навыка не меняется. Если обновления нет, ничего не меняется (`meta.version_created` — `false`).  Для навыка, установленного не из каталога, вернётся 409 с `error_code` `skill_is_not_installed_from_catalog`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_skill201_response import CreateAgentSkill201Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    skill_id = 12 # object | ID навыка

    try:
        # Применение обновления навыка из каталога
        api_response = api_instance.apply_agent_skill_catalog_update(skill_id)
        print("The response of AIAgentSkillsApi->apply_agent_skill_catalog_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->apply_agent_skill_catalog_update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | [**object**](.md)| ID навыка | 

### Return type

[**CreateAgentSkill201Response**](CreateAgentSkill201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;skill&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **connect_agent_skills_to_agent**
> GetAgentSkillsForAgent200Response connect_agent_skills_to_agent(agent_id, connect_skills)

Подключение нескольких навыков к агенту

Чтобы подключить и сразу включить у агента несколько навыков, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/connect`.  Навыки, которых нет в аккаунте, пропускаются без ошибки. Уже подключённые навыки включаются; если для них передана версия, агент закрепляется на ней. В ответе — только навыки, которые удалось подключить.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.connect_skills import ConnectSkills
from timeweb_cloud_api.models.get_agent_skills_for_agent200_response import GetAgentSkillsForAgent200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    agent_id = 113191 # object | ID агента
    connect_skills = timeweb_cloud_api.ConnectSkills() # ConnectSkills | 

    try:
        # Подключение нескольких навыков к агенту
        api_response = api_instance.connect_agent_skills_to_agent(agent_id, connect_skills)
        print("The response of AIAgentSkillsApi->connect_agent_skills_to_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->connect_agent_skills_to_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 
 **connect_skills** | [**ConnectSkills**](ConnectSkills.md)|  | 

### Return type

[**GetAgentSkillsForAgent200Response**](GetAgentSkillsForAgent200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;agent_skills&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_skill**
> CreateAgentSkill201Response create_agent_skill(create_skill)

Создание навыка

Чтобы создать навык, отправьте POST-запрос на `/api/v1/cloud-ai/skills`.  Навык создаётся с версией 1 и ни к одному агенту не подключается. Предупреждения о качестве текста приходят в `meta.warnings` и не мешают сохранению. Скрипты передаются в теле запроса. Их общий размер — до 10 МБ, а всё тело запроса — до 16 МБ; запрос с телом больше отклоняется до проверки.  Если навык с таким названием уже есть, вернётся 409 с `error_code` `skill_name_already_exists`. Если скрипты не прошли проверку (больше 20 файлов, повторяющиеся имена, общий размер больше 10 МБ, файл без содержимого), вернётся 400 с `error_code` `skill_scripts_invalid`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_skill201_response import CreateAgentSkill201Response
from timeweb_cloud_api.models.create_skill import CreateSkill
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    create_skill = timeweb_cloud_api.CreateSkill() # CreateSkill | 

    try:
        # Создание навыка
        api_response = api_instance.create_agent_skill(create_skill)
        print("The response of AIAgentSkillsApi->create_agent_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->create_agent_skill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_skill** | [**CreateSkill**](CreateSkill.md)|  | 

### Return type

[**CreateAgentSkill201Response**](CreateAgentSkill201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключами &#x60;skill&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_skill**
> delete_agent_skill(skill_id)

Удаление навыка

Чтобы удалить навык, отправьте DELETE-запрос на `/api/v1/cloud-ai/skills/{skill_id}`.  Навык отключается от всех агентов, история версий и скрипты удаляются. Срабатывания навыка под старыми ответами агентов сохраняются.

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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    skill_id = 12 # object | ID навыка

    try:
        # Удаление навыка
        api_instance.delete_agent_skill(skill_id)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->delete_agent_skill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | [**object**](.md)| ID навыка | 

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
**204** | Навык удалён |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_agent_skill_from_agent**
> disconnect_agent_skill_from_agent(agent_id, skill_id)

Отключение навыка от агента

Чтобы полностью отключить навык от агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}`.  Закреплённая версия при этом не сохраняется. Чтобы выключить навык на время, используйте PUT-запрос с `is_enabled: false`. Если навык не подключён к агенту, вернётся 404 с `error_code` `agent_skill_link_not_found`.

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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    agent_id = 113191 # object | ID агента
    skill_id = 12 # object | ID навыка

    try:
        # Отключение навыка от агента
        api_instance.disconnect_agent_skill_from_agent(agent_id, skill_id)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->disconnect_agent_skill_from_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 
 **skill_id** | [**object**](.md)| ID навыка | 

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
**204** | Навык отключён от агента |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **duplicate_agent_skill**
> CreateAgentSkill201Response duplicate_agent_skill(skill_id)

Копирование навыка

Чтобы создать копию навыка, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/duplicate`.  Копия получает свободное название вида «Название (копия)» или «Название (копия 2)», текст и скрипты текущей версии оригинала и собственную историю с версии 1. К агентам копия не подключается. Копия навыка из каталога становится обычным навыком аккаунта.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_skill201_response import CreateAgentSkill201Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    skill_id = 12 # object | ID навыка

    try:
        # Копирование навыка
        api_response = api_instance.duplicate_agent_skill(skill_id)
        print("The response of AIAgentSkillsApi->duplicate_agent_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->duplicate_agent_skill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | [**object**](.md)| ID навыка | 

### Return type

[**CreateAgentSkill201Response**](CreateAgentSkill201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключами &#x60;skill&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_skill**
> GetAgentSkill200Response get_agent_skill(skill_id)

Получение навыка

Чтобы получить карточку навыка, отправьте GET-запрос на `/api/v1/cloud-ai/skills/{skill_id}`.  В карточке есть скрипты текущей версии (без содержимого), счётчик версий и агенты, к которым подключён навык.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_skill200_response import GetAgentSkill200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    skill_id = 12 # object | ID навыка

    try:
        # Получение навыка
        api_response = api_instance.get_agent_skill(skill_id)
        print("The response of AIAgentSkillsApi->get_agent_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->get_agent_skill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | [**object**](.md)| ID навыка | 

### Return type

[**GetAgentSkill200Response**](GetAgentSkill200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;skill&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_skill_catalog**
> GetAgentSkillCatalog200Response get_agent_skill_catalog()

Получение каталога навыков

Чтобы получить каталог готовых навыков Timeweb Cloud, отправьте GET-запрос на `/api/v1/cloud-ai/skill-catalog`.  Навыки приходят в порядке показа, сгруппированные по `category`. Инструкция возвращается полностью, чтобы её можно было прочитать до установки. Для установленных навыков заполнены `is_installed`, `installed_skill_id`, `is_modified` и `has_catalog_update`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_skill_catalog200_response import GetAgentSkillCatalog200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)

    try:
        # Получение каталога навыков
        api_response = api_instance.get_agent_skill_catalog()
        print("The response of AIAgentSkillsApi->get_agent_skill_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->get_agent_skill_catalog: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAgentSkillCatalog200Response**](GetAgentSkillCatalog200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;skill_catalog_items&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_skill_library**
> GetAgentSkillLibrary200Response get_agent_skill_library(search=search)

Получение списка навыков

Чтобы получить навыки аккаунта, отправьте GET-запрос на `/api/v1/cloud-ai/skills`.  Сначала идут недавно изменённые. Параметр `search` ищет по названию и по тексту инструкции.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_skill_library200_response import GetAgentSkillLibrary200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    search = возврат # object | Поиск по названию навыка и по тексту инструкции (optional)

    try:
        # Получение списка навыков
        api_response = api_instance.get_agent_skill_library(search=search)
        print("The response of AIAgentSkillsApi->get_agent_skill_library:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->get_agent_skill_library: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | [**object**](.md)| Поиск по названию навыка и по тексту инструкции | [optional] 

### Return type

[**GetAgentSkillLibrary200Response**](GetAgentSkillLibrary200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;skills&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_skill_version**
> GetAgentSkillVersion200Response get_agent_skill_version(skill_id, version)

Получение версии навыка

Чтобы получить текст конкретной версии навыка, отправьте GET-запрос на `/api/v1/cloud-ai/skills/{skill_id}/versions/{version}`.  Номер версии сработавшего навыка есть в срабатываниях под ответами агента.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_skill_version200_response import GetAgentSkillVersion200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    skill_id = 12 # object | ID навыка
    version = 2 # object | Номер версии навыка

    try:
        # Получение версии навыка
        api_response = api_instance.get_agent_skill_version(skill_id, version)
        print("The response of AIAgentSkillsApi->get_agent_skill_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->get_agent_skill_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | [**object**](.md)| ID навыка | 
 **version** | [**object**](.md)| Номер версии навыка | 

### Return type

[**GetAgentSkillVersion200Response**](GetAgentSkillVersion200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;skill_version&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_skill_versions**
> GetAgentSkillVersions200Response get_agent_skill_versions(skill_id)

Получение истории версий навыка

Чтобы получить историю версий навыка, отправьте GET-запрос на `/api/v1/cloud-ai/skills/{skill_id}/versions`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_skill_versions200_response import GetAgentSkillVersions200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    skill_id = 12 # object | ID навыка

    try:
        # Получение истории версий навыка
        api_response = api_instance.get_agent_skill_versions(skill_id)
        print("The response of AIAgentSkillsApi->get_agent_skill_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->get_agent_skill_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | [**object**](.md)| ID навыка | 

### Return type

[**GetAgentSkillVersions200Response**](GetAgentSkillVersions200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;skill_versions&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_skills_for_agent**
> GetAgentSkillsForAgent200Response get_agent_skills_for_agent(agent_id)

Получение навыков агента

Чтобы получить навыки агента, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills`.  В ответе все навыки аккаунта: неподключённые приходят с `is_connected: false`. `has_newer_version: true` означает, что агент закреплён на устаревшей версии.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_skills_for_agent200_response import GetAgentSkillsForAgent200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    agent_id = 113191 # object | ID агента

    try:
        # Получение навыков агента
        api_response = api_instance.get_agent_skills_for_agent(agent_id)
        print("The response of AIAgentSkillsApi->get_agent_skills_for_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->get_agent_skills_for_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 

### Return type

[**GetAgentSkillsForAgent200Response**](GetAgentSkillsForAgent200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;agent_skills&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_agent_skill_from_catalog**
> InstallAgentSkillFromCatalog200Response install_agent_skill_from_catalog(catalog_item_id)

Установка навыка из каталога

Чтобы установить навык из каталога в библиотеку аккаунта, отправьте POST-запрос на `/api/v1/cloud-ai/skill-catalog/{catalog_item_id}/install`.  Повторная установка не создаёт копию, а возвращает уже установленный навык с `meta.already_installed: true`. Если название занято вашим навыком, к нему добавляется «(копия)». Чтобы сразу включить навык у агента, используйте `POST /api/v1/cloud-ai/agents/{agent_id}/skills/install-and-connect`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.install_agent_skill_from_catalog200_response import InstallAgentSkillFromCatalog200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    catalog_item_id = 3 # object | ID навыка в каталоге

    try:
        # Установка навыка из каталога
        api_response = api_instance.install_agent_skill_from_catalog(catalog_item_id)
        print("The response of AIAgentSkillsApi->install_agent_skill_from_catalog:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->install_agent_skill_from_catalog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_item_id** | [**object**](.md)| ID навыка в каталоге | 

### Return type

[**InstallAgentSkillFromCatalog200Response**](InstallAgentSkillFromCatalog200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;skill&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_and_connect_agent_skill**
> InstallAndConnectAgentSkill200Response install_and_connect_agent_skill(agent_id, install_and_connect_skill)

Установка навыка из каталога и включение у агента

Чтобы установить навык из каталога и сразу включить его у агента, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/install-and-connect`.  Если навык уже установлен, копия не создаётся (`meta.already_installed: true`), навык просто включается у агента.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.install_and_connect_agent_skill200_response import InstallAndConnectAgentSkill200Response
from timeweb_cloud_api.models.install_and_connect_skill import InstallAndConnectSkill
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    agent_id = 113191 # object | ID агента
    install_and_connect_skill = timeweb_cloud_api.InstallAndConnectSkill() # InstallAndConnectSkill | 

    try:
        # Установка навыка из каталога и включение у агента
        api_response = api_instance.install_and_connect_agent_skill(agent_id, install_and_connect_skill)
        print("The response of AIAgentSkillsApi->install_and_connect_agent_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->install_and_connect_agent_skill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 
 **install_and_connect_skill** | [**InstallAndConnectSkill**](InstallAndConnectSkill.md)|  | 

### Return type

[**InstallAndConnectAgentSkill200Response**](InstallAndConnectAgentSkill200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;agent_skill&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rollback_agent_skill_version**
> CreateAgentSkill201Response rollback_agent_skill_version(skill_id, version)

Переключение навыка на версию из истории

Чтобы сделать версию из истории текущей, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/versions/{version}/rollback`.  Новая версия не создаётся (`meta.version_created` — `false`), название навыка не меняется. Агенты остаются на своих закреплённых версиях. Если выбранная версия уже текущая, ничего не меняется.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_skill201_response import CreateAgentSkill201Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    skill_id = 12 # object | ID навыка
    version = 2 # object | Номер версии навыка

    try:
        # Переключение навыка на версию из истории
        api_response = api_instance.rollback_agent_skill_version(skill_id, version)
        print("The response of AIAgentSkillsApi->rollback_agent_skill_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->rollback_agent_skill_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | [**object**](.md)| ID навыка | 
 **version** | [**object**](.md)| Номер версии навыка | 

### Return type

[**CreateAgentSkill201Response**](CreateAgentSkill201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;skill&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_agent_skill_for_agent**
> SetAgentSkillForAgent200Response set_agent_skill_for_agent(agent_id, skill_id, set_agent_skill)

Включение и выключение навыка у агента

Чтобы включить или выключить навык у агента, отправьте PUT-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}`.  Первое включение подключает навык и закрепляет агента на текущей версии навыка или на версии из `version`. Выключение сохраняет закреплённую версию, поэтому повторное включение вернёт то же поведение. Изменения действуют сразу. Выключение неподключённого навыка ничего не меняет.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.set_agent_skill import SetAgentSkill
from timeweb_cloud_api.models.set_agent_skill_for_agent200_response import SetAgentSkillForAgent200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    agent_id = 113191 # object | ID агента
    skill_id = 12 # object | ID навыка
    set_agent_skill = timeweb_cloud_api.SetAgentSkill() # SetAgentSkill | 

    try:
        # Включение и выключение навыка у агента
        api_response = api_instance.set_agent_skill_for_agent(agent_id, skill_id, set_agent_skill)
        print("The response of AIAgentSkillsApi->set_agent_skill_for_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->set_agent_skill_for_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 
 **skill_id** | [**object**](.md)| ID навыка | 
 **set_agent_skill** | [**SetAgentSkill**](SetAgentSkill.md)|  | 

### Return type

[**SetAgentSkillForAgent200Response**](SetAgentSkillForAgent200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;agent_skill&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_agent_skill_agents_versions**
> SyncAgentSkillAgentsVersions200Response sync_agent_skill_agents_versions(skill_id)

Перевод всех агентов навыка на текущую версию

Чтобы перевести всех агентов, у которых включён навык, на его текущую версию, отправьте POST-запрос на `/api/v1/cloud-ai/skills/{skill_id}/agents/sync-versions`.  Агенты, у которых навык выключен, остаются на своих версиях. Сколько агентов переведено, видно в `meta.updated_count`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.sync_agent_skill_agents_versions200_response import SyncAgentSkillAgentsVersions200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    skill_id = 12 # object | ID навыка

    try:
        # Перевод всех агентов навыка на текущую версию
        api_response = api_instance.sync_agent_skill_agents_versions(skill_id)
        print("The response of AIAgentSkillsApi->sync_agent_skill_agents_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->sync_agent_skill_agents_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | [**object**](.md)| ID навыка | 

### Return type

[**SyncAgentSkillAgentsVersions200Response**](SyncAgentSkillAgentsVersions200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;skill&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync_agent_skill_versions_for_agent**
> SyncAgentSkillVersionsForAgent200Response sync_agent_skill_versions_for_agent(agent_id)

Перевод всех навыков агента на текущие версии

Чтобы перевести все включённые у агента навыки на их текущие версии, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/sync-versions`.  В ответе все навыки аккаунта с состоянием у агента, как в списке навыков агента. Сколько навыков переведено, видно в `updated_count` в корне ответа.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.sync_agent_skill_versions_for_agent200_response import SyncAgentSkillVersionsForAgent200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    agent_id = 113191 # object | ID агента

    try:
        # Перевод всех навыков агента на текущие версии
        api_response = api_instance.sync_agent_skill_versions_for_agent(agent_id)
        print("The response of AIAgentSkillsApi->sync_agent_skill_versions_for_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->sync_agent_skill_versions_for_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 

### Return type

[**SyncAgentSkillVersionsForAgent200Response**](SyncAgentSkillVersionsForAgent200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;agent_skills&#x60;, &#x60;meta&#x60; и &#x60;updated_count&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_skill**
> CreateAgentSkill201Response update_agent_skill(skill_id, update_skill)

Изменение навыка

Чтобы изменить навык, отправьте PATCH-запрос на `/api/v1/cloud-ai/skills/{skill_id}`, передав только изменяемые поля.  Изменение «когда применять», инструкции или скриптов создаёт новую версию. Переименование и сохранение без изменений версию не создают (`meta.version_created`). Подключённые агенты остаются на своих версиях. Сколько агентов затронуто, видно в `meta.affected_agents_count`. Если в истории уже 50 версий, самая старая свободная версия удаляется (`meta.pruned_versions`). Скрипты передаются в теле запроса. Их общий размер — до 10 МБ, а всё тело запроса — до 16 МБ; запрос с телом больше отклоняется до проверки.  Возможные ошибки 409: `skill_name_already_exists` — название занято; `skill_versions_limit_exceeded` — все 50 версий заняты текущей и закреплёнными за агентами; `skill_was_modified_concurrently` — навык одновременно изменён другим запросом, повторите сохранение.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_skill201_response import CreateAgentSkill201Response
from timeweb_cloud_api.models.update_skill import UpdateSkill
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    skill_id = 12 # object | ID навыка
    update_skill = timeweb_cloud_api.UpdateSkill() # UpdateSkill | 

    try:
        # Изменение навыка
        api_response = api_instance.update_agent_skill(skill_id, update_skill)
        print("The response of AIAgentSkillsApi->update_agent_skill:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->update_agent_skill: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skill_id** | [**object**](.md)| ID навыка | 
 **update_skill** | [**UpdateSkill**](UpdateSkill.md)|  | 

### Return type

[**CreateAgentSkill201Response**](CreateAgentSkill201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;skill&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_skill_version_for_agent**
> SetAgentSkillForAgent200Response update_agent_skill_version_for_agent(agent_id, skill_id)

Перевод агента на текущую версию навыка

Чтобы перевести агента на текущую версию навыка, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/skills/{skill_id}/update-version`.  Если навык не подключён к агенту, вернётся 404 с `error_code` `agent_skill_link_not_found`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.set_agent_skill_for_agent200_response import SetAgentSkillForAgent200Response
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
    api_instance = timeweb_cloud_api.AIAgentSkillsApi(api_client)
    agent_id = 113191 # object | ID агента
    skill_id = 12 # object | ID навыка

    try:
        # Перевод агента на текущую версию навыка
        api_response = api_instance.update_agent_skill_version_for_agent(agent_id, skill_id)
        print("The response of AIAgentSkillsApi->update_agent_skill_version_for_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentSkillsApi->update_agent_skill_version_for_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 
 **skill_id** | [**object**](.md)| ID навыка | 

### Return type

[**SetAgentSkillForAgent200Response**](SetAgentSkillForAgent200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;agent_skill&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

