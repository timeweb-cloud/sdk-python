# GetVPCServices200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**services** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.get_vpc_services200_response import GetVPCServices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetVPCServices200Response from a JSON string
get_vpc_services200_response_instance = GetVPCServices200Response.from_json(json)
# print the JSON string representation of the object
print GetVPCServices200Response.to_json()

# convert the object into a dict
get_vpc_services200_response_dict = get_vpc_services200_response_instance.to_dict()
# create an instance of GetVPCServices200Response from a dict
get_vpc_services200_response_form_dict = get_vpc_services200_response.from_dict(get_vpc_services200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


