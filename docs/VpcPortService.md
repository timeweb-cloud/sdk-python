# VpcPortService

Сервис, к которому привязан порт.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Идентификатор сервиса. | 
**type** | **object** | Тип сервиса. | 
**name** | **object** | Название сервиса. | 

## Example

```python
from timeweb_cloud_api.models.vpc_port_service import VpcPortService

# TODO update the JSON string below
json = "{}"
# create an instance of VpcPortService from a JSON string
vpc_port_service_instance = VpcPortService.from_json(json)
# print the JSON string representation of the object
print VpcPortService.to_json()

# convert the object into a dict
vpc_port_service_dict = vpc_port_service_instance.to_dict()
# create an instance of VpcPortService from a dict
vpc_port_service_form_dict = vpc_port_service.from_dict(vpc_port_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


