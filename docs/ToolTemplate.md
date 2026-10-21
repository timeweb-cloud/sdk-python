# ToolTemplate

Шаблон MCP-инструмента из маркетплейса

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID шаблона. Передаётся в &#x60;template_id&#x60; при установке | 
**name** | **object** | Название | 
**key** | **object** | Уникальный ключ шаблона | [optional] 
**description** | **object** | Описание | 
**type** | **object** | Тип инструмента | 
**version** | **object** | Версия шаблона | 
**is_approved** | **object** | Шаблон одобрен для маркетплейса: &#x60;1&#x60; — да, &#x60;0&#x60; — нет | 
**author_account_id** | **object** | Автор шаблона. &#x60;null&#x60; — шаблон Timeweb Cloud | [optional] 
**is_system** | **object** | Системный шаблон платформы: &#x60;1&#x60; — да, &#x60;0&#x60; — нет | 
**install_count** | **object** | Сколько раз шаблон установлен | 
**category** | **object** | Категория шаблона | [optional] 
**config_schema** | [**ToolTemplateConfigSchema**](ToolTemplateConfigSchema.md) |  | [optional] 
**auth_type** | **object** | Способ авторизации на MCP-сервере | 
**deployment_type** | **object** | Где работает MCP-сервер: &#x60;managed&#x60; — на стороне Timeweb Cloud, &#x60;external&#x60; — у стороннего сервиса | 
**created_at** | **object** | Дата и время создания | 
**updated_at** | **object** | Дата и время последнего изменения | 

## Example

```python
from timeweb_cloud_api.models.tool_template import ToolTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ToolTemplate from a JSON string
tool_template_instance = ToolTemplate.from_json(json)
# print the JSON string representation of the object
print ToolTemplate.to_json()

# convert the object into a dict
tool_template_dict = tool_template_instance.to_dict()
# create an instance of ToolTemplate from a dict
tool_template_form_dict = tool_template.from_dict(tool_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


