# RegistryEdit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **object** | Новое описание реестра | [optional] 
**preset_id** | **object** | ID тарифа. Нельзя передавать вместе с &#x60;configuration&#x60; | [optional] 
**configuration** | [**RegistryInConfiguration**](RegistryInConfiguration.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.registry_edit import RegistryEdit

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryEdit from a JSON string
registry_edit_instance = RegistryEdit.from_json(json)
# print the JSON string representation of the object
print RegistryEdit.to_json()

# convert the object into a dict
registry_edit_dict = registry_edit_instance.to_dict()
# create an instance of RegistryEdit from a dict
registry_edit_form_dict = registry_edit.from_dict(registry_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


