# RenameStorageFileRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_filename** | **object** | Новое название файла или папки. Названия папок должны быть указаны с \&quot;/\&quot; в конце, например: \&quot;dirname/\&quot;. | 
**old_filename** | **object** | Старое название файла или папки. Названия папок должны быть указаны с \&quot;/\&quot; в конце, например: \&quot;dirname/\&quot;. | 

## Example

```python
from timeweb_cloud_api.models.rename_storage_file_request import RenameStorageFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RenameStorageFileRequest from a JSON string
rename_storage_file_request_instance = RenameStorageFileRequest.from_json(json)
# print the JSON string representation of the object
print RenameStorageFileRequest.to_json()

# convert the object into a dict
rename_storage_file_request_dict = rename_storage_file_request_instance.to_dict()
# create an instance of RenameStorageFileRequest from a dict
rename_storage_file_request_form_dict = rename_storage_file_request.from_dict(rename_storage_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


