# UpdateAgent

Данные для обновления AI агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название агента | [optional] 
**description** | **object** | Описание агента | [optional] 
**access_type** | **object** | Тип доступа к агенту | [optional] 
**status** | **object** | Статус агента | [optional] 
**token_package_id** | **object** | ID пакета токенов | [optional] 
**settings** | [**UpdateAgentSettings**](UpdateAgentSettings.md) |  | [optional] 
**project_id** | **object** | ID проекта | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_agent import UpdateAgent

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAgent from a JSON string
update_agent_instance = UpdateAgent.from_json(json)
# print the JSON string representation of the object
print UpdateAgent.to_json()

# convert the object into a dict
update_agent_dict = update_agent_instance.to_dict()
# create an instance of UpdateAgent from a dict
update_agent_form_dict = update_agent.from_dict(update_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


