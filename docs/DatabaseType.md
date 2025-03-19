# DatabaseType

Тип кластера базы данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название кластера базы данных. | 
**version** | **object** | Версия кластера базы данных. | 
**type** | **object** | Тип кластера базы данных. Передается при создании кластера в поле &#x60;type&#x60; | 
**is_available_replication** | **object** | Поддерживает ли база данных репликацию. | 
**is_deprecated** | **object** | Устарела ли версия базы. | 
**requirements** | [**DatabaseTypeRequirements**](DatabaseTypeRequirements.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.database_type import DatabaseType

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseType from a JSON string
database_type_instance = DatabaseType.from_json(json)
# print the JSON string representation of the object
print DatabaseType.to_json()

# convert the object into a dict
database_type_dict = database_type_instance.to_dict()
# create an instance of DatabaseType from a dict
database_type_form_dict = database_type.from_dict(database_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


