# DedicatedServerPresetCpu

Объект, содержащий информацию о процессоре выделенного сервера.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **object** | Описание характеристик процессора выделенного сервера. | 
**description_short** | **object** | Краткое описание характеристик процессора выделенного сервера. | 
**count** | **object** | Количество ядер процессора выделенного сервера. | 

## Example

```python
from openapi_client.models.dedicated_server_preset_cpu import DedicatedServerPresetCpu

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedServerPresetCpu from a JSON string
dedicated_server_preset_cpu_instance = DedicatedServerPresetCpu.from_json(json)
# print the JSON string representation of the object
print DedicatedServerPresetCpu.to_json()

# convert the object into a dict
dedicated_server_preset_cpu_dict = dedicated_server_preset_cpu_instance.to_dict()
# create an instance of DedicatedServerPresetCpu from a dict
dedicated_server_preset_cpu_form_dict = dedicated_server_preset_cpu.from_dict(dedicated_server_preset_cpu_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


