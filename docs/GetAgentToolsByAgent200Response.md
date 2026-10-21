# GetAgentToolsByAgent200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_tools** | **object** |  | 
**meta** | [**GetAgentToolsByAgent200ResponseMeta**](GetAgentToolsByAgent200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_agent_tools_by_agent200_response import GetAgentToolsByAgent200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentToolsByAgent200Response from a JSON string
get_agent_tools_by_agent200_response_instance = GetAgentToolsByAgent200Response.from_json(json)
# print the JSON string representation of the object
print GetAgentToolsByAgent200Response.to_json()

# convert the object into a dict
get_agent_tools_by_agent200_response_dict = get_agent_tools_by_agent200_response_instance.to_dict()
# create an instance of GetAgentToolsByAgent200Response from a dict
get_agent_tools_by_agent200_response_form_dict = get_agent_tools_by_agent200_response.from_dict(get_agent_tools_by_agent200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


