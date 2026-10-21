# CreateSkill

Данные нового навыка. Пробелы по краям строк обрезаются

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название навыка, уникальное в аккаунте | 
**when_to_use** | **object** | Когда применять навык. Описывайте ситуации и формулировки клиента. Если текст короче 40 символов, придёт предупреждение &#x60;when_to_use_too_short&#x60; | 
**instruction** | **object** | Инструкция навыка | 
**scripts** | **object** | Скрипты навыка: до 20 файлов общим размером до 10 МБ | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_skill import CreateSkill

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSkill from a JSON string
create_skill_instance = CreateSkill.from_json(json)
# print the JSON string representation of the object
print CreateSkill.to_json()

# convert the object into a dict
create_skill_dict = create_skill_instance.to_dict()
# create an instance of CreateSkill from a dict
create_skill_form_dict = create_skill.from_dict(create_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


