# AiKeyCallsStatisticPoint

Количество запросов ключа за интервал

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **object** | Начало интервала | 
**call_count** | **object** | Количество запросов за интервал | 

## Example

```python
from timeweb_cloud_api.models.ai_key_calls_statistic_point import AiKeyCallsStatisticPoint

# TODO update the JSON string below
json = "{}"
# create an instance of AiKeyCallsStatisticPoint from a JSON string
ai_key_calls_statistic_point_instance = AiKeyCallsStatisticPoint.from_json(json)
# print the JSON string representation of the object
print AiKeyCallsStatisticPoint.to_json()

# convert the object into a dict
ai_key_calls_statistic_point_dict = ai_key_calls_statistic_point_instance.to_dict()
# create an instance of AiKeyCallsStatisticPoint from a dict
ai_key_calls_statistic_point_form_dict = ai_key_calls_statistic_point.from_dict(ai_key_calls_statistic_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


