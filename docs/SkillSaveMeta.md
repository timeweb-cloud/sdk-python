# SkillSaveMeta

Результат сохранения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_created** | **object** | Создана ли новая версия. &#x60;false&#x60; — изменился только заголовок или изменений не было | 
**affected_agents_count** | **object** | У скольких агентов навык включён. Их поведение не меняется, пока их не переведут на новую версию | 
**warnings** | **object** | Предупреждения, которые не мешают сохранению. &#x60;when_to_use_too_short&#x60; — текст «когда применять» короче 40 символов: модель не сможет отличить подходящий запрос от постороннего | 
**pruned_versions** | **object** | Номера версий, удалённых из истории из-за лимита в 50 версий | 

## Example

```python
from timeweb_cloud_api.models.skill_save_meta import SkillSaveMeta

# TODO update the JSON string below
json = "{}"
# create an instance of SkillSaveMeta from a JSON string
skill_save_meta_instance = SkillSaveMeta.from_json(json)
# print the JSON string representation of the object
print SkillSaveMeta.to_json()

# convert the object into a dict
skill_save_meta_dict = skill_save_meta_instance.to_dict()
# create an instance of SkillSaveMeta from a dict
skill_save_meta_form_dict = skill_save_meta.from_dict(skill_save_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


