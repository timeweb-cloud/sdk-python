# RegistryOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID реестра | 
**name** | **object** | Название реестра | 
**description** | **object** | Описание | 
**preset_id** | **object** | ID тарифа | 
**configurator_id** | **object** | ID конфигуратора | 
**project_id** | **object** | ID проекта | 
**created_at** | **object** | Дата и время создания реестра в формате ISO8601 | 
**updated_at** | **object** | Дата и время обновления реестра в формате ISO8601 | 
**disk_stats** | [**RegistryOutDiskStats**](RegistryOutDiskStats.md) |  | 

## Example

```python
from timeweb_cloud_api.models.registry_out import RegistryOut

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryOut from a JSON string
registry_out_instance = RegistryOut.from_json(json)
# print the JSON string representation of the object
print RegistryOut.to_json()

# convert the object into a dict
registry_out_dict = registry_out_instance.to_dict()
# create an instance of RegistryOut from a dict
registry_out_form_dict = registry_out.from_dict(registry_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


