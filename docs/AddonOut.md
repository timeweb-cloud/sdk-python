# AddonOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID дополнения | 
**type** | **object** | Тип дополнения | 
**status** | **object** | Статус дополнения | 
**created_at** | **object** | Дата и время создания дополнения в формате ISO8601 | 
**version** | **object** | Версия дополнения | 
**config** | **object** | Дополнительная конфигурация дополнения | [optional] 
**yaml_config** | **object** | Yaml конфигурация дополнения | 
**config_type** | **object** | Тип конфигурации дополнения | 

## Example

```python
from timeweb_cloud_api.models.addon_out import AddonOut

# TODO update the JSON string below
json = "{}"
# create an instance of AddonOut from a JSON string
addon_out_instance = AddonOut.from_json(json)
# print the JSON string representation of the object
print AddonOut.to_json()

# convert the object into a dict
addon_out_dict = addon_out_instance.to_dict()
# create an instance of AddonOut from a dict
addon_out_form_dict = addon_out.from_dict(addon_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


