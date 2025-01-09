# AppDiskStatus

Объект с конфигурацией диска. Определен для приложений `type: backend`.Для приложений `type: frontend` всегда null.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **object** | Использованное пространство диска. | [optional] 
**size** | **object** | Размер диска. | [optional] 
**disk_id** | **object** | ID диска. | [optional] 

## Example

```python
from timeweb_cloud_api.models.app_disk_status import AppDiskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AppDiskStatus from a JSON string
app_disk_status_instance = AppDiskStatus.from_json(json)
# print the JSON string representation of the object
print AppDiskStatus.to_json()

# convert the object into a dict
app_disk_status_dict = app_disk_status_instance.to_dict()
# create an instance of AppDiskStatus from a dict
app_disk_status_form_dict = app_disk_status.from_dict(app_disk_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


