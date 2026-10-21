# AiGatewayErrorError

Описание ошибки

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **object** | Текст ошибки | 
**type** | **object** | Тип ошибки, например &#x60;auth_error&#x60; или &#x60;invalid_request_error&#x60;. Может быть &#x60;null&#x60; или строкой &#x60;\&quot;None\&quot;&#x60; | [optional] 
**param** | **object** | Параметр запроса, к которому относится ошибка. Может быть &#x60;null&#x60; или строкой &#x60;\&quot;None\&quot;&#x60; | [optional] 
**code** | **object** | HTTP-код ответа строкой | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_error_error import AiGatewayErrorError

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayErrorError from a JSON string
ai_gateway_error_error_instance = AiGatewayErrorError.from_json(json)
# print the JSON string representation of the object
print AiGatewayErrorError.to_json()

# convert the object into a dict
ai_gateway_error_error_dict = ai_gateway_error_error_instance.to_dict()
# create an instance of AiGatewayErrorError from a dict
ai_gateway_error_error_form_dict = ai_gateway_error_error.from_dict(ai_gateway_error_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


