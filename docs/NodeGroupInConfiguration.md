# NodeGroupInConfiguration

Параметры конфигурации воркер-ноды. Нельзя передавать вместе с `preset_id`. Локация воркер-нод должна совпадать с локацией кластера

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurator_id** | **object** | ID конфигуратора кластера | 
**disk** | **object** | Размер диска в МБ | 
**cpu** | **object** | Количество ядер процессора | 
**ram** | **object** | Размер ОЗУ сервера в МБ | 
**gpu** | **object** | Количество видеокарт | [optional] 

## Example

```python
from timeweb_cloud_api.models.node_group_in_configuration import NodeGroupInConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of NodeGroupInConfiguration from a JSON string
node_group_in_configuration_instance = NodeGroupInConfiguration.from_json(json)
# print the JSON string representation of the object
print NodeGroupInConfiguration.to_json()

# convert the object into a dict
node_group_in_configuration_dict = node_group_in_configuration_instance.to_dict()
# create an instance of NodeGroupInConfiguration from a dict
node_group_in_configuration_form_dict = node_group_in_configuration.from_dict(node_group_in_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


