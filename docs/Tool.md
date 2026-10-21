# Tool

MCP-инструмент аккаунта

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID инструмента | 
**account_id** | **object** | Логин аккаунта-владельца | 
**template_id** | **object** | ID шаблона маркетплейса, из которого установлен инструмент. &#x60;null&#x60; — собственный MCP-сервер | 
**key** | **object** | Ключ шаблона маркетплейса. Сейчас в ответах не возвращается | [optional] 
**name** | **object** | Название инструмента | 
**description** | **object** | Описание инструмента | 
**type** | **object** | Тип инструмента. У инструментов из шаблонов может быть &#x60;null&#x60; | 
**protocol** | **object** | Транспорт MCP: &#x60;http&#x60; — Streamable HTTP, &#x60;sse&#x60; — Server-Sent Events. У инструментов из шаблонов всегда &#x60;null&#x60; | 
**url** | **object** | Адрес MCP-сервера. У инструментов из шаблонов всегда &#x60;null&#x60; | 
**methods** | **object** | Методы MCP-сервера. &#x60;null&#x60; или пустой массив — методы ещё не получены, например до завершения OAuth2-авторизации | 
**auth_data** | [**ToolAuthData**](ToolAuthData.md) |  | 
**status** | **object** | Статус инструмента: &#x60;active&#x60; — работает, &#x60;inactive&#x60; — выключен вручную, &#x60;pending_auth&#x60; — ожидает OAuth2-авторизации, &#x60;error&#x60; — последнее обновление методов завершилось ошибкой (причина в &#x60;status_info&#x60;). Агент вызывает только инструменты в статусе &#x60;active&#x60; | 
**status_info** | **object** | Причина статуса &#x60;error&#x60; | 
**created_at** | **object** | Дата и время создания | 
**updated_at** | **object** | Дата и время последнего изменения | 

## Example

```python
from timeweb_cloud_api.models.tool import Tool

# TODO update the JSON string below
json = "{}"
# create an instance of Tool from a JSON string
tool_instance = Tool.from_json(json)
# print the JSON string representation of the object
print Tool.to_json()

# convert the object into a dict
tool_dict = tool_instance.to_dict()
# create an instance of Tool from a dict
tool_form_dict = tool.from_dict(tool_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


