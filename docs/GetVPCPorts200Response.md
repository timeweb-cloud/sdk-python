# GetVPCPorts200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**vpc_ports** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.get_vpc_ports200_response import GetVPCPorts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetVPCPorts200Response from a JSON string
get_vpc_ports200_response_instance = GetVPCPorts200Response.from_json(json)
# print the JSON string representation of the object
print GetVPCPorts200Response.to_json()

# convert the object into a dict
get_vpc_ports200_response_dict = get_vpc_ports200_response_instance.to_dict()
# create an instance of GetVPCPorts200Response from a dict
get_vpc_ports200_response_form_dict = get_vpc_ports200_response.from_dict(get_vpc_ports200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


