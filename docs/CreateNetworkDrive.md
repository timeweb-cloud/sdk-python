# CreateNetworkDrive


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название сетевого диска. | 
**comment** | **object** | Комментарий | [optional] 
**size** | **object** | Размер диска в Гб | 
**preset_id** | **object** | Идентификатор сетевого диска. | 

## Example

```python
from timeweb_cloud_api.models.create_network_drive import CreateNetworkDrive

# TODO update the JSON string below
json = "{}"
# create an instance of CreateNetworkDrive from a JSON string
create_network_drive_instance = CreateNetworkDrive.from_json(json)
# print the JSON string representation of the object
print CreateNetworkDrive.to_json()

# convert the object into a dict
create_network_drive_dict = create_network_drive_instance.to_dict()
# create an instance of CreateNetworkDrive from a dict
create_network_drive_form_dict = create_network_drive.from_dict(create_network_drive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


