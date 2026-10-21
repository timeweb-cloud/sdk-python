# timeweb_cloud_api.AIAgentIntegrationsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_bot_max_bot**](AIAgentIntegrationsApi.md#create_agent_bot_max_bot) | **POST** /api/v1/cloud-ai/max-bots | Подключение бота MAX к агенту
[**create_agent_bot_telegram_bot**](AIAgentIntegrationsApi.md#create_agent_bot_telegram_bot) | **POST** /api/v1/cloud-ai/bots | Подключение Telegram-бота к агенту
[**create_agent_integration_crisp**](AIAgentIntegrationsApi.md#create_agent_integration_crisp) | **POST** /api/v1/cloud-ai/agent/{agent_id}/crisp | Подключение агента к Crisp
[**create_agent_integration_jivo**](AIAgentIntegrationsApi.md#create_agent_integration_jivo) | **POST** /api/v1/cloud-ai/agent/{agent_id}/jivo | Подключение агента к Jivo
[**delete_agent_bot_max_bot**](AIAgentIntegrationsApi.md#delete_agent_bot_max_bot) | **DELETE** /api/v1/cloud-ai/max-bots/{bot_id} | Отключение бота MAX
[**delete_agent_bot_telegram_bot**](AIAgentIntegrationsApi.md#delete_agent_bot_telegram_bot) | **DELETE** /api/v1/cloud-ai/bots/{bot_id} | Отключение Telegram-бота
[**delete_agent_integration_crisp**](AIAgentIntegrationsApi.md#delete_agent_integration_crisp) | **DELETE** /api/v1/cloud-ai/agent/{agent_id}/crisp | Отключение агента от Crisp
[**delete_agent_integration_jivo**](AIAgentIntegrationsApi.md#delete_agent_integration_jivo) | **DELETE** /api/v1/cloud-ai/agent/{agent_id}/jivo | Отключение агента от Jivo
[**get_agent_bot_max_bot**](AIAgentIntegrationsApi.md#get_agent_bot_max_bot) | **GET** /api/v1/cloud-ai/max-bots/{bot_id} | Получение информации о боте MAX
[**get_agent_bot_max_bots**](AIAgentIntegrationsApi.md#get_agent_bot_max_bots) | **GET** /api/v1/cloud-ai/max-bots | Получение списка ботов MAX
[**get_agent_bot_max_bots_by_agent**](AIAgentIntegrationsApi.md#get_agent_bot_max_bots_by_agent) | **GET** /api/v1/cloud-ai/agents/{agent_id}/max-bots | Получение списка ботов MAX агента
[**get_agent_bot_telegram_bot**](AIAgentIntegrationsApi.md#get_agent_bot_telegram_bot) | **GET** /api/v1/cloud-ai/bots/{bot_id} | Получение информации о Telegram-боте
[**get_agent_bot_telegram_bots**](AIAgentIntegrationsApi.md#get_agent_bot_telegram_bots) | **GET** /api/v1/cloud-ai/bots | Получение списка Telegram-ботов
[**get_agent_bot_telegram_bots_by_agent**](AIAgentIntegrationsApi.md#get_agent_bot_telegram_bots_by_agent) | **GET** /api/v1/cloud-ai/agents/{agent_id}/bots | Получение списка Telegram-ботов агента
[**get_agent_integration_crisp**](AIAgentIntegrationsApi.md#get_agent_integration_crisp) | **GET** /api/v1/cloud-ai/agent/{agent_id}/crisp | Получение интеграции агента с Crisp
[**get_agent_integration_jivo**](AIAgentIntegrationsApi.md#get_agent_integration_jivo) | **GET** /api/v1/cloud-ai/agent/{agent_id}/jivo | Получение интеграции агента с Jivo
[**update_agent_bot_max_bot**](AIAgentIntegrationsApi.md#update_agent_bot_max_bot) | **PATCH** /api/v1/cloud-ai/max-bots/{bot_id} | Изменение бота MAX
[**update_agent_bot_telegram_bot**](AIAgentIntegrationsApi.md#update_agent_bot_telegram_bot) | **PATCH** /api/v1/cloud-ai/bots/{bot_id} | Изменение Telegram-бота


# **create_agent_bot_max_bot**
> CreateAgentBotTelegramBot201Response create_agent_bot_max_bot(create_max_bot)

Подключение бота MAX к агенту

Чтобы подключить бота MAX к AI агенту, отправьте POST-запрос на `/api/v1/cloud-ai/max-bots`, передав ID агента и токен бота от @MasterBot.  Платформа проверит токен в MAX, сохранит бота и сама подпишет его на события (вебхук) — настраивать подписку в MAX не нужно. После этого агент начинает отвечать пользователям бота.  Один бот может быть подключен только к одному агенту. Если бот уже подключен к агенту, который был удален, бот будет переподключен к новому агенту. Ограничение доступа по списку пользователей для ботов MAX не поддерживается.  Ошибки: - `400 invalid_max_token` — MAX не принял токен; - `400 max_webhook_error` — не удалось подписать бота на события; - `409 bot_already_exists` — бот уже подключен к существующему агенту или к другому аккаунту.  Тело ответа будет представлять собой объект JSON с ключом `bot`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_bot_telegram_bot201_response import CreateAgentBotTelegramBot201Response
from timeweb_cloud_api.models.create_max_bot import CreateMaxBot
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    create_max_bot = timeweb_cloud_api.CreateMaxBot() # CreateMaxBot | 

    try:
        # Подключение бота MAX к агенту
        api_response = api_instance.create_agent_bot_max_bot(create_max_bot)
        print("The response of AIAgentIntegrationsApi->create_agent_bot_max_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->create_agent_bot_max_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_max_bot** | [**CreateMaxBot**](CreateMaxBot.md)|  | 

### Return type

[**CreateAgentBotTelegramBot201Response**](CreateAgentBotTelegramBot201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;bot&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_bot_telegram_bot**
> CreateAgentBotTelegramBot201Response create_agent_bot_telegram_bot(create_bot)

Подключение Telegram-бота к агенту

Чтобы подключить Telegram-бота к AI агенту, отправьте POST-запрос на `/api/v1/cloud-ai/bots`, передав ID агента и токен бота от @BotFather.  Платформа проверит токен в Telegram, сохранит бота и сама установит ему вебхук — настраивать вебхук в Telegram не нужно. После этого агент начинает отвечать пользователям бота. Ранее накопленные у бота обновления сбрасываются.  Один бот может быть подключен только к одному агенту. Если бот уже подключен к агенту, который был удален, бот будет переподключен к новому агенту.  Ошибки: - `400 invalid_telegram_token` — Telegram не принял токен; - `400 telegram_webhook_error` — не удалось установить вебхук; - `409 bot_already_exists` — бот уже подключен к существующему агенту или к другому аккаунту.  Тело ответа будет представлять собой объект JSON с ключом `bot`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_bot_telegram_bot201_response import CreateAgentBotTelegramBot201Response
from timeweb_cloud_api.models.create_bot import CreateBot
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    create_bot = timeweb_cloud_api.CreateBot() # CreateBot | 

    try:
        # Подключение Telegram-бота к агенту
        api_response = api_instance.create_agent_bot_telegram_bot(create_bot)
        print("The response of AIAgentIntegrationsApi->create_agent_bot_telegram_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->create_agent_bot_telegram_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_bot** | [**CreateBot**](CreateBot.md)|  | 

### Return type

[**CreateAgentBotTelegramBot201Response**](CreateAgentBotTelegramBot201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;bot&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_integration_crisp**
> GetAgentIntegrationCrisp200Response create_agent_integration_crisp(agent_id, create_crisp_integration)

Подключение агента к Crisp

Чтобы подключить AI агента к Crisp, отправьте POST-запрос на `/api/v1/cloud-ai/agent/{agent_id}/crisp`, передав Website ID сайта и API-токен Crisp (Identifier и Key).  Платформа проверит токен в Crisp и вернет `webhook_secret`. Затем добавьте в Crisp вебхук `https://api.timeweb.cloud/api/v1/crisp/{website_id}/webhook/{webhook_secret}` — подробнее в разделе «Интеграции AI агентов».  К одному агенту можно подключить один сайт Crisp, и один сайт — только к одному агенту.  Ошибки: - `400 invalid_crisp_token` — Crisp не принял токен для этого сайта; - `409 bot_already_exists` — у агента уже есть интеграция с Crisp или сайт подключен к другому агенту; - `503` — интеграция с Crisp временно недоступна.  Тело ответа будет представлять собой объект JSON с ключом `crisp_integration`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_crisp_integration import CreateCrispIntegration
from timeweb_cloud_api.models.get_agent_integration_crisp200_response import GetAgentIntegrationCrisp200Response
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    agent_id = 1 # object | ID агента
    create_crisp_integration = timeweb_cloud_api.CreateCrispIntegration() # CreateCrispIntegration | 

    try:
        # Подключение агента к Crisp
        api_response = api_instance.create_agent_integration_crisp(agent_id, create_crisp_integration)
        print("The response of AIAgentIntegrationsApi->create_agent_integration_crisp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->create_agent_integration_crisp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 
 **create_crisp_integration** | [**CreateCrispIntegration**](CreateCrispIntegration.md)|  | 

### Return type

[**GetAgentIntegrationCrisp200Response**](GetAgentIntegrationCrisp200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;crisp_integration&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**503** | Интеграция с Crisp временно недоступна |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_agent_integration_jivo**
> GetAgentIntegrationJivo200Response create_agent_integration_jivo(agent_id, create_jivo_integration)

Подключение агента к Jivo

Чтобы подключить AI агента к Jivo, отправьте POST-запрос на `/api/v1/cloud-ai/agent/{agent_id}/jivo`, передав Provider ID, выданный поддержкой Jivo.  Подготовка описана в разделе «Интеграции AI агентов»: адрес для событий и токен бота нужно заранее передать в поддержку Jivo.  Если агент не найден, вернется ошибка `404 agent_not_found`.  К одному агенту можно подключить одну интеграцию Jivo. Если она уже есть, вернется ошибка `409 bot_already_exists`.  Тело ответа будет представлять собой объект JSON с ключом `jivo_integration`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_jivo_integration import CreateJivoIntegration
from timeweb_cloud_api.models.get_agent_integration_jivo200_response import GetAgentIntegrationJivo200Response
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    agent_id = 1 # object | ID агента
    create_jivo_integration = timeweb_cloud_api.CreateJivoIntegration() # CreateJivoIntegration | 

    try:
        # Подключение агента к Jivo
        api_response = api_instance.create_agent_integration_jivo(agent_id, create_jivo_integration)
        print("The response of AIAgentIntegrationsApi->create_agent_integration_jivo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->create_agent_integration_jivo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 
 **create_jivo_integration** | [**CreateJivoIntegration**](CreateJivoIntegration.md)|  | 

### Return type

[**GetAgentIntegrationJivo200Response**](GetAgentIntegrationJivo200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;jivo_integration&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_bot_max_bot**
> delete_agent_bot_max_bot(bot_id)

Отключение бота MAX

Чтобы отключить бота MAX от агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/max-bots/{bot_id}`.  Платформа отпишет бота от событий в MAX и удалит подключение. Сам бот в MAX не удаляется — его можно подключить снова.

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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    bot_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID бота (поле `id` из ответа)

    try:
        # Отключение бота MAX
        api_instance.delete_agent_bot_max_bot(bot_id)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->delete_agent_bot_max_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | [**object**](.md)| ID бота (поле &#x60;id&#x60; из ответа) | 

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
**204** | Бот MAX отключен |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_bot_telegram_bot**
> delete_agent_bot_telegram_bot(bot_id)

Отключение Telegram-бота

Чтобы отключить Telegram-бота от агента, отправьте DELETE-запрос на `/api/v1/cloud-ai/bots/{bot_id}`.  Платформа снимет вебхук бота в Telegram и удалит подключение. Сам бот в Telegram не удаляется — его можно подключить снова.

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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    bot_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID бота (поле `id` из ответа)

    try:
        # Отключение Telegram-бота
        api_instance.delete_agent_bot_telegram_bot(bot_id)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->delete_agent_bot_telegram_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | [**object**](.md)| ID бота (поле &#x60;id&#x60; из ответа) | 

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
**204** | Telegram-бот отключен |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_integration_crisp**
> delete_agent_integration_crisp(agent_id)

Отключение агента от Crisp

Чтобы отключить AI агента от Crisp, отправьте DELETE-запрос на `/api/v1/cloud-ai/agent/{agent_id}/crisp`.  После удаления интеграции агент перестает отвечать в чатах Crisp. Вебхук в настройках Crisp можно удалить вручную.

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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    agent_id = 1 # object | ID агента

    try:
        # Отключение агента от Crisp
        api_instance.delete_agent_integration_crisp(agent_id)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->delete_agent_integration_crisp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | Интеграция с Crisp удалена |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_agent_integration_jivo**
> delete_agent_integration_jivo(agent_id)

Отключение агента от Jivo

Чтобы отключить AI агента от Jivo, отправьте DELETE-запрос на `/api/v1/cloud-ai/agent/{agent_id}/jivo`.  После удаления интеграции агент перестает отвечать на события Jivo. Настройки бота в самом Jivo не меняются.

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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    agent_id = 1 # object | ID агента

    try:
        # Отключение агента от Jivo
        api_instance.delete_agent_integration_jivo(agent_id)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->delete_agent_integration_jivo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**204** | Интеграция с Jivo удалена |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_bot_max_bot**
> CreateAgentBotTelegramBot201Response get_agent_bot_max_bot(bot_id)

Получение информации о боте MAX

Чтобы получить информацию о боте MAX, отправьте GET-запрос на `/api/v1/cloud-ai/max-bots/{bot_id}`.  Тело ответа будет представлять собой объект JSON с ключом `bot`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_bot_telegram_bot201_response import CreateAgentBotTelegramBot201Response
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    bot_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID бота (поле `id` из ответа)

    try:
        # Получение информации о боте MAX
        api_response = api_instance.get_agent_bot_max_bot(bot_id)
        print("The response of AIAgentIntegrationsApi->get_agent_bot_max_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->get_agent_bot_max_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | [**object**](.md)| ID бота (поле &#x60;id&#x60; из ответа) | 

### Return type

[**CreateAgentBotTelegramBot201Response**](CreateAgentBotTelegramBot201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;bot&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_bot_max_bots**
> GetAgentBotMaxBots200Response get_agent_bot_max_bots()

Получение списка ботов MAX

Чтобы получить список ботов MAX, подключенных к агентам аккаунта, отправьте GET-запрос на `/api/v1/cloud-ai/max-bots`.  Тело ответа будет представлять собой объект JSON с ключами `bots` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_bot_max_bots200_response import GetAgentBotMaxBots200Response
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)

    try:
        # Получение списка ботов MAX
        api_response = api_instance.get_agent_bot_max_bots()
        print("The response of AIAgentIntegrationsApi->get_agent_bot_max_bots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->get_agent_bot_max_bots: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAgentBotMaxBots200Response**](GetAgentBotMaxBots200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;bots&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_bot_max_bots_by_agent**
> GetAgentBotMaxBotsByAgent200Response get_agent_bot_max_bots_by_agent(agent_id)

Получение списка ботов MAX агента

Чтобы получить список ботов MAX, подключенных к AI агенту, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{agent_id}/max-bots`.  Тело ответа будет представлять собой объект JSON с ключами `bots` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_bot_max_bots_by_agent200_response import GetAgentBotMaxBotsByAgent200Response
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    agent_id = 1 # object | ID агента

    try:
        # Получение списка ботов MAX агента
        api_response = api_instance.get_agent_bot_max_bots_by_agent(agent_id)
        print("The response of AIAgentIntegrationsApi->get_agent_bot_max_bots_by_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->get_agent_bot_max_bots_by_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 

### Return type

[**GetAgentBotMaxBotsByAgent200Response**](GetAgentBotMaxBotsByAgent200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;bots&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_bot_telegram_bot**
> CreateAgentBotTelegramBot201Response get_agent_bot_telegram_bot(bot_id)

Получение информации о Telegram-боте

Чтобы получить информацию о Telegram-боте, отправьте GET-запрос на `/api/v1/cloud-ai/bots/{bot_id}`.  Тело ответа будет представлять собой объект JSON с ключом `bot`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_bot_telegram_bot201_response import CreateAgentBotTelegramBot201Response
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    bot_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID бота (поле `id` из ответа)

    try:
        # Получение информации о Telegram-боте
        api_response = api_instance.get_agent_bot_telegram_bot(bot_id)
        print("The response of AIAgentIntegrationsApi->get_agent_bot_telegram_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->get_agent_bot_telegram_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | [**object**](.md)| ID бота (поле &#x60;id&#x60; из ответа) | 

### Return type

[**CreateAgentBotTelegramBot201Response**](CreateAgentBotTelegramBot201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;bot&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_bot_telegram_bots**
> GetAgentBotTelegramBots200Response get_agent_bot_telegram_bots()

Получение списка Telegram-ботов

Чтобы получить список Telegram-ботов, подключенных к агентам аккаунта, отправьте GET-запрос на `/api/v1/cloud-ai/bots`.  Тело ответа будет представлять собой объект JSON с ключами `bots` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_bot_telegram_bots200_response import GetAgentBotTelegramBots200Response
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)

    try:
        # Получение списка Telegram-ботов
        api_response = api_instance.get_agent_bot_telegram_bots()
        print("The response of AIAgentIntegrationsApi->get_agent_bot_telegram_bots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->get_agent_bot_telegram_bots: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetAgentBotTelegramBots200Response**](GetAgentBotTelegramBots200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;bots&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_bot_telegram_bots_by_agent**
> GetAgentBotTelegramBotsByAgent200Response get_agent_bot_telegram_bots_by_agent(agent_id)

Получение списка Telegram-ботов агента

Чтобы получить список Telegram-ботов, подключенных к AI агенту, отправьте GET-запрос на `/api/v1/cloud-ai/agents/{agent_id}/bots`.  Тело ответа будет представлять собой объект JSON с ключами `bots` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_bot_telegram_bots_by_agent200_response import GetAgentBotTelegramBotsByAgent200Response
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    agent_id = 1 # object | ID агента

    try:
        # Получение списка Telegram-ботов агента
        api_response = api_instance.get_agent_bot_telegram_bots_by_agent(agent_id)
        print("The response of AIAgentIntegrationsApi->get_agent_bot_telegram_bots_by_agent:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->get_agent_bot_telegram_bots_by_agent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 

### Return type

[**GetAgentBotTelegramBotsByAgent200Response**](GetAgentBotTelegramBotsByAgent200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;bots&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_integration_crisp**
> GetAgentIntegrationCrisp200Response get_agent_integration_crisp(agent_id)

Получение интеграции агента с Crisp

Чтобы получить интеграцию AI агента с Crisp, отправьте GET-запрос на `/api/v1/cloud-ai/agent/{agent_id}/crisp`.  В ответе есть `webhook_secret` — по нему можно восстановить адрес вебхука для Crisp. Если агент не подключен к Crisp, вернется ошибка 404.  Тело ответа будет представлять собой объект JSON с ключом `crisp_integration`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_integration_crisp200_response import GetAgentIntegrationCrisp200Response
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    agent_id = 1 # object | ID агента

    try:
        # Получение интеграции агента с Crisp
        api_response = api_instance.get_agent_integration_crisp(agent_id)
        print("The response of AIAgentIntegrationsApi->get_agent_integration_crisp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->get_agent_integration_crisp: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 

### Return type

[**GetAgentIntegrationCrisp200Response**](GetAgentIntegrationCrisp200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;crisp_integration&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**503** | Интеграция с Crisp временно недоступна |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_integration_jivo**
> GetAgentIntegrationJivo200Response get_agent_integration_jivo(agent_id)

Получение интеграции агента с Jivo

Чтобы получить интеграцию AI агента с Jivo, отправьте GET-запрос на `/api/v1/cloud-ai/agent/{agent_id}/jivo`.  Если агент не подключен к Jivo, вернется ошибка 404.  Тело ответа будет представлять собой объект JSON с ключом `jivo_integration`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_agent_integration_jivo200_response import GetAgentIntegrationJivo200Response
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    agent_id = 1 # object | ID агента

    try:
        # Получение интеграции агента с Jivo
        api_response = api_instance.get_agent_integration_jivo(agent_id)
        print("The response of AIAgentIntegrationsApi->get_agent_integration_jivo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->get_agent_integration_jivo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | [**object**](.md)| ID агента | 

### Return type

[**GetAgentIntegrationJivo200Response**](GetAgentIntegrationJivo200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;jivo_integration&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_bot_max_bot**
> CreateAgentBotTelegramBot201Response update_agent_bot_max_bot(bot_id, update_max_bot)

Изменение бота MAX

Чтобы изменить бота MAX, отправьте PATCH-запрос на `/api/v1/cloud-ai/max-bots/{bot_id}`, передав только изменяемые поля.  Через `token` можно заменить токен того же бота: платформа проверит новый токен и заново подпишет бота на события. Перенести подключение на другого бота нельзя — для этого удалите бота и подключите новый.  Ошибки: - `400 invalid_max_token` — MAX не принял токен или токен принадлежит другому боту; - `400 max_webhook_error` — не удалось подписать бота на события.  Тело ответа будет представлять собой объект JSON с ключом `bot`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_bot_telegram_bot201_response import CreateAgentBotTelegramBot201Response
from timeweb_cloud_api.models.update_max_bot import UpdateMaxBot
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    bot_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID бота (поле `id` из ответа)
    update_max_bot = timeweb_cloud_api.UpdateMaxBot() # UpdateMaxBot | 

    try:
        # Изменение бота MAX
        api_response = api_instance.update_agent_bot_max_bot(bot_id, update_max_bot)
        print("The response of AIAgentIntegrationsApi->update_agent_bot_max_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->update_agent_bot_max_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | [**object**](.md)| ID бота (поле &#x60;id&#x60; из ответа) | 
 **update_max_bot** | [**UpdateMaxBot**](UpdateMaxBot.md)|  | 

### Return type

[**CreateAgentBotTelegramBot201Response**](CreateAgentBotTelegramBot201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;bot&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_agent_bot_telegram_bot**
> CreateAgentBotTelegramBot201Response update_agent_bot_telegram_bot(bot_id, update_bot)

Изменение Telegram-бота

Чтобы изменить Telegram-бота, отправьте PATCH-запрос на `/api/v1/cloud-ai/bots/{bot_id}`, передав только изменяемые поля.  Через `token` можно заменить токен того же бота, например после его перевыпуска в @BotFather: платформа проверит новый токен и переустановит вебхук. Перенести подключение на другого бота нельзя — для этого удалите бота и подключите новый. Агента, к которому подключен бот, этим запросом сменить нельзя.  Ошибки: - `400 invalid_telegram_token` — Telegram не принял токен или токен принадлежит другому боту; - `400 telegram_webhook_error` — не удалось переустановить вебхук.  Тело ответа будет представлять собой объект JSON с ключом `bot`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_agent_bot_telegram_bot201_response import CreateAgentBotTelegramBot201Response
from timeweb_cloud_api.models.update_bot import UpdateBot
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
    api_instance = timeweb_cloud_api.AIAgentIntegrationsApi(api_client)
    bot_id = 550e8400-e29b-41d4-a716-446655440000 # object | ID бота (поле `id` из ответа)
    update_bot = timeweb_cloud_api.UpdateBot() # UpdateBot | 

    try:
        # Изменение Telegram-бота
        api_response = api_instance.update_agent_bot_telegram_bot(bot_id, update_bot)
        print("The response of AIAgentIntegrationsApi->update_agent_bot_telegram_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIAgentIntegrationsApi->update_agent_bot_telegram_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bot_id** | [**object**](.md)| ID бота (поле &#x60;id&#x60; из ответа) | 
 **update_bot** | [**UpdateBot**](UpdateBot.md)|  | 

### Return type

[**CreateAgentBotTelegramBot201Response**](CreateAgentBotTelegramBot201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;bot&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

