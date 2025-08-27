# RegistryIn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя реестра. Должно быть уникальным, от 3 до 48 символов, начинаться и заканчиваться буквой или числом, содержать только латинские буквы в нижнем регистре, цифры и символ «-», без пробелов | 
**description** | **object** | Описание реестра | [optional] 
**preset_id** | **object** | ID тарифа. Нельзя передавать вместе с &#x60;configuration&#x60; | [optional] 
**configuration** | [**RegistryInConfiguration**](RegistryInConfiguration.md) |  | [optional] 
**project_id** | **object** | ID проекта | [optional] 

## Example

```python
from timeweb_cloud_api.models.registry_in import RegistryIn

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryIn from a JSON string
registry_in_instance = RegistryIn.from_json(json)
# print the JSON string representation of the object
print RegistryIn.to_json()

# convert the object into a dict
registry_in_dict = registry_in_instance.to_dict()
# create an instance of RegistryIn from a dict
registry_in_form_dict = registry_in.from_dict(registry_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


