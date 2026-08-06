# CreateClusterDiskAutoscaling

Настройки автоматического расширения диска.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включить автоматическое расширение диска. | 
**step_size** | **object** | Шаг расширения диска (в Мб). | [optional] 
**threshold_percent** | **object** | Порог заполнения диска (в процентах), при достижении которого диск расширяется. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_cluster_disk_autoscaling import CreateClusterDiskAutoscaling

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterDiskAutoscaling from a JSON string
create_cluster_disk_autoscaling_instance = CreateClusterDiskAutoscaling.from_json(json)
# print the JSON string representation of the object
print CreateClusterDiskAutoscaling.to_json()

# convert the object into a dict
create_cluster_disk_autoscaling_dict = create_cluster_disk_autoscaling_instance.to_dict()
# create an instance of CreateClusterDiskAutoscaling from a dict
create_cluster_disk_autoscaling_form_dict = create_cluster_disk_autoscaling.from_dict(create_cluster_disk_autoscaling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


