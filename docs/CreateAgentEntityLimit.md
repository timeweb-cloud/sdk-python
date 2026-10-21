# CreateAgentEntityLimit

Новый лимит агента. Нужно передать `limit` или `money_limit`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit_type** | **object** | Период лимита | 
**model_id** | **object** | ID модели, на запросы к которой действует лимит. Не передан или &#x60;null&#x60; — лимит на все модели агента. | [optional] 
**limit** | **object** | Лимит в токенах за период. Если не передан — &#x60;0&#x60;, тогда обязателен &#x60;money_limit&#x60;. Не действует, если задан &#x60;money_limit&#x60;. &#x60;0&#x60; при отсутствии &#x60;money_limit&#x60; — запрещены все запросы. | [optional] 
**money_limit** | **object** | Лимит расходов за период в валюте аккаунта, до 8 знаков после запятой. Приоритетнее &#x60;limit&#x60;. &#x60;0&#x60; — запрещены все запросы. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_agent_entity_limit import CreateAgentEntityLimit

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentEntityLimit from a JSON string
create_agent_entity_limit_instance = CreateAgentEntityLimit.from_json(json)
# print the JSON string representation of the object
print CreateAgentEntityLimit.to_json()

# convert the object into a dict
create_agent_entity_limit_dict = create_agent_entity_limit_instance.to_dict()
# create an instance of CreateAgentEntityLimit from a dict
create_agent_entity_limit_form_dict = create_agent_entity_limit.from_dict(create_agent_entity_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


