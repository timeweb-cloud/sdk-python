# ClusterInConfiguration

Параметры конфигурации мастер-ноды. Нельзя передавать вместе с `preset_id`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurator_id** | **object** | ID конфигуратора мастер-ноды | 
**disk** | **object** | Размер диска в МБ | 
**cpu** | **object** | Количество ядер процессора | 
**ram** | **object** | Размер ОЗУ сервера в МБ | 

## Example

```python
from timeweb_cloud_api.models.cluster_in_configuration import ClusterInConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInConfiguration from a JSON string
cluster_in_configuration_instance = ClusterInConfiguration.from_json(json)
# print the JSON string representation of the object
print ClusterInConfiguration.to_json()

# convert the object into a dict
cluster_in_configuration_dict = cluster_in_configuration_instance.to_dict()
# create an instance of ClusterInConfiguration from a dict
cluster_in_configuration_form_dict = cluster_in_configuration.from_dict(cluster_in_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


