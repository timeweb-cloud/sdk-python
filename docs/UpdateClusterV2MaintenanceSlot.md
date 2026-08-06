# UpdateClusterV2MaintenanceSlot

Период технического обслуживания кластера базы данных.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.update_cluster_v2_maintenance_slot import UpdateClusterV2MaintenanceSlot

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterV2MaintenanceSlot from a JSON string
update_cluster_v2_maintenance_slot_instance = UpdateClusterV2MaintenanceSlot.from_json(json)
# print the JSON string representation of the object
print UpdateClusterV2MaintenanceSlot.to_json()

# convert the object into a dict
update_cluster_v2_maintenance_slot_dict = update_cluster_v2_maintenance_slot_instance.to_dict()
# create an instance of UpdateClusterV2MaintenanceSlot from a dict
update_cluster_v2_maintenance_slot_form_dict = update_cluster_v2_maintenance_slot.from_dict(update_cluster_v2_maintenance_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


