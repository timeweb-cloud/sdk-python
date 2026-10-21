# UploadResult

Результат загрузки файлов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uploaded_files** | **object** | ID созданных документов | 
**documents** | **object** | Созданные документы | 

## Example

```python
from timeweb_cloud_api.models.upload_result import UploadResult

# TODO update the JSON string below
json = "{}"
# create an instance of UploadResult from a JSON string
upload_result_instance = UploadResult.from_json(json)
# print the JSON string representation of the object
print UploadResult.to_json()

# convert the object into a dict
upload_result_dict = upload_result_instance.to_dict()
# create an instance of UploadResult from a dict
upload_result_form_dict = upload_result.from_dict(upload_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


