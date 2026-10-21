# ConnectAgentTool

Данные для подключения инструмента к агенту

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_id** | **object** | ID инструмента | 
**allowed_methods** | **object** | Методы, которые агенту разрешено вызывать: имена из &#x60;methods[].name&#x60; инструмента. Пустой массив тоже допустим | 

## Example

```python
from timeweb_cloud_api.models.connect_agent_tool import ConnectAgentTool

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectAgentTool from a JSON string
connect_agent_tool_instance = ConnectAgentTool.from_json(json)
# print the JSON string representation of the object
print ConnectAgentTool.to_json()

# convert the object into a dict
connect_agent_tool_dict = connect_agent_tool_instance.to_dict()
# create an instance of ConnectAgentTool from a dict
connect_agent_tool_form_dict = connect_agent_tool.from_dict(connect_agent_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


