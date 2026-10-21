# SkillVersion

Версия навыка

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID версии | 
**version** | **object** | Номер версии | 
**name** | **object** | Название навыка на момент создания версии | 
**when_to_use** | **object** | Текст «когда применять» в этой версии | 
**instruction** | **object** | Инструкция в этой версии | 
**rolled_back_from_version** | **object** | Номер версии, с которой эта версия создана откатом | 
**is_current** | **object** | Это текущая версия навыка | 
**created_at** | **object** | Дата и время создания версии | 

## Example

```python
from timeweb_cloud_api.models.skill_version import SkillVersion

# TODO update the JSON string below
json = "{}"
# create an instance of SkillVersion from a JSON string
skill_version_instance = SkillVersion.from_json(json)
# print the JSON string representation of the object
print SkillVersion.to_json()

# convert the object into a dict
skill_version_dict = skill_version_instance.to_dict()
# create an instance of SkillVersion from a dict
skill_version_form_dict = skill_version.from_dict(skill_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


