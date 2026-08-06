# UpdateClusterConfiguration

Конфигуратор кластера базы данных. Нельзя передавать вместе с `preset_id`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurator_id** | **object** | ID конфигуратора | 
**disk** | **object** | Размер диска (в Мб). Значение должно быть кратно 1024 | 
**cpu** | **object** | Количество ядер процессора | 
**ram** | **object** | Объем оперативной памяти (в Мб). Значение должно быть кратно 1024 | 

## Example

```python
from timeweb_cloud_api.models.update_cluster_configuration import UpdateClusterConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterConfiguration from a JSON string
update_cluster_configuration_instance = UpdateClusterConfiguration.from_json(json)
# print the JSON string representation of the object
print UpdateClusterConfiguration.to_json()

# convert the object into a dict
update_cluster_configuration_dict = update_cluster_configuration_instance.to_dict()
# create an instance of UpdateClusterConfiguration from a dict
update_cluster_configuration_form_dict = update_cluster_configuration.from_dict(update_cluster_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


