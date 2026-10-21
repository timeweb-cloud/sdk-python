# AiGatewayResponseCreateRequestReasoning

Настройки рассуждений

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effort** | **object** | Уровень рассуждений, например &#x60;low&#x60;, &#x60;high&#x60; | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_response_create_request_reasoning import AiGatewayResponseCreateRequestReasoning

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayResponseCreateRequestReasoning from a JSON string
ai_gateway_response_create_request_reasoning_instance = AiGatewayResponseCreateRequestReasoning.from_json(json)
# print the JSON string representation of the object
print AiGatewayResponseCreateRequestReasoning.to_json()

# convert the object into a dict
ai_gateway_response_create_request_reasoning_dict = ai_gateway_response_create_request_reasoning_instance.to_dict()
# create an instance of AiGatewayResponseCreateRequestReasoning from a dict
ai_gateway_response_create_request_reasoning_form_dict = ai_gateway_response_create_request_reasoning.from_dict(ai_gateway_response_create_request_reasoning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


