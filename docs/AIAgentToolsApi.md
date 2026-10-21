# timeweb_cloud_api.AIAgentToolsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_agent_tool_to_agent**](AIAgentToolsApi.md#connect_agent_tool_to_agent) | **POST** /api/v1/cloud-ai/agents/{agent_id}/tools | Подключение MCP-инструмента к агенту
[**create_agent_tool**](AIAgentToolsApi.md#create_agent_tool) | **POST** /api/v1/cloud-ai/tools | Подключение собственного MCP-сервера
[**delete_agent_tool**](AIAgentToolsApi.md#delete_agent_tool) | **DELETE** /api/v1/cloud-ai/tools/{id} | Удаление MCP-инструмента
[**disconnect_agent_tool_from_agent**](AIAgentToolsApi.md#disconnect_agent_tool_from_agent) | **DELETE** /api/v1/cloud-ai/agents/{agent_id}/tools/{tool_id} | Отключение MCP-инструмента от агента
[**get_agent_tool**](AIAgentToolsApi.md#get_agent_tool) | **GET** /api/v1/cloud-ai/tools/{id} | Получение MCP-инструмента
[**get_agent_tool_o_auth2_authorize_url**](AIAgentToolsApi.md#get_agent_tool_o_auth2_authorize_url) | **GET** /api/v1/cloud-ai/tools/oauth2/authorize-url/{tool_id} | Получение ссылки на OAuth2-авторизацию инструмента
[**get_agent_tool_template_prices**](AIAgentToolsApi.md#get_agent_tool_template_prices) | **GET** /api/v1/cloud-ai/tools/templates/prices | Получение цен системных инструментов
[**get_agent_tool_templates**](AIAgentToolsApi.md#get_agent_tool_templates) | **GET** /api/v1/cloud-ai/tools/templates/marketplace | Получение шаблонов MCP-инструментов из маркетплейса
[**get_agent_tools**](AIAgentToolsApi.md#get_agent_tools) | **GET** /api/v1/cloud-ai/tools | Получение списка MCP-инструментов
[**get_agent_tools_by_agent**](AIAgentToolsApi.md#get_agent_tools_by_agent) | **GET** /api/v1/cloud-ai/agents/{agent_id}/tools | Получение MCP-инструментов агента
[**install_agent_tool_from_template**](AIAgentToolsApi.md#install_agent_tool_from_template) | **POST** /api/v1/cloud-ai/tools/install | Установка MCP-инструмента из маркетплейса
[**refresh_agent_tool_methods**](AIAgentToolsApi.md#refresh_agent_tool_methods) | **POST** /api/v1/cloud-ai/tools/{id}/refresh-methods | Обновление списка методов MCP-инструмента
[**update_agent_tool**](AIAgentToolsApi.md#update_agent_tool) | **PUT** /api/v1/cloud-ai/tools/{id} | Изменение MCP-инструмента
[**update_agent_tool_connection**](AIAgentToolsApi.md#update_agent_tool_connection) | **PUT** /api/v1/cloud-ai/agents/{agent_id}/tools/{tool_id} | Изменение разрешённых методов MCP-инструмента у агента


# **connect_agent_tool_to_agent**
> connect_agent_tool_to_agent(agent_id, connect_agent_tool)

Подключение MCP-инструмента к агенту

Чтобы подключить MCP-инструмент к агенту, отправьте POST-запрос на `/api/v1/cloud-ai/agents/{agent_id}/tools`.  В `allowed_methods` перечислите методы, которые агенту разрешено вызывать. Подходят только имена из `methods[].name` инструмента, иначе вернётся 400 с `error_code` `invalid_methods_provided`. Повторно подключить уже подключённый инструмент нельзя. Чтобы изменить список методов, используйте PUT-запрос.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.connect_agent_tool import ConnectAgentTool
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    agent_id = 113191 # object | ID агента
    connect_agent_tool = timeweb_cloud_api.ConnectAgentTool() # ConnectAgentTool | 

    try:
        # Подключение MCP-инструмента к агенту
        api_instance.connect_agent_tool_to_agent(agent_id, connect_agent_tool)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->connect_agent_tool_to_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 
 **connect_agent_tool** | [**ConnectAgentTool**](ConnectAgentTool.md)|  | 

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
**201** | Инструмент подключён к агенту. Тело ответа пустое |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_tool**
> CreateAgentTool201Response create_agent_tool(create_tool)

Подключение собственного MCP-сервера

Чтобы подключить собственный MCP-сервер, отправьте POST-запрос на `/api/v1/cloud-ai/tools`.  Платформа сразу подключается к серверу и сохраняет список его методов. Если сервер недоступен или отвечает ошибкой, инструмент не создаётся: вернётся 400 с `error_code` `invalid_methods_provided`. Адреса частных сетей и localhost отклоняются с ошибкой 400.  Для `auth_data.type = oauth2` подключение к серверу при создании не проверяется. Инструмент создаётся в статусе `pending_auth` с пустым списком методов, а методы загружаются после авторизации пользователя: см. «Получение ссылки на OAuth2-авторизацию инструмента». Если не удалось определить адреса авторизации или зарегистрировать клиента, вернётся 401 с `error_code` `tool_authentication_failed`.  Чтобы агент мог пользоваться инструментом, подключите его к агенту.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_tool201_response import CreateAgentTool201Response
from timeweb_cloud_api.models.create_tool import CreateTool
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    create_tool = timeweb_cloud_api.CreateTool() # CreateTool | 

    try:
        # Подключение собственного MCP-сервера
        api_response = api_instance.create_agent_tool(create_tool)
        print("The response of AIAgentToolsApi->create_agent_tool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->create_agent_tool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_tool** | [**CreateTool**](CreateTool.md)|  | 

### Return type

[**CreateAgentTool201Response**](CreateAgentTool201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;tool&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_tool**
> delete_agent_tool(id)

Удаление MCP-инструмента

Чтобы удалить MCP-инструмент, отправьте DELETE-запрос на `/api/v1/cloud-ai/tools/{id}`.  Инструмент автоматически отключается от всех агентов.

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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    id = 417 # object | ID инструмента

    try:
        # Удаление MCP-инструмента
        api_instance.delete_agent_tool(id)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->delete_agent_tool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID инструмента | 

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
**200** | Инструмент удалён. Тело ответа пустое |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disconnect_agent_tool_from_agent**
> disconnect_agent_tool_from_agent(agent_id, tool_id)

Отключение MCP-инструмента от агента

Чтобы отключить MCP-инструмент от агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/agents/{agent_id}/tools/{tool_id}`.  Сам инструмент остаётся в аккаунте и у других агентов.

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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    agent_id = 113191 # object | ID агента
    tool_id = 417 # object | ID инструмента

    try:
        # Отключение MCP-инструмента от агента
        api_instance.disconnect_agent_tool_from_agent(agent_id, tool_id)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->disconnect_agent_tool_from_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 
 **tool_id** | [**object**](.md)| ID инструмента | 

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
**200** | Инструмент отключён от агента. Тело ответа пустое |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_tool**
> CreateAgentTool201Response get_agent_tool(id)

Получение MCP-инструмента

Чтобы получить MCP-инструмент, отправьте GET-запрос на `/api/v1/cloud-ai/tools/{id}`.  По полю `status` можно отследить завершение OAuth2-авторизации: после неё статус меняется с `pending_auth` на `active`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_tool201_response import CreateAgentTool201Response
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    id = 417 # object | ID инструмента

    try:
        # Получение MCP-инструмента
        api_response = api_instance.get_agent_tool(id)
        print("The response of AIAgentToolsApi->get_agent_tool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->get_agent_tool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID инструмента | 

### Return type

[**CreateAgentTool201Response**](CreateAgentTool201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;tool&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_tool_o_auth2_authorize_url**
> AuthorizeUrl get_agent_tool_o_auth2_authorize_url(tool_id, redirect_url=redirect_url)

Получение ссылки на OAuth2-авторизацию инструмента

Чтобы получить ссылку на OAuth2-авторизацию MCP-инструмента, отправьте GET-запрос на `/api/v1/cloud-ai/tools/oauth2/authorize-url/{tool_id}`.  Откройте `authorize_url` в браузере пользователя. Ссылка действует 30 минут. После входа и согласия провайдер вернёт пользователя на адрес возврата платформы `https://api.timeweb.cloud/api/v1/cloud-ai/oauth2/callback`. Платформа обменяет код на токены, переведёт инструмент в статус `active` и загрузит список методов.  Чтобы узнать результат, запрашивайте инструмент, пока его статус не сменится с `pending_auth` на `active`. Этим же запросом можно повторно авторизовать уже активный инструмент.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.authorize_url import AuthorizeUrl
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    tool_id = 417 # object | ID инструмента
    redirect_url = https://timeweb.cloud/my/cloud-ai # object | Куда вернуть пользователя после авторизации. Принимаются только адреса на доменах `timeweb.cloud` и `timeweb.net` и их поддоменах; другие адреса молча игнорируются. После успешной авторизации к адресу добавляются `oauth_success=true&tool_id=<id>`, после ошибки — `oauth_error=<текст>&tool_id=<id>`. Без параметра страница возврата показывает результат в виде JSON. (optional)

    try:
        # Получение ссылки на OAuth2-авторизацию инструмента
        api_response = api_instance.get_agent_tool_o_auth2_authorize_url(tool_id, redirect_url=redirect_url)
        print("The response of AIAgentToolsApi->get_agent_tool_o_auth2_authorize_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->get_agent_tool_o_auth2_authorize_url: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_id** | [**object**](.md)| ID инструмента | 
 **redirect_url** | [**object**](.md)| Куда вернуть пользователя после авторизации. Принимаются только адреса на доменах &#x60;timeweb.cloud&#x60; и &#x60;timeweb.net&#x60; и их поддоменах; другие адреса молча игнорируются. После успешной авторизации к адресу добавляются &#x60;oauth_success&#x3D;true&amp;tool_id&#x3D;&lt;id&gt;&#x60;, после ошибки — &#x60;oauth_error&#x3D;&lt;текст&gt;&amp;tool_id&#x3D;&lt;id&gt;&#x60;. Без параметра страница возврата показывает результат в виде JSON. | [optional] 

### Return type

[**AuthorizeUrl**](AuthorizeUrl.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;authorize_url&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_tool_template_prices**
> GetAgentToolTemplatePrices200Response get_agent_tool_template_prices(locale=locale)

Получение цен системных инструментов

Чтобы получить цены системных инструментов платформы, например веб-поиска, отправьте GET-запрос на `/api/v1/cloud-ai/tools/templates/prices`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_tool_template_prices200_response import GetAgentToolTemplatePrices200Response
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    locale = ru # object | Валюта цены: `ru` — в рублях, `en` — в долларах США. По умолчанию `ru`. (optional)

    try:
        # Получение цен системных инструментов
        api_response = api_instance.get_agent_tool_template_prices(locale=locale)
        print("The response of AIAgentToolsApi->get_agent_tool_template_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->get_agent_tool_template_prices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **locale** | [**object**](.md)| Валюта цены: &#x60;ru&#x60; — в рублях, &#x60;en&#x60; — в долларах США. По умолчанию &#x60;ru&#x60;. | [optional] 

### Return type

[**GetAgentToolTemplatePrices200Response**](GetAgentToolTemplatePrices200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;system_tool_prices&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_tool_templates**
> GetAgentToolTemplates200Response get_agent_tool_templates()

Получение шаблонов MCP-инструментов из маркетплейса

Чтобы получить готовые интеграции маркетплейса, отправьте GET-запрос на `/api/v1/cloud-ai/tools/templates/marketplace`.  Сначала идут самые популярные шаблоны. Поле `config_schema` описывает, что нужно передать в `config_values` при установке.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_tool_templates200_response import GetAgentToolTemplates200Response
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)

    try:
        # Получение шаблонов MCP-инструментов из маркетплейса
        api_response = api_instance.get_agent_tool_templates()
        print("The response of AIAgentToolsApi->get_agent_tool_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->get_agent_tool_templates: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAgentToolTemplates200Response**](GetAgentToolTemplates200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;tool_templates&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_tools**
> GetAgentTools200Response get_agent_tools()

Получение списка MCP-инструментов

Чтобы получить список MCP-инструментов аккаунта, отправьте GET-запрос на `/api/v1/cloud-ai/tools`.  В списке есть и собственные MCP-серверы, и инструменты, установленные из маркетплейса. Сначала идут новые. Удалённые инструменты не возвращаются. Секреты в `auth_data` заменены на `********`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_tools200_response import GetAgentTools200Response
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)

    try:
        # Получение списка MCP-инструментов
        api_response = api_instance.get_agent_tools()
        print("The response of AIAgentToolsApi->get_agent_tools:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->get_agent_tools: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAgentTools200Response**](GetAgentTools200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;tools&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_tools_by_agent**
> GetAgentToolsByAgent200Response get_agent_tools_by_agent(agent_id)

Получение MCP-инструментов агента

Чтобы получить MCP-инструменты, подключённые к агенту, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{agent_id}/tools`.  В ответе — инструменты целиком, в том же виде, что и в списке инструментов аккаунта. Списка разрешённых агенту методов в ответе нет.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_tools_by_agent200_response import GetAgentToolsByAgent200Response
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    agent_id = 113191 # object | ID агента

    try:
        # Получение MCP-инструментов агента
        api_response = api_instance.get_agent_tools_by_agent(agent_id)
        print("The response of AIAgentToolsApi->get_agent_tools_by_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->get_agent_tools_by_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 

### Return type

[**GetAgentToolsByAgent200Response**](GetAgentToolsByAgent200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;agent_tools&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **install_agent_tool_from_template**
> CreateAgentTool201Response install_agent_tool_from_template(install_tool)

Установка MCP-инструмента из маркетплейса

Чтобы установить MCP-инструмент из шаблона маркетплейса, отправьте POST-запрос на `/api/v1/cloud-ai/tools/install`.  Значения полей из `config_schema` шаблона передайте в `config_values`. Платформа соберёт из них заголовки авторизации, подключится к MCP-серверу и сохранит список методов. Если у шаблона есть `config_schema`, поле `auth_data` не используется. Если подключиться к серверу не удалось, вернётся 400 с `error_code` `invalid_methods_provided`.  Один шаблон можно установить несколько раз, например с разными ключами.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_tool201_response import CreateAgentTool201Response
from timeweb_cloud_api.models.install_tool import InstallTool
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    install_tool = timeweb_cloud_api.InstallTool() # InstallTool | 

    try:
        # Установка MCP-инструмента из маркетплейса
        api_response = api_instance.install_agent_tool_from_template(install_tool)
        print("The response of AIAgentToolsApi->install_agent_tool_from_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->install_agent_tool_from_template: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_tool** | [**InstallTool**](InstallTool.md)|  | 

### Return type

[**CreateAgentTool201Response**](CreateAgentTool201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;tool&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_agent_tool_methods**
> CreateAgentTool201Response refresh_agent_tool_methods(id)

Обновление списка методов MCP-инструмента

Чтобы заново получить список методов с MCP-сервера, отправьте POST-запрос на `/api/v1/cloud-ai/tools/{id}/refresh-methods`.  Список `methods` заменяется полученным с сервера, а методы, которых больше нет, убираются из разрешённых у всех агентов. Если обновление прошло успешно, инструмент переходит в статус `active`. Если сервер недоступен, инструмент переходит в статус `error` с причиной в `status_info`, а запрос возвращает 400 с `error_code` `invalid_methods_provided`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_tool201_response import CreateAgentTool201Response
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    id = 417 # object | ID инструмента

    try:
        # Обновление списка методов MCP-инструмента
        api_response = api_instance.refresh_agent_tool_methods(id)
        print("The response of AIAgentToolsApi->refresh_agent_tool_methods:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->refresh_agent_tool_methods: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID инструмента | 

### Return type

[**CreateAgentTool201Response**](CreateAgentTool201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;tool&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_tool**
> CreateAgentTool201Response update_agent_tool(id, update_tool)

Изменение MCP-инструмента

Чтобы изменить MCP-инструмент, отправьте PUT-запрос на `/api/v1/cloud-ai/tools/{id}`, передав только изменяемые поля.  Если передать в `auth_data` секрет `********` из ответа API, сохранённый секрет не изменится. Изменение адреса или авторизации не обновляет список методов: после него вызовите обновление методов. Статус `inactive` выключает инструмент у всех агентов, к которым он подключён.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_tool201_response import CreateAgentTool201Response
from timeweb_cloud_api.models.update_tool import UpdateTool
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    id = 417 # object | ID инструмента
    update_tool = timeweb_cloud_api.UpdateTool() # UpdateTool | 

    try:
        # Изменение MCP-инструмента
        api_response = api_instance.update_agent_tool(id, update_tool)
        print("The response of AIAgentToolsApi->update_agent_tool:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->update_agent_tool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)| ID инструмента | 
 **update_tool** | [**UpdateTool**](UpdateTool.md)|  | 

### Return type

[**CreateAgentTool201Response**](CreateAgentTool201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;tool&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_tool_connection**
> update_agent_tool_connection(agent_id, tool_id, update_agent_tool)

Изменение разрешённых методов MCP-инструмента у агента

Чтобы изменить список методов, которые агенту разрешено вызывать, отправьте PUT-запрос на `/api/v1/cloud-ai/agents/{agent_id}/tools/{tool_id}`.  Список заменяется целиком. Подходят только имена из `methods[].name` инструмента, иначе вернётся 400 с `error_code` `invalid_methods_provided`. Если инструмент не подключён к агенту, вернётся 404 с `error_code` `agent-tool_link_not_found`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.update_agent_tool import UpdateAgentTool
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
    api_instance = timeweb_cloud_api.AIAgentToolsApi(api_client)
    agent_id = 113191 # object | ID агента
    tool_id = 417 # object | ID инструмента
    update_agent_tool = timeweb_cloud_api.UpdateAgentTool() # UpdateAgentTool | 

    try:
        # Изменение разрешённых методов MCP-инструмента у агента
        api_instance.update_agent_tool_connection(agent_id, tool_id, update_agent_tool)
    except Exception as e:
        print("Exception when calling AIAgentToolsApi->update_agent_tool_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 
 **tool_id** | [**object**](.md)| ID инструмента | 
 **update_agent_tool** | [**UpdateAgentTool**](UpdateAgentTool.md)|  | 

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
**200** | Запрос выполнен. Тело ответа пустое |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

