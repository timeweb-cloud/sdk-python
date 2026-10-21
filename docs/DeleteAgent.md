# DeleteAgent

Причина удаления агента (необязательно)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reason** | **object** | Причина удаления | [optional] 
**comment** | **object** | Комментарий к причине удаления | [optional] 

## Example

```python
from timeweb_cloud_api.models.delete_agent import DeleteAgent

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteAgent from a JSON string
delete_agent_instance = DeleteAgent.from_json(json)
# print the JSON string representation of the object
print DeleteAgent.to_json()

# convert the object into a dict
delete_agent_dict = delete_agent_instance.to_dict()
# create an instance of DeleteAgent from a dict
delete_agent_form_dict = delete_agent.from_dict(delete_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


