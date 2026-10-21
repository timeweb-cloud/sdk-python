# AiGatewayBatchRequestCounts

Счётчики запросов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **object** | Всего запросов | [optional] 
**completed** | **object** | Выполнено | [optional] 
**failed** | **object** | С ошибкой | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_batch_request_counts import AiGatewayBatchRequestCounts

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayBatchRequestCounts from a JSON string
ai_gateway_batch_request_counts_instance = AiGatewayBatchRequestCounts.from_json(json)
# print the JSON string representation of the object
print AiGatewayBatchRequestCounts.to_json()

# convert the object into a dict
ai_gateway_batch_request_counts_dict = ai_gateway_batch_request_counts_instance.to_dict()
# create an instance of AiGatewayBatchRequestCounts from a dict
ai_gateway_batch_request_counts_form_dict = ai_gateway_batch_request_counts.from_dict(ai_gateway_batch_request_counts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


