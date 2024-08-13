# AppConfiguration

Объект с конфигурацией сервера. Определен для приложений `type: backend`.Для приложений `type: frontend` всегда null.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **object** | Количество ядер процессора. | [optional] 
**ram** | **object** | Объем оперативной памяти (в МБ). | [optional] 
**network_bandwidth** | **object** | Скорость сетевого канала (в Мбит/с). | [optional] 
**cpu_frequency** | **object** | Частота процессора (в ГГц). | [optional] 
**disk_type** | **object** | Тип диска. | [optional] 

## Example

```python
from timeweb_cloud_api.models.app_configuration import AppConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AppConfiguration from a JSON string
app_configuration_instance = AppConfiguration.from_json(json)
# print the JSON string representation of the object
print AppConfiguration.to_json()

# convert the object into a dict
app_configuration_dict = app_configuration_instance.to_dict()
# create an instance of AppConfiguration from a dict
app_configuration_form_dict = app_configuration.from_dict(app_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


