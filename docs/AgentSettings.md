# AgentSettings

Настройки агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**AgentModelSettings**](AgentModelSettings.md) |  | 
**system_prompt** | **object** | Системный промпт | 
**refine_query** | **object** | Уточнять ли запрос перед обработкой | 
**widget** | [**AgentSettingsWidget**](AgentSettingsWidget.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.agent_settings import AgentSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AgentSettings from a JSON string
agent_settings_instance = AgentSettings.from_json(json)
# print the JSON string representation of the object
print AgentSettings.to_json()

# convert the object into a dict
agent_settings_dict = agent_settings_instance.to_dict()
# create an instance of AgentSettings from a dict
agent_settings_form_dict = agent_settings.from_dict(agent_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


