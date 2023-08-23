# S3Object

An object consists of data and its descriptive metadata.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **object** | Название файла или папки. | [optional] 
**last_modified** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была сделана последняя модификация файла или папки. | [optional] 
**etag** | **object** | Тег. | [optional] 
**size** | **object** | Размер (в байтах) файла или папки. | [optional] 
**storage_class** | **object** | Класс хранилища. | [optional] 
**checksum_algorithm** | **object** | Алгоритм | [optional] 
**owner** | [**S3ObjectOwner**](S3ObjectOwner.md) |  | [optional] 
**type** | **object** | Тип (файл или папка). | 

## Example

```python
from timeweb_cloud_api.models.s3_object import S3Object

# TODO update the JSON string below
json = "{}"
# create an instance of S3Object from a JSON string
s3_object_instance = S3Object.from_json(json)
# print the JSON string representation of the object
print S3Object.to_json()

# convert the object into a dict
s3_object_dict = s3_object_instance.to_dict()
# create an instance of S3Object from a dict
s3_object_form_dict = s3_object.from_dict(s3_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


