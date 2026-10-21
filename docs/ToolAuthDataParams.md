# ToolAuthDataParams

Параметры авторизации. Набор полей зависит от `type`: для `none` — пустой объект, для `bearer` — `token`, для `custom_headers` — `headers`, для `oauth2` — поля OAuth2-клиента.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **object** | Токен для заголовка &#x60;Authorization: Bearer&#x60; (для &#x60;bearer&#x60;). В ответах заменён на &#x60;********&#x60; | [optional] 
**headers** | **Dict[str, object]** | HTTP-заголовки, которые передаются MCP-серверу (для &#x60;custom_headers&#x60;). В ответах значения заменены на &#x60;********&#x60; | [optional] 
**client_id** | **object** | ID OAuth2-клиента (для &#x60;oauth2&#x60;). Не нужен, если сервер поддерживает динамическую регистрацию клиентов | [optional] 
**client_secret** | **object** | Секрет OAuth2-клиента (для &#x60;oauth2&#x60;). В ответах заменён на &#x60;********&#x60; | [optional] 
**authorization_url** | **object** | Адрес страницы авторизации провайдера (для &#x60;oauth2&#x60;). Если не задан, определяется по метаданным сервера | [optional] 
**token_url** | **object** | Адрес получения токенов провайдера (для &#x60;oauth2&#x60;). Если не задан, определяется по метаданным сервера | [optional] 
**registration_url** | **object** | Адрес динамической регистрации клиента (для &#x60;oauth2&#x60;) | [optional] 
**scopes** | **object** | Запрашиваемые права (для &#x60;oauth2&#x60;). Если не заданы, берутся из метаданных сервера | [optional] 

## Example

```python
from timeweb_cloud_api.models.tool_auth_data_params import ToolAuthDataParams

# TODO update the JSON string below
json = "{}"
# create an instance of ToolAuthDataParams from a JSON string
tool_auth_data_params_instance = ToolAuthDataParams.from_json(json)
# print the JSON string representation of the object
print ToolAuthDataParams.to_json()

# convert the object into a dict
tool_auth_data_params_dict = tool_auth_data_params_instance.to_dict()
# create an instance of ToolAuthDataParams from a dict
tool_auth_data_params_form_dict = tool_auth_data_params.from_dict(tool_auth_data_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


