# AiGatewayFileDeleted

Результат удаления файла

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID удалённого файла | [optional] 
**object** | **object** | Тип объекта | [optional] 
**deleted** | **object** | Файл удалён | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_file_deleted import AiGatewayFileDeleted

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayFileDeleted from a JSON string
ai_gateway_file_deleted_instance = AiGatewayFileDeleted.from_json(json)
# print the JSON string representation of the object
print AiGatewayFileDeleted.to_json()

# convert the object into a dict
ai_gateway_file_deleted_dict = ai_gateway_file_deleted_instance.to_dict()
# create an instance of AiGatewayFileDeleted from a dict
ai_gateway_file_deleted_form_dict = ai_gateway_file_deleted.from_dict(ai_gateway_file_deleted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


