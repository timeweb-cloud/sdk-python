# Preset

Тариф CDN

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID тарифа. Указывается в поле &#x60;preset_id&#x60; при создании и изменении ресурса. | 
**service_name** | **object** | Название тарифа. | 
**description** | **object** | Описание тарифа. | 
**description_short** | **object** | Краткое описание тарифа. | 
**cost** | **object** | Абонентская плата за тариф в рублях. | 
**traffic_rate_cost** | **object** | Стоимость единицы исходящего трафика по тарифу аккаунта, в рублях. | 
**request_rate_cost** | **object** | Стоимость единицы запросов по тарифу аккаунта, в рублях. | 

## Example

```python
from timeweb_cloud_api.models.preset import Preset

# TODO update the JSON string below
json = "{}"
# create an instance of Preset from a JSON string
preset_instance = Preset.from_json(json)
# print the JSON string representation of the object
print Preset.to_json()

# convert the object into a dict
preset_dict = preset_instance.to_dict()
# create an instance of Preset from a dict
preset_form_dict = preset.from_dict(preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


