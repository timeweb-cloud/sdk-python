# DedicatedServerPresetDisk

Объект, содержащий информацию о диске выделенного сервера.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **object** | Описание характеристик диска выделенного сервера. | 
**count** | **object** | Количество дисков выделенного сервера. | 
**total_size** | **object** | Общий размер дисков выделенного сервера. | 
**type** | **object** | Тип дисков выделенного сервера. | 

## Example

```python
from timeweb_cloud_api.models.dedicated_server_preset_disk import DedicatedServerPresetDisk

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedServerPresetDisk from a JSON string
dedicated_server_preset_disk_instance = DedicatedServerPresetDisk.from_json(json)
# print the JSON string representation of the object
print DedicatedServerPresetDisk.to_json()

# convert the object into a dict
dedicated_server_preset_disk_dict = dedicated_server_preset_disk_instance.to_dict()
# create an instance of DedicatedServerPresetDisk from a dict
dedicated_server_preset_disk_form_dict = dedicated_server_preset_disk.from_dict(dedicated_server_preset_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


