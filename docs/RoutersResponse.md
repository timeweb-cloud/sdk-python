# RoutersResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**routers** | **object** | Роутеры | 
**meta** | [**ComponentsSchemasMeta**](ComponentsSchemasMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.routers_response import RoutersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutersResponse from a JSON string
routers_response_instance = RoutersResponse.from_json(json)
# print the JSON string representation of the object
print RoutersResponse.to_json()

# convert the object into a dict
routers_response_dict = routers_response_instance.to_dict()
# create an instance of RoutersResponse from a dict
routers_response_form_dict = routers_response.from_dict(routers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


