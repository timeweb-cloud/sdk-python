# Statistics

Статистика CDN-ресурса за период, с разбивкой по часам

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traffic** | **object** | Исходящий трафик по часовым интервалам. | 
**requests** | **object** | Количество запросов по часовым интервалам с разбивкой по классам HTTP-статуса ответа. | 

## Example

```python
from timeweb_cloud_api.models.statistics import Statistics

# TODO update the JSON string below
json = "{}"
# create an instance of Statistics from a JSON string
statistics_instance = Statistics.from_json(json)
# print the JSON string representation of the object
print Statistics.to_json()

# convert the object into a dict
statistics_dict = statistics_instance.to_dict()
# create an instance of Statistics from a dict
statistics_form_dict = statistics.from_dict(statistics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


