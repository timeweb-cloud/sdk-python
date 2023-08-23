# MasterPresetOutApi


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор тарифа | 
**description** | **object** | Описание тарифа | 
**description_short** | **object** | Краткое описание тарифа | 
**price** | **object** | Стоимость | 
**cpu** | **object** | Количество ядер ноды | 
**ram** | **object** | Количество памяти ноды | 
**disk** | **object** | Количество пространства на ноде | 
**network** | **object** | Пропускная способность ноды | 
**type** | **object** | Тип тарифа | [optional] 
**limit** | **object** | Ограничение по количеству воркер-нод в кластере | [optional] 

## Example

```python
from timeweb_cloud_api.models.master_preset_out_api import MasterPresetOutApi

# TODO update the JSON string below
json = "{}"
# create an instance of MasterPresetOutApi from a JSON string
master_preset_out_api_instance = MasterPresetOutApi.from_json(json)
# print the JSON string representation of the object
print MasterPresetOutApi.to_json()

# convert the object into a dict
master_preset_out_api_dict = master_preset_out_api_instance.to_dict()
# create an instance of MasterPresetOutApi from a dict
master_preset_out_api_form_dict = master_preset_out_api.from_dict(master_preset_out_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


