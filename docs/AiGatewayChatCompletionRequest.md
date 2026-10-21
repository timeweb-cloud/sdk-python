# AiGatewayChatCompletionRequest

Запрос Chat Completions в формате OpenAI. Перечислены основные поля, остальные параметры OpenAI передаются модели как есть. Параметры, которые модель не поддерживает, могут быть отклонены с ошибкой 400

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **object** | ID модели из &#x60;GET /v1/models&#x60; | 
**messages** | **object** | История диалога целиком | 
**stream** | **object** | Отправлять ответ потоком Server-Sent Events (&#x60;text/event-stream&#x60;) | [optional] 
**stream_options** | [**AiGatewayChatCompletionRequestStreamOptions**](AiGatewayChatCompletionRequestStreamOptions.md) |  | [optional] 
**max_completion_tokens** | **object** | Максимум выходных токенов, включая рассуждения | [optional] 
**max_tokens** | **object** | Устаревший синоним &#x60;max_completion_tokens&#x60; | [optional] 
**temperature** | **object** | Температура выборки | [optional] 
**top_p** | **object** | Порог nucleus sampling | [optional] 
**n** | **object** | Количество вариантов ответа | [optional] 
**stop** | **object** | Строка или список строк, на которых генерация останавливается | [optional] 
**tools** | **object** | Функции, которые может вызвать модель | [optional] 
**tool_choice** | **object** | Режим вызова функций: &#x60;none&#x60;, &#x60;auto&#x60;, &#x60;required&#x60; или объект с конкретной функцией | [optional] 
**response_format** | **Dict[str, object]** | Формат ответа: &#x60;{\&quot;type\&quot;: \&quot;json_object\&quot;}&#x60; или &#x60;{\&quot;type\&quot;: \&quot;json_schema\&quot;, \&quot;json_schema\&quot;: {...}}&#x60; | [optional] 
**reasoning_effort** | **object** | Уровень рассуждений для моделей с рассуждениями, например &#x60;low&#x60;, &#x60;high&#x60; | [optional] 
**user** | **object** | Идентификатор вашего конечного пользователя | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_chat_completion_request import AiGatewayChatCompletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayChatCompletionRequest from a JSON string
ai_gateway_chat_completion_request_instance = AiGatewayChatCompletionRequest.from_json(json)
# print the JSON string representation of the object
print AiGatewayChatCompletionRequest.to_json()

# convert the object into a dict
ai_gateway_chat_completion_request_dict = ai_gateway_chat_completion_request_instance.to_dict()
# create an instance of AiGatewayChatCompletionRequest from a dict
ai_gateway_chat_completion_request_form_dict = ai_gateway_chat_completion_request.from_dict(ai_gateway_chat_completion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


