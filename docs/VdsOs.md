# VdsOs

Операционная система сервера.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор операционной системы. | 
**name** | **object** | Тип операционной системы. | 
**version** | **object** | Версия операционной системы. | 

## Example

```python
from timeweb_cloud_api.models.vds_os import VdsOs

# TODO update the JSON string below
json = "{}"
# create an instance of VdsOs from a JSON string
vds_os_instance = VdsOs.from_json(json)
# print the JSON string representation of the object
print VdsOs.to_json()

# convert the object into a dict
vds_os_dict = vds_os_instance.to_dict()
# create an instance of VdsOs from a dict
vds_os_form_dict = vds_os.from_dict(vds_os_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


