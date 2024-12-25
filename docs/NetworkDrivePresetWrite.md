# NetworkDrivePresetWrite


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **object** | Запись IOPS | [optional] 
**max** | **object** | Запись IOPS | [optional] 

## Example

```python
from timeweb_cloud_api.models.network_drive_preset_write import NetworkDrivePresetWrite

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDrivePresetWrite from a JSON string
network_drive_preset_write_instance = NetworkDrivePresetWrite.from_json(json)
# print the JSON string representation of the object
print NetworkDrivePresetWrite.to_json()

# convert the object into a dict
network_drive_preset_write_dict = network_drive_preset_write_instance.to_dict()
# create an instance of NetworkDrivePresetWrite from a dict
network_drive_preset_write_form_dict = network_drive_preset_write.from_dict(network_drive_preset_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


