# StaticRouteOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID статического маршрута | 
**nexthop** | **object** | IP-адрес следующего узла | 
**subnet** | **object** | Сеть назначения в формате CIDR | 

## Example

```python
from timeweb_cloud_api.models.static_route_out import StaticRouteOut

# TODO update the JSON string below
json = "{}"
# create an instance of StaticRouteOut from a JSON string
static_route_out_instance = StaticRouteOut.from_json(json)
# print the JSON string representation of the object
print StaticRouteOut.to_json()

# convert the object into a dict
static_route_out_dict = static_route_out_instance.to_dict()
# create an instance of StaticRouteOut from a dict
static_route_out_form_dict = static_route_out.from_dict(static_route_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


