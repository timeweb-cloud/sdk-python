# AgentTokenStatistic

Точка статистики использования токенов агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **object** | Начало интервала | 
**model_name** | **object** | Модель, на которую пришлись запросы. В интервалах без запросов поле отсутствует. | [optional] 
**ingoing_tokens** | **object** | Входящие токены (промпты). Если для аккаунта включена тарификация кэша, токены из кэша считаются отдельно. | 
**outgoing_tokens** | **object** | Исходящие токены (ответы) | 
**cache_read_tokens** | **object** | Входящие токены, прочитанные из кэша | 
**cache_write_tokens** | **object** | Входящие токены, записанные в кэш | 
**total_cost** | **object** | Стоимость токенов интервала до учёта бонусов, в валюте аккаунта. &#x60;null&#x60; — стоимость посчитать не удалось. | 

## Example

```python
from timeweb_cloud_api.models.agent_token_statistic import AgentTokenStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of AgentTokenStatistic from a JSON string
agent_token_statistic_instance = AgentTokenStatistic.from_json(json)
# print the JSON string representation of the object
print AgentTokenStatistic.to_json()

# convert the object into a dict
agent_token_statistic_dict = agent_token_statistic_instance.to_dict()
# create an instance of AgentTokenStatistic from a dict
agent_token_statistic_form_dict = agent_token_statistic.from_dict(agent_token_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


