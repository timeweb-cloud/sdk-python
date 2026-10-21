# UpdateSkill

Изменяемые поля навыка. Незаданные поля не меняются, пустые строки не принимаются

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название навыка. Изменение названия не создаёт новую версию | [optional] 
**when_to_use** | **object** | Когда применять навык | [optional] 
**instruction** | **object** | Инструкция навыка | [optional] 
**scripts** | **object** | Новый набор скриптов, заменяет прежний целиком. Пустой массив удаляет все скрипты. Если поле не передано, скрипты не меняются | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_skill import UpdateSkill

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSkill from a JSON string
update_skill_instance = UpdateSkill.from_json(json)
# print the JSON string representation of the object
print UpdateSkill.to_json()

# convert the object into a dict
update_skill_dict = update_skill_instance.to_dict()
# create an instance of UpdateSkill from a dict
update_skill_form_dict = update_skill.from_dict(update_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


