# ConfigAccess

Настройки доступа к ресурсу. Секция доступна только для чтения — изменить ее через API нельзя.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_methods** | **object** | Дополнительные HTTP-методы, разрешенные при обращении к ресурсу. &#x60;null&#x60; — используется набор методов по умолчанию. | [optional] [readonly] 

## Example

```python
from timeweb_cloud_api.models.config_access import ConfigAccess

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigAccess from a JSON string
config_access_instance = ConfigAccess.from_json(json)
# print the JSON string representation of the object
print ConfigAccess.to_json()

# convert the object into a dict
config_access_dict = config_access_instance.to_dict()
# create an instance of ConfigAccess from a dict
config_access_form_dict = config_access.from_dict(config_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


