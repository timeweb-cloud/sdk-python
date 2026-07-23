# CreateAgentV2

Данные для создания AI агента через API v2

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название агента | 
**description** | **object** | Описание агента | [optional] 
**access_type** | **object** | Тип доступа к агенту | 
**model_id** | **object** | ID основной модели | 
**token_limit** | **object** | Дневной лимит токенов для агента (0 — без лимита) | [optional] 
**settings** | [**AgentSettings**](AgentSettings.md) |  | 
**project_id** | **object** | ID проекта | [optional] 
**additional_model_ids** | **object** | Список ID дополнительных моделей агента | [optional] 
**is_web_search_enabled** | **object** | Признак использования веб-поиска агентом | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_agent_v2 import CreateAgentV2

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentV2 from a JSON string
create_agent_v2_instance = CreateAgentV2.from_json(json)
# print the JSON string representation of the object
print CreateAgentV2.to_json()

# convert the object into a dict
create_agent_v2_dict = create_agent_v2_instance.to_dict()
# create an instance of CreateAgentV2 from a dict
create_agent_v2_form_dict = create_agent_v2.from_dict(create_agent_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


