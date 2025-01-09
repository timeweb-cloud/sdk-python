# ServersConfiguratorRequirements


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_min** | **object** | Минимальное количество ядер процессора. | 
**cpu_step** | **object** | Размер шага ядер процессора. | 
**cpu_max** | **object** | Максимальное количество ядер процессора. | 
**ram_min** | **object** | Минимальное количество оперативной памяти (в Мб). | 
**ram_step** | **object** | Размер шага оперативной памяти. | 
**ram_max** | **object** | Максимальное количество оперативной памяти (в Мб). | 
**disk_min** | **object** | Минимальный размер диска (в Мб). | 
**disk_step** | **object** | Размер шага диска | 
**disk_max** | **object** | Максимальный размер диска (в Мб). | 
**network_bandwidth_min** | **object** | Минимальныая пропускная способноть интернет-канала (в Мб) | 
**network_bandwidth_step** | **object** | Размер шага пропускной способноти интернет-канала (в Мб) | 
**network_bandwidth_max** | **object** | Максимальная пропускная способноть интернет-канала (в Мб) | 
**gpu_min** | **object** | Минимальное количество видеокарт | 
**gpu_max** | **object** | Максимальное количество видеокарт | 
**gpu_step** | **object** | Размер шага видеокарт | 

## Example

```python
from timeweb_cloud_api.models.servers_configurator_requirements import ServersConfiguratorRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of ServersConfiguratorRequirements from a JSON string
servers_configurator_requirements_instance = ServersConfiguratorRequirements.from_json(json)
# print the JSON string representation of the object
print ServersConfiguratorRequirements.to_json()

# convert the object into a dict
servers_configurator_requirements_dict = servers_configurator_requirements_instance.to_dict()
# create an instance of ServersConfiguratorRequirements from a dict
servers_configurator_requirements_form_dict = servers_configurator_requirements.from_dict(servers_configurator_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


