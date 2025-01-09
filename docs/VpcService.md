# VpcService


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID сервисв. | 
**name** | **object** | Имя сервиса. | 
**public_ip** | **object** | Публичный IP-адрес сервиса | [optional] 
**local_ip** | **object** | Приватный IP-адрес сервиса | [optional] 
**type** | **object** | Тип сервиса. | [optional] 

## Example

```python
from timeweb_cloud_api.models.vpc_service import VpcService

# TODO update the JSON string below
json = "{}"
# create an instance of VpcService from a JSON string
vpc_service_instance = VpcService.from_json(json)
# print the JSON string representation of the object
print VpcService.to_json()

# convert the object into a dict
vpc_service_dict = vpc_service_instance.to_dict()
# create an instance of VpcService from a dict
vpc_service_form_dict = vpc_service.from_dict(vpc_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


