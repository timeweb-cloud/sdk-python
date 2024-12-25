# UpdateNetworkDrive


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название сетевого диска. | [optional] 
**comment** | **object** | Комментарий | [optional] 
**size** | **object** | Размер диска в Гб | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_network_drive import UpdateNetworkDrive

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNetworkDrive from a JSON string
update_network_drive_instance = UpdateNetworkDrive.from_json(json)
# print the JSON string representation of the object
print UpdateNetworkDrive.to_json()

# convert the object into a dict
update_network_drive_dict = update_network_drive_instance.to_dict()
# create an instance of UpdateNetworkDrive from a dict
update_network_drive_form_dict = update_network_drive.from_dict(update_network_drive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


