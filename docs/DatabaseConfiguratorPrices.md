# DatabaseConfiguratorPrices

Стоимость единицы каждого ресурса. Объект возвращается только для конфигураторов с поресурсной тарификацией.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **object** | Стоимость одного ядра процессора. | 
**ram** | **object** | Стоимость одной единицы оперативной памяти. | 
**disk** | **object** | Стоимость одной единицы дискового пространства. | 
**bandwidth** | **object** | Стоимость одной единицы пропускной способности интернет-канала. | 

## Example

```python
from timeweb_cloud_api.models.database_configurator_prices import DatabaseConfiguratorPrices

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseConfiguratorPrices from a JSON string
database_configurator_prices_instance = DatabaseConfiguratorPrices.from_json(json)
# print the JSON string representation of the object
print DatabaseConfiguratorPrices.to_json()

# convert the object into a dict
database_configurator_prices_dict = database_configurator_prices_instance.to_dict()
# create an instance of DatabaseConfiguratorPrices from a dict
database_configurator_prices_form_dict = database_configurator_prices.from_dict(database_configurator_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


