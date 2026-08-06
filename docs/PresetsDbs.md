# PresetsDbs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID для каждого экземпляра тарифа базы данных. | [optional] 
**description** | **object** | Описание тарифа. | [optional] 
**description_short** | **object** | Краткое описание тарифа. | [optional] 
**cpu** | **object** | Количество ядер процессора тарифа. | [optional] 
**cpu_frequency** | **object** | Частота процессора (в ГГц). | [optional] 
**ram** | **object** | Объём оперативной памяти тарифа (в Мб). | [optional] 
**disk** | **object** | Размер диска тарифа (в Мб). | [optional] 
**type** | **object** | Семейство СУБД тарифа. Значение не совпадает с типом кластера, который передаётся в поле &#x60;type&#x60; при создании кластера (&#x60;POST /api/v1/databases&#x60;): там используется версионированный тип, например &#x60;postgres17&#x60;. Тарифы для Valkey возвращаются со значением &#x60;redis&#x60; — отдельного значения &#x60;valkey&#x60; в этом поле не бывает. | [optional] 
**price** | **object** | Стоимость тарифа базы данных | [optional] 
**location** | **object** | Географическое расположение тарифа. | [optional] 
**tags** | **object** | Теги тарифа, в том числе тег группы тарифов, в пределах которой доступна смена тарифа. | [optional] 

## Example

```python
from timeweb_cloud_api.models.presets_dbs import PresetsDbs

# TODO update the JSON string below
json = "{}"
# create an instance of PresetsDbs from a JSON string
presets_dbs_instance = PresetsDbs.from_json(json)
# print the JSON string representation of the object
print PresetsDbs.to_json()

# convert the object into a dict
presets_dbs_dict = presets_dbs_instance.to_dict()
# create an instance of PresetsDbs from a dict
presets_dbs_form_dict = presets_dbs.from_dict(presets_dbs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


