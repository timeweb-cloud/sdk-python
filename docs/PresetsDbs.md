# PresetsDbs


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор для каждого экземпляра тарифа базы данных. | [optional] 
**description** | **object** | Описание тарифа. | [optional] 
**description_short** | **object** | Краткое описание тарифа. | [optional] 
**cpu** | **object** | Описание процессора тарифа. | [optional] 
**ram** | **object** | Описание ОЗУ тарифа. | [optional] 
**disk** | **object** | Описание диска тарифа. | [optional] 
**type** | **object** | Тип тарифа базы данных | [optional] 
**price** | **object** | Стоимость тарифа базы данных | [optional] 
**location** | **object** | Географическое расположение тарифа. | [optional] 

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


