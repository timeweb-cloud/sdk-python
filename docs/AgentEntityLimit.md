# AgentEntityLimit

Лимит агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID лимита | 
**ai_key_id** | **object** | ID служебного ключа агента, на котором учитывается лимит | 
**entity_type** | **object** | Тип сущности — всегда &#x60;agent&#x60; | 
**entity_id** | **object** | ID агента | 
**limit_type** | **object** | Период лимита | 
**model_id** | **object** | ID модели, на запросы к которой действует лимит. &#x60;null&#x60; — лимит на все модели агента. | 
**limit** | **object** | Лимит в токенах за период. Не действует, если задан &#x60;money_limit&#x60;. &#x60;0&#x60; — запрещены все запросы. | 
**money_limit** | **object** | Лимит расходов за период в валюте аккаунта; &#x60;null&#x60; — не задан, действует &#x60;limit&#x60; | 
**usage** | **object** | Израсходовано токенов в текущем периоде | 
**money_usage** | **object** | Израсходовано денег в текущем периоде (полная стоимость запросов до бонусов) | 
**created_at** | **object** | Дата создания лимита | 
**expire_at** | **object** | Окончание текущего периода — после него расход обнуляется | 

## Example

```python
from timeweb_cloud_api.models.agent_entity_limit import AgentEntityLimit

# TODO update the JSON string below
json = "{}"
# create an instance of AgentEntityLimit from a JSON string
agent_entity_limit_instance = AgentEntityLimit.from_json(json)
# print the JSON string representation of the object
print AgentEntityLimit.to_json()

# convert the object into a dict
agent_entity_limit_dict = agent_entity_limit_instance.to_dict()
# create an instance of AgentEntityLimit from a dict
agent_entity_limit_form_dict = agent_entity_limit.from_dict(agent_entity_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


