# ImageUrlIn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**URLType**](URLType.md) |  | [optional] 
**filename** | **object** | Имя файла для загрузки в облачное хранилище | [optional] 
**auth** | [**ImageUrlAuth**](ImageUrlAuth.md) |  | [optional] 

## Example

```python
from openapi_client.models.image_url_in import ImageUrlIn

# TODO update the JSON string below
json = "{}"
# create an instance of ImageUrlIn from a JSON string
image_url_in_instance = ImageUrlIn.from_json(json)
# print the JSON string representation of the object
print ImageUrlIn.to_json()

# convert the object into a dict
image_url_in_dict = image_url_in_instance.to_dict()
# create an instance of ImageUrlIn from a dict
image_url_in_form_dict = image_url_in.from_dict(image_url_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


