# ServersConfigurator


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор конфигуратора сервера. | 
**location** | **object** | Локация сервера. | 
**disk_type** | **object** | Тип диска. | 
**is_allowed_local_network** | **object** | Есть возможность подключения локальной сети | 
**cpu_frequency** | **object** | Частота процессора. | 
**requirements** | [**ServersConfiguratorRequirements**](ServersConfiguratorRequirements.md) |  | 

## Example

```python
from openapi_client.models.servers_configurator import ServersConfigurator

# TODO update the JSON string below
json = "{}"
# create an instance of ServersConfigurator from a JSON string
servers_configurator_instance = ServersConfigurator.from_json(json)
# print the JSON string representation of the object
print ServersConfigurator.to_json()

# convert the object into a dict
servers_configurator_dict = servers_configurator_instance.to_dict()
# create an instance of ServersConfigurator from a dict
servers_configurator_form_dict = servers_configurator.from_dict(servers_configurator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


