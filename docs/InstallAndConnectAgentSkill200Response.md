# InstallAndConnectAgentSkill200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_skill** | [**AgentSkill**](AgentSkill.md) |  | 
**meta** | [**InstallAgentSkillFromCatalog200ResponseMeta**](InstallAgentSkillFromCatalog200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.install_and_connect_agent_skill200_response import InstallAndConnectAgentSkill200Response

# TODO update the JSON string below
json = "{}"
# create an instance of InstallAndConnectAgentSkill200Response from a JSON string
install_and_connect_agent_skill200_response_instance = InstallAndConnectAgentSkill200Response.from_json(json)
# print the JSON string representation of the object
print InstallAndConnectAgentSkill200Response.to_json()

# convert the object into a dict
install_and_connect_agent_skill200_response_dict = install_and_connect_agent_skill200_response_instance.to_dict()
# create an instance of InstallAndConnectAgentSkill200Response from a dict
install_and_connect_agent_skill200_response_form_dict = install_and_connect_agent_skill200_response.from_dict(install_and_connect_agent_skill200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


