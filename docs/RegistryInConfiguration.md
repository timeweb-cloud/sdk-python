# RegistryInConfiguration

Параметры конфигурации. Нельзя передавать вместе с `preset_id`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID конфигуратора | 
**disk** | **object** | Размер диска в ГБ | 

## Example

```python
from timeweb_cloud_api.models.registry_in_configuration import RegistryInConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryInConfiguration from a JSON string
registry_in_configuration_instance = RegistryInConfiguration.from_json(json)
# print the JSON string representation of the object
print RegistryInConfiguration.to_json()

# convert the object into a dict
registry_in_configuration_dict = registry_in_configuration_instance.to_dict()
# create an instance of RegistryInConfiguration from a dict
registry_in_configuration_form_dict = registry_in_configuration.from_dict(registry_in_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


