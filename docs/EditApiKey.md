# EditApiKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя, установленное для токена. | [optional] 
**is_able_to_delete** | **object** | Это логическое значение, которое показывает, можно ли удалять управляемые сервисы при помощи данного токена без подтверждения через Телеграм, когда это подтверждение включено. | [optional] 

## Example

```python
from openapi_client.models.edit_api_key import EditApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of EditApiKey from a JSON string
edit_api_key_instance = EditApiKey.from_json(json)
# print the JSON string representation of the object
print EditApiKey.to_json()

# convert the object into a dict
edit_api_key_dict = edit_api_key_instance.to_dict()
# create an instance of EditApiKey from a dict
edit_api_key_form_dict = edit_api_key.from_dict(edit_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


