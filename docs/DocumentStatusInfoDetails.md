# DocumentStatusInfoDetails

Дополнительные детали, зависящие от типа статуса

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_at** | **object** | Время начала индексации | [optional] 
**current_stage** | **object** | Текущий этап индексации | [optional] 
**progress** | **object** | Прогресс в процентах (0-100) | [optional] 

## Example

```python
from timeweb_cloud_api.models.document_status_info_details import DocumentStatusInfoDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentStatusInfoDetails from a JSON string
document_status_info_details_instance = DocumentStatusInfoDetails.from_json(json)
# print the JSON string representation of the object
print DocumentStatusInfoDetails.to_json()

# convert the object into a dict
document_status_info_details_dict = document_status_info_details_instance.to_dict()
# create an instance of DocumentStatusInfoDetails from a dict
document_status_info_details_form_dict = document_status_info_details.from_dict(document_status_info_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


