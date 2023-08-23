# ImageUpdateAPI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя образа | [optional] 
**description** | **object** | Описание образа | [optional] 

## Example

```python
from openapi_client.models.image_update_api import ImageUpdateAPI

# TODO update the JSON string below
json = "{}"
# create an instance of ImageUpdateAPI from a JSON string
image_update_api_instance = ImageUpdateAPI.from_json(json)
# print the JSON string representation of the object
print ImageUpdateAPI.to_json()

# convert the object into a dict
image_update_api_dict = image_update_api_instance.to_dict()
# create an instance of ImageUpdateAPI from a dict
image_update_api_form_dict = image_update_api.from_dict(image_update_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


