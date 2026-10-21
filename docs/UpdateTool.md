# UpdateTool

Изменяемые поля инструмента. Незаданные поля не меняются

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название инструмента | [optional] 
**description** | **object** | Описание инструмента | [optional] 
**type** | **object** | Тип инструмента | [optional] 
**protocol** | **object** | Транспорт MCP | [optional] 
**url** | **object** | Адрес MCP-сервера. Список методов при смене адреса не обновляется — вызовите обновление методов | [optional] 
**auth_data** | [**ToolAuthData**](ToolAuthData.md) |  | [optional] 
**status** | **object** | Статус инструмента. Чтобы временно выключить инструмент у всех агентов, передайте &#x60;inactive&#x60;, чтобы включить — &#x60;active&#x60; | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_tool import UpdateTool

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateTool from a JSON string
update_tool_instance = UpdateTool.from_json(json)
# print the JSON string representation of the object
print UpdateTool.to_json()

# convert the object into a dict
update_tool_dict = update_tool_instance.to_dict()
# create an instance of UpdateTool from a dict
update_tool_form_dict = update_tool.from_dict(update_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


