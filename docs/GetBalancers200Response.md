# GetBalancers200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**balancers** | **object** |  | 

## Example

```python
from openapi_client.models.get_balancers200_response import GetBalancers200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBalancers200Response from a JSON string
get_balancers200_response_instance = GetBalancers200Response.from_json(json)
# print the JSON string representation of the object
print GetBalancers200Response.to_json()

# convert the object into a dict
get_balancers200_response_dict = get_balancers200_response_instance.to_dict()
# create an instance of GetBalancers200Response from a dict
get_balancers200_response_form_dict = get_balancers200_response.from_dict(get_balancers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


