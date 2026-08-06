# CreateClusterBackupSchedule

Расписание резервного копирования кластера базы данных.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_count** | **object** | Количество хранимых резервных копий. | [optional] 
**interval** | **object** | Периодичность создания резервных копий. | [optional] 
**day_of_week** | **object** | День недели (от 1 до 7) для создания резервной копии. Учитывается только при &#x60;interval: week&#x60;. | [optional] 
**day_of_month** | **object** | День месяца (от 1 до 28) для создания резервной копии. Учитывается только при &#x60;interval: month&#x60;. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_cluster_backup_schedule import CreateClusterBackupSchedule

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterBackupSchedule from a JSON string
create_cluster_backup_schedule_instance = CreateClusterBackupSchedule.from_json(json)
# print the JSON string representation of the object
print CreateClusterBackupSchedule.to_json()

# convert the object into a dict
create_cluster_backup_schedule_dict = create_cluster_backup_schedule_instance.to_dict()
# create an instance of CreateClusterBackupSchedule from a dict
create_cluster_backup_schedule_form_dict = create_cluster_backup_schedule.from_dict(create_cluster_backup_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


