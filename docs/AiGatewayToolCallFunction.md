# AiGatewayToolCallFunction

Вызываемая функция

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название функции | [optional] 
**arguments** | **object** | Аргументы — JSON-строка | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_tool_call_function import AiGatewayToolCallFunction

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayToolCallFunction from a JSON string
ai_gateway_tool_call_function_instance = AiGatewayToolCallFunction.from_json(json)
# print the JSON string representation of the object
print AiGatewayToolCallFunction.to_json()

# convert the object into a dict
ai_gateway_tool_call_function_dict = ai_gateway_tool_call_function_instance.to_dict()
# create an instance of AiGatewayToolCallFunction from a dict
ai_gateway_tool_call_function_form_dict = ai_gateway_tool_call_function.from_dict(ai_gateway_tool_call_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


