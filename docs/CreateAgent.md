# CreateAgent

Данные для создания AI агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название агента | 
**description** | **object** | Описание агента | [optional] 
**access_type** | **object** | Тип доступа к агенту | 
**model_id** | **object** | ID модели | 
**token_package_id** | **object** | ID пакета токенов | 
**settings** | [**AgentSettings**](AgentSettings.md) |  | 
**project_id** | **object** | ID проекта | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_agent import CreateAgent

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgent from a JSON string
create_agent_instance = CreateAgent.from_json(json)
# print the JSON string representation of the object
print CreateAgent.to_json()

# convert the object into a dict
create_agent_dict = create_agent_instance.to_dict()
# create an instance of CreateAgent from a dict
create_agent_form_dict = create_agent.from_dict(create_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


