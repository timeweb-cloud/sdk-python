# AgentModelSettings

Параметры модели агента. Допустимые параметры и их границы зависят от модели (см. параметры модели в разделе «AI Модели»): параметры, которые модель не поддерживает, отбрасываются при сохранении, а значения вне допустимых границ отклоняются с ошибкой 400.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**temperature** | **object** | Температура: чем выше, тем случайнее ответы модели. | [optional] 
**top_p** | **object** | Nucleus sampling: доля вероятностной массы, из которой выбираются токены. | [optional] 
**max_tokens** | **object** | Максимальное количество токенов в ответе модели. | [optional] 
**frequency_penalty** | **object** | Штраф за частоту: положительные значения снижают повторы уже использованных токенов. | [optional] 
**presence_penalty** | **object** | Штраф за присутствие: положительные значения поощряют новые темы. | [optional] 
**enable_thinking** | **object** | Включает режим рассуждений (thinking) для моделей, которые его поддерживают. | [optional] 

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


