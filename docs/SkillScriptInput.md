# SkillScriptInput

Скрипт навыка в запросе

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя файла: латиница, цифры, &#x60;_&#x60;, &#x60;.&#x60; и &#x60;-&#x60;, без путей, с расширением &#x60;.py&#x60;, &#x60;.js&#x60;, &#x60;.mjs&#x60; или &#x60;.cjs&#x60;. Имена в навыке не повторяются | 
**description** | **object** | Что делает скрипт. По этому тексту модель решает, запускать ли его, поэтому описывайте результат, а не реализацию | 
**args_hint** | **object** | Какие аргументы принимает скрипт | [optional] 
**content** | **object** | Текст скрипта. Обязателен для нового файла. Для файла, который уже есть в текущей версии навыка, можно не передавать: содержимое возьмётся из неё по имени. Общий размер скриптов навыка — до 10 МБ (10 485 760 байт в UTF-8) | [optional] 

## Example

```python
from timeweb_cloud_api.models.skill_script_input import SkillScriptInput

# TODO update the JSON string below
json = "{}"
# create an instance of SkillScriptInput from a JSON string
skill_script_input_instance = SkillScriptInput.from_json(json)
# print the JSON string representation of the object
print SkillScriptInput.to_json()

# convert the object into a dict
skill_script_input_dict = skill_script_input_instance.to_dict()
# create an instance of SkillScriptInput from a dict
skill_script_input_form_dict = skill_script_input.from_dict(skill_script_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


