# SetAgentSkill

Состояние навыка у агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включить (&#x60;true&#x60;) или выключить (&#x60;false&#x60;) навык у агента | 
**version** | **object** | Закрепить агента на этой версии из истории навыка. Если не передано, при первом включении закрепляется текущая версия, а у уже подключённого навыка закреплённая версия не меняется | [optional] 

## Example

```python
from timeweb_cloud_api.models.set_agent_skill import SetAgentSkill

# TODO update the JSON string below
json = "{}"
# create an instance of SetAgentSkill from a JSON string
set_agent_skill_instance = SetAgentSkill.from_json(json)
# print the JSON string representation of the object
print SetAgentSkill.to_json()

# convert the object into a dict
set_agent_skill_dict = set_agent_skill_instance.to_dict()
# create an instance of SetAgentSkill from a dict
set_agent_skill_form_dict = set_agent_skill.from_dict(set_agent_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


