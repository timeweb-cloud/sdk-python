# timeweb_cloud_api.AIGatewayInferenceApi

All URIs are relative to *https://api.timeweb.cloud*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_ai_gateway_batch**](AIGatewayInferenceApi.md#cancel_ai_gateway_batch) | **POST** /v1/batches/{batch_id}/cancel | Отмена батча
[**cancel_ai_gateway_response**](AIGatewayInferenceApi.md#cancel_ai_gateway_response) | **POST** /v1/responses/{response_id}/cancel | Отмена фонового ответа (Responses API)
[**create_ai_gateway_batch**](AIGatewayInferenceApi.md#create_ai_gateway_batch) | **POST** /v1/batches | Создание батча
[**create_ai_gateway_chat_completion**](AIGatewayInferenceApi.md#create_ai_gateway_chat_completion) | **POST** /v1/chat/completions | Генерация ответа в диалоге (Chat Completions)
[**create_ai_gateway_completion**](AIGatewayInferenceApi.md#create_ai_gateway_completion) | **POST** /v1/completions | Продолжение текста (Completions)
[**create_ai_gateway_embedding**](AIGatewayInferenceApi.md#create_ai_gateway_embedding) | **POST** /v1/embeddings | Получение эмбеддингов
[**create_ai_gateway_image**](AIGatewayInferenceApi.md#create_ai_gateway_image) | **POST** /v1/images/generations | Генерация изображений
[**create_ai_gateway_image_edit**](AIGatewayInferenceApi.md#create_ai_gateway_image_edit) | **POST** /v1/images/edits | Редактирование изображений
[**create_ai_gateway_response**](AIGatewayInferenceApi.md#create_ai_gateway_response) | **POST** /v1/responses | Создание ответа (Responses API)
[**create_ai_gateway_speech**](AIGatewayInferenceApi.md#create_ai_gateway_speech) | **POST** /v1/audio/speech | Синтез речи
[**create_ai_gateway_transcription**](AIGatewayInferenceApi.md#create_ai_gateway_transcription) | **POST** /v1/audio/transcriptions | Распознавание речи
[**delete_ai_gateway_file**](AIGatewayInferenceApi.md#delete_ai_gateway_file) | **DELETE** /v1/files/{file_id} | Удаление файла
[**delete_ai_gateway_response**](AIGatewayInferenceApi.md#delete_ai_gateway_response) | **DELETE** /v1/responses/{response_id} | Удаление ответа (Responses API)
[**download_ai_gateway_file_content**](AIGatewayInferenceApi.md#download_ai_gateway_file_content) | **GET** /v1/files/{file_id}/content | Скачивание файла
[**get_ai_gateway_batch**](AIGatewayInferenceApi.md#get_ai_gateway_batch) | **GET** /v1/batches/{batch_id} | Получение батча
[**get_ai_gateway_batches**](AIGatewayInferenceApi.md#get_ai_gateway_batches) | **GET** /v1/batches | Получение списка батчей
[**get_ai_gateway_file**](AIGatewayInferenceApi.md#get_ai_gateway_file) | **GET** /v1/files/{file_id} | Получение информации о файле
[**get_ai_gateway_models**](AIGatewayInferenceApi.md#get_ai_gateway_models) | **GET** /v1/models | Получение списка моделей AI Gateway
[**get_ai_gateway_response**](AIGatewayInferenceApi.md#get_ai_gateway_response) | **GET** /v1/responses/{response_id} | Получение ответа (Responses API)
[**upload_ai_gateway_file**](AIGatewayInferenceApi.md#upload_ai_gateway_file) | **POST** /v1/files | Загрузка файла


# **cancel_ai_gateway_batch**
> AiGatewayBatch cancel_ai_gateway_batch(batch_id)

Отмена батча

Чтобы отменить батч, отправьте POST-запрос на `/v1/batches/{batch_id}/cancel`.  Батч переходит в статус `cancelling`, отмена выполняется асинхронно и может занять несколько минут; итоговый статус `cancelled` проверяйте через `GET /v1/batches/{batch_id}`. Пока отмена не завершилась, входной файл батча удалить нельзя.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_batch import AiGatewayBatch
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    batch_id = batch_abc123 # object | ID батча

    try:
        # Отмена батча
        api_response = api_instance.cancel_ai_gateway_batch(batch_id)
        print("The response of AIGatewayInferenceApi->cancel_ai_gateway_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->cancel_ai_gateway_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | [**object**](.md)| ID батча | 

### Return type

[**AiGatewayBatch**](AiGatewayBatch.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Отменяемый батч |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**404** | Батч не найден |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_ai_gateway_response**
> AiGatewayResponse cancel_ai_gateway_response(response_id)

Отмена фонового ответа (Responses API)

Чтобы отменить ответ, запущенный с `\"background\": true`, отправьте POST-запрос на `/v1/responses/{response_id}/cancel`.  Отмена может завершиться не сразу: итоговый статус `cancelled` проверяйте через `GET /v1/responses/{response_id}`. Ответ, созданный без `background`, отменить нельзя — вернётся ошибка 400. Неизвестный `response_id` также возвращает 400.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_response import AiGatewayResponse
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    response_id = resp_abc123 # object | ID ответа Responses API

    try:
        # Отмена фонового ответа (Responses API)
        api_response = api_instance.cancel_ai_gateway_response(response_id)
        print("The response of AIGatewayInferenceApi->cancel_ai_gateway_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->cancel_ai_gateway_response: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | [**object**](.md)| ID ответа Responses API | 

### Return type

[**AiGatewayResponse**](AiGatewayResponse.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Отменяемый ответ |  -  |
**400** | Ответ нельзя отменить (создан без &#x60;background&#x60;) или не найден |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_gateway_batch**
> AiGatewayBatch create_ai_gateway_batch(ai_gateway_batch_create_request)

Создание батча

Чтобы запустить асинхронную обработку входного файла, загруженного с `purpose=batch`, отправьте POST-запрос на `/v1/batches`.  При создании батча его оценочная стоимость резервируется на балансе, фактическая стоимость списывается по цене Batch API после выполнения. Модели, эндпоинты и коэффициенты цены Batch API — в поле `batch` каталога моделей (`GET https://api.timeweb.cloud/api/v3/cloud-ai/models`). Batch API доступен только для ключей AI Gateway.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_batch import AiGatewayBatch
from timeweb_cloud_api.models.ai_gateway_batch_create_request import AiGatewayBatchCreateRequest
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    ai_gateway_batch_create_request = timeweb_cloud_api.AiGatewayBatchCreateRequest() # AiGatewayBatchCreateRequest | 

    try:
        # Создание батча
        api_response = api_instance.create_ai_gateway_batch(ai_gateway_batch_create_request)
        print("The response of AIGatewayInferenceApi->create_ai_gateway_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->create_ai_gateway_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_gateway_batch_create_request** | [**AiGatewayBatchCreateRequest**](AiGatewayBatchCreateRequest.md)|  | 

### Return type

[**AiGatewayBatch**](AiGatewayBatch.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Созданный батч |  -  |
**400** | Некорректный запрос: неверный &#x60;input_file_id&#x60;, &#x60;endpoint&#x60; не совпадает с &#x60;url&#x60; строк файла, неверный &#x60;completion_window&#x60; |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**402** | Недостаточно средств на балансе: оценочная стоимость запроса больше доступного баланса (с учётом ещё не списанной стоимости недавних и выполняющихся запросов) |  -  |
**403** | Ключ недействителен, аккаунт заблокирован или Batch API недоступен для ключа |  -  |
**404** | Модель не найдена: неизвестный или не переданный &#x60;model&#x60; |  -  |
**405** | Модель не поддерживает Batch API или этот эндпоинт |  -  |
**410** | Модель снята с обслуживания |  -  |
**422** | Исчерпан лимит расхода ключа |  -  |
**429** | Достигнут лимит очереди Batch API для модели — дождитесь завершения ваших батчей и повторите запрос |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_gateway_chat_completion**
> AiGatewayChatCompletion create_ai_gateway_chat_completion(request_body)

Генерация ответа в диалоге (Chat Completions)

Чтобы получить следующий ответ модели в диалоге, отправьте POST-запрос на `/v1/chat/completions`.  Запрос не хранит состояние: передавайте всю историю диалога в `messages`. Поддерживаются вызов функций (`tools`), структурированный ответ (`response_format`) и изображения во входных сообщениях (для моделей с поддержкой зрения).  С `\"stream\": true` ответ приходит потоком Server-Sent Events: события `chat.completion.chunk` в строках `data:`, в конце — `data: [DONE]`. С `\"stream_options\": {\"include_usage\": true}` последний чанк содержит расход токенов.  Если у ключа настроены запасные модели и запрошенная модель не ответила, запрос повторяется на запасных. Заголовок ответа `x-timeweb-attempted-fallbacks` показывает, сколько запасных моделей было опробовано.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_chat_completion import AiGatewayChatCompletion
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Генерация ответа в диалоге (Chat Completions)
        api_response = api_instance.create_ai_gateway_chat_completion(request_body)
        print("The response of AIGatewayInferenceApi->create_ai_gateway_chat_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->create_ai_gateway_chat_completion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AiGatewayChatCompletion**](AiGatewayChatCompletion.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ модели или, с &#x60;\&quot;stream\&quot;: true&#x60;, поток чанков |  -  |
**400** | Некорректный запрос: не переданы или неверны параметры (например, пустой &#x60;messages&#x60;), модель не поддерживает операцию (например, модель эмбеддингов) или временно недоступна |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**402** | Недостаточно средств на балансе: оценочная стоимость запроса больше доступного баланса (с учётом ещё не списанной стоимости недавних и выполняющихся запросов) |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**404** | Модель не найдена: неизвестный или не переданный &#x60;model&#x60; |  -  |
**410** | Модель снята с обслуживания |  -  |
**422** | Исчерпан лимит расхода ключа |  -  |
**429** | Превышен лимит запросов провайдера модели (текст ошибки — от провайдера). Повторите запрос позже |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_gateway_completion**
> AiGatewayCompletion create_ai_gateway_completion(request_body)

Продолжение текста (Completions)

Чтобы получить продолжение текста `prompt`, отправьте POST-запрос на `/v1/completions`.  Это устаревший API OpenAI — для новых интеграций используйте `/v1/chat/completions`. С `\"stream\": true` ответ приходит потоком Server-Sent Events и заканчивается `data: [DONE]`.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_completion import AiGatewayCompletion
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Продолжение текста (Completions)
        api_response = api_instance.create_ai_gateway_completion(request_body)
        print("The response of AIGatewayInferenceApi->create_ai_gateway_completion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->create_ai_gateway_completion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AiGatewayCompletion**](AiGatewayCompletion.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Продолжение текста или, с &#x60;\&quot;stream\&quot;: true&#x60;, поток событий |  -  |
**400** | Некорректный запрос: не переданы или неверны параметры, модель не поддерживает операцию или временно недоступна |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**402** | Недостаточно средств на балансе: оценочная стоимость запроса больше доступного баланса (с учётом ещё не списанной стоимости недавних и выполняющихся запросов) |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**404** | Модель не найдена или снята с обслуживания |  -  |
**422** | Исчерпан лимит расхода ключа |  -  |
**429** | Превышен лимит запросов провайдера модели (текст ошибки — от провайдера). Повторите запрос позже |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_gateway_embedding**
> AiGatewayEmbeddingList create_ai_gateway_embedding(request_body)

Получение эмбеддингов

Чтобы получить векторные представления текстов, отправьте POST-запрос на `/v1/embeddings`.  Используйте модель с `mode: embedding` из `GET /v1/models`. Эмбеддинги возвращаются в порядке входных текстов.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_embedding_list import AiGatewayEmbeddingList
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Получение эмбеддингов
        api_response = api_instance.create_ai_gateway_embedding(request_body)
        print("The response of AIGatewayInferenceApi->create_ai_gateway_embedding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->create_ai_gateway_embedding: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AiGatewayEmbeddingList**](AiGatewayEmbeddingList.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Эмбеддинги |  -  |
**400** | Некорректный запрос: не передан &#x60;input&#x60;, модель не поддерживает эмбеддинги или временно недоступна |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**402** | Недостаточно средств на балансе: оценочная стоимость запроса больше доступного баланса (с учётом ещё не списанной стоимости недавних и выполняющихся запросов) |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**404** | Модель не найдена: неизвестный или не переданный &#x60;model&#x60; |  -  |
**410** | Модель снята с обслуживания |  -  |
**422** | Исчерпан лимит расхода ключа |  -  |
**429** | Превышен лимит запросов провайдера модели (текст ошибки — от провайдера). Повторите запрос позже |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_gateway_image**
> AiGatewayImagesResponse create_ai_gateway_image(request_body)

Генерация изображений

Чтобы сгенерировать изображения по текстовому описанию, отправьте POST-запрос на `/v1/images/generations`.  Используйте модель с `mode: image_generation` из `GET /v1/models`.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_images_response import AiGatewayImagesResponse
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Генерация изображений
        api_response = api_instance.create_ai_gateway_image(request_body)
        print("The response of AIGatewayInferenceApi->create_ai_gateway_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->create_ai_gateway_image: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AiGatewayImagesResponse**](AiGatewayImagesResponse.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Сгенерированные изображения |  -  |
**400** | Некорректный запрос: не переданы или неверны параметры, модель не поддерживает операцию или временно недоступна |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**402** | Недостаточно средств на балансе: оценочная стоимость запроса больше доступного баланса (с учётом ещё не списанной стоимости недавних и выполняющихся запросов) |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**404** | Модель не найдена: неизвестный или не переданный &#x60;model&#x60; |  -  |
**410** | Модель снята с обслуживания |  -  |
**422** | Исчерпан лимит расхода ключа |  -  |
**429** | Превышен лимит запросов провайдера модели (текст ошибки — от провайдера). Повторите запрос позже |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_gateway_image_edit**
> AiGatewayImagesResponse create_ai_gateway_image_edit(model, image, prompt, mask=mask, n=n, size=size, quality=quality)

Редактирование изображений

Чтобы изменить или дополнить изображения по описанию, отправьте POST-запрос на `/v1/images/edits` (multipart/form-data).  Доступно для моделей GPT Image (`openai/gpt-image-*`) и FLUX.2 (`black_forest_labs/flux-2-*`). Для других моделей, в том числе неизвестных, возвращается ошибка 405.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_images_response import AiGatewayImagesResponse
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    model = None # object | ID модели: GPT Image (`openai/gpt-image-*`) или FLUX.2 (`black_forest_labs/flux-2-*`)
    image = None # object | Исходное изображение или несколько файлов в поле `image[]`
    prompt = None # object | Что изменить
    mask = None # object | Маска: прозрачные области будут изменены (optional)
    n = None # object | Количество изображений (optional)
    size = None # object | Размер изображения (optional)
    quality = None # object | Качество изображения (optional)

    try:
        # Редактирование изображений
        api_response = api_instance.create_ai_gateway_image_edit(model, image, prompt, mask=mask, n=n, size=size, quality=quality)
        print("The response of AIGatewayInferenceApi->create_ai_gateway_image_edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->create_ai_gateway_image_edit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**object**](object.md)| ID модели: GPT Image (&#x60;openai/gpt-image-*&#x60;) или FLUX.2 (&#x60;black_forest_labs/flux-2-*&#x60;) | 
 **image** | [**object**](object.md)| Исходное изображение или несколько файлов в поле &#x60;image[]&#x60; | 
 **prompt** | [**object**](object.md)| Что изменить | 
 **mask** | [**object**](object.md)| Маска: прозрачные области будут изменены | [optional] 
 **n** | [**object**](object.md)| Количество изображений | [optional] 
 **size** | [**object**](object.md)| Размер изображения | [optional] 
 **quality** | [**object**](object.md)| Качество изображения | [optional] 

### Return type

[**AiGatewayImagesResponse**](AiGatewayImagesResponse.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Изменённые изображения |  -  |
**400** | Некорректный запрос: не переданы или неверны параметры, модель не поддерживает операцию или временно недоступна |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**402** | Недостаточно средств на балансе: оценочная стоимость запроса больше доступного баланса (с учётом ещё не списанной стоимости недавних и выполняющихся запросов) |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**405** | Модель не поддерживает редактирование изображений или не найдена |  -  |
**410** | Модель снята с обслуживания |  -  |
**422** | Исчерпан лимит расхода ключа |  -  |
**429** | Превышен лимит запросов провайдера модели (текст ошибки — от провайдера). Повторите запрос позже |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_gateway_response**
> AiGatewayResponse create_ai_gateway_response(request_body)

Создание ответа (Responses API)

Чтобы получить ответ модели через OpenAI Responses API, отправьте POST-запрос на `/v1/responses`.  Диалог можно продолжить по `previous_response_id`, долгие запросы — выполнить в фоне с `\"background\": true` и получать результат через `GET /v1/responses/{response_id}`.  С `\"stream\": true` ответ приходит потоком типизированных событий Server-Sent Events (`response.created`, `response.output_text.delta`, `response.completed` и др.), в конце потока — `data: [DONE]`.  Если у ключа настроены запасные модели и запрошенная модель не ответила, запрос повторяется на запасных (заголовок `x-timeweb-attempted-fallbacks`).

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_response import AiGatewayResponse
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Создание ответа (Responses API)
        api_response = api_instance.create_ai_gateway_response(request_body)
        print("The response of AIGatewayInferenceApi->create_ai_gateway_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->create_ai_gateway_response: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AiGatewayResponse**](AiGatewayResponse.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/event-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ или, с &#x60;\&quot;stream\&quot;: true&#x60;, поток событий |  -  |
**400** | Некорректный запрос: не переданы или неверны параметры, модель не поддерживает операцию или временно недоступна |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**402** | Недостаточно средств на балансе: оценочная стоимость запроса больше доступного баланса (с учётом ещё не списанной стоимости недавних и выполняющихся запросов) |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**404** | Модель не найдена: неизвестный или не переданный &#x60;model&#x60; |  -  |
**410** | Модель снята с обслуживания |  -  |
**422** | Исчерпан лимит расхода ключа |  -  |
**429** | Превышен лимит запросов провайдера модели (текст ошибки — от провайдера). Повторите запрос позже |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_gateway_speech**
> object create_ai_gateway_speech(request_body)

Синтез речи

Чтобы озвучить текст, отправьте POST-запрос на `/v1/audio/speech`.  Используйте модель с `mode: audio_speech` из `GET /v1/models`. Ответ — аудиофайл в формате `response_format` (по умолчанию `mp3`).

### Example

* Bearer Authentication (AiGatewayKey):
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Синтез речи
        api_response = api_instance.create_ai_gateway_speech(request_body)
        print("The response of AIGatewayInferenceApi->create_ai_gateway_speech:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->create_ai_gateway_speech: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

**object**

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: audio/mpeg, audio/wav, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Аудиофайл |  -  |
**400** | Некорректный запрос: не переданы или неверны параметры, модель не поддерживает операцию или временно недоступна |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**402** | Недостаточно средств на балансе: оценочная стоимость запроса больше доступного баланса (с учётом ещё не списанной стоимости недавних и выполняющихся запросов) |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**410** | Модель снята с обслуживания |  -  |
**422** | Исчерпан лимит расхода ключа |  -  |
**429** | Превышен лимит запросов провайдера модели (текст ошибки — от провайдера). Повторите запрос позже |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ai_gateway_transcription**
> AiGatewayTranscription create_ai_gateway_transcription(file, model, language=language, prompt=prompt, response_format=response_format, temperature=temperature)

Распознавание речи

Чтобы распознать речь в аудиофайле, отправьте POST-запрос на `/v1/audio/transcriptions` (multipart/form-data).  Доступно для моделей распознавания речи `*-transcribe` (например, `openai/gpt-4o-mini-transcribe`). Для других моделей, в том числе неизвестных, возвращается ошибка 405. Ответ возвращается в JSON.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_transcription import AiGatewayTranscription
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    file = None # object | Аудиофайл
    model = None # object | ID модели распознавания речи (`*-transcribe`)
    language = None # object | Язык аудио в формате ISO-639-1 (optional)
    prompt = None # object | Подсказка для распознавания: термины, имена, стиль (optional)
    response_format = None # object | Формат ответа (optional)
    temperature = None # object | Температура выборки (optional)

    try:
        # Распознавание речи
        api_response = api_instance.create_ai_gateway_transcription(file, model, language=language, prompt=prompt, response_format=response_format, temperature=temperature)
        print("The response of AIGatewayInferenceApi->create_ai_gateway_transcription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->create_ai_gateway_transcription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**object**](object.md)| Аудиофайл | 
 **model** | [**object**](object.md)| ID модели распознавания речи (&#x60;*-transcribe&#x60;) | 
 **language** | [**object**](object.md)| Язык аудио в формате ISO-639-1 | [optional] 
 **prompt** | [**object**](object.md)| Подсказка для распознавания: термины, имена, стиль | [optional] 
 **response_format** | [**object**](object.md)| Формат ответа | [optional] 
 **temperature** | [**object**](object.md)| Температура выборки | [optional] 

### Return type

[**AiGatewayTranscription**](AiGatewayTranscription.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Распознанный текст |  -  |
**400** | Некорректный запрос, например повреждённый аудиофайл |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**402** | Недостаточно средств на балансе: оценочная стоимость запроса больше доступного баланса (с учётом ещё не списанной стоимости недавних и выполняющихся запросов) |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**405** | Модель не поддерживает распознавание речи или не найдена |  -  |
**410** | Модель снята с обслуживания |  -  |
**422** | Исчерпан лимит расхода ключа (формат OpenAI) или не прошла проверка параметров multipart-запроса, например не передан файл (формат &#x60;{\&quot;detail\&quot;: ...}&#x60;) |  -  |
**429** | Превышен лимит запросов провайдера модели (текст ошибки — от провайдера). Повторите запрос позже |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ai_gateway_file**
> AiGatewayFileDeleted delete_ai_gateway_file(file_id)

Удаление файла

Чтобы удалить файл, отправьте DELETE-запрос на `/v1/files/{file_id}`.  Входной файл батча, который ещё выполняется или отменяется, и результаты батча, расход которого ещё не списан, удалить нельзя — вернётся ошибка 409.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_file_deleted import AiGatewayFileDeleted
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    file_id = file-abc123 # object | ID файла

    try:
        # Удаление файла
        api_response = api_instance.delete_ai_gateway_file(file_id)
        print("The response of AIGatewayInferenceApi->delete_ai_gateway_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->delete_ai_gateway_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**object**](.md)| ID файла | 

### Return type

[**AiGatewayFileDeleted**](AiGatewayFileDeleted.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Результат удаления |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**404** | Файл не найден |  -  |
**409** | Файл используется батчем, который ещё выполняется |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ai_gateway_response**
> AiGatewayResponseDeleted delete_ai_gateway_response(response_id)

Удаление ответа (Responses API)

Чтобы удалить сохранённый ответ, отправьте DELETE-запрос на `/v1/responses/{response_id}`.  Неизвестный или уже удалённый `response_id` возвращает ошибку 400.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_response_deleted import AiGatewayResponseDeleted
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    response_id = resp_abc123 # object | ID ответа Responses API

    try:
        # Удаление ответа (Responses API)
        api_response = api_instance.delete_ai_gateway_response(response_id)
        print("The response of AIGatewayInferenceApi->delete_ai_gateway_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->delete_ai_gateway_response: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | [**object**](.md)| ID ответа Responses API | 

### Return type

[**AiGatewayResponseDeleted**](AiGatewayResponseDeleted.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Результат удаления |  -  |
**400** | Ответ с таким &#x60;response_id&#x60; не найден (в том числе уже удалён) или запрос некорректен |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_ai_gateway_file_content**
> object download_ai_gateway_file_content(file_id)

Скачивание файла

Чтобы скачать содержимое файла — например, результаты выполненного батча (`output_file_id`), — отправьте GET-запрос на `/v1/files/{file_id}/content`.  Перед скачиванием результатов получите батч через `GET /v1/batches/{batch_id}` и убедитесь, что он в статусе `completed`. Файлы с `purpose=user_data` скачать нельзя — вернётся ошибка 400.

### Example

* Bearer Authentication (AiGatewayKey):
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    file_id = file-abc123 # object | ID файла

    try:
        # Скачивание файла
        api_response = api_instance.download_ai_gateway_file_content(file_id)
        print("The response of AIGatewayInferenceApi->download_ai_gateway_file_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->download_ai_gateway_file_content: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**object**](.md)| ID файла | 

### Return type

**object**

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Содержимое файла |  -  |
**400** | Файл этого назначения скачать нельзя |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**404** | Файл не найден |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_gateway_batch**
> AiGatewayBatch get_ai_gateway_batch(batch_id)

Получение батча

Чтобы получить статус батча, отправьте GET-запрос на `/v1/batches/{batch_id}`.  Когда статус станет `completed`, скачайте результаты по `output_file_id` через `GET /v1/files/{file_id}/content`.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_batch import AiGatewayBatch
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    batch_id = batch_abc123 # object | ID батча

    try:
        # Получение батча
        api_response = api_instance.get_ai_gateway_batch(batch_id)
        print("The response of AIGatewayInferenceApi->get_ai_gateway_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->get_ai_gateway_batch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | [**object**](.md)| ID батча | 

### Return type

[**AiGatewayBatch**](AiGatewayBatch.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Батч |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**404** | Батч не найден |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_gateway_batches**
> AiGatewayBatchList get_ai_gateway_batches(limit=limit, after=after)

Получение списка батчей

Чтобы получить список батчей, отправьте GET-запрос на `/v1/batches`.  Для следующей страницы передайте в `after` значение `last_id`, пока `has_more` равно `true`.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_batch_list import AiGatewayBatchList
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    limit = 20 # object | Количество батчей на странице (optional)
    after = batch_abc123 # object | Вернуть батчи после батча с этим ID (значение `last_id` предыдущей страницы) (optional)

    try:
        # Получение списка батчей
        api_response = api_instance.get_ai_gateway_batches(limit=limit, after=after)
        print("The response of AIGatewayInferenceApi->get_ai_gateway_batches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->get_ai_gateway_batches: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)| Количество батчей на странице | [optional] 
 **after** | [**object**](.md)| Вернуть батчи после батча с этим ID (значение &#x60;last_id&#x60; предыдущей страницы) | [optional] 

### Return type

[**AiGatewayBatchList**](AiGatewayBatchList.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список батчей |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**422** | Неверные параметры запроса, например нечисловой &#x60;limit&#x60; |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |
**503** | Сервис или провайдер модели временно недоступен. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_gateway_file**
> AiGatewayFile get_ai_gateway_file(file_id)

Получение информации о файле

Чтобы получить информацию о загруженном файле, отправьте GET-запрос на `/v1/files/{file_id}`.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_file import AiGatewayFile
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    file_id = file-abc123 # object | ID файла

    try:
        # Получение информации о файле
        api_response = api_instance.get_ai_gateway_file(file_id)
        print("The response of AIGatewayInferenceApi->get_ai_gateway_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->get_ai_gateway_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | [**object**](.md)| ID файла | 

### Return type

[**AiGatewayFile**](AiGatewayFile.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Файл |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**404** | Файл не найден |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_gateway_models**
> AiGatewayModelList get_ai_gateway_models()

Получение списка моделей AI Gateway

Чтобы получить список моделей, доступных ключу, отправьте GET-запрос на `/v1/models`.  Поле `mode` показывает назначение модели. В списке могут оставаться модели, снятые с обслуживания: запросы к ним возвращают ошибку 410. Актуальный статус, цены и возможности моделей — в каталоге `GET https://api.timeweb.cloud/api/v3/cloud-ai/models` (снятые модели — `is_stopped: true`).

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_model_list import AiGatewayModelList
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)

    try:
        # Получение списка моделей AI Gateway
        api_response = api_instance.get_ai_gateway_models()
        print("The response of AIGatewayInferenceApi->get_ai_gateway_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->get_ai_gateway_models: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AiGatewayModelList**](AiGatewayModelList.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Список моделей |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_gateway_response**
> AiGatewayResponse get_ai_gateway_response(response_id)

Получение ответа (Responses API)

Чтобы получить сохранённый ответ — например, дождаться завершения фонового ответа, — отправьте GET-запрос на `/v1/responses/{response_id}`.  Неизвестный или удалённый `response_id` возвращает ошибку 400.

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_response import AiGatewayResponse
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    response_id = resp_abc123 # object | ID ответа Responses API

    try:
        # Получение ответа (Responses API)
        api_response = api_instance.get_ai_gateway_response(response_id)
        print("The response of AIGatewayInferenceApi->get_ai_gateway_response:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->get_ai_gateway_response: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_id** | [**object**](.md)| ID ответа Responses API | 

### Return type

[**AiGatewayResponse**](AiGatewayResponse.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ответ |  -  |
**400** | Ответ с таким &#x60;response_id&#x60; не найден (в том числе уже удалён) или запрос некорректен |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_ai_gateway_file**
> AiGatewayFile upload_ai_gateway_file(file, purpose, model=model, target_model_names=target_model_names)

Загрузка файла

Чтобы загрузить файл, отправьте POST-запрос на `/v1/files` (multipart/form-data).  Файл загружается для конкретной модели, поэтому `model` (или `target_model_names`) обязателен: - `purpose=batch` — входной JSONL-файл Batch API. Все строки должны обращаться к одной модели — той, что указана в `model`, иначе вернётся 400. Размер — до 50 МБ и до 50 000 запросов; - `user_data` и другие назначения OpenAI — файлы, на которые можно сослаться по `file_id` в сообщениях.  Загрузка бесплатна. Сохраняйте `id` загруженных файлов: получить список файлов нельзя (`GET /v1/files` возвращает 405).

### Example

* Bearer Authentication (AiGatewayKey):
```python
import time
import os
import timeweb_cloud_api
from timeweb_cloud_api.models.ai_gateway_file import AiGatewayFile
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

# Configure Bearer authorization: AiGatewayKey
configuration = timeweb_cloud_api.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with timeweb_cloud_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = timeweb_cloud_api.AIGatewayInferenceApi(api_client)
    file = None # object | Файл. Для Batch API — JSONL, по одному запросу в строке
    purpose = None # object | Назначение: `batch` — входной файл Batch API, `user_data` и другие назначения OpenAI — файлы для передачи модели
    model = None # object | Модель, для которой загружается файл. Обязателен, если не передан `target_model_names` (optional)
    target_model_names = None # object | Список моделей через запятую — вместо `model` (optional)

    try:
        # Загрузка файла
        api_response = api_instance.upload_ai_gateway_file(file, purpose, model=model, target_model_names=target_model_names)
        print("The response of AIGatewayInferenceApi->upload_ai_gateway_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AIGatewayInferenceApi->upload_ai_gateway_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**object**](object.md)| Файл. Для Batch API — JSONL, по одному запросу в строке | 
 **purpose** | [**object**](object.md)| Назначение: &#x60;batch&#x60; — входной файл Batch API, &#x60;user_data&#x60; и другие назначения OpenAI — файлы для передачи модели | 
 **model** | [**object**](object.md)| Модель, для которой загружается файл. Обязателен, если не передан &#x60;target_model_names&#x60; | [optional] 
 **target_model_names** | [**object**](object.md)| Список моделей через запятую — вместо &#x60;model&#x60; | [optional] 

### Return type

[**AiGatewayFile**](AiGatewayFile.md)

### Authorization

[AiGatewayKey](../README.md#AiGatewayKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Загруженный файл |  -  |
**400** | Некорректный запрос, например модель в строках файла не совпадает с &#x60;model&#x60; |  -  |
**401** | Ключ не передан или имеет неверный формат |  -  |
**403** | Ключ недействителен или аккаунт заблокирован |  -  |
**422** | Не прошла проверка параметров, например не передан файл |  -  |
**500** | Внутренняя ошибка или некорректный ответ провайдера модели. Повторите запрос позже |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

