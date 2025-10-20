# AgentModelSettings

Настройки модели агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**temperature** | **object** | Контролирует случайность вывода модели. | [optional] 
**top_p** | **object** | Контролирует разнообразие вывода модели. | [optional] 
**max_tokens** | **object** | Максимальное количество токенов в выводе. | [optional] 
**frequency_penalty** | **object** | Положительные значения штрафуют новые токены на основе их существующей частоты. | [optional] 
**presence_penalty** | **object** | Положительные значения штрафуют новые токены на основе того, встречались ли они в тексте ранее. | [optional] 

## Example

```python
from timeweb_cloud_api.models.agent_model_settings import AgentModelSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AgentModelSettings from a JSON string
agent_model_settings_instance = AgentModelSettings.from_json(json)
# print the JSON string representation of the object
print AgentModelSettings.to_json()

# convert the object into a dict
agent_model_settings_dict = agent_model_settings_instance.to_dict()
# create an instance of AgentModelSettings from a dict
agent_model_settings_form_dict = agent_model_settings.from_dict(agent_model_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


