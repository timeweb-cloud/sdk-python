# AiGatewayFile

Файл

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID файла | [optional] 
**object** | **object** | Тип объекта | [optional] 
**bytes** | **object** | Размер файла в байтах | [optional] 
**created_at** | **object** | Время загрузки, Unix-время в секундах | [optional] 
**filename** | **object** | Имя файла | [optional] 
**purpose** | **object** | Назначение файла | [optional] 
**status** | **object** | Статус обработки файла, например &#x60;uploaded&#x60; или &#x60;processed&#x60; | [optional] 
**expires_at** | **object** | Когда файл будет удалён, Unix-время в секундах. &#x60;null&#x60; — не ограничено | [optional] 

## Example

```python
from timeweb_cloud_api.models.ai_gateway_file import AiGatewayFile

# TODO update the JSON string below
json = "{}"
# create an instance of AiGatewayFile from a JSON string
ai_gateway_file_instance = AiGatewayFile.from_json(json)
# print the JSON string representation of the object
print AiGatewayFile.to_json()

# convert the object into a dict
ai_gateway_file_dict = ai_gateway_file_instance.to_dict()
# create an instance of AiGatewayFile from a dict
ai_gateway_file_form_dict = ai_gateway_file.from_dict(ai_gateway_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


