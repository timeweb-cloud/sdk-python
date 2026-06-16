# StaticRouteIn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnet** | **object** | Сеть назначения в формате CIDR | 
**nexthop** | **object** | IP-адрес следующего узла (IPv4) | 

## Example

```python
from timeweb_cloud_api.models.static_route_in import StaticRouteIn

# TODO update the JSON string below
json = "{}"
# create an instance of StaticRouteIn from a JSON string
static_route_in_instance = StaticRouteIn.from_json(json)
# print the JSON string representation of the object
print StaticRouteIn.to_json()

# convert the object into a dict
static_route_in_dict = static_route_in_instance.to_dict()
# create an instance of StaticRouteIn from a dict
static_route_in_form_dict = static_route_in.from_dict(static_route_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


