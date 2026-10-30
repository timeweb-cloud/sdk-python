# CreateAppV2Configuration

Произвольная конфигурация backend-приложения вместо preset_id. Все вложенные поля обязательны. Нельзя передавать вместе с preset_id.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurator_id** | **object** | ID конфигуратора приложения. | 
**disk** | **object** | Размер диска в МБ, положительное число, кратное 1024. | 
**cpu** | **object** | Количество ядер процессора. | 
**ram** | **object** | Объём оперативной памяти в МБ, положительное число, кратное 1024. | 

## Example

```python
from timeweb_cloud_api.models.create_app_v2_configuration import CreateAppV2Configuration

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppV2Configuration from a JSON string
create_app_v2_configuration_instance = CreateAppV2Configuration.from_json(json)
# print the JSON string representation of the object
print CreateAppV2Configuration.to_json()

# convert the object into a dict
create_app_v2_configuration_dict = create_app_v2_configuration_instance.to_dict()
# create an instance of CreateAppV2Configuration from a dict
create_app_v2_configuration_form_dict = create_app_v2_configuration.from_dict(create_app_v2_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


