# CreateStorageRequestConfigurator

Параметры конфигурации хранилища. Нельзя передавать вместе с `preset_id`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | **object** | Размер диска в МБ.. | [optional] 
**id** | **object** | ID конфигуратора хранилища. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_storage_request_configurator import CreateStorageRequestConfigurator

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStorageRequestConfigurator from a JSON string
create_storage_request_configurator_instance = CreateStorageRequestConfigurator.from_json(json)
# print the JSON string representation of the object
print CreateStorageRequestConfigurator.to_json()

# convert the object into a dict
create_storage_request_configurator_dict = create_storage_request_configurator_instance.to_dict()
# create an instance of CreateStorageRequestConfigurator from a dict
create_storage_request_configurator_form_dict = create_storage_request_configurator.from_dict(create_storage_request_configurator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


