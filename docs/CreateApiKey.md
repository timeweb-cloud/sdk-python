# CreateApiKey


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя, установленное для токена. | 
**expire** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда истекает токен. | [optional] 
**is_able_to_delete** | **object** | Это логическое значение, которое показывает, можно ли удалять управляемые сервисы при помощи данного токена без подтверждения через Телеграм, когда это подтверждение включено. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_api_key import CreateApiKey

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApiKey from a JSON string
create_api_key_instance = CreateApiKey.from_json(json)
# print the JSON string representation of the object
print CreateApiKey.to_json()

# convert the object into a dict
create_api_key_dict = create_api_key_instance.to_dict()
# create an instance of CreateApiKey from a dict
create_api_key_form_dict = create_api_key.from_dict(create_api_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


