# DocumentStatusInfo

Подробности о состоянии индексации документа. `null`, если информации нет

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип состояния, совпадает со статусом документа | 
**timestamp** | **object** | Время, когда записано состояние | 
**error_code** | **object** | Код ошибки, только для &#x60;type: error&#x60;: - &#x60;INSUFFICIENT_TOKENS&#x60; — недостаточно токенов для индексации - &#x60;CRITICAL_BALANCE&#x60; — критически низкий остаток токенов - &#x60;NEGATIVE_BALANCE&#x60; — отрицательный остаток токенов - &#x60;INDEXING_ERROR&#x60; — не удалось обработать документ | [optional] 
**stage** | **object** | Этап индексации, на котором произошла ошибка | [optional] 
**trace_id** | **object** | Идентификатор операции индексации — укажите его при обращении в поддержку | [optional] 
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


