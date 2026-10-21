# SkillScript

Скрипт навыка

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя файла | 
**description** | **object** | Что делает скрипт | 
**args_hint** | **object** | Какие аргументы принимает скрипт | 
**size_bytes** | **object** | Размер содержимого в байтах | 

## Example

```python
from timeweb_cloud_api.models.skill_script import SkillScript

# TODO update the JSON string below
json = "{}"
# create an instance of SkillScript from a JSON string
skill_script_instance = SkillScript.from_json(json)
# print the JSON string representation of the object
print SkillScript.to_json()

# convert the object into a dict
skill_script_dict = skill_script_instance.to_dict()
# create an instance of SkillScript from a dict
skill_script_form_dict = skill_script.from_dict(skill_script_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


