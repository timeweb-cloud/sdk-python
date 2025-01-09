# ImageDownloadsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**downloads** | **object** | Массив объектов \&quot;Ссылка на загрузку\&quot; | 

## Example

```python
from timeweb_cloud_api.models.image_downloads_response import ImageDownloadsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageDownloadsResponse from a JSON string
image_downloads_response_instance = ImageDownloadsResponse.from_json(json)
# print the JSON string representation of the object
print ImageDownloadsResponse.to_json()

# convert the object into a dict
image_downloads_response_dict = image_downloads_response_instance.to_dict()
# create an instance of ImageDownloadsResponse from a dict
image_downloads_response_form_dict = image_downloads_response.from_dict(image_downloads_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


