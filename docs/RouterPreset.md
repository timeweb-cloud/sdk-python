# RouterPreset


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID тарифа | 
**node_count** | **object** | Количество нод | 
**cpu** | **object** | Количество ядер процессора | 
**cpu_frequency** | **object** | Частота процессора | 
**ram** | **object** | Размер ОЗУ в ГБ | 
**bandwidth** | **object** | Пропускная способность | 
**cost** | **object** | Цена в рублях | 
**location** | **object** | Локация | 

## Example

```python
from timeweb_cloud_api.models.router_preset import RouterPreset

# TODO update the JSON string below
json = "{}"
# create an instance of RouterPreset from a JSON string
router_preset_instance = RouterPreset.from_json(json)
# print the JSON string representation of the object
print RouterPreset.to_json()

# convert the object into a dict
router_preset_dict = router_preset_instance.to_dict()
# create an instance of RouterPreset from a dict
router_preset_form_dict = router_preset.from_dict(router_preset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


