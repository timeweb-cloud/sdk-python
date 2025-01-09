# ImageDownloadResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**download** | [**ImageDownloadAPI**](ImageDownloadAPI.md) |  | 

## Example

```python
from timeweb_cloud_api.models.image_download_response import ImageDownloadResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageDownloadResponse from a JSON string
image_download_response_instance = ImageDownloadResponse.from_json(json)
# print the JSON string representation of the object
print ImageDownloadResponse.to_json()

# convert the object into a dict
image_download_response_dict = image_download_response_instance.to_dict()
# create an instance of ImageDownloadResponse from a dict
image_download_response_form_dict = image_download_response.from_dict(image_download_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


