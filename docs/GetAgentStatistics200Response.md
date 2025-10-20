# GetAgentStatistics200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_statistics** | **object** |  | 
**meta** | [**GetAgentStatistics200ResponseMeta**](GetAgentStatistics200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_agent_statistics200_response import GetAgentStatistics200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentStatistics200Response from a JSON string
get_agent_statistics200_response_instance = GetAgentStatistics200Response.from_json(json)
# print the JSON string representation of the object
print GetAgentStatistics200Response.to_json()

# convert the object into a dict
get_agent_statistics200_response_dict = get_agent_statistics200_response_instance.to_dict()
# create an instance of GetAgentStatistics200Response from a dict
get_agent_statistics200_response_form_dict = get_agent_statistics200_response.from_dict(get_agent_statistics200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


