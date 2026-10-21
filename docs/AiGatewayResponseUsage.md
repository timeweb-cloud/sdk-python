# AiGatewayResponseUsage

Расход токенов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_tokens** | **object** | Входные токены | [optional] 
**output_tokens** | **object** | Выходные токены | [optional] 
**total_tokens** | **object** | Всего токенов | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_response_usage import AiGatewayResponseUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayResponseUsage from a JSON string
ai_gateway_response_usage_instance = AiGatewayResponseUsage.from_json(json)
# print the JSON string representation of the object
print AiGatewayResponseUsage.to_json()

# convert the object into a dict
ai_gateway_response_usage_dict = ai_gateway_response_usage_instance.to_dict()
# create an instance of AiGatewayResponseUsage from a dict
ai_gateway_response_usage_form_dict = ai_gateway_response_usage.from_dict(ai_gateway_response_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


