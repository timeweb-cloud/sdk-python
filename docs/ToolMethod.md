# ToolMethod

Метод MCP-сервера

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя метода. Именно его указывают в &#x60;allowed_methods&#x60; при подключении к агенту | 
**description** | **object** | Описание метода, полученное от MCP-сервера | [optional] 
**public_name** | **object** | Отображаемое название метода. Задаётся у некоторых шаблонов маркетплейса | [optional] 

## Example

```python
from timeweb_cloud_api.models.tool_method import ToolMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ToolMethod from a JSON string
tool_method_instance = ToolMethod.from_json(json)
# print the JSON string representation of the object
print ToolMethod.to_json()

# convert the object into a dict
tool_method_dict = tool_method_instance.to_dict()
# create an instance of ToolMethod from a dict
tool_method_form_dict = tool_method.from_dict(tool_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


