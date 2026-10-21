# GetAgentToolTemplatePrices200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_tool_prices** | **object** |  | 
**meta** | [**GetAgentTools200ResponseMeta**](GetAgentTools200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_agent_tool_template_prices200_response import GetAgentToolTemplatePrices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentToolTemplatePrices200Response from a JSON string
get_agent_tool_template_prices200_response_instance = GetAgentToolTemplatePrices200Response.from_json(json)
# print the JSON string representation of the object
print GetAgentToolTemplatePrices200Response.to_json()

# convert the object into a dict
get_agent_tool_template_prices200_response_dict = get_agent_tool_template_prices200_response_instance.to_dict()
# create an instance of GetAgentToolTemplatePrices200Response from a dict
get_agent_tool_template_prices200_response_form_dict = get_agent_tool_template_prices200_response.from_dict(get_agent_tool_template_prices200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


