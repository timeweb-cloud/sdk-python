# CreateServerConfiguration

Параметры конфигурации сервера. Нельзя передавать вместе с `preset_id`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurator_id** | **object** | Уникальный идентификатор конфигуратора сервера. | 
**disk** | **object** | Размер диска в МБ. | 
**cpu** | **object** | Количество ядер процессора. | 
**ram** | **object** | Размер ОЗУ сервера в МБ. | 

## Example

```python
from timeweb_cloud_api.models.create_server_configuration import CreateServerConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServerConfiguration from a JSON string
create_server_configuration_instance = CreateServerConfiguration.from_json(json)
# print the JSON string representation of the object
print CreateServerConfiguration.to_json()

# convert the object into a dict
create_server_configuration_dict = create_server_configuration_instance.to_dict()
# create an instance of CreateServerConfiguration from a dict
create_server_configuration_form_dict = create_server_configuration.from_dict(create_server_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


