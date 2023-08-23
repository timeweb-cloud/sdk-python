# UpdateDb

Дополнительные параметры конфигурации базы данных.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **object** | Пароль для подключения к базе данных. | [optional] 
**name** | **object** | Название базы данных. | [optional] 
**preset_id** | **object** | Идентификатор тарифа. | [optional] 
**config_parameters** | [**ConfigParameters**](ConfigParameters.md) |  | [optional] 
**is_external_ip** | **object** | Использовать или нет внешний ip. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_db import UpdateDb

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDb from a JSON string
update_db_instance = UpdateDb.from_json(json)
# print the JSON string representation of the object
print UpdateDb.to_json()

# convert the object into a dict
update_db_dict = update_db_instance.to_dict()
# create an instance of UpdateDb from a dict
update_db_form_dict = update_db.from_dict(update_db_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


