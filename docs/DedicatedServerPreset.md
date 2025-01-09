# DedicatedServerPreset

Выделенный сервер

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID тарифа выделенного сервера. | 
**description** | **object** | Описание характеристик тарифа выделенного сервера. | 
**is_ipmi_enabled** | **object** | Это логическое значение, которое показывает, доступен ли IPMI у данного тарифа. | 
**is_pre_installed** | **object** | Это логическое значение, которое показывает, готов ли выделенный сервер к моментальной выдаче. | 
**cpu** | [**DedicatedServerPresetCpu**](DedicatedServerPresetCpu.md) |  | 
**disk** | [**DedicatedServerPresetDisk**](DedicatedServerPresetDisk.md) |  | 
**price** | **object** | Стоимость тарифа выделенного сервера | [optional] 
**memory** | [**DedicatedServerPresetMemory**](DedicatedServerPresetMemory.md) |  | 
**location** | **object** | Локация. | 

## Example

```python
from timeweb_cloud_api.models.dedicated_server_preset import DedicatedServerPreset

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedServerPreset from a JSON string
dedicated_server_preset_instance = DedicatedServerPreset.from_json(json)
# print the JSON string representation of the object
print DedicatedServerPreset.to_json()

# convert the object into a dict
dedicated_server_preset_dict = dedicated_server_preset_instance.to_dict()
# create an instance of DedicatedServerPreset from a dict
dedicated_server_preset_form_dict = dedicated_server_preset.from_dict(dedicated_server_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


