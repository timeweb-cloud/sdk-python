# NetworkDriveAvailableResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **object** | Уникальный идентификатор сервиса. | 
**resource_type** | **object** | Тип ресурса. | 
**ip** | **object** | IP-адрес сервиса. | [optional] 
**availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  | 

## Example

```python
from timeweb_cloud_api.models.network_drive_available_resource import NetworkDriveAvailableResource

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDriveAvailableResource from a JSON string
network_drive_available_resource_instance = NetworkDriveAvailableResource.from_json(json)
# print the JSON string representation of the object
print NetworkDriveAvailableResource.to_json()

# convert the object into a dict
network_drive_available_resource_dict = network_drive_available_resource_instance.to_dict()
# create an instance of NetworkDriveAvailableResource from a dict
network_drive_available_resource_form_dict = network_drive_available_resource.from_dict(network_drive_available_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


