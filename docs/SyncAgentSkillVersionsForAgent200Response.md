# SyncAgentSkillVersionsForAgent200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_skills** | **object** |  | 
**meta** | [**GetAgentSkillsForAgent200ResponseMeta**](GetAgentSkillsForAgent200ResponseMeta.md) |  | 
**updated_count** | **object** | Сколько навыков переведено на текущую версию | 

## Example

```python
from timeweb_cloud_api.models.sync_agent_skill_versions_for_agent200_response import SyncAgentSkillVersionsForAgent200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SyncAgentSkillVersionsForAgent200Response from a JSON string
sync_agent_skill_versions_for_agent200_response_instance = SyncAgentSkillVersionsForAgent200Response.from_json(json)
# print the JSON string representation of the object
print SyncAgentSkillVersionsForAgent200Response.to_json()

# convert the object into a dict
sync_agent_skill_versions_for_agent200_response_dict = sync_agent_skill_versions_for_agent200_response_instance.to_dict()
# create an instance of SyncAgentSkillVersionsForAgent200Response from a dict
sync_agent_skill_versions_for_agent200_response_form_dict = sync_agent_skill_versions_for_agent200_response.from_dict(sync_agent_skill_versions_for_agent200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


