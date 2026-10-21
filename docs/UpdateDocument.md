# UpdateDocument

Данные для изменения документа. Передайте только поля, которые нужно изменить

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Новое название документа | [optional] 
**url** | **object** | Новый HTTP(S)-адрес. Только для документов типа &#x60;link&#x60;; после смены адреса документ переиндексируется | [optional] 
**indexing_schedule** | [**IndexingSchedule**](IndexingSchedule.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_document import UpdateDocument

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDocument from a JSON string
update_document_instance = UpdateDocument.from_json(json)
# print the JSON string representation of the object
print UpdateDocument.to_json()

# convert the object into a dict
update_document_dict = update_document_instance.to_dict()
# create an instance of UpdateDocument from a dict
update_document_form_dict = update_document.from_dict(update_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


