# AiGatewayError

Ошибка в формате OpenAI

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**AiGatewayErrorError**](AiGatewayErrorError.md) |  | 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_error import AiGatewayError

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayError from a JSON string
ai_gateway_error_instance = AiGatewayError.from_json(json)
# print the JSON string representation of the object
print AiGatewayError.to_json()

# convert the object into a dict
ai_gateway_error_dict = ai_gateway_error_instance.to_dict()
# create an instance of AiGatewayError from a dict
ai_gateway_error_form_dict = ai_gateway_error.from_dict(ai_gateway_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


