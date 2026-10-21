# CreateTool

Данные для подключения собственного MCP-сервера

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название инструмента | 
**description** | **object** | Описание инструмента | [optional] 
**type** | **object** | Тип инструмента. Поддерживается только &#x60;MCP&#x60; | 
**protocol** | **object** | Транспорт MCP: &#x60;http&#x60; — Streamable HTTP, &#x60;sse&#x60; — Server-Sent Events | 
**url** | **object** | Адрес MCP-сервера. Сервер должен быть доступен из интернета | 
**auth_data** | [**ToolAuthData**](ToolAuthData.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_tool import CreateTool

# TODO update the JSON string below
json = "{}"
# create an instance of CreateTool from a JSON string
create_tool_instance = CreateTool.from_json(json)
# print the JSON string representation of the object
print CreateTool.to_json()

# convert the object into a dict
create_tool_dict = create_tool_instance.to_dict()
# create an instance of CreateTool from a dict
create_tool_form_dict = create_tool.from_dict(create_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


