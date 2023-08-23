# UpdateStorageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**preset_id** | **object** | Идентификатор тарифа. | [optional] 
**bucket_type** | **object** | Тип хранилища. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_storage_request import UpdateStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStorageRequest from a JSON string
update_storage_request_instance = UpdateStorageRequest.from_json(json)
# print the JSON string representation of the object
print UpdateStorageRequest.to_json()

# convert the object into a dict
update_storage_request_dict = update_storage_request_instance.to_dict()
# create an instance of UpdateStorageRequest from a dict
update_storage_request_form_dict = update_storage_request.from_dict(update_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


