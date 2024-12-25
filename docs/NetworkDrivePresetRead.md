# NetworkDrivePresetRead


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **object** | Чтение IOPS | [optional] 
**max** | **object** | Чтение IOPS | [optional] 

## Example

```python
from timeweb_cloud_api.models.network_drive_preset_read import NetworkDrivePresetRead

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDrivePresetRead from a JSON string
network_drive_preset_read_instance = NetworkDrivePresetRead.from_json(json)
# print the JSON string representation of the object
print NetworkDrivePresetRead.to_json()

# convert the object into a dict
network_drive_preset_read_dict = network_drive_preset_read_instance.to_dict()
# create an instance of NetworkDrivePresetRead from a dict
network_drive_preset_read_form_dict = network_drive_preset_read.from_dict(network_drive_preset_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


