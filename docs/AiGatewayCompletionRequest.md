# AiGatewayCompletionRequest

Запрос Completions (устаревший API OpenAI)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **object** | ID модели из &#x60;GET /v1/models&#x60; | 
**prompt** | **object** | Текст или список текстов для продолжения | 
**max_tokens** | **object** | Максимум выходных токенов | [optional] 
**temperature** | **object** | Температура выборки | [optional] 
**top_p** | **object** | Порог nucleus sampling | [optional] 
**stop** | **object** | Строка или список строк, на которых генерация останавливается | [optional] 
**stream** | **object** | Отправлять ответ потоком Server-Sent Events (&#x60;text/event-stream&#x60;) | [optional] 
**stream_options** | [**AiGatewayChatCompletionRequestStreamOptions**](AiGatewayChatCompletionRequestStreamOptions.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_completion_request import AiGatewayCompletionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayCompletionRequest from a JSON string
ai_gateway_completion_request_instance = AiGatewayCompletionRequest.from_json(json)
# print the JSON string representation of the object
print AiGatewayCompletionRequest.to_json()

# convert the object into a dict
ai_gateway_completion_request_dict = ai_gateway_completion_request_instance.to_dict()
# create an instance of AiGatewayCompletionRequest from a dict
ai_gateway_completion_request_form_dict = ai_gateway_completion_request.from_dict(ai_gateway_completion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


