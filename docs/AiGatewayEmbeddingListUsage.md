# AiGatewayEmbeddingListUsage

Расход токенов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **object** | Входные токены | [optional] 
**total_tokens** | **object** | Всего токенов | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_embedding_list_usage import AiGatewayEmbeddingListUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayEmbeddingListUsage from a JSON string
ai_gateway_embedding_list_usage_instance = AiGatewayEmbeddingListUsage.from_json(json)
# print the JSON string representation of the object
print AiGatewayEmbeddingListUsage.to_json()

# convert the object into a dict
ai_gateway_embedding_list_usage_dict = ai_gateway_embedding_list_usage_instance.to_dict()
# create an instance of AiGatewayEmbeddingListUsage from a dict
ai_gateway_embedding_list_usage_form_dict = ai_gateway_embedding_list_usage.from_dict(ai_gateway_embedding_list_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


