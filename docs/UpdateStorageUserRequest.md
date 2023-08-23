# UpdateStorageUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret_key** | **object** | Новый пароль пользователя-администратора хранилища. | 

## Example

```python
from timeweb_cloud_api.models.update_storage_user_request import UpdateStorageUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStorageUserRequest from a JSON string
update_storage_user_request_instance = UpdateStorageUserRequest.from_json(json)
# print the JSON string representation of the object
print UpdateStorageUserRequest.to_json()

# convert the object into a dict
update_storage_user_request_dict = update_storage_user_request_instance.to_dict()
# create an instance of UpdateStorageUserRequest from a dict
update_storage_user_request_form_dict = update_storage_user_request.from_dict(update_storage_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


