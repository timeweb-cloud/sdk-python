# GetAgentChatList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat_list** | **object** |  | 
**meta** | [**GetAgentChatList200ResponseMeta**](GetAgentChatList200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_agent_chat_list200_response import GetAgentChatList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentChatList200Response from a JSON string
get_agent_chat_list200_response_instance = GetAgentChatList200Response.from_json(json)
# print the JSON string representation of the object
print GetAgentChatList200Response.to_json()

# convert the object into a dict
get_agent_chat_list200_response_dict = get_agent_chat_list200_response_instance.to_dict()
# create an instance of GetAgentChatList200Response from a dict
get_agent_chat_list200_response_form_dict = get_agent_chat_list200_response.from_dict(get_agent_chat_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


