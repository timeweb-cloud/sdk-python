# AiGatewayUsageCompletionTokensDetails

Детализация выходных токенов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reasoning_tokens** | **object** | Токены, потраченные на рассуждения | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_usage_completion_tokens_details import AiGatewayUsageCompletionTokensDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayUsageCompletionTokensDetails from a JSON string
ai_gateway_usage_completion_tokens_details_instance = AiGatewayUsageCompletionTokensDetails.from_json(json)
# print the JSON string representation of the object
print AiGatewayUsageCompletionTokensDetails.to_json()

# convert the object into a dict
ai_gateway_usage_completion_tokens_details_dict = ai_gateway_usage_completion_tokens_details_instance.to_dict()
# create an instance of AiGatewayUsageCompletionTokensDetails from a dict
ai_gateway_usage_completion_tokens_details_form_dict = ai_gateway_usage_completion_tokens_details.from_dict(ai_gateway_usage_completion_tokens_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


