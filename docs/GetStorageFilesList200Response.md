# GetStorageFilesList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openapi_client.models.get_storage_files_list200_response import GetStorageFilesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetStorageFilesList200Response from a JSON string
get_storage_files_list200_response_instance = GetStorageFilesList200Response.from_json(json)
# print the JSON string representation of the object
print GetStorageFilesList200Response.to_json()

# convert the object into a dict
get_storage_files_list200_response_dict = get_storage_files_list200_response_instance.to_dict()
# create an instance of GetStorageFilesList200Response from a dict
get_storage_files_list200_response_form_dict = get_storage_files_list200_response.from_dict(get_storage_files_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


