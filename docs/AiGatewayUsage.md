# AiGatewayUsage

Расход токенов запроса

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **object** | Входные токены | [optional] 
**completion_tokens** | **object** | Выходные токены | [optional] 
**total_tokens** | **object** | Всего токенов | [optional] 
**prompt_tokens_details** | [**AiGatewayUsagePromptTokensDetails**](AiGatewayUsagePromptTokensDetails.md) |  | [optional] 
**completion_tokens_details** | [**AiGatewayUsageCompletionTokensDetails**](AiGatewayUsageCompletionTokensDetails.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_usage import AiGatewayUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayUsage from a JSON string
ai_gateway_usage_instance = AiGatewayUsage.from_json(json)
# print the JSON string representation of the object
print AiGatewayUsage.to_json()

# convert the object into a dict
ai_gateway_usage_dict = ai_gateway_usage_instance.to_dict()
# create an instance of AiGatewayUsage from a dict
ai_gateway_usage_form_dict = ai_gateway_usage.from_dict(ai_gateway_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


