# Document

Документ в базе знаний

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор документа | 
**name** | **object** | Название документа | 
**size** | **object** | Размер документа в байтах | 
**status** | **object** | Статус индексации документа | 
**indexing_version** | **object** | Версия индексации | [optional] 
**status_info** | [**DocumentStatusInfo**](DocumentStatusInfo.md) |  | [optional] 
**created_at** | **object** | Дата создания документа | 
**updated_at** | **object** | Дата обновления документа | 

## Example

```python
from timeweb_cloud_api.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print Document.to_json()

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_form_dict = document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


