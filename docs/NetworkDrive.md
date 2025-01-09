# NetworkDrive


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID сетевого диска. | 
**name** | **object** | Название сетевого диска. | 
**comment** | **object** | Комментарий | 
**size** | **object** | Размер диска в Гб | 
**service_list** | **object** | Список сервисов к которым подключен диск. | 
**location** | **object** | Локация сетевого диска. | 
**status** | **object** | Статус сетевого диска. | 
**availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  | 
**type** | **object** | Тип сетевого диска. | 
**preset_id** | **object** | ID тарифа. | 

## Example

```python
from timeweb_cloud_api.models.network_drive import NetworkDrive

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkDrive from a JSON string
network_drive_instance = NetworkDrive.from_json(json)
# print the JSON string representation of the object
print NetworkDrive.to_json()

# convert the object into a dict
network_drive_dict = network_drive_instance.to_dict()
# create an instance of NetworkDrive from a dict
network_drive_form_dict = network_drive.from_dict(network_drive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


