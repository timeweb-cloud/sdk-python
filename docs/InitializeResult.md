# InitializeResult

Результат `initialize`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol_version** | **object** | Версия протокола: запрошенная клиентом, если сервер её поддерживает, иначе &#x60;2025-11-25&#x60; | 
**capabilities** | **Dict[str, object]** | Возможности сервера | 
**server_info** | [**InitializeResultServerInfo**](InitializeResultServerInfo.md) |  | 
**instructions** | **object** | Правила для модели: какой инструмент на какой вопрос отвечает. MCP-клиенты передают их модели автоматически | [optional] 

## Example

```python
from timeweb_cloud_api.models.initialize_result import InitializeResult

# TODO update the JSON string below
json = "{}"
# create an instance of InitializeResult from a JSON string
initialize_result_instance = InitializeResult.from_json(json)
# print the JSON string representation of the object
print InitializeResult.to_json()

# convert the object into a dict
initialize_result_dict = initialize_result_instance.to_dict()
# create an instance of InitializeResult from a dict
initialize_result_form_dict = initialize_result.from_dict(initialize_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


