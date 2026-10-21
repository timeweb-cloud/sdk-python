# AgentSettings

Настройки агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**AgentModelSettings**](AgentModelSettings.md) |  | 
**system_prompt** | **object** | Системный промпт (инструкция) агента | 
**refine_query** | **object** | Уточнять (переформулировать) запрос пользователя перед поиском по базам знаний | 
**memory_enabled** | **object** | Запоминать факты о каждом авторизованном пользователе и учитывать их в ответах. В виджете не работает. | [optional] 
**widget** | [**AgentWidgetSettings**](AgentWidgetSettings.md) |  | [optional] 
**web_search_allowed_sites** | **object** | Домены, которыми ограничивается веб-поиск агента (не более 5). Каждый элемент — домен (&#x60;timeweb.ru&#x60;) или домен с путём (&#x60;timeweb.ru/docs&#x60;). Если поле не передано при обновлении, сохранённый список не меняется. | [optional] 
**additional_models** | **object** | Настройки дополнительных моделей. Заполняется автоматически из поля &#x60;additional_models&#x60; запроса создания или обновления агента, передавать здесь не нужно. | [optional] 

## Example

```python
from timeweb_cloud_api.models.agent_settings import AgentSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSettings from a JSON string
agent_settings_instance = AgentSettings.from_json(json)
# print the JSON string representation of the object
print AgentSettings.to_json()

# convert the object into a dict
agent_settings_dict = agent_settings_instance.to_dict()
# create an instance of AgentSettings from a dict
agent_settings_form_dict = agent_settings.from_dict(agent_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


