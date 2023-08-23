# CreateDb


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **object** | Логин для подключения к базе данных. | [optional] 
**password** | **object** | Пароль для подключения к базе данных. | 
**name** | **object** | Название базы данных. | 
**type** | **object** | Тип базы данных. | 
**hash_type** | **object** | Тип хеширования базы данных (mysql5 | mysql | postgres). | [optional] 
**preset_id** | **object** | Идентификатор тарифа. | 
**config_parameters** | [**ConfigParameters**](ConfigParameters.md) |  | [optional] 
**network** | [**Network**](Network.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_db import CreateDb

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDb from a JSON string
create_db_instance = CreateDb.from_json(json)
# print the JSON string representation of the object
print CreateDb.to_json()

# convert the object into a dict
create_db_dict = create_db_instance.to_dict()
# create an instance of CreateDb from a dict
create_db_form_dict = create_db.from_dict(create_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


