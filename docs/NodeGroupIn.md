# NodeGroupIn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название группы | 
**preset_id** | **object** | ID тарифа воркер-ноды. Нельзя передавать вместе с &#x60;configuration&#x60;. Локация воркер-нод должна совпадать с локацией кластера | [optional] 
**configuration** | [**NodeGroupInConfiguration**](NodeGroupInConfiguration.md) |  | [optional] 
**node_count** | **object** | Количество нод в группе | 
**labels** | **object** | Лейблы для группы нод | [optional] 
**is_autoscaling** | **object** | Автомасштабирование. Автоматическое увеличение и уменьшение количества нод в группе в зависимости от текущей нагрузки | [optional] 
**min_size** | **object** | Минимальное количество нод. Передавать в связке с параметрами &#x60;is_autoscaling&#x60; и &#x60;max_size&#x60; | [optional] 
**max_size** | **object** | Максимальное количество нод. Передавать в связке с параметрами &#x60;is_autoscaling&#x60; и &#x60;min_size&#x60;. Максимальное количество нод ограничено тарифом кластера | [optional] 

## Example

```python
from timeweb_cloud_api.models.node_group_in import NodeGroupIn

# TODO update the JSON string below
json = "{}"
# create an instance of NodeGroupIn from a JSON string
node_group_in_instance = NodeGroupIn.from_json(json)
# print the JSON string representation of the object
print NodeGroupIn.to_json()

# convert the object into a dict
node_group_in_dict = node_group_in_instance.to_dict()
# create an instance of NodeGroupIn from a dict
node_group_in_form_dict = node_group_in.from_dict(node_group_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


