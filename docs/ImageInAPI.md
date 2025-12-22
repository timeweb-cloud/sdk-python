# ImageInAPI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя образа. | [optional] 
**description** | **object** | Описание образа. | [optional] 
**disk_id** | **object** | ID диска, для которого создается образ. | [optional] 
**upload_url** | **object** | Ссылка для загрузки образа. | [optional] 
**location** | [**Location**](Location.md) |  | 
**os** | [**OS**](OS.md) |  | 

## Example

```python
from timeweb_cloud_api.models.image_in_api import ImageInAPI

# TODO update the JSON string below
json = "{}"
# create an instance of ImageInAPI from a JSON string
image_in_api_instance = ImageInAPI.from_json(json)
# print the JSON string representation of the object
print ImageInAPI.to_json()

# convert the object into a dict
image_in_api_dict = image_in_api_instance.to_dict()
# create an instance of ImageInAPI from a dict
image_in_api_form_dict = image_in_api.from_dict(image_in_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


