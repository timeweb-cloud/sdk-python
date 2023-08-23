# TransferStorageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key** | **object** | Идентификатор доступа стороннего S3-хранилища. | 
**secret_key** | **object** | Пароль доступа стороннего S3-хранилища. | 
**location** | **object** | Регион хранилища источника. | 
**is_force_path_style** | **object** | Это логическое значение, которое показывает, следует ли принудительно указывать URL-адреса для объектов S3. | 
**endpoint** | **object** | URL S3-хранилища источника. | 
**bucket_name** | **object** | Имя хранилища источника. | 
**new_bucket_name** | **object** | Имя хранилища получателя. | 

## Example

```python
from timeweb_cloud_api.models.transfer_storage_request import TransferStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TransferStorageRequest from a JSON string
transfer_storage_request_instance = TransferStorageRequest.from_json(json)
# print the JSON string representation of the object
print TransferStorageRequest.to_json()

# convert the object into a dict
transfer_storage_request_dict = transfer_storage_request_instance.to_dict()
# create an instance of TransferStorageRequest from a dict
transfer_storage_request_form_dict = transfer_storage_request.from_dict(transfer_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


