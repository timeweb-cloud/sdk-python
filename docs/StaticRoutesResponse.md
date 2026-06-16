# StaticRoutesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**static_routes** | **object** | Статические маршруты | 
**meta** | [**ComponentsSchemasMeta**](ComponentsSchemasMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.static_routes_response import StaticRoutesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StaticRoutesResponse from a JSON string
static_routes_response_instance = StaticRoutesResponse.from_json(json)
# print the JSON string representation of the object
print StaticRoutesResponse.to_json()

# convert the object into a dict
static_routes_response_dict = static_routes_response_instance.to_dict()
# create an instance of StaticRoutesResponse from a dict
static_routes_response_form_dict = static_routes_response.from_dict(static_routes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


