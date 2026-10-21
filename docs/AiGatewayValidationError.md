# AiGatewayValidationError

Ошибка в формате `{\"detail\": ...}`: так отвечают на ошибки проверки параметров multipart-запросов и query-параметров, а также на неизвестный путь

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **object** | Описание ошибки: строка или список ошибок по полям запроса | 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_validation_error import AiGatewayValidationError

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayValidationError from a JSON string
ai_gateway_validation_error_instance = AiGatewayValidationError.from_json(json)
# print the JSON string representation of the object
print AiGatewayValidationError.to_json()

# convert the object into a dict
ai_gateway_validation_error_dict = ai_gateway_validation_error_instance.to_dict()
# create an instance of AiGatewayValidationError from a dict
ai_gateway_validation_error_form_dict = ai_gateway_validation_error.from_dict(ai_gateway_validation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


