# AiGatewayCompletion

Ответ Completions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID ответа | [optional] 
**object** | **object** | Тип объекта | [optional] 
**created** | **object** | Время создания, Unix-время в секундах | [optional] 
**model** | **object** | Модель, которая ответила | [optional] 
**choices** | **object** | Варианты продолжения | [optional] 
**usage** | [**AiGatewayUsage**](AiGatewayUsage.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_completion import AiGatewayCompletion

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayCompletion from a JSON string
ai_gateway_completion_instance = AiGatewayCompletion.from_json(json)
# print the JSON string representation of the object
print AiGatewayCompletion.to_json()

# convert the object into a dict
ai_gateway_completion_dict = ai_gateway_completion_instance.to_dict()
# create an instance of AiGatewayCompletion from a dict
ai_gateway_completion_form_dict = ai_gateway_completion.from_dict(ai_gateway_completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


