# CreateDocument

Данные для добавления документа по ссылке

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название документа | 
**type** | **object** | Тип документа. Поддерживается только &#x60;link&#x60;; файлы загружайте через &#x60;POST /api/v1/cloud-ai/knowledge-bases/{id}/upload&#x60; | 
**url** | **object** | Публично доступный HTTP(S)-адрес документа | 
**indexing_schedule** | [**IndexingSchedule**](IndexingSchedule.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_document import CreateDocument

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDocument from a JSON string
create_document_instance = CreateDocument.from_json(json)
# print the JSON string representation of the object
print CreateDocument.to_json()

# convert the object into a dict
create_document_dict = create_document_instance.to_dict()
# create an instance of CreateDocument from a dict
create_document_form_dict = create_document.from_dict(create_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


