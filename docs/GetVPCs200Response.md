# GetVPCs200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**vpcs** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.get_vpcs200_response import GetVPCs200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetVPCs200Response from a JSON string
get_vpcs200_response_instance = GetVPCs200Response.from_json(json)
# print the JSON string representation of the object
print GetVPCs200Response.to_json()

# convert the object into a dict
get_vpcs200_response_dict = get_vpcs200_response_instance.to_dict()
# create an instance of GetVPCs200Response from a dict
get_vpcs200_response_form_dict = get_vpcs200_response.from_dict(get_vpcs200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


