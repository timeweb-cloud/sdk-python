# ServerDisk

Диск сервера

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор диска. | 
**size** | **object** | Размер диска (в Мб). | 
**used** | **object** | Количество использованной памяти диска (в Мб). | 
**type** | **object** | Тип диска. | 
**is_mounted** | **object** | Является ли диск примонтированным. | 
**is_system** | **object** | Является ли диск системным. | 
**system_name** | **object** | Системное название диска. | 
**status** | **object** | Статус диска. | 

## Example

```python
from timeweb_cloud_api.models.server_disk import ServerDisk

# TODO update the JSON string below
json = "{}"
# create an instance of ServerDisk from a JSON string
server_disk_instance = ServerDisk.from_json(json)
# print the JSON string representation of the object
print ServerDisk.to_json()

# convert the object into a dict
server_disk_dict = server_disk_instance.to_dict()
# create an instance of ServerDisk from a dict
server_disk_form_dict = server_disk.from_dict(server_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


