# AvailableStaticRoutesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**available_networks** | **object** | Доступные подсети | 
**meta** | [**ComponentsSchemasMeta**](ComponentsSchemasMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.available_static_routes_response import AvailableStaticRoutesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableStaticRoutesResponse from a JSON string
available_static_routes_response_instance = AvailableStaticRoutesResponse.from_json(json)
# print the JSON string representation of the object
print AvailableStaticRoutesResponse.to_json()

# convert the object into a dict
available_static_routes_response_dict = available_static_routes_response_instance.to_dict()
# create an instance of AvailableStaticRoutesResponse from a dict
available_static_routes_response_form_dict = available_static_routes_response.from_dict(available_static_routes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


