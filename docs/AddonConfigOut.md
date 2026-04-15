# AddonConfigOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID конфигурации дополнения | 
**type** | **object** | Тип дополнения | 
**version** | **object** | Версия дополнения | 
**dependencies** | **object** | Зависимости дополнения | 
**yaml_config** | **object** | YAML конфигурации дополнения | 

## Example

```python
from timeweb_cloud_api.models.addon_config_out import AddonConfigOut

# TODO update the JSON string below
json = "{}"
# create an instance of AddonConfigOut from a JSON string
addon_config_out_instance = AddonConfigOut.from_json(json)
# print the JSON string representation of the object
print AddonConfigOut.to_json()

# convert the object into a dict
addon_config_out_dict = addon_config_out_instance.to_dict()
# create an instance of AddonConfigOut from a dict
addon_config_out_form_dict = addon_config_out.from_dict(addon_config_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


