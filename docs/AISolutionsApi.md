# timeweb_cloud_api.AISolutionsApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_ai_solution_telegram_bot**](AISolutionsApi.md#add_ai_solution_telegram_bot) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/telegram/bots | Подключение Telegram-бота к AI-решению
[**approve_ai_solution_telegram_pairing**](AISolutionsApi.md#approve_ai_solution_telegram_pairing) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key}/pairing/approve | Подтверждение владельца Telegram-бота AI-решения
[**create_ai_solution**](AISolutionsApi.md#create_ai_solution) | **POST** /api/v1/cloud-ai/solutions | Создание AI-решения
[**delete_ai_solution**](AISolutionsApi.md#delete_ai_solution) | **DELETE** /api/v1/cloud-ai/solutions/{solution_id} | Удаление AI-решения
[**get_ai_solution**](AISolutionsApi.md#get_ai_solution) | **GET** /api/v1/cloud-ai/solutions/{solution_id} | Получение AI-решения
[**get_ai_solution_chat_full_history**](AISolutionsApi.md#get_ai_solution_chat_full_history) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/chat/history | Получение всей истории чата AI-решения
[**get_ai_solution_chat_history**](AISolutionsApi.md#get_ai_solution_chat_history) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/chat/conversations/{conversation_id}/messages | Получение истории разговора AI-решения
[**get_ai_solution_chat_status**](AISolutionsApi.md#get_ai_solution_chat_status) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/chat/status | Получение статуса чата AI-решения
[**get_ai_solution_main_chat_history**](AISolutionsApi.md#get_ai_solution_main_chat_history) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/chat/messages | Получение истории основного разговора AI-решения
[**list_ai_solution_conversations**](AISolutionsApi.md#list_ai_solution_conversations) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/chat/conversations | Получение списка разговоров AI-решения
[**list_ai_solution_telegram_bots**](AISolutionsApi.md#list_ai_solution_telegram_bots) | **GET** /api/v1/cloud-ai/solutions/{solution_id}/telegram/bots | Получение списка Telegram-ботов AI-решения
[**list_ai_solution_types**](AISolutionsApi.md#list_ai_solution_types) | **GET** /api/v1/cloud-ai/solutions/types | Получение списка типов AI-решений
[**list_ai_solutions**](AISolutionsApi.md#list_ai_solutions) | **GET** /api/v1/cloud-ai/solutions | Получение списка AI-решений
[**regenerate_ai_solution_ai_key**](AISolutionsApi.md#regenerate_ai_solution_ai_key) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/ai-key/regenerate | Перевыпуск ключа AI Gateway решения
[**remove_ai_solution_telegram_bot**](AISolutionsApi.md#remove_ai_solution_telegram_bot) | **DELETE** /api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key} | Отключение Telegram-бота от AI-решения
[**reset_ai_solution_chat**](AISolutionsApi.md#reset_ai_solution_chat) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/chat/reset | Сброс контекста разговора AI-решения
[**send_ai_solution_message**](AISolutionsApi.md#send_ai_solution_message) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/chat/messages | Отправка сообщения агенту AI-решения
[**shutdown_ai_solution**](AISolutionsApi.md#shutdown_ai_solution) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/shutdown | Выключение AI-решения
[**start_ai_solution**](AISolutionsApi.md#start_ai_solution) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/start | Запуск AI-решения
[**stop_ai_solution_chat**](AISolutionsApi.md#stop_ai_solution_chat) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/chat/stop | Остановка хода агента AI-решения
[**stream_ai_solution_chat**](AISolutionsApi.md#stream_ai_solution_chat) | **POST** /api/v1/cloud-ai/solutions/{solution_id}/chat/stream | Отправка сообщения агенту AI-решения с потоковым ответом
[**update_ai_solution**](AISolutionsApi.md#update_ai_solution) | **PATCH** /api/v1/cloud-ai/solutions/{solution_id} | Изменение AI-решения


# **add_ai_solution_telegram_bot**
> AddAiSolutionTelegramBot201Response add_ai_solution_telegram_bot(solution_id, connect_telegram)

Подключение Telegram-бота к AI-решению

Чтобы подключить Telegram-бота к решению, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots`.  Принимает токен бота от @BotFather, проверяет его в Telegram и настраивает бота на сервере решения. Владелец подтверждается кодом: пока он не подтверждён, бот никому не отвечает. Напишите боту в личные сообщения, получите в ответ код и передайте его в метод подтверждения владельца.  К решению можно подключить только одного бота: повторный запрос для того же бота обновляет его токен, для другого бота — возвращает 409 `ai_solution_already_has_a_connected_telegram_bot`. Если Telegram отклонил токен, ответ — 400 `ai_solution_telegram_token_is_invalid`.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.add_ai_solution_telegram_bot201_response import AddAiSolutionTelegramBot201Response
from timeweb_cloud_api.models.connect_telegram import ConnectTelegram
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения
    connect_telegram = timeweb_cloud_api.ConnectTelegram() # ConnectTelegram | 

    try:
        # Подключение Telegram-бота к AI-решению
        api_response = api_instance.add_ai_solution_telegram_bot(solution_id, connect_telegram)
        print("The response of AISolutionsApi->add_ai_solution_telegram_bot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->add_ai_solution_telegram_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 
 **connect_telegram** | [**ConnectTelegram**](ConnectTelegram.md)|  | 

### Return type

[**AddAiSolutionTelegramBot201Response**](AddAiSolutionTelegramBot201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;ai_solution_telegram_bot&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**502** | Сервер решения не смог настроить бота (&#x60;ai_solution_chat_request_failed&#x60;) |  -  |
**503** | Сервер решения недоступен или не поддерживает Telegram — во втором случае пересоздайте решение (&#x60;ai_solution_chat_is_unavailable&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_ai_solution_telegram_pairing**
> approve_ai_solution_telegram_pairing(solution_id, account_key, approve_telegram_pairing)

Подтверждение владельца Telegram-бота AI-решения

Чтобы подтвердить владельца Telegram-бота, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key}/pairing/approve`.  Передайте код, который бот прислал в личные сообщения в ответ на первое сообщение. После подтверждения агент отвечает этому пользователю Telegram в боте, а бот переходит в состояние `connected`. Владелец привязывается к конкретному боту. Повторный запрос с кодом, уже подтверждённым в последние 15 минут, считается успешным. Некорректный `account_key` — ответ 400 `ai_solution_telegram_token_is_invalid`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.approve_telegram_pairing import ApproveTelegramPairing
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения
    account_key = b123456789 # object | ID Telegram-бота в решении (`account_key` из списка ботов) в формате `b<число>`, например `b123456789`
    approve_telegram_pairing = timeweb_cloud_api.ApproveTelegramPairing() # ApproveTelegramPairing | 

    try:
        # Подтверждение владельца Telegram-бота AI-решения
        api_instance.approve_ai_solution_telegram_pairing(solution_id, account_key, approve_telegram_pairing)
    except Exception as e:
        print("Exception when calling AISolutionsApi->approve_ai_solution_telegram_pairing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 
 **account_key** | [**object**](.md)| ID Telegram-бота в решении (&#x60;account_key&#x60; из списка ботов) в формате &#x60;b&lt;число&gt;&#x60;, например &#x60;b123456789&#x60; | 
 **approve_telegram_pairing** | [**ApproveTelegramPairing**](ApproveTelegramPairing.md)|  | 

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
**204** | Владелец подтверждён |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**502** | Сервер решения не подтвердил владельца — например, код неверный или устарел (&#x60;ai_solution_chat_request_failed&#x60;) |  -  |
**503** | Сервер решения недоступен или не поддерживает Telegram — во втором случае пересоздайте решение (&#x60;ai_solution_chat_is_unavailable&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_solution**
> CreateAiSolution201Response create_ai_solution(create_ai_solution)

Создание AI-решения

Чтобы создать AI-решение, отправьте POST-запрос на `/api/v1/cloud-ai/solutions`.  Выпускает для решения ключ AI Gateway и создаёт облачный сервер из образа решения; агент на сервере настраивается на выбранную модель через этот ключ. Сервер тарифицируется по выбранному тарифу, обращения к модели — через ключ AI Gateway.  Решение возвращается в статусе `creating`: развёртывание сервера и настройка агента занимают несколько минут. Дождитесь статуса `active`, а затем `ready: true` в методе получения статуса чата.  Тариф (`preset_id`) должен быть из той же локации, что и зона доступности (`availability_zone` или зона по умолчанию для региона аккаунта), иначе — 400 `invalid_location_zone`. Соответствие тарифа `requirements` типа решения при создании не проверяется — выбирайте тариф не ниже требований сами. Ответ 409 `no_free_node` означает, что в выбранной зоне сейчас нет свободных ресурсов под этот тариф — выберите другой тариф или зону. Неподходящая или устаревшая модель — 404 `model_not_found`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_ai_solution import CreateAiSolution
from timeweb_cloud_api.models.create_ai_solution201_response import CreateAiSolution201Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    create_ai_solution = timeweb_cloud_api.CreateAiSolution() # CreateAiSolution | 

    try:
        # Создание AI-решения
        api_response = api_instance.create_ai_solution(create_ai_solution)
        print("The response of AISolutionsApi->create_ai_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->create_ai_solution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_ai_solution** | [**CreateAiSolution**](CreateAiSolution.md)|  | 

### Return type

[**CreateAiSolution201Response**](CreateAiSolution201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Объект JSON c ключом &#x60;ai_solution&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**402** | Баланса аккаунта не хватает на час работы выбранного тарифа (&#x60;insufficient_account_balance_to_create_ai_solution&#x60;) |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**503** | Образ решения недоступен в выбранной зоне или в зоне по умолчанию для региона аккаунта (&#x60;ai_solution_image_is_not_available_in_this_zone&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ai_solution**
> delete_ai_solution(solution_id)

Удаление AI-решения

Чтобы удалить AI-решение, отправьте DELETE-запрос на `/api/v1/cloud-ai/solutions/{solution_id}`.  Решение удаляется вместе с сервером и ключом AI Gateway. Действие необратимо: решение и история его чата становятся недоступны.

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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения

    try:
        # Удаление AI-решения
        api_instance.delete_ai_solution(solution_id)
    except Exception as e:
        print("Exception when calling AISolutionsApi->delete_ai_solution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 

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
**204** | Решение удалено |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_solution**
> CreateAiSolution201Response get_ai_solution(solution_id)

Получение AI-решения

Чтобы получить AI-решение, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}`.  Статус решения выводится из текущего состояния его сервера. Тело ответа будет представлять собой объект JSON с ключом `ai_solution`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_ai_solution201_response import CreateAiSolution201Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения

    try:
        # Получение AI-решения
        api_response = api_instance.get_ai_solution(solution_id)
        print("The response of AISolutionsApi->get_ai_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->get_ai_solution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 

### Return type

[**CreateAiSolution201Response**](CreateAiSolution201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ai_solution&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_solution_chat_full_history**
> GetAiSolutionMainChatHistory200Response get_ai_solution_chat_full_history(solution_id, limit=limit, offset=offset)

Получение всей истории чата AI-решения

Чтобы получить сообщения всех разговоров решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/history`.  В отличие от `chat/messages` (только основной разговор) и `chat/conversations/{conversation_id}/messages` (конкретный разговор), возвращает сообщения из всех разговоров сразу. Сообщения отсортированы по дате создания от новых к старым. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_chat_messages` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_solution_main_chat_history200_response import GetAiSolutionMainChatHistory200Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения
    limit = 100 # object | Количество сообщений на странице, от 1 до 10 000 (optional)
    offset = 0 # object | Количество сообщений, которые нужно пропустить (optional)

    try:
        # Получение всей истории чата AI-решения
        api_response = api_instance.get_ai_solution_chat_full_history(solution_id, limit=limit, offset=offset)
        print("The response of AISolutionsApi->get_ai_solution_chat_full_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->get_ai_solution_chat_full_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 
 **limit** | [**object**](.md)| Количество сообщений на странице, от 1 до 10 000 | [optional] 
 **offset** | [**object**](.md)| Количество сообщений, которые нужно пропустить | [optional] 

### Return type

[**GetAiSolutionMainChatHistory200Response**](GetAiSolutionMainChatHistory200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_solution_chat_messages&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_solution_chat_history**
> GetAiSolutionMainChatHistory200Response get_ai_solution_chat_history(solution_id, conversation_id, limit=limit, offset=offset)

Получение истории разговора AI-решения

Чтобы получить историю разговора, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/conversations/{conversation_id}/messages`.  Сообщения отсортированы по дате создания от новых к старым: первая страница — последние сообщения разговора. Для несуществующего разговора возвращается пустой список. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_chat_messages` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_solution_main_chat_history200_response import GetAiSolutionMainChatHistory200Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения
    conversation_id = solution-15 # object | ID разговора. У основного разговора решения — `solution-<solution_id>`
    limit = 100 # object | Количество сообщений на странице, от 1 до 10 000 (optional)
    offset = 0 # object | Количество сообщений, которые нужно пропустить (optional)

    try:
        # Получение истории разговора AI-решения
        api_response = api_instance.get_ai_solution_chat_history(solution_id, conversation_id, limit=limit, offset=offset)
        print("The response of AISolutionsApi->get_ai_solution_chat_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->get_ai_solution_chat_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 
 **conversation_id** | [**object**](.md)| ID разговора. У основного разговора решения — &#x60;solution-&lt;solution_id&gt;&#x60; | 
 **limit** | [**object**](.md)| Количество сообщений на странице, от 1 до 10 000 | [optional] 
 **offset** | [**object**](.md)| Количество сообщений, которые нужно пропустить | [optional] 

### Return type

[**GetAiSolutionMainChatHistory200Response**](GetAiSolutionMainChatHistory200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_solution_chat_messages&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_solution_chat_status**
> GetAiSolutionChatStatus200Response get_ai_solution_chat_status(solution_id)

Получение статуса чата AI-решения

Чтобы узнать, готов ли агент решения принимать сообщения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/status`.  Готовность чата отличается от статуса решения: тот выводится из состояния сервера, а сервер включается задолго до того, как будет установлено и настроено ПО агента. После создания или запуска решения опрашивайте этот метод, пока `ready` не станет `true`. Тело ответа будет представлять собой объект JSON с ключом `ai_solution_chat_status`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_solution_chat_status200_response import GetAiSolutionChatStatus200Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения

    try:
        # Получение статуса чата AI-решения
        api_response = api_instance.get_ai_solution_chat_status(solution_id)
        print("The response of AISolutionsApi->get_ai_solution_chat_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->get_ai_solution_chat_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 

### Return type

[**GetAiSolutionChatStatus200Response**](GetAiSolutionChatStatus200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ai_solution_chat_status&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_solution_main_chat_history**
> GetAiSolutionMainChatHistory200Response get_ai_solution_main_chat_history(solution_id, limit=limit, offset=offset)

Получение истории основного разговора AI-решения

Чтобы получить историю основного разговора решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/messages`.  ID основного разговора знать не нужно; для других разговоров используйте метод с явным `conversation_id`. Сообщения отсортированы по дате создания от новых к старым: первая страница — последние сообщения. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_chat_messages` и `meta` (`meta.total` — общее количество сообщений).

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.get_ai_solution_main_chat_history200_response import GetAiSolutionMainChatHistory200Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения
    limit = 100 # object | Количество сообщений на странице, от 1 до 10 000 (optional)
    offset = 0 # object | Количество сообщений, которые нужно пропустить (optional)

    try:
        # Получение истории основного разговора AI-решения
        api_response = api_instance.get_ai_solution_main_chat_history(solution_id, limit=limit, offset=offset)
        print("The response of AISolutionsApi->get_ai_solution_main_chat_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->get_ai_solution_main_chat_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 
 **limit** | [**object**](.md)| Количество сообщений на странице, от 1 до 10 000 | [optional] 
 **offset** | [**object**](.md)| Количество сообщений, которые нужно пропустить | [optional] 

### Return type

[**GetAiSolutionMainChatHistory200Response**](GetAiSolutionMainChatHistory200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_solution_chat_messages&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ai_solution_conversations**
> ListAiSolutionConversations200Response list_ai_solution_conversations(solution_id)

Получение списка разговоров AI-решения

Чтобы получить список разговоров с агентом решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/conversations`.  Возвращает все разговоры решения, в которых есть сообщения, включая основной, отсортированные по дате последнего сообщения от новых к старым. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_conversations` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.list_ai_solution_conversations200_response import ListAiSolutionConversations200Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения

    try:
        # Получение списка разговоров AI-решения
        api_response = api_instance.list_ai_solution_conversations(solution_id)
        print("The response of AISolutionsApi->list_ai_solution_conversations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->list_ai_solution_conversations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 

### Return type

[**ListAiSolutionConversations200Response**](ListAiSolutionConversations200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_solution_conversations&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ai_solution_telegram_bots**
> ListAiSolutionTelegramBots200Response list_ai_solution_telegram_bots(solution_id)

Получение списка Telegram-ботов AI-решения

Чтобы получить список Telegram-ботов решения, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots`.  Возвращает подключённых к решению ботов и состояние их подтверждения. Список читается с сервера решения. Тело ответа будет представлять собой объект JSON с ключами `ai_solution_telegram_bots` и `meta`.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.list_ai_solution_telegram_bots200_response import ListAiSolutionTelegramBots200Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения

    try:
        # Получение списка Telegram-ботов AI-решения
        api_response = api_instance.list_ai_solution_telegram_bots(solution_id)
        print("The response of AISolutionsApi->list_ai_solution_telegram_bots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->list_ai_solution_telegram_bots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 

### Return type

[**ListAiSolutionTelegramBots200Response**](ListAiSolutionTelegramBots200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_solution_telegram_bots&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**502** | Сервер решения ответил ошибкой (&#x60;ai_solution_chat_request_failed&#x60;) |  -  |
**503** | Сервер решения недоступен или не поддерживает Telegram — во втором случае пересоздайте решение (&#x60;ai_solution_chat_is_unavailable&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ai_solution_types**
> ListAiSolutionTypes200Response list_ai_solution_types()

Получение списка типов AI-решений

Чтобы получить список типов AI-решений, отправьте GET-запрос на `/api/v1/cloud-ai/solutions/types`.  Возвращает каталог готовых решений, которые можно развернуть на облачном сервере, с минимальными требованиями к конфигурации сервера (`requirements`). Тело ответа будет представлять собой объект JSON с ключами `ai_solution_types` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.list_ai_solution_types200_response import ListAiSolutionTypes200Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)

    try:
        # Получение списка типов AI-решений
        api_response = api_instance.list_ai_solution_types()
        print("The response of AISolutionsApi->list_ai_solution_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->list_ai_solution_types: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAiSolutionTypes200Response**](ListAiSolutionTypes200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_solution_types&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ai_solutions**
> ListAiSolutions200Response list_ai_solutions()

Получение списка AI-решений

Чтобы получить список AI-решений аккаунта, отправьте GET-запрос на `/api/v1/cloud-ai/solutions`.  Возвращает все решения аккаунта, кроме удалённых. Статус каждого решения выводится из текущего состояния его сервера. Тело ответа будет представлять собой объект JSON с ключами `ai_solutions` и `meta`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.list_ai_solutions200_response import ListAiSolutions200Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)

    try:
        # Получение списка AI-решений
        api_response = api_instance.list_ai_solutions()
        print("The response of AISolutionsApi->list_ai_solutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->list_ai_solutions: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListAiSolutions200Response**](ListAiSolutions200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключами &#x60;ai_solutions&#x60; и &#x60;meta&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_ai_solution_ai_key**
> RegenerateAiSolutionAiKey200Response regenerate_ai_solution_ai_key(solution_id)

Перевыпуск ключа AI Gateway решения

Чтобы перевыпустить ключ AI Gateway решения, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/ai-key/regenerate`.  Единственный способ сменить этот ключ: он выпущен платформой для решения и в разделе AI Gateway доступен только для чтения. Новый ключ сразу записывается в конфигурацию агента на сервере решения, старый перестаёт работать немедленно. Сервер должен быть включён и полностью развёрнут — это проверяется до перевыпуска, потому что отменить его нельзя. Если записать новый ключ на сервер не удалось, повторите запрос.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.regenerate_ai_solution_ai_key200_response import RegenerateAiSolutionAiKey200Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения

    try:
        # Перевыпуск ключа AI Gateway решения
        api_response = api_instance.regenerate_ai_solution_ai_key(solution_id)
        print("The response of AISolutionsApi->regenerate_ai_solution_ai_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->regenerate_ai_solution_ai_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 

### Return type

[**RegenerateAiSolutionAiKey200Response**](RegenerateAiSolutionAiKey200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ai_solution_ai_key&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**502** | Сервер решения не принял новый ключ (&#x60;ai_solution_configuration_failed&#x60;) |  -  |
**503** | Сервер решения нельзя настроить: он выключен, недоступен, ещё разворачивается или создан старой версией решения (&#x60;ai_solution_machine_is_unavailable&#x60;), либо у него нет публичного IP (&#x60;ai_solution_chat_is_unavailable&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_ai_solution_telegram_bot**
> remove_ai_solution_telegram_bot(solution_id, account_key)

Отключение Telegram-бота от AI-решения

Чтобы отключить Telegram-бота от решения, отправьте DELETE-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/telegram/bots/{account_key}`.  Удаляет бота из конфигурации сервера решения: агент перестаёт отвечать в этом боте. Если бот не подключён, запрос всё равно возвращает 204. Некорректный `account_key` — ответ 400 `ai_solution_telegram_token_is_invalid`.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.

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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения
    account_key = b123456789 # object | ID Telegram-бота в решении (`account_key` из списка ботов) в формате `b<число>`, например `b123456789`

    try:
        # Отключение Telegram-бота от AI-решения
        api_instance.remove_ai_solution_telegram_bot(solution_id, account_key)
    except Exception as e:
        print("Exception when calling AISolutionsApi->remove_ai_solution_telegram_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 
 **account_key** | [**object**](.md)| ID Telegram-бота в решении (&#x60;account_key&#x60; из списка ботов) в формате &#x60;b&lt;число&gt;&#x60;, например &#x60;b123456789&#x60; | 

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
**204** | Бот отключён |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**502** | Сервер решения не смог отключить бота (&#x60;ai_solution_chat_request_failed&#x60;) |  -  |
**503** | Сервер решения недоступен или не поддерживает Telegram — во втором случае пересоздайте решение (&#x60;ai_solution_chat_is_unavailable&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_ai_solution_chat**
> ResetAiSolutionChat200Response reset_ai_solution_chat(solution_id, reset_ai_solution_chat=reset_ai_solution_chat)

Сброс контекста разговора AI-решения

Чтобы сбросить контекст разговора, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/reset`.  Контекст сбрасывается на месте: разговор сохраняет `conversation_id`, но агент больше не видит предыдущих сообщений. Без `conversation_id` сбрасывается основной разговор решения. В историю добавляется служебное сообщение с ролью `context-reset`, отмечающее границу текущего контекста, — оно и возвращается в ответе (с ключом `ai_solution_chat_message`). Отметка добавляется и для разговора, в котором ещё не было сообщений.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.reset_ai_solution_chat import ResetAiSolutionChat
from timeweb_cloud_api.models.reset_ai_solution_chat200_response import ResetAiSolutionChat200Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения
    reset_ai_solution_chat = timeweb_cloud_api.ResetAiSolutionChat() # ResetAiSolutionChat |  (optional)

    try:
        # Сброс контекста разговора AI-решения
        api_response = api_instance.reset_ai_solution_chat(solution_id, reset_ai_solution_chat=reset_ai_solution_chat)
        print("The response of AISolutionsApi->reset_ai_solution_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->reset_ai_solution_chat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 
 **reset_ai_solution_chat** | [**ResetAiSolutionChat**](ResetAiSolutionChat.md)|  | [optional] 

### Return type

[**ResetAiSolutionChat200Response**](ResetAiSolutionChat200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ai_solution_chat_message&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**502** | Агент на сервере решения ответил ошибкой (&#x60;ai_solution_chat_request_failed&#x60;) |  -  |
**503** | Чат решения недоступен: сервер разворачивается, выключен или у него нет публичного IP (&#x60;ai_solution_chat_is_unavailable&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_ai_solution_message**
> SendAiSolutionMessage200Response send_ai_solution_message(solution_id, send_ai_solution_message)

Отправка сообщения агенту AI-решения

Чтобы отправить сообщение агенту решения, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/messages`.  Ответ возвращается целиком после завершения хода агента (ожидание — до 3 минут). Без `conversation_id` сообщение уходит в основной разговор решения; новый разговор начинается только при явной передаче нового ID. Без `message` агент сам здоровается — так можно показать первую реплику чата. Чтобы получать ответ по мере генерации, используйте потоковый метод.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.send_ai_solution_message import SendAiSolutionMessage
from timeweb_cloud_api.models.send_ai_solution_message200_response import SendAiSolutionMessage200Response
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения
    send_ai_solution_message = timeweb_cloud_api.SendAiSolutionMessage() # SendAiSolutionMessage | 

    try:
        # Отправка сообщения агенту AI-решения
        api_response = api_instance.send_ai_solution_message(solution_id, send_ai_solution_message)
        print("The response of AISolutionsApi->send_ai_solution_message:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->send_ai_solution_message: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 
 **send_ai_solution_message** | [**SendAiSolutionMessage**](SendAiSolutionMessage.md)|  | 

### Return type

[**SendAiSolutionMessage200Response**](SendAiSolutionMessage200Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ai_solution_chat_reply&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**402** | Исчерпан лимит расходов ключа AI Gateway решения (&#x60;ai_solution_chat_budget_exceeded&#x60;): поднимите лимит или дождитесь его сброса. В &#x60;details&#x60; — &#x60;max_budget&#x60;, &#x60;spend&#x60; и &#x60;budget_reset_at&#x60;, если они известны |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**502** | Агент на сервере решения ответил ошибкой (&#x60;ai_solution_chat_request_failed&#x60;) |  -  |
**503** | Чат решения недоступен: сервер разворачивается, выключен или у него нет публичного IP (&#x60;ai_solution_chat_is_unavailable&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_ai_solution**
> shutdown_ai_solution(solution_id)

Выключение AI-решения

Чтобы выключить AI-решение, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/shutdown`.  Выключает сервер решения. Действие асинхронное: следите за результатом по статусу решения (обычно 1–2 минуты до `stopped`). Пока сервер выключен, чат недоступен, а сервер продолжает тарифицироваться. Выключение уже выключенного решения возвращает 204. Пока над сервером выполняется другое действие, ответ — 409 `ai_solution_is_busy`.

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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения

    try:
        # Выключение AI-решения
        api_instance.shutdown_ai_solution(solution_id)
    except Exception as e:
        print("Exception when calling AISolutionsApi->shutdown_ai_solution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 

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
**204** | Выключение начато |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**502** | Действие над сервером решения не выполнено (&#x60;ai_solution_action_failed&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_ai_solution**
> start_ai_solution(solution_id)

Запуск AI-решения

Чтобы запустить AI-решение, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/start`.  Включает сервер решения. Действие асинхронное: следите за результатом по статусу решения, а готовность агента проверяйте методом получения статуса чата. Пока над сервером выполняется действие, запуск и выключение возвращают 409 `ai_solution_is_busy`.  Не вызывайте метод для работающего решения: запрос будет принят (204) и запустит действие над сервером, а решение на несколько минут станет занятым.

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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения

    try:
        # Запуск AI-решения
        api_instance.start_ai_solution(solution_id)
    except Exception as e:
        print("Exception when calling AISolutionsApi->start_ai_solution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 

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
**204** | Запуск начат |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**502** | Действие над сервером решения не выполнено (&#x60;ai_solution_action_failed&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_ai_solution_chat**
> stop_ai_solution_chat(solution_id, stop_ai_solution_chat=stop_ai_solution_chat)

Остановка хода агента AI-решения

Чтобы остановить текущий ход агента, отправьте POST-запрос на `/api/v1/cloud-ai/solutions/{solution_id}/chat/stop`.  Прерывает генерацию ответа — например, если ответ зациклился или тратит слишком много токенов. Без `conversation_id` останавливается текущий ход основного разговора решения. Ход прерывается на стороне агента: закрыть соединение недостаточно, потому что принятый агентом ход продолжает выполняться независимо от клиента. Если хода нет, запрос всё равно возвращает 204.  Перед вызовом убедитесь, что чат готов (`ready: true` в методе получения статуса чата): пока сервер решения разворачивается или выключен, запрос завершается ошибкой.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.stop_ai_solution_chat import StopAiSolutionChat
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения
    stop_ai_solution_chat = timeweb_cloud_api.StopAiSolutionChat() # StopAiSolutionChat |  (optional)

    try:
        # Остановка хода агента AI-решения
        api_instance.stop_ai_solution_chat(solution_id, stop_ai_solution_chat=stop_ai_solution_chat)
    except Exception as e:
        print("Exception when calling AISolutionsApi->stop_ai_solution_chat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 
 **stop_ai_solution_chat** | [**StopAiSolutionChat**](StopAiSolutionChat.md)|  | [optional] 

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
**204** | Ход остановлен |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**502** | Агент на сервере решения ответил ошибкой (&#x60;ai_solution_chat_request_failed&#x60;) |  -  |
**503** | Чат решения недоступен: сервер разворачивается, выключен или у него нет публичного IP (&#x60;ai_solution_chat_is_unavailable&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stream_ai_solution_chat**
> object stream_ai_solution_chat(solution_id, send_ai_solution_message)

Отправка сообщения агенту AI-решения с потоковым ответом

Чтобы отправить сообщение агенту решения и получать ответ потоком, отправьте POST-запрос на `https://agent.timeweb.cloud/api/v1/cloud-ai/solutions/{solution_id}/chat/stream`.  Метод работает на `https://agent.timeweb.cloud`, а не на `https://api.timeweb.cloud`: шлюз публичного API накапливает ответ целиком и не может передавать его по частям. Авторизация та же — API-токен в заголовке `Authorization`; токену с ограниченными правами нужен доступ на запись к AI-сервисам. Тело запроса такое же, как у метода отправки сообщения.  Ответ — `text/event-stream`: каждое событие приходит как `event: <тип>` и `data: <JSON>`. Отправка сообщения и подписка на ответ — один запрос, поэтому начало ответа не теряется. Строки, начинающиеся с `:`, — комментарии для поддержания соединения (каждые 15 секунд), их нужно игнорировать. ID разговора возвращается в заголовке ответа `X-Conversation-Id`.  Типы событий: - `subscribed` `{}` — ход принят; - `delta` `{text, seq, runId}` — очередной фрагмент ответа; - `tool` `{name, target, phase, status, seq, runId}` — агент использует инструмент; - `message` `{text, seq, id, stopReason}` — финальный ответ целиком, всегда после последнего `delta`; - `done` `{phase, seq, runId}` — ход завершён; - `error` `{reason, message, budget?}` — ход не удался. `reason`: `empty_reply` — агент не выдал текста; `stream_failed` — поток прервался; `agent_failed` — ход упал на стороне агента при исправном соединении, повтор имеет смысл; `budget_exceeded` — исчерпан лимит расходов ключа AI Gateway решения, в `budget` `{max, spent, resetAt}` — цифры лимита, если они известны. `error` всегда последнее событие потока и может прийти после `done` (например, с `empty_reply`).  Ошибки, возникшие до начала потока (решение не найдено, некорректный запрос, нет доступа), возвращаются обычным JSON-ответом с соответствующим HTTP-статусом. Если сервер решения выключен или недоступен, поток может открыться и сразу завершиться событием `error` с `reason: stream_failed` — проверяйте готовность чата заранее методом получения статуса чата.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.send_ai_solution_message import SendAiSolutionMessage
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения
    send_ai_solution_message = timeweb_cloud_api.SendAiSolutionMessage() # SendAiSolutionMessage | 

    try:
        # Отправка сообщения агенту AI-решения с потоковым ответом
        api_response = api_instance.stream_ai_solution_chat(solution_id, send_ai_solution_message)
        print("The response of AISolutionsApi->stream_ai_solution_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->stream_ai_solution_chat: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 
 **send_ai_solution_message** | [**SendAiSolutionMessage**](SendAiSolutionMessage.md)|  | 

### Return type

**object**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Поток событий ответа |  * X-Conversation-Id - ID разговора, в который ушёл ход <br>  |
**400** | Некорректные параметры запроса |  -  |
**403** | Токен не передан или недействителен, либо у него нет доступа на запись к AI-сервисам |  -  |
**404** | Решение не найдено (&#x60;ai_solution_not_found&#x60;) |  -  |
**500** | Внутренняя ошибка |  -  |
**503** | Чат решения недоступен (&#x60;ai_solution_chat_is_unavailable&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ai_solution**
> CreateAiSolution201Response update_ai_solution(solution_id, update_ai_solution)

Изменение AI-решения

Чтобы изменить AI-решение, отправьте PATCH-запрос на `/api/v1/cloud-ai/solutions/{solution_id}`.  Меняются только переданные поля; `description: null` очищает описание. Смена модели переписывает конфигурацию агента на сервере решения и перезапускает агента, поэтому сервер должен быть включён и полностью развёрнут — иначе запрос завершится ошибкой и ничего не изменится. Смена только названия или описания сервер не затрагивает. Неподходящая модель — 404 `model_not_found`.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.create_ai_solution201_response import CreateAiSolution201Response
from timeweb_cloud_api.models.update_ai_solution import UpdateAiSolution
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
    api_instance = timeweb_cloud_api.AISolutionsApi(api_client)
    solution_id = 15 # object | ID AI-решения
    update_ai_solution = timeweb_cloud_api.UpdateAiSolution() # UpdateAiSolution | 

    try:
        # Изменение AI-решения
        api_response = api_instance.update_ai_solution(solution_id, update_ai_solution)
        print("The response of AISolutionsApi->update_ai_solution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AISolutionsApi->update_ai_solution: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | [**object**](.md)| ID AI-решения | 
 **update_ai_solution** | [**UpdateAiSolution**](UpdateAiSolution.md)|  | 

### Return type

[**CreateAiSolution201Response**](CreateAiSolution201Response.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Объект JSON c ключом &#x60;ai_solution&#x60; |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**429** |  |  -  |
**500** |  |  -  |
**502** | Сервер решения не применил изменение (&#x60;ai_solution_configuration_failed&#x60;) |  -  |
**503** | Сервер решения нельзя настроить: он выключен, недоступен, ещё разворачивается или создан старой версией решения (&#x60;ai_solution_machine_is_unavailable&#x60;), либо у него нет публичного IP (&#x60;ai_solution_chat_is_unavailable&#x60;) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

