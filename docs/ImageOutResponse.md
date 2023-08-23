# ImageOutResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**image** | [**ImageOutAPI**](ImageOutAPI.md) |  | 

## Example

```python
from timeweb_cloud_api.models.image_out_response import ImageOutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageOutResponse from a JSON string
image_out_response_instance = ImageOutResponse.from_json(json)
# print the JSON string representation of the object
print ImageOutResponse.to_json()

# convert the object into a dict
image_out_response_dict = image_out_response_instance.to_dict()
# create an instance of ImageOutResponse from a dict
image_out_response_form_dict = image_out_response.from_dict(image_out_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


