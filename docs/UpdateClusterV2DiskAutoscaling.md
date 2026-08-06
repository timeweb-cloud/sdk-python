# UpdateClusterV2DiskAutoscaling

Настройки автоматического расширения диска.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включить автоматическое расширение диска. | 
**step_size** | **object** | Шаг расширения диска (в Мб). Значение должно быть кратно 5120, минимум — 5120, максимум — 102400. | [optional] 
**threshold_percent** | **object** | Порог заполнения диска (в процентах), при достижении которого диск расширяется. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_cluster_v2_disk_autoscaling import UpdateClusterV2DiskAutoscaling

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterV2DiskAutoscaling from a JSON string
update_cluster_v2_disk_autoscaling_instance = UpdateClusterV2DiskAutoscaling.from_json(json)
# print the JSON string representation of the object
print UpdateClusterV2DiskAutoscaling.to_json()

# convert the object into a dict
update_cluster_v2_disk_autoscaling_dict = update_cluster_v2_disk_autoscaling_instance.to_dict()
# create an instance of UpdateClusterV2DiskAutoscaling from a dict
update_cluster_v2_disk_autoscaling_form_dict = update_cluster_v2_disk_autoscaling.from_dict(update_cluster_v2_disk_autoscaling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


