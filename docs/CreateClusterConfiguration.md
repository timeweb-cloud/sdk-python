# CreateClusterConfiguration

Конфигуратор кластера базы данных. Нельзя передавать вместе с `preset_id`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurator_id** | **object** | ID конфигуратора | 
**disk** | **object** | Размер диска (в Мб) | 
**cpu** | **object** | Количество ядер процессора | 
**ram** | **object** | Объем оперативной памяти (в Мб) | 

## Example

```python
from timeweb_cloud_api.models.create_cluster_configuration import CreateClusterConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterConfiguration from a JSON string
create_cluster_configuration_instance = CreateClusterConfiguration.from_json(json)
# print the JSON string representation of the object
print CreateClusterConfiguration.to_json()

# convert the object into a dict
create_cluster_configuration_dict = create_cluster_configuration_instance.to_dict()
# create an instance of CreateClusterConfiguration from a dict
create_cluster_configuration_form_dict = create_cluster_configuration.from_dict(create_cluster_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


