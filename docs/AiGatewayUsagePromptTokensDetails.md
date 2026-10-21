# AiGatewayUsagePromptTokensDetails

Детализация входных токенов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cached_tokens** | **object** | Входные токены, прочитанные из кэша промпта | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_usage_prompt_tokens_details import AiGatewayUsagePromptTokensDetails

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayUsagePromptTokensDetails from a JSON string
ai_gateway_usage_prompt_tokens_details_instance = AiGatewayUsagePromptTokensDetails.from_json(json)
# print the JSON string representation of the object
print AiGatewayUsagePromptTokensDetails.to_json()

# convert the object into a dict
ai_gateway_usage_prompt_tokens_details_dict = ai_gateway_usage_prompt_tokens_details_instance.to_dict()
# create an instance of AiGatewayUsagePromptTokensDetails from a dict
ai_gateway_usage_prompt_tokens_details_form_dict = ai_gateway_usage_prompt_tokens_details.from_dict(ai_gateway_usage_prompt_tokens_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


