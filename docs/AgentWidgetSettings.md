# AgentWidgetSettings

Настройки виджета чата агента для встраивания на сайт

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**whitelist_domains** | **object** | Домены, на которых разрешено показывать виджет. Пустой массив — без ограничений. | 
**name** | **object** | Отображаемое имя агента в виджете | 
**signature** | **object** | Подпись под именем агента в виджете | [optional] 
**welcome_message** | **object** | Приветственное сообщение при открытии виджета | 
**primary_color** | **object** | Основной цвет виджета в формате &#x60;#RRGGBB&#x60; | 
**text_color** | **object** | Цвет текста в формате &#x60;#RRGGBB&#x60; | [optional] 
**background_color** | **object** | Цвет фона в формате &#x60;#RRGGBB&#x60; | [optional] 
**header_footer_color** | **object** | Цвет шапки и подвала виджета в формате &#x60;#RRGGBB&#x60; | [optional] 
**font** | **object** | Шрифт виджета. Пустая строка — шрифт сайта. | 
**icon_url** | **object** | URL иконки агента в виджете | [optional] 
**use_avatar** | **object** | Использовать загруженный в панели аватар как иконку агента | [optional] 
**show_button** | **object** | Показывать кнопку открытия виджета | [optional] 
**show_tool_processing** | **object** | Показывать в виджете статус выполнения инструментов агента | [optional] 
**show_confirmation_buttons** | **object** | Показывать кнопки подтверждения и отмены операций, которые агент выполняет через инструменты | [optional] 
**chat_position** | **object** | Положение виджета на странице | 
**chat_position_adjustment_x** | **object** | Смещение виджета по горизонтали в пикселях | [optional] 
**chat_position_adjustment_y** | **object** | Смещение виджета по вертикали в пикселях | [optional] 

## Example

```python
from timeweb_cloud_api.models.agent_widget_settings import AgentWidgetSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AgentWidgetSettings from a JSON string
agent_widget_settings_instance = AgentWidgetSettings.from_json(json)
# print the JSON string representation of the object
print AgentWidgetSettings.to_json()

# convert the object into a dict
agent_widget_settings_dict = agent_widget_settings_instance.to_dict()
# create an instance of AgentWidgetSettings from a dict
agent_widget_settings_form_dict = agent_widget_settings.from_dict(agent_widget_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


