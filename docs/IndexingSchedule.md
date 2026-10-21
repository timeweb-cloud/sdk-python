# IndexingSchedule

Расписание автоматической переиндексации документа по ссылке

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **object** | Дни недели, в которые выполняется переиндексация (минимум один) | 
**time** | **object** | Время запуска в формате &#x60;HH:mm&#x60; (24 часа) | 

## Example

```python
from timeweb_cloud_api.models.indexing_schedule import IndexingSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of IndexingSchedule from a JSON string
indexing_schedule_instance = IndexingSchedule.from_json(json)
# print the JSON string representation of the object
print IndexingSchedule.to_json()

# convert the object into a dict
indexing_schedule_dict = indexing_schedule_instance.to_dict()
# create an instance of IndexingSchedule from a dict
indexing_schedule_form_dict = indexing_schedule.from_dict(indexing_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


