# AiGatewayToolCall

Вызов функции моделью

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID вызова. Передайте его в &#x60;tool_call_id&#x60; сообщения с результатом | [optional] 
**type** | **object** | Тип вызова | [optional] 
**function** | [**AiGatewayToolCallFunction**](AiGatewayToolCallFunction.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_tool_call import AiGatewayToolCall

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayToolCall from a JSON string
ai_gateway_tool_call_instance = AiGatewayToolCall.from_json(json)
# print the JSON string representation of the object
print AiGatewayToolCall.to_json()

# convert the object into a dict
ai_gateway_tool_call_dict = ai_gateway_tool_call_instance.to_dict()
# create an instance of AiGatewayToolCall from a dict
ai_gateway_tool_call_form_dict = ai_gateway_tool_call.from_dict(ai_gateway_tool_call_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


