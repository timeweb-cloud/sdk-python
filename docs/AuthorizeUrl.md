# AuthorizeUrl

Ссылка на авторизацию

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorize_url** | **object** | Ссылка на страницу авторизации провайдера. Откройте её в браузере пользователя | 

## Example

```python
from timeweb_cloud_api.models.authorize_url import AuthorizeUrl

# TODO update the JSON string below
json = "{}"
# create an instance of AuthorizeUrl from a JSON string
authorize_url_instance = AuthorizeUrl.from_json(json)
# print the JSON string representation of the object
print AuthorizeUrl.to_json()

# convert the object into a dict
authorize_url_dict = authorize_url_instance.to_dict()
# create an instance of AuthorizeUrl from a dict
authorize_url_form_dict = authorize_url.from_dict(authorize_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


