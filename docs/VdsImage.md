# VdsImage

Образ сервера.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор образа сервера. | 
**name** | **object** | Название образа сервера. | 
**is_custom** | **object** | Является ли образ кастомным. | 

## Example

```python
from timeweb_cloud_api.models.vds_image import VdsImage

# TODO update the JSON string below
json = "{}"
# create an instance of VdsImage from a JSON string
vds_image_instance = VdsImage.from_json(json)
# print the JSON string representation of the object
print VdsImage.to_json()

# convert the object into a dict
vds_image_dict = vds_image_instance.to_dict()
# create an instance of VdsImage from a dict
vds_image_form_dict = vds_image.from_dict(vds_image_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


