# AgentSettingsWidget

Настройки виджета

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whitelist_domains** | **object** | Массив разрешенных доменов для виджета | 
**name** | **object** | Отображаемое имя агента в виджете | 
**signature** | **object** | Подпись/подзаголовок, отображаемый под именем агента в виджете | [optional] 
**welcome_message** | **object** | Приветственное сообщение, показываемое при открытии виджета | 
**primary_color** | **object** | Основной цвет виджета (hex-код цвета в формате #RRGGBB) | 
**font** | **object** | Семейство шрифтов для виджета | 
**icon_url** | **object** | URL иконки виджета | [optional] 
**chat_position** | **object** | Позиция виджета чата на странице | 

## Example

```python
from timeweb_cloud_api.models.agent_settings_widget import AgentSettingsWidget

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSettingsWidget from a JSON string
agent_settings_widget_instance = AgentSettingsWidget.from_json(json)
# print the JSON string representation of the object
print AgentSettingsWidget.to_json()

# convert the object into a dict
agent_settings_widget_dict = agent_settings_widget_instance.to_dict()
# create an instance of AgentSettingsWidget from a dict
agent_settings_widget_form_dict = agent_settings_widget.from_dict(agent_settings_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


