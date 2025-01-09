# PresetsStorage

Тариф

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID для каждого экземпляра тарифа хранилища. | 
**description** | **object** | Описание тарифа. | 
**description_short** | **object** | Краткое описание тарифа. | 
**disk** | **object** | Описание диска хранилища. | 
**price** | **object** | Стоимость тарифа хранилища. | 
**location** | **object** | Географическое расположение тарифа. | 

## Example

```python
from timeweb_cloud_api.models.presets_storage import PresetsStorage

# TODO update the JSON string below
json = "{}"
# create an instance of PresetsStorage from a JSON string
presets_storage_instance = PresetsStorage.from_json(json)
# print the JSON string representation of the object
print PresetsStorage.to_json()

# convert the object into a dict
presets_storage_dict = presets_storage_instance.to_dict()
# create an instance of PresetsStorage from a dict
presets_storage_form_dict = presets_storage.from_dict(presets_storage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


