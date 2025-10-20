# UpdateAgentSettings

Настройки агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**AgentModelSettings**](AgentModelSettings.md) |  | [optional] 
**system_prompt** | **object** | Системный промпт | [optional] 
**refine_query** | **object** | Уточнять ли запрос перед обработкой | [optional] 
**widget** | [**AgentSettingsWidget**](AgentSettingsWidget.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_agent_settings import UpdateAgentSettings

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgentSettings from a JSON string
update_agent_settings_instance = UpdateAgentSettings.from_json(json)
# print the JSON string representation of the object
print UpdateAgentSettings.to_json()

# convert the object into a dict
update_agent_settings_dict = update_agent_settings_instance.to_dict()
# create an instance of UpdateAgentSettings from a dict
update_agent_settings_form_dict = update_agent_settings.from_dict(update_agent_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


