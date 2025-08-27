# ClusterInMaintenanceSlot

Окно обслуживания кластера

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | В любое время или в заданное время. При значении &#x60;fixed_time&#x60; поля &#x60;from&#x60; и &#x60;to&#x60; являются обязательными. Минимально допустимый временной интервал — 3 часа. Время задается в часовом поясе UTC. | 
**var_from** | **object** | Интервал времени с. Время должно быть в формате HH:MM (24 часа) | [optional] 
**to** | **object** | Интервал времени до. Время должно быть в формате HH:MM (24 часа) | [optional] 

## Example

```python
from timeweb_cloud_api.models.cluster_in_maintenance_slot import ClusterInMaintenanceSlot

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInMaintenanceSlot from a JSON string
cluster_in_maintenance_slot_instance = ClusterInMaintenanceSlot.from_json(json)
# print the JSON string representation of the object
print ClusterInMaintenanceSlot.to_json()

# convert the object into a dict
cluster_in_maintenance_slot_dict = cluster_in_maintenance_slot_instance.to_dict()
# create an instance of ClusterInMaintenanceSlot from a dict
cluster_in_maintenance_slot_form_dict = cluster_in_maintenance_slot.from_dict(cluster_in_maintenance_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


