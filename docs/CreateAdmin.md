# CreateAdmin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **object** | Имя пользователя базы данных | 
**password** | **object** | Пароль пользователя базы данных | 
**host** | **object** | Хост пользователя | [optional] 
**privileges** | **object** | Список привилегий пользователя базы данных | 
**description** | **object** | Описание пользователя базы данных | [optional] 

## Example

```python
from openapi_client.models.create_admin import CreateAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAdmin from a JSON string
create_admin_instance = CreateAdmin.from_json(json)
# print the JSON string representation of the object
print CreateAdmin.to_json()

# convert the object into a dict
create_admin_dict = create_admin_instance.to_dict()
# create an instance of CreateAdmin from a dict
create_admin_form_dict = create_admin.from_dict(create_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


