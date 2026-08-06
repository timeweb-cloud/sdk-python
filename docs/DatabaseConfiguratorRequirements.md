# DatabaseConfiguratorRequirements

Границы и шаг изменения ресурсов конфигуратора.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_min** | **object** | Минимальное количество ядер процессора. | 
**cpu_step** | **object** | Размер шага ядер процессора. | 
**cpu_max** | **object** | Максимальное количество ядер процессора. | 
**ram_min** | **object** | Минимальный объём оперативной памяти (в Мб). | 
**ram_step** | **object** | Размер шага оперативной памяти (в Мб). | 
**ram_max** | **object** | Максимальный объём оперативной памяти (в Мб). | 
**disk_min** | **object** | Минимальный размер диска (в Мб). | 
**disk_step** | **object** | Размер шага диска (в Мб). | 
**disk_max** | **object** | Максимальный размер диска (в Мб). | 
**network_bandwidth_min** | **object** | Минимальная пропускная способность интернет-канала (в Мбит/с). | 
**network_bandwidth_step** | **object** | Размер шага пропускной способности интернет-канала (в Мбит/с). | 
**network_bandwidth_max** | **object** | Максимальная пропускная способность интернет-канала (в Мбит/с). | 

## Example

```python
from timeweb_cloud_api.models.database_configurator_requirements import DatabaseConfiguratorRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseConfiguratorRequirements from a JSON string
database_configurator_requirements_instance = DatabaseConfiguratorRequirements.from_json(json)
# print the JSON string representation of the object
print DatabaseConfiguratorRequirements.to_json()

# convert the object into a dict
database_configurator_requirements_dict = database_configurator_requirements_instance.to_dict()
# create an instance of DatabaseConfiguratorRequirements from a dict
database_configurator_requirements_form_dict = database_configurator_requirements.from_dict(database_configurator_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


