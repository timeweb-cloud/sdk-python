# CreateClusterMaintenanceSlot

Период технического обслуживания кластера базы данных.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Режим обслуживания. | 
**var_from** | **object** | Начало периода обслуживания в формате &#x60;HH:mmZ&#x60; (UTC). Учитывается только при &#x60;type: fixed_time&#x60;. | [optional] 
**to** | **object** | Конец периода обслуживания в формате &#x60;HH:mmZ&#x60; (UTC). Учитывается только при &#x60;type: fixed_time&#x60;. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_cluster_maintenance_slot import CreateClusterMaintenanceSlot

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterMaintenanceSlot from a JSON string
create_cluster_maintenance_slot_instance = CreateClusterMaintenanceSlot.from_json(json)
# print the JSON string representation of the object
print CreateClusterMaintenanceSlot.to_json()

# convert the object into a dict
create_cluster_maintenance_slot_dict = create_cluster_maintenance_slot_instance.to_dict()
# create an instance of CreateClusterMaintenanceSlot from a dict
create_cluster_maintenance_slot_form_dict = create_cluster_maintenance_slot.from_dict(create_cluster_maintenance_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


