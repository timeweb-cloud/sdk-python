# Agent

AI Agent

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор агента | 
**name** | **object** | Название агента | 
**description** | **object** | Описание агента | 
**model_id** | **object** | ID модели | 
**provider_id** | **object** | ID провайдера | 
**settings** | [**AgentSettings**](AgentSettings.md) |  | 
**status** | **object** | Статус агента | 
**access_type** | **object** | Тип доступа к агенту | 
**total_tokens** | **object** | Всего токенов выделено агенту | 
**used_tokens** | **object** | Использовано токенов | 
**remaining_tokens** | **object** | Осталось токенов | 
**token_package_id** | **object** | ID пакета токенов | 
**subscription_renewal_date** | **object** | Дата обновления подписки | 
**knowledge_bases_ids** | **object** | ID баз знаний, связанных с агентом | 
**access_id** | **object** | ID доступа | 
**created_at** | **object** | Дата создания агента | 

## Example

```python
from timeweb_cloud_api.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print Agent.to_json()

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_form_dict = agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


