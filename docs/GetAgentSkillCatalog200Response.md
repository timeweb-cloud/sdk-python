# GetAgentSkillCatalog200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill_catalog_items** | **object** |  | 
**meta** | [**GetAgentSkillCatalog200ResponseMeta**](GetAgentSkillCatalog200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_agent_skill_catalog200_response import GetAgentSkillCatalog200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAgentSkillCatalog200Response from a JSON string
get_agent_skill_catalog200_response_instance = GetAgentSkillCatalog200Response.from_json(json)
# print the JSON string representation of the object
print GetAgentSkillCatalog200Response.to_json()

# convert the object into a dict
get_agent_skill_catalog200_response_dict = get_agent_skill_catalog200_response_instance.to_dict()
# create an instance of GetAgentSkillCatalog200Response from a dict
get_agent_skill_catalog200_response_form_dict = get_agent_skill_catalog200_response.from_dict(get_agent_skill_catalog200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


