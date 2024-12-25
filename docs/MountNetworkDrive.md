# MountNetworkDrive


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_type** | **object** | Тип ресурса. | 
**resource_id** | **object** | Id ресурса. | 

## Example

```python
from timeweb_cloud_api.models.mount_network_drive import MountNetworkDrive

# TODO update the JSON string below
json = "{}"
# create an instance of MountNetworkDrive from a JSON string
mount_network_drive_instance = MountNetworkDrive.from_json(json)
# print the JSON string representation of the object
print MountNetworkDrive.to_json()

# convert the object into a dict
mount_network_drive_dict = mount_network_drive_instance.to_dict()
# create an instance of MountNetworkDrive from a dict
mount_network_drive_form_dict = mount_network_drive.from_dict(mount_network_drive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


