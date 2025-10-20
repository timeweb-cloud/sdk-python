# DocumentStatusInfo

Детальная информация о текущем состоянии документа в базе знаний

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип статуса документа | 
**timestamp** | **object** | Время записи информации (ISO string) | 
**error_code** | **object** | Код ошибки (только для type: &#39;error&#39;) | [optional] 
**details** | [**DocumentStatusInfoDetails**](DocumentStatusInfoDetails.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.document_status_info import DocumentStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentStatusInfo from a JSON string
document_status_info_instance = DocumentStatusInfo.from_json(json)
# print the JSON string representation of the object
print DocumentStatusInfo.to_json()

# convert the object into a dict
document_status_info_dict = document_status_info_instance.to_dict()
# create an instance of DocumentStatusInfo from a dict
document_status_info_form_dict = document_status_info.from_dict(document_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


