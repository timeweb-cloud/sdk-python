# AppV2Configuration

Конфигурация сервера backend-приложения. До создания сервера поле отсутствует. Для frontend — null.

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
from timeweb_cloud_api.models.app_v2_configuration import AppV2Configuration

# TODO update the JSON string below
json = "{}"
# create an instance of AppV2Configuration from a JSON string
app_v2_configuration_instance = AppV2Configuration.from_json(json)
# print the JSON string representation of the object
print AppV2Configuration.to_json()

# convert the object into a dict
app_v2_configuration_dict = app_v2_configuration_instance.to_dict()
# create an instance of AppV2Configuration from a dict
app_v2_configuration_form_dict = app_v2_configuration.from_dict(app_v2_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


