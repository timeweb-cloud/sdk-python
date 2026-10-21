# UpdateAgentTool

Новый список разрешённых методов

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_methods** | **object** | Методы, которые агенту разрешено вызывать: имена из &#x60;methods[].name&#x60; инструмента. Список заменяется целиком | 

## Example

```python
from timeweb_cloud_api.models.update_agent_tool import UpdateAgentTool

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgentTool from a JSON string
update_agent_tool_instance = UpdateAgentTool.from_json(json)
# print the JSON string representation of the object
print UpdateAgentTool.to_json()

# convert the object into a dict
update_agent_tool_dict = update_agent_tool_instance.to_dict()
# create an instance of UpdateAgentTool from a dict
update_agent_tool_form_dict = update_agent_tool.from_dict(update_agent_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


