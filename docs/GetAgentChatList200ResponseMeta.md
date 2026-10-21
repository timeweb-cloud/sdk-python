# GetAgentChatList200ResponseMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **object** | Количество чатов с учётом фильтров | 
**metrics** | [**ChatListMetrics**](ChatListMetrics.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.get_agent_chat_list200_response_meta import GetAgentChatList200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentChatList200ResponseMeta from a JSON string
get_agent_chat_list200_response_meta_instance = GetAgentChatList200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print GetAgentChatList200ResponseMeta.to_json()

# convert the object into a dict
get_agent_chat_list200_response_meta_dict = get_agent_chat_list200_response_meta_instance.to_dict()
# create an instance of GetAgentChatList200ResponseMeta from a dict
get_agent_chat_list200_response_meta_form_dict = get_agent_chat_list200_response_meta.from_dict(get_agent_chat_list200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


