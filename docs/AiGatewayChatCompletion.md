# AiGatewayChatCompletion

Ответ Chat Completions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID ответа | [optional] 
**object** | **object** | Тип объекта | [optional] 
**created** | **object** | Время создания, Unix-время в секундах | [optional] 
**model** | **object** | Модель, которая ответила | [optional] 
**choices** | **object** | Варианты ответа | [optional] 
**usage** | [**AiGatewayUsage**](AiGatewayUsage.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_chat_completion import AiGatewayChatCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayChatCompletion from a JSON string
ai_gateway_chat_completion_instance = AiGatewayChatCompletion.from_json(json)
# print the JSON string representation of the object
print AiGatewayChatCompletion.to_json()

# convert the object into a dict
ai_gateway_chat_completion_dict = ai_gateway_chat_completion_instance.to_dict()
# create an instance of AiGatewayChatCompletion from a dict
ai_gateway_chat_completion_form_dict = ai_gateway_chat_completion.from_dict(ai_gateway_chat_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


