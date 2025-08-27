# UpdateStorageRequestConfigurator

Параметры конфигурации хранилища.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disk** | **object** | Размер диска в МБ. | [optional] 
**id** | **object** | ID конфигуратора хранилища. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_storage_request_configurator import UpdateStorageRequestConfigurator

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateStorageRequestConfigurator from a JSON string
update_storage_request_configurator_instance = UpdateStorageRequestConfigurator.from_json(json)
# print the JSON string representation of the object
print UpdateStorageRequestConfigurator.to_json()

# convert the object into a dict
update_storage_request_configurator_dict = update_storage_request_configurator_instance.to_dict()
# create an instance of UpdateStorageRequestConfigurator from a dict
update_storage_request_configurator_form_dict = update_storage_request_configurator.from_dict(update_storage_request_configurator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


