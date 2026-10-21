# AiGatewayResponseDeleted

Результат удаления ответа

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID удалённого ответа | [optional] 
**object** | **object** | Тип объекта | [optional] 
**deleted** | **object** | Ответ удалён | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_response_deleted import AiGatewayResponseDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayResponseDeleted from a JSON string
ai_gateway_response_deleted_instance = AiGatewayResponseDeleted.from_json(json)
# print the JSON string representation of the object
print AiGatewayResponseDeleted.to_json()

# convert the object into a dict
ai_gateway_response_deleted_dict = ai_gateway_response_deleted_instance.to_dict()
# create an instance of AiGatewayResponseDeleted from a dict
ai_gateway_response_deleted_form_dict = ai_gateway_response_deleted.from_dict(ai_gateway_response_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


