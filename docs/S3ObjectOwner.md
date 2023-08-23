# S3ObjectOwner

Информация о владельце файла или папки.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Идентификатор владельца файла. | [optional] 
**display_name** | **object** | Имя владельца файла. | [optional] 

## Example

```python
from timeweb_cloud_api.models.s3_object_owner import S3ObjectOwner

# TODO update the JSON string below
json = "{}"
# create an instance of S3ObjectOwner from a JSON string
s3_object_owner_instance = S3ObjectOwner.from_json(json)
# print the JSON string representation of the object
print S3ObjectOwner.to_json()

# convert the object into a dict
s3_object_owner_dict = s3_object_owner_instance.to_dict()
# create an instance of S3ObjectOwner from a dict
s3_object_owner_form_dict = s3_object_owner.from_dict(s3_object_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


