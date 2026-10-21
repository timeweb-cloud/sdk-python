# AgentSkill

Навык аккаунта и его состояние у агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill_id** | **object** | ID навыка | 
**name** | **object** | Название навыка | 
**when_to_use** | **object** | Когда применять навык | 
**current_version** | **object** | Номер текущей версии навыка | 
**is_connected** | **object** | Навык подключён к агенту | 
**is_enabled** | **object** | Навык включён у агента | 
**pinned_version** | **object** | Версия, на которой закреплён агент. &#x60;null&#x60; — навык не подключён | 
**has_newer_version** | **object** | Текущая версия навыка отличается от закреплённой | 
**is_from_catalog** | **object** | Навык установлен из каталога | 
**is_modified** | **object** | Установленный из каталога навык изменялся владельцем | 

## Example

```python
from timeweb_cloud_api.models.agent_skill import AgentSkill

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSkill from a JSON string
agent_skill_instance = AgentSkill.from_json(json)
# print the JSON string representation of the object
print AgentSkill.to_json()

# convert the object into a dict
agent_skill_dict = agent_skill_instance.to_dict()
# create an instance of AgentSkill from a dict
agent_skill_form_dict = agent_skill.from_dict(agent_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


