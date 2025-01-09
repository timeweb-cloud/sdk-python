# PresetsBalancer


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID для каждого экземпляра тарифа базы данных. | 
**description** | **object** | Описание тарифа. | 
**description_short** | **object** | Краткое описание тарифа. | 
**bandwidth** | **object** | Пропускная способность тарифа. | 
**replica_count** | **object** | Количество реплик. | 
**request_per_second** | **object** | Запросов в секунду. | 
**price** | **object** | Стоимость тарифа базы данных. | 
**location** | **object** | Географическое расположение тарифа. | 

## Example

```python
from timeweb_cloud_api.models.presets_balancer import PresetsBalancer

# TODO update the JSON string below
json = "{}"
# create an instance of PresetsBalancer from a JSON string
presets_balancer_instance = PresetsBalancer.from_json(json)
# print the JSON string representation of the object
print PresetsBalancer.to_json()

# convert the object into a dict
presets_balancer_dict = presets_balancer_instance.to_dict()
# create an instance of PresetsBalancer from a dict
presets_balancer_form_dict = presets_balancer.from_dict(presets_balancer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


