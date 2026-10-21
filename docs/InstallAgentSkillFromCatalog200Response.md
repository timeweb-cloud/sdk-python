# InstallAgentSkillFromCatalog200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill** | [**Skill**](Skill.md) |  | 
**meta** | [**InstallAgentSkillFromCatalog200ResponseMeta**](InstallAgentSkillFromCatalog200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.install_agent_skill_from_catalog200_response import InstallAgentSkillFromCatalog200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstallAgentSkillFromCatalog200Response from a JSON string
install_agent_skill_from_catalog200_response_instance = InstallAgentSkillFromCatalog200Response.from_json(json)
# print the JSON string representation of the object
print InstallAgentSkillFromCatalog200Response.to_json()

# convert the object into a dict
install_agent_skill_from_catalog200_response_dict = install_agent_skill_from_catalog200_response_instance.to_dict()
# create an instance of InstallAgentSkillFromCatalog200Response from a dict
install_agent_skill_from_catalog200_response_form_dict = install_agent_skill_from_catalog200_response.from_dict(install_agent_skill_from_catalog200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


