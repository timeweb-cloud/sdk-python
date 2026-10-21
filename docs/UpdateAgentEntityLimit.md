# UpdateAgentEntityLimit

Изменение лимита агента. Непереданные поля не меняются.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **object** | Лимит в токенах за период. Не действует, если задан &#x60;money_limit&#x60;. &#x60;0&#x60; — запрещены все запросы. | [optional] 
**money_limit** | **object** | Лимит расходов за период в валюте аккаунта, до 8 знаков после запятой. Приоритетнее &#x60;limit&#x60;. &#x60;0&#x60; — запрещены все запросы. &#x60;null&#x60; — снять денежный лимит (только вместе с &#x60;limit&#x60;). | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_agent_entity_limit import UpdateAgentEntityLimit

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgentEntityLimit from a JSON string
update_agent_entity_limit_instance = UpdateAgentEntityLimit.from_json(json)
# print the JSON string representation of the object
print UpdateAgentEntityLimit.to_json()

# convert the object into a dict
update_agent_entity_limit_dict = update_agent_entity_limit_instance.to_dict()
# create an instance of UpdateAgentEntityLimit from a dict
update_agent_entity_limit_form_dict = update_agent_entity_limit.from_dict(update_agent_entity_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


