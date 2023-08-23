# DedicatedServerAdditionalService

Дополнительная услуга для выделенного сервера

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор дополнительной услуги для выделенного сервера. | 
**price** | **object** | Стоимость (в рублях) дополнительной услуги для выделенного сервера. | 
**period** | **object** | Период оплаты. | 
**description** | **object** | Описание дополнительной услуги выделенного сервера. | 
**short_description** | **object** | Краткое описание дополнительной услуги выделенного сервера. | 
**name** | **object** | Уникально имя дополнительной услуги выделенного сервера. | 

## Example

```python
from timeweb_cloud_api.models.dedicated_server_additional_service import DedicatedServerAdditionalService

# TODO update the JSON string below
json = "{}"
# create an instance of DedicatedServerAdditionalService from a JSON string
dedicated_server_additional_service_instance = DedicatedServerAdditionalService.from_json(json)
# print the JSON string representation of the object
print DedicatedServerAdditionalService.to_json()

# convert the object into a dict
dedicated_server_additional_service_dict = dedicated_server_additional_service_instance.to_dict()
# create an instance of DedicatedServerAdditionalService from a dict
dedicated_server_additional_service_form_dict = dedicated_server_additional_service.from_dict(dedicated_server_additional_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


