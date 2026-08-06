# DatabaseExtensions

Расширения (плагины) базы данных. Поддерживаются только кластерами PostgreSQL и RabbitMQ.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extension_list** | **object** | Список расширений базы данных. | 
**is_global** | **object** | Установить расширения во всех базах данных кластера (&#x60;true&#x60;) или только в этой базе данных (&#x60;false&#x60;). | 

## Example

```python
from timeweb_cloud_api.models.database_extensions import DatabaseExtensions

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseExtensions from a JSON string
database_extensions_instance = DatabaseExtensions.from_json(json)
# print the JSON string representation of the object
print DatabaseExtensions.to_json()

# convert the object into a dict
database_extensions_dict = database_extensions_instance.to_dict()
# create an instance of DatabaseExtensions from a dict
database_extensions_form_dict = database_extensions.from_dict(database_extensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


