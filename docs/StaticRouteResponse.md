# StaticRouteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**static_route** | [**StaticRouteOut**](StaticRouteOut.md) |  | 

## Example

```python
from timeweb_cloud_api.models.static_route_response import StaticRouteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StaticRouteResponse from a JSON string
static_route_response_instance = StaticRouteResponse.from_json(json)
# print the JSON string representation of the object
print StaticRouteResponse.to_json()

# convert the object into a dict
static_route_response_dict = static_route_response_instance.to_dict()
# create an instance of StaticRouteResponse from a dict
static_route_response_form_dict = static_route_response.from_dict(static_route_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


