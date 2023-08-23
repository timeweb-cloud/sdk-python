# DedicatedServerPresetMemory

Объект, содержащий информацию об ОЗУ выделенного сервера.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **object** | Описание характеристик ОЗУ выделенного сервера. | 
**count** | **object** | Количество ОЗУ выделенного сервера. | 
**size** | **object** | Размер (в Мб) ОЗУ выделенного сервера. | 

## Example

```python
from openapi_client.models.dedicated_server_preset_memory import DedicatedServerPresetMemory

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedServerPresetMemory from a JSON string
dedicated_server_preset_memory_instance = DedicatedServerPresetMemory.from_json(json)
# print the JSON string representation of the object
print DedicatedServerPresetMemory.to_json()

# convert the object into a dict
dedicated_server_preset_memory_dict = dedicated_server_preset_memory_instance.to_dict()
# create an instance of DedicatedServerPresetMemory from a dict
dedicated_server_preset_memory_form_dict = dedicated_server_preset_memory.from_dict(dedicated_server_preset_memory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


