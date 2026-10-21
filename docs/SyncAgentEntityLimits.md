# SyncAgentEntityLimits

Полный набор лимитов агента за период

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit_type** | **object** | Период лимита | 
**limits** | **object** | Лимиты за период — по одному на модель (&#x60;model_id&#x60; не должен повторяться). Лимиты этого периода, которых нет в списке, удаляются; пустой массив удаляет все лимиты периода. | 

## Example

```python
from timeweb_cloud_api.models.sync_agent_entity_limits import SyncAgentEntityLimits

# TODO update the JSON string below
json = "{}"
# create an instance of SyncAgentEntityLimits from a JSON string
sync_agent_entity_limits_instance = SyncAgentEntityLimits.from_json(json)
# print the JSON string representation of the object
print SyncAgentEntityLimits.to_json()

# convert the object into a dict
sync_agent_entity_limits_dict = sync_agent_entity_limits_instance.to_dict()
# create an instance of SyncAgentEntityLimits from a dict
sync_agent_entity_limits_form_dict = sync_agent_entity_limits.from_dict(sync_agent_entity_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


