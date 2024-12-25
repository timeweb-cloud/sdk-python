# NetworkDrivePreset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор тарифа. | 
**cost_per_gb** | **object** | Стоимость тарифа сетевого диска. | 
**min** | **object** | Минимальный размер диска (в Гб). | 
**max** | **object** | Максимальный размер диска (в Гб). | 
**step** | **object** | Размер шага диска | 
**type** | **object** | Тип сетевого диска. | 
**read** | [**NetworkDrivePresetRead**](NetworkDrivePresetRead.md) |  | 
**write** | [**NetworkDrivePresetWrite**](NetworkDrivePresetWrite.md) |  | 

## Example

```python
from timeweb_cloud_api.models.network_drive_preset import NetworkDrivePreset

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDrivePreset from a JSON string
network_drive_preset_instance = NetworkDrivePreset.from_json(json)
# print the JSON string representation of the object
print NetworkDrivePreset.to_json()

# convert the object into a dict
network_drive_preset_dict = network_drive_preset_instance.to_dict()
# create an instance of NetworkDrivePreset from a dict
network_drive_preset_form_dict = network_drive_preset.from_dict(network_drive_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


