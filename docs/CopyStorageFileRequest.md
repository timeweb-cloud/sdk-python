# CopyStorageFileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **object** | Новый путь до файлов. | 
**source** | **object** |  | 

## Example

```python
from openapi_client.models.copy_storage_file_request import CopyStorageFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CopyStorageFileRequest from a JSON string
copy_storage_file_request_instance = CopyStorageFileRequest.from_json(json)
# print the JSON string representation of the object
print CopyStorageFileRequest.to_json()

# convert the object into a dict
copy_storage_file_request_dict = copy_storage_file_request_instance.to_dict()
# create an instance of CopyStorageFileRequest from a dict
copy_storage_file_request_form_dict = copy_storage_file_request.from_dict(copy_storage_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


