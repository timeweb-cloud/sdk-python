# DatabaseClusterMaintenanceSlot

Период технического обслуживания кластера базы данных. Если период не задан, возвращается `any_time`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.database_cluster_maintenance_slot import DatabaseClusterMaintenanceSlot

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseClusterMaintenanceSlot from a JSON string
database_cluster_maintenance_slot_instance = DatabaseClusterMaintenanceSlot.from_json(json)
# print the JSON string representation of the object
print DatabaseClusterMaintenanceSlot.to_json()

# convert the object into a dict
database_cluster_maintenance_slot_dict = database_cluster_maintenance_slot_instance.to_dict()
# create an instance of DatabaseClusterMaintenanceSlot from a dict
database_cluster_maintenance_slot_form_dict = database_cluster_maintenance_slot.from_dict(database_cluster_maintenance_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


