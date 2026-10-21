# DocumentStatusInfoDetails

Подробности, набор полей зависит от состояния. Могут присутствовать и другие поля

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**started_at** | **object** | &#x60;indexing&#x60;: время начала индексации | [optional] 
**current_stage** | **object** | &#x60;indexing&#x60;: текущий этап | [optional] 
**progress** | **object** | &#x60;indexing&#x60;: прогресс в процентах | [optional] 
**indexing_duration_ms** | **object** | &#x60;indexed&#x60;: длительность индексации в миллисекундах | [optional] 
**tokens_used** | **object** | &#x60;indexed&#x60;: израсходовано токенов | [optional] 
**tokens_estimated** | **object** | &#x60;indexed&#x60;: оценка количества токенов перед индексацией | [optional] 
**chunks_count** | **object** | &#x60;indexed&#x60;: количество фрагментов, на которые разбит документ | [optional] 
**needed** | **object** | &#x60;INSUFFICIENT_TOKENS&#x60;: сколько токенов нужно | [optional] 
**available** | **object** | &#x60;INSUFFICIENT_TOKENS&#x60;: сколько токенов доступно | [optional] 
**estimated** | **object** | &#x60;INSUFFICIENT_TOKENS&#x60;: оценка без запаса | [optional] 
**balance** | **object** | &#x60;CRITICAL_BALANCE&#x60;, &#x60;NEGATIVE_BALANCE&#x60;: текущий остаток токенов | [optional] 
**min_required** | **object** | &#x60;CRITICAL_BALANCE&#x60;: минимально необходимый остаток | [optional] 

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


