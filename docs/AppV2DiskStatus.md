# AppV2DiskStatus

Состояние диска backend-приложения. До создания сервера поле отсутствует. Для frontend — null.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**used** | **object** | Использованное пространство диска. | [optional] 
**size** | **object** | Размер диска. | [optional] 
**disk_id** | **object** | ID диска. | [optional] 

## Example

```python
from timeweb_cloud_api.models.app_v2_disk_status import AppV2DiskStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AppV2DiskStatus from a JSON string
app_v2_disk_status_instance = AppV2DiskStatus.from_json(json)
# print the JSON string representation of the object
print AppV2DiskStatus.to_json()

# convert the object into a dict
app_v2_disk_status_dict = app_v2_disk_status_instance.to_dict()
# create an instance of AppV2DiskStatus from a dict
app_v2_disk_status_form_dict = app_v2_disk_status.from_dict(app_v2_disk_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


