# ImageUrlAuth


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **object** | Токен доступа к API облачного хранилища | 
**refresh_token** | **object** | Токен обновления доступов к API | [optional] 
**expiry** | **object** | Время истечения работы токена доступа | [optional] 
**token_type** | **object** | Тип токена доступа | [optional] 

## Example

```python
from timeweb_cloud_api.models.image_url_auth import ImageUrlAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ImageUrlAuth from a JSON string
image_url_auth_instance = ImageUrlAuth.from_json(json)
# print the JSON string representation of the object
print ImageUrlAuth.to_json()

# convert the object into a dict
image_url_auth_dict = image_url_auth_instance.to_dict()
# create an instance of ImageUrlAuth from a dict
image_url_auth_form_dict = image_url_auth.from_dict(image_url_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


