# CreateStorageRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название хранилища. | 
**description** | **object** | Комментарий к хранилищу. | [optional] 
**type** | **object** | Тип хранилища. | 
**preset_id** | **object** | ID тарифа. Нельзя передавать вместе с &#x60;configurator&#x60;. | [optional] 
**configurator** | [**CreateStorageRequestConfigurator**](CreateStorageRequestConfigurator.md) |  | [optional] 
**project_id** | **object** | ID проекта. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_storage_request import CreateStorageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateStorageRequest from a JSON string
create_storage_request_instance = CreateStorageRequest.from_json(json)
# print the JSON string representation of the object
print CreateStorageRequest.to_json()

# convert the object into a dict
create_storage_request_dict = create_storage_request_instance.to_dict()
# create an instance of CreateStorageRequest from a dict
create_storage_request_form_dict = create_storage_request.from_dict(create_storage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


