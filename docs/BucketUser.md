# BucketUser

Пользователь хранилища

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор пользователя. | 
**access_key** | **object** | Логин пользователя. | 
**secret_key** | **object** | Пароль пользователя. | 

## Example

```python
from timeweb_cloud_api.models.bucket_user import BucketUser

# TODO update the JSON string below
json = "{}"
# create an instance of BucketUser from a JSON string
bucket_user_instance = BucketUser.from_json(json)
# print the JSON string representation of the object
print BucketUser.to_json()

# convert the object into a dict
bucket_user_dict = bucket_user_instance.to_dict()
# create an instance of BucketUser from a dict
bucket_user_form_dict = bucket_user.from_dict(bucket_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


