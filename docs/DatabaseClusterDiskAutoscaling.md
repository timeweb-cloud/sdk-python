# DatabaseClusterDiskAutoscaling

Настройки автоматического расширения диска.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включено ли автоматическое расширение диска. | 
**step_size** | **object** | Шаг расширения диска (в Мб). | 
**threshold_percent** | **object** | Порог заполнения диска (в процентах), при достижении которого диск расширяется. | 

## Example

```python
from timeweb_cloud_api.models.database_cluster_disk_autoscaling import DatabaseClusterDiskAutoscaling

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseClusterDiskAutoscaling from a JSON string
database_cluster_disk_autoscaling_instance = DatabaseClusterDiskAutoscaling.from_json(json)
# print the JSON string representation of the object
print DatabaseClusterDiskAutoscaling.to_json()

# convert the object into a dict
database_cluster_disk_autoscaling_dict = database_cluster_disk_autoscaling_instance.to_dict()
# create an instance of DatabaseClusterDiskAutoscaling from a dict
database_cluster_disk_autoscaling_form_dict = database_cluster_disk_autoscaling.from_dict(database_cluster_disk_autoscaling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


