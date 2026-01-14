# GetAgentsTokenPackages200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token_packages** | **object** |  | 
**meta** | [**GetAgentsTokenPackages200ResponseMeta**](GetAgentsTokenPackages200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_agents_token_packages200_response import GetAgentsTokenPackages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentsTokenPackages200Response from a JSON string
get_agents_token_packages200_response_instance = GetAgentsTokenPackages200Response.from_json(json)
# print the JSON string representation of the object
print GetAgentsTokenPackages200Response.to_json()

# convert the object into a dict
get_agents_token_packages200_response_dict = get_agents_token_packages200_response_instance.to_dict()
# create an instance of GetAgentsTokenPackages200Response from a dict
get_agents_token_packages200_response_form_dict = get_agents_token_packages200_response.from_dict(get_agents_token_packages200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


