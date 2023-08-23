# UploadSuccessfulResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**upload_successful** | [**UploadSuccessful**](UploadSuccessful.md) |  | 

## Example

```python
from timeweb_cloud_api.models.upload_successful_response import UploadSuccessfulResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSuccessfulResponse from a JSON string
upload_successful_response_instance = UploadSuccessfulResponse.from_json(json)
# print the JSON string representation of the object
print UploadSuccessfulResponse.to_json()

# convert the object into a dict
upload_successful_response_dict = upload_successful_response_instance.to_dict()
# create an instance of UploadSuccessfulResponse from a dict
upload_successful_response_form_dict = upload_successful_response.from_dict(upload_successful_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


