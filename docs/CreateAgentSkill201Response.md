# CreateAgentSkill201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill** | [**Skill**](Skill.md) |  | 
**meta** | [**SkillSaveMeta**](SkillSaveMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.create_agent_skill201_response import CreateAgentSkill201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentSkill201Response from a JSON string
create_agent_skill201_response_instance = CreateAgentSkill201Response.from_json(json)
# print the JSON string representation of the object
print CreateAgentSkill201Response.to_json()

# convert the object into a dict
create_agent_skill201_response_dict = create_agent_skill201_response_instance.to_dict()
# create an instance of CreateAgentSkill201Response from a dict
create_agent_skill201_response_form_dict = create_agent_skill201_response.from_dict(create_agent_skill201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


