# UpdateServerConfigurator

Параметры конфигурации сервера. Нельзя передавать вместе с `preset_id`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configurator_id** | **object** | Уникальный идентификатор конфигуратора сервера. | [optional] 
**disk** | **object** | Размер диска в МБ. | [optional] 
**cpu** | **object** | Количество ядер процессора. | [optional] 
**ram** | **object** | Размер ОЗУ сервера в МБ. | [optional] 

## Example

```python
from openapi_client.models.update_server_configurator import UpdateServerConfigurator

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServerConfigurator from a JSON string
update_server_configurator_instance = UpdateServerConfigurator.from_json(json)
# print the JSON string representation of the object
print UpdateServerConfigurator.to_json()

# convert the object into a dict
update_server_configurator_dict = update_server_configurator_instance.to_dict()
# create an instance of UpdateServerConfigurator from a dict
update_server_configurator_form_dict = update_server_configurator.from_dict(update_server_configurator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


