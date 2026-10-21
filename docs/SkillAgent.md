# SkillAgent

Агент, к которому подключён навык

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **object** | ID агента | 
**agent_name** | **object** | Название агента | 
**is_enabled** | **object** | Навык включён у агента | 
**pinned_version** | **object** | Версия навыка, на которой закреплён агент | 
**has_newer_version** | **object** | Текущая версия навыка отличается от закреплённой | 

## Example

```python
from timeweb_cloud_api.models.skill_agent import SkillAgent

# TODO update the JSON string below
json = "{}"
# create an instance of SkillAgent from a JSON string
skill_agent_instance = SkillAgent.from_json(json)
# print the JSON string representation of the object
print SkillAgent.to_json()

# convert the object into a dict
skill_agent_dict = skill_agent_instance.to_dict()
# create an instance of SkillAgent from a dict
skill_agent_form_dict = skill_agent.from_dict(skill_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


