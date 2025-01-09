# ServersPreset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID тарифа сервера. | 
**location** | **object** | Локация сервера. | 
**price** | **object** | Стоимость в рублях. | 
**cpu** | **object** | Количество ядер процессора. | 
**cpu_frequency** | **object** | Частота процессора. | 
**ram** | **object** | Количество (в Мб) оперативной памяти. | 
**disk** | **object** | Размер диска (в Мб). | 
**disk_type** | **object** | Тип диска. | 
**bandwidth** | **object** | Пропускная способность тарифа. | 
**description** | **object** | Описание тарифа. | 
**description_short** | **object** | Короткое описание тарифа. | 
**is_allowed_local_network** | **object** | Есть возможность подключения локальной сети | 
**tags** | **object** | Список тегов тарифа. | 

## Example

```python
from timeweb_cloud_api.models.servers_preset import ServersPreset

# TODO update the JSON string below
json = "{}"
# create an instance of ServersPreset from a JSON string
servers_preset_instance = ServersPreset.from_json(json)
# print the JSON string representation of the object
print ServersPreset.to_json()

# convert the object into a dict
servers_preset_dict = servers_preset_instance.to_dict()
# create an instance of ServersPreset from a dict
servers_preset_form_dict = servers_preset.from_dict(servers_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


