# ToolConfigField

Поле настройки шаблона: что нужно передать в `config_values` при установке

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **object** | Ключ поля в &#x60;config_values&#x60; | 
**label** | **object** | Название поля для пользователя | 
**type** | **object** | Тип значения | 
**required** | **object** | Поле обязательно | 
**description** | **object** | Подсказка к полю | [optional] 
**placeholder** | **object** | Пример значения | [optional] 
**header_name** | **object** | HTTP-заголовок, в котором значение передаётся MCP-серверу | [optional] 
**prefix** | **object** | Префикс, который добавляется перед значением в заголовке | [optional] 
**options** | **object** | Допустимые значения (для &#x60;select&#x60;) | [optional] 
**default** | **object** | Значение по умолчанию | [optional] 

## Example

```python
from timeweb_cloud_api.models.tool_config_field import ToolConfigField

# TODO update the JSON string below
json = "{}"
# create an instance of ToolConfigField from a JSON string
tool_config_field_instance = ToolConfigField.from_json(json)
# print the JSON string representation of the object
print ToolConfigField.to_json()

# convert the object into a dict
tool_config_field_dict = tool_config_field_instance.to_dict()
# create an instance of ToolConfigField from a dict
tool_config_field_form_dict = tool_config_field.from_dict(tool_config_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


