# TrafficUsage

Потребление ресурса с начала текущего расчетного месяца. Счетчики обнуляются в начале каждого расчетного периода.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requests** | **object** | Количество запросов к ресурсу с начала расчетного месяца. | 
**outgoing_traffic** | **object** | Исходящий трафик ресурса с начала расчетного месяца, в байтах. | 
**cache_ratio** | **object** | Доля запросов, отданных из кэша, в процентах. | 

## Example

```python
from timeweb_cloud_api.models.traffic_usage import TrafficUsage

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficUsage from a JSON string
traffic_usage_instance = TrafficUsage.from_json(json)
# print the JSON string representation of the object
print TrafficUsage.to_json()

# convert the object into a dict
traffic_usage_dict = traffic_usage_instance.to_dict()
# create an instance of TrafficUsage from a dict
traffic_usage_form_dict = traffic_usage.from_dict(traffic_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


