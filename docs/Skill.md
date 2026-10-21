# Skill

Навык

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID навыка | 
**name** | **object** | Название навыка, уникальное в аккаунте | 
**when_to_use** | **object** | Когда применять навык. Это поле читает модель, когда выбирает навык | 
**instruction** | **object** | Инструкция навыка. Попадает в контекст модели только при срабатывании | 
**current_version** | **object** | Номер текущей версии | 
**agents_count** | **object** | У скольких агентов навык включён | 
**first_agent_name** | **object** | Имя агента, если навык включён ровно у одного агента | 
**catalog_item_id** | **object** | ID навыка в каталоге, из которого установлен этот навык | 
**catalog_version** | **object** | Версия каталожного навыка, из которой установлен или обновлён этот навык | 
**is_from_catalog** | **object** | Навык установлен из каталога | 
**is_modified** | **object** | Установленный из каталога навык изменялся владельцем | 
**created_at** | **object** | Дата и время создания | 
**updated_at** | **object** | Дата и время последнего изменения | 

## Example

```python
from timeweb_cloud_api.models.skill import Skill

# TODO update the JSON string below
json = "{}"
# create an instance of Skill from a JSON string
skill_instance = Skill.from_json(json)
# print the JSON string representation of the object
print Skill.to_json()

# convert the object into a dict
skill_dict = skill_instance.to_dict()
# create an instance of Skill from a dict
skill_form_dict = skill.from_dict(skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


