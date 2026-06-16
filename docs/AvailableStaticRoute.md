# AvailableStaticRoute


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_name** | **object** | Имя сервиса | 
**service_type** | **object** | Тип сервиса | 
**nexthop** | **object** | IP-адрес следующего узла | 
**subnets** | **object** | Доступные подсети | [optional] 

## Example

```python
from timeweb_cloud_api.models.available_static_route import AvailableStaticRoute

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableStaticRoute from a JSON string
available_static_route_instance = AvailableStaticRoute.from_json(json)
# print the JSON string representation of the object
print AvailableStaticRoute.to_json()

# convert the object into a dict
available_static_route_dict = available_static_route_instance.to_dict()
# create an instance of AvailableStaticRoute from a dict
available_static_route_form_dict = available_static_route.from_dict(available_static_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


