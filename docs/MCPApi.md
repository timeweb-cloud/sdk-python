# timeweb_cloud_api.MCPApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_mcp_search_session**](MCPApi.md#delete_mcp_search_session) | **DELETE** /api/v1/mcp/search | Завершение сессии сервера MCP с поиском инструментов
[**delete_mcp_session**](MCPApi.md#delete_mcp_session) | **DELETE** /api/v1/mcp | Завершение сессии сервера MCP
[**open_mcp_search_stream**](MCPApi.md#open_mcp_search_stream) | **GET** /api/v1/mcp/search | Открытие потока событий сервера MCP с поиском инструментов
[**open_mcp_stream**](MCPApi.md#open_mcp_stream) | **GET** /api/v1/mcp | Открытие потока событий сервера MCP
[**send_mcp_message**](MCPApi.md#send_mcp_message) | **POST** /api/v1/mcp | Отправка JSON-RPC-сообщения серверу MCP
[**send_mcp_search_message**](MCPApi.md#send_mcp_search_message) | **POST** /api/v1/mcp/search | Отправка JSON-RPC-сообщения серверу MCP с поиском инструментов


# **delete_mcp_search_session**
> delete_mcp_search_session()

Завершение сессии сервера MCP с поиском инструментов

Чтобы завершить сессию сервера MCP `timeweb-cloud-mcp-search`, отправьте DELETE-запрос на `/api/v1/mcp/search`.  Сервер не хранит сессий (не выдаёт `Mcp-Session-Id`), поэтому завершать нечего: ответ всегда 200 без тела.

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
    api_instance = timeweb_cloud_api.MCPApi(api_client)

    try:
        # Завершение сессии сервера MCP с поиском инструментов
        api_instance.delete_mcp_search_session()
    except Exception as e:
        print("Exception when calling MCPApi->delete_mcp_search_session: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | Готово, тела нет |  -  |
**401** |  |  -  |
**429** | Превышен лимит запросов для токена |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mcp_session**
> delete_mcp_session()

Завершение сессии сервера MCP

Чтобы завершить сессию сервера MCP `timeweb-cloud-mcp`, отправьте DELETE-запрос на `/api/v1/mcp`.  Сервер не хранит сессий (не выдаёт `Mcp-Session-Id`), поэтому завершать нечего: ответ всегда 200 без тела.

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
    api_instance = timeweb_cloud_api.MCPApi(api_client)

    try:
        # Завершение сессии сервера MCP
        api_instance.delete_mcp_session()
    except Exception as e:
        print("Exception when calling MCPApi->delete_mcp_session: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**200** | Готово, тела нет |  -  |
**401** |  |  -  |
**429** | Превышен лимит запросов для токена |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_mcp_search_stream**
> object open_mcp_search_stream(accept, mcp_protocol_version=mcp_protocol_version)

Открытие потока событий сервера MCP с поиском инструментов

Чтобы открыть поток сообщений, которые сервер MCP `timeweb-cloud-mcp-search` отправляет по своей инициативе, отправьте GET-запрос на `/api/v1/mcp/search`.  Сервер не отправляет сообщений по своей инициативе, поэтому поток не содержит событий и остаётся открытым, пока его не закроет шлюз. Через шлюз заголовки ответа на этот запрос могут долго не приходить. Открывать поток не нужно: работайте с сервером только POST-запросами — если клиент позволяет выбрать режим, отключите в нём GET-поток.

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
    api_instance = timeweb_cloud_api.MCPApi(api_client)
    accept = text/event-stream # object | Должен содержать `text/event-stream`, иначе сервер ответит 406
    mcp_protocol_version = 2025-06-18 # object | Версия протокола, согласованная в `initialize`. Неподдерживаемое значение — ответ 400 (optional)

    try:
        # Открытие потока событий сервера MCP с поиском инструментов
        api_response = api_instance.open_mcp_search_stream(accept, mcp_protocol_version=mcp_protocol_version)
        print("The response of MCPApi->open_mcp_search_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->open_mcp_search_stream: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | [**object**](.md)| Должен содержать &#x60;text/event-stream&#x60;, иначе сервер ответит 406 | 
 **mcp_protocol_version** | [**object**](.md)| Версия протокола, согласованная в &#x60;initialize&#x60;. Неподдерживаемое значение — ответ 400 | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Поток событий без событий: сервер не отправляет сообщений по своей инициативе |  -  |
**401** |  |  -  |
**406** | Заголовок &#x60;Accept&#x60; не содержит &#x60;text/event-stream&#x60; |  -  |
**429** | Превышен лимит запросов для токена |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_mcp_stream**
> object open_mcp_stream(accept, mcp_protocol_version=mcp_protocol_version)

Открытие потока событий сервера MCP

Чтобы открыть поток сообщений, которые сервер MCP `timeweb-cloud-mcp` отправляет по своей инициативе, отправьте GET-запрос на `/api/v1/mcp`.  Сервер не отправляет сообщений по своей инициативе, поэтому поток не содержит событий и остаётся открытым, пока его не закроет шлюз. Через шлюз заголовки ответа на этот запрос могут долго не приходить. Открывать поток не нужно: работайте с сервером только POST-запросами — если клиент позволяет выбрать режим, отключите в нём GET-поток.

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
    api_instance = timeweb_cloud_api.MCPApi(api_client)
    accept = text/event-stream # object | Должен содержать `text/event-stream`, иначе сервер ответит 406
    mcp_protocol_version = 2025-06-18 # object | Версия протокола, согласованная в `initialize`. Неподдерживаемое значение — ответ 400 (optional)

    try:
        # Открытие потока событий сервера MCP
        api_response = api_instance.open_mcp_stream(accept, mcp_protocol_version=mcp_protocol_version)
        print("The response of MCPApi->open_mcp_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->open_mcp_stream: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | [**object**](.md)| Должен содержать &#x60;text/event-stream&#x60;, иначе сервер ответит 406 | 
 **mcp_protocol_version** | [**object**](.md)| Версия протокола, согласованная в &#x60;initialize&#x60;. Неподдерживаемое значение — ответ 400 | [optional] 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Поток событий без событий: сервер не отправляет сообщений по своей инициативе |  -  |
**401** |  |  -  |
**406** | Заголовок &#x60;Accept&#x60; не содержит &#x60;text/event-stream&#x60; |  -  |
**429** | Превышен лимит запросов для токена |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_mcp_message**
> JsonRpcResultResponse send_mcp_message(accept, json_rpc_request, mcp_protocol_version=mcp_protocol_version, x_mcp_confirmation_ui=x_mcp_confirmation_ui)

Отправка JSON-RPC-сообщения серверу MCP

Чтобы отправить запрос или уведомление серверу MCP `timeweb-cloud-mcp`, отправьте POST-запрос на `/api/v1/mcp` с сообщением JSON-RPC 2.0 в теле.  Через этот метод идут все запросы MCP: `initialize`, `tools/list` (все инструменты сразу), `tools/call`, `resources/list`, `resources/read`, `ping`. Ответ на запрос приходит потоком `text/event-stream` с одним событием `message`, уведомление принимается с кодом 202 без тела. Изменяющие инструменты выполняются в два вызова с `confirm_token` — см. описание раздела.  Заголовки `x-tool-access` и `x-allowed-tools` здесь не действуют — используйте `/api/v1/mcp/search`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.json_rpc_request import JsonRpcRequest
from timeweb_cloud_api.models.json_rpc_result_response import JsonRpcResultResponse
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
    api_instance = timeweb_cloud_api.MCPApi(api_client)
    accept = application/json, text/event-stream # object | Должен содержать и `application/json`, и `text/event-stream`, иначе сервер ответит 406
    json_rpc_request = {"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"my-agent","version":"1.0.0"}}} # JsonRpcRequest | 
    mcp_protocol_version = 2025-06-18 # object | Версия протокола, согласованная в `initialize`. Неподдерживаемое значение — ответ 400 (optional)
    x_mcp_confirmation_ui = text # object | Как `request_user_confirmation` спрашивает пользователя. `text` (по умолчанию) — пользователь отвечает в чате, на `/api/v1/mcp` инструмент в этом режиме не выводится. `buttons` — инструмент возвращает `ui_action` с кнопками для клиентов, которые умеют их показывать. Регистр не важен, другие значения игнорируются (optional)

    try:
        # Отправка JSON-RPC-сообщения серверу MCP
        api_response = api_instance.send_mcp_message(accept, json_rpc_request, mcp_protocol_version=mcp_protocol_version, x_mcp_confirmation_ui=x_mcp_confirmation_ui)
        print("The response of MCPApi->send_mcp_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->send_mcp_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | [**object**](.md)| Должен содержать и &#x60;application/json&#x60;, и &#x60;text/event-stream&#x60;, иначе сервер ответит 406 | 
 **json_rpc_request** | [**JsonRpcRequest**](JsonRpcRequest.md)|  | 
 **mcp_protocol_version** | [**object**](.md)| Версия протокола, согласованная в &#x60;initialize&#x60;. Неподдерживаемое значение — ответ 400 | [optional] 
 **x_mcp_confirmation_ui** | [**object**](.md)| Как &#x60;request_user_confirmation&#x60; спрашивает пользователя. &#x60;text&#x60; (по умолчанию) — пользователь отвечает в чате, на &#x60;/api/v1/mcp&#x60; инструмент в этом режиме не выводится. &#x60;buttons&#x60; — инструмент возвращает &#x60;ui_action&#x60; с кнопками для клиентов, которые умеют их показывать. Регистр не важен, другие значения игнорируются | [optional] 

### Return type

[**JsonRpcResultResponse**](JsonRpcResultResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ на запрос: поток &#x60;text/event-stream&#x60; с одним событием &#x60;message&#x60;. В &#x60;data&#x60; события — ответ JSON-RPC (схема и примеры ниже): успешный или с ошибкой JSON-RPC, например &#x60;-32601&#x60; для неизвестного метода. Пример потока:  &#x60;&#x60;&#x60; event: message data: {\&quot;jsonrpc\&quot;:\&quot;2.0\&quot;,\&quot;id\&quot;:1,\&quot;result\&quot;:{\&quot;tools\&quot;:[...]}} &#x60;&#x60;&#x60; |  -  |
**202** | Уведомление принято, тела нет |  -  |
**400** | Тело не является корректным JSON или сообщением JSON-RPC (&#x60;-32700&#x60;), заголовок &#x60;MCP-Protocol-Version&#x60; содержит неподдерживаемую версию (&#x60;-32000&#x60;) |  -  |
**401** |  |  -  |
**406** | Заголовок &#x60;Accept&#x60; не содержит &#x60;application/json&#x60; или &#x60;text/event-stream&#x60; |  -  |
**415** | &#x60;Content-Type&#x60; не &#x60;application/json&#x60; |  -  |
**429** | Превышен лимит запросов для токена |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_mcp_search_message**
> JsonRpcResultResponse send_mcp_search_message(accept, json_rpc_request, mcp_protocol_version=mcp_protocol_version, x_tool_access=x_tool_access, x_allowed_tools=x_allowed_tools, x_mcp_confirmation_ui=x_mcp_confirmation_ui)

Отправка JSON-RPC-сообщения серверу MCP с поиском инструментов

Чтобы отправить запрос или уведомление серверу MCP `timeweb-cloud-mcp-search`, отправьте POST-запрос на `/api/v1/mcp/search` с сообщением JSON-RPC 2.0 в теле.  `tools/list` возвращает четыре инструмента: `search_tools`, `get_tool_definition`, `execute_tool` и `request_user_confirmation`. Все операции облака находятся через `search_tools` и выполняются через `execute_tool`; изменяющие операции — в два вызова `execute_tool` с `confirm_token` внутри `arguments`.  Доступ модели можно сузить заголовками `x-tool-access` и `x-allowed-tools`. Недопустимое значение `x-tool-access` — ответ 400 с ошибкой `-32600`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.json_rpc_request import JsonRpcRequest
from timeweb_cloud_api.models.json_rpc_result_response import JsonRpcResultResponse
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
    api_instance = timeweb_cloud_api.MCPApi(api_client)
    accept = application/json, text/event-stream # object | Должен содержать и `application/json`, и `text/event-stream`, иначе сервер ответит 406
    json_rpc_request = {jsonrpc=2.0, id=1, method=initialize, params={protocolVersion=2025-06-18, capabilities={}, clientInfo={name=my-agent, version=1.0.0}}} # JsonRpcRequest | 
    mcp_protocol_version = 2025-06-18 # object | Версия протокола, согласованная в `initialize`. Неподдерживаемое значение — ответ 400 (optional)
    x_tool_access = read-only # object | Только операции чтения: поиск и определения пропускают изменяющие инструменты, а `execute_tool` отказывает с `tool_not_allowed`. Единственное допустимое значение — `read-only` (регистр не важен); любое другое, в том числе пустое, — ответ 400 с ошибкой `-32600` (optional)
    x_allowed_tools = list_servers,get_server,server_action # object | Имена разрешённых операций через запятую — все остальные недоступны. Неизвестные имена игнорируются, пустое значение не разрешает ничего. Вместе с `x-tool-access` операция должна пройти оба ограничения (optional)
    x_mcp_confirmation_ui = text # object | Как `request_user_confirmation` спрашивает пользователя. `text` (по умолчанию) — пользователь отвечает в чате, на `/api/v1/mcp` инструмент в этом режиме не выводится. `buttons` — инструмент возвращает `ui_action` с кнопками для клиентов, которые умеют их показывать. Регистр не важен, другие значения игнорируются (optional)

    try:
        # Отправка JSON-RPC-сообщения серверу MCP с поиском инструментов
        api_response = api_instance.send_mcp_search_message(accept, json_rpc_request, mcp_protocol_version=mcp_protocol_version, x_tool_access=x_tool_access, x_allowed_tools=x_allowed_tools, x_mcp_confirmation_ui=x_mcp_confirmation_ui)
        print("The response of MCPApi->send_mcp_search_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->send_mcp_search_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accept** | [**object**](.md)| Должен содержать и &#x60;application/json&#x60;, и &#x60;text/event-stream&#x60;, иначе сервер ответит 406 | 
 **json_rpc_request** | [**JsonRpcRequest**](JsonRpcRequest.md)|  | 
 **mcp_protocol_version** | [**object**](.md)| Версия протокола, согласованная в &#x60;initialize&#x60;. Неподдерживаемое значение — ответ 400 | [optional] 
 **x_tool_access** | [**object**](.md)| Только операции чтения: поиск и определения пропускают изменяющие инструменты, а &#x60;execute_tool&#x60; отказывает с &#x60;tool_not_allowed&#x60;. Единственное допустимое значение — &#x60;read-only&#x60; (регистр не важен); любое другое, в том числе пустое, — ответ 400 с ошибкой &#x60;-32600&#x60; | [optional] 
 **x_allowed_tools** | [**object**](.md)| Имена разрешённых операций через запятую — все остальные недоступны. Неизвестные имена игнорируются, пустое значение не разрешает ничего. Вместе с &#x60;x-tool-access&#x60; операция должна пройти оба ограничения | [optional] 
 **x_mcp_confirmation_ui** | [**object**](.md)| Как &#x60;request_user_confirmation&#x60; спрашивает пользователя. &#x60;text&#x60; (по умолчанию) — пользователь отвечает в чате, на &#x60;/api/v1/mcp&#x60; инструмент в этом режиме не выводится. &#x60;buttons&#x60; — инструмент возвращает &#x60;ui_action&#x60; с кнопками для клиентов, которые умеют их показывать. Регистр не важен, другие значения игнорируются | [optional] 

### Return type

[**JsonRpcResultResponse**](JsonRpcResultResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ на запрос: поток &#x60;text/event-stream&#x60; с одним событием &#x60;message&#x60;. В &#x60;data&#x60; события — ответ JSON-RPC (схема и примеры ниже): успешный или с ошибкой JSON-RPC, например &#x60;-32601&#x60; для неизвестного метода. Пример потока:  &#x60;&#x60;&#x60; event: message data: {\&quot;jsonrpc\&quot;:\&quot;2.0\&quot;,\&quot;id\&quot;:1,\&quot;result\&quot;:{\&quot;tools\&quot;:[...]}} &#x60;&#x60;&#x60; |  -  |
**202** | Уведомление принято, тела нет |  -  |
**400** | Тело не является корректным JSON или сообщением JSON-RPC (&#x60;-32700&#x60;), заголовок &#x60;MCP-Protocol-Version&#x60; содержит неподдерживаемую версию (&#x60;-32000&#x60;) или недопустимое значение &#x60;x-tool-access&#x60; (&#x60;-32600&#x60;) |  -  |
**401** |  |  -  |
**406** | Заголовок &#x60;Accept&#x60; не содержит &#x60;application/json&#x60; или &#x60;text/event-stream&#x60; |  -  |
**415** | &#x60;Content-Type&#x60; не &#x60;application/json&#x60; |  -  |
**429** | Превышен лимит запросов для токена |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

