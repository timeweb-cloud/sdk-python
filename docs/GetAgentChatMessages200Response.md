# GetAgentChatMessages200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_list_messages** | **object** |  | 
**meta** | [**GetAgentChatMessages200ResponseMeta**](GetAgentChatMessages200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_agent_chat_messages200_response import GetAgentChatMessages200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentChatMessages200Response from a JSON string
get_agent_chat_messages200_response_instance = GetAgentChatMessages200Response.from_json(json)
# print the JSON string representation of the object
print GetAgentChatMessages200Response.to_json()

# convert the object into a dict
get_agent_chat_messages200_response_dict = get_agent_chat_messages200_response_instance.to_dict()
# create an instance of GetAgentChatMessages200Response from a dict
get_agent_chat_messages200_response_form_dict = get_agent_chat_messages200_response.from_dict(get_agent_chat_messages200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


