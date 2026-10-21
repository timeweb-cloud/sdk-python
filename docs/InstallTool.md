# InstallTool

Данные для установки инструмента из шаблона маркетплейса

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **object** | ID шаблона маркетплейса | 
**name** | **object** | Своё название инструмента. Если не задано, используется название шаблона | [optional] 
**description** | **object** | Своё описание инструмента. Если не задано, используется описание шаблона | [optional] 
**config_values** | **Dict[str, object]** | Значения полей из &#x60;config_schema&#x60; шаблона: ключ — &#x60;fields[].key&#x60;, значение — строка. Поля с &#x60;required: true&#x60; обязательны | [optional] 
**auth_data** | [**ToolAuthData**](ToolAuthData.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.install_tool import InstallTool

# TODO update the JSON string below
json = "{}"
# create an instance of InstallTool from a JSON string
install_tool_instance = InstallTool.from_json(json)
# print the JSON string representation of the object
print InstallTool.to_json()

# convert the object into a dict
install_tool_dict = install_tool_instance.to_dict()
# create an instance of InstallTool from a dict
install_tool_form_dict = install_tool.from_dict(install_tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


