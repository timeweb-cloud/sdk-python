# RegistryOutDiskStats

Конфигурация диска

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **object** | Размер диска | 
**used** | **object** | Используемый размер | 

## Example

```python
from timeweb_cloud_api.models.registry_out_disk_stats import RegistryOutDiskStats

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryOutDiskStats from a JSON string
registry_out_disk_stats_instance = RegistryOutDiskStats.from_json(json)
# print the JSON string representation of the object
print RegistryOutDiskStats.to_json()

# convert the object into a dict
registry_out_disk_stats_dict = registry_out_disk_stats_instance.to_dict()
# create an instance of RegistryOutDiskStats from a dict
registry_out_disk_stats_form_dict = registry_out_disk_stats.from_dict(registry_out_disk_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


