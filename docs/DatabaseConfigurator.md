# DatabaseConfigurator

Конфигуратор кластера базы данных — произвольная конфигурация ресурсов вместо готового тарифа

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID конфигуратора. Передаётся при создании кластера в поле &#x60;configurator_id&#x60;. | 
**disk_type** | **object** | Тип диска. | 
**cpu_frequency** | **object** | Частота процессора (в ГГц). | 
**is_allowed_local_network** | **object** | Есть возможность подключения локальной сети. | 
**location** | **object** | Географическое расположение конфигуратора. | 
**requirements** | [**DatabaseConfiguratorRequirements**](DatabaseConfiguratorRequirements.md) |  | 
**prices** | [**DatabaseConfiguratorPrices**](DatabaseConfiguratorPrices.md) |  | [optional] 
**tags** | **object** | Теги конфигуратора, в том числе тег группы, в пределах которой доступна смена конфигурации кластера. | 

## Example

```python
from timeweb_cloud_api.models.database_configurator import DatabaseConfigurator

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseConfigurator from a JSON string
database_configurator_instance = DatabaseConfigurator.from_json(json)
# print the JSON string representation of the object
print DatabaseConfigurator.to_json()

# convert the object into a dict
database_configurator_dict = database_configurator_instance.to_dict()
# create an instance of DatabaseConfigurator from a dict
database_configurator_form_dict = database_configurator.from_dict(database_configurator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


