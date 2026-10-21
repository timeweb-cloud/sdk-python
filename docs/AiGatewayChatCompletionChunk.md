# AiGatewayChatCompletionChunk

Событие `data:` потокового ответа. Поток завершается строкой `data: [DONE]`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID ответа | [optional] 
**object** | **object** | Тип объекта | [optional] 
**created** | **object** | Время создания, Unix-время в секундах | [optional] 
**model** | **object** | Модель, которая отвечает | [optional] 
**choices** | **object** | Части вариантов ответа | [optional] 
**usage** | [**AiGatewayUsage**](AiGatewayUsage.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_chat_completion_chunk import AiGatewayChatCompletionChunk

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayChatCompletionChunk from a JSON string
ai_gateway_chat_completion_chunk_instance = AiGatewayChatCompletionChunk.from_json(json)
# print the JSON string representation of the object
print AiGatewayChatCompletionChunk.to_json()

# convert the object into a dict
ai_gateway_chat_completion_chunk_dict = ai_gateway_chat_completion_chunk_instance.to_dict()
# create an instance of AiGatewayChatCompletionChunk from a dict
ai_gateway_chat_completion_chunk_form_dict = ai_gateway_chat_completion_chunk.from_dict(ai_gateway_chat_completion_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


