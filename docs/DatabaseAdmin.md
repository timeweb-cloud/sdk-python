# DatabaseAdmin

Пользователь базы данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID для каждого экземпляра пользователя базы данных. Автоматически генерируется при создании. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была создана база данных. | 
**login** | **object** | Имя пользователя базы данных | 
**password** | **object** | Пароль пользователя базы данных | 
**description** | **object** | Описание пользователя базы данных | 
**host** | **object** | Хост пользователя | 
**instances** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.database_admin import DatabaseAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseAdmin from a JSON string
database_admin_instance = DatabaseAdmin.from_json(json)
# print the JSON string representation of the object
print DatabaseAdmin.to_json()

# convert the object into a dict
database_admin_dict = database_admin_instance.to_dict()
# create an instance of DatabaseAdmin from a dict
database_admin_form_dict = database_admin.from_dict(database_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


