# GetKnowledgebaseStatistics200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledgebase_statistics** | **object** |  | 
**meta** | [**GetAgentStatistics200ResponseMeta**](GetAgentStatistics200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_knowledgebase_statistics200_response import GetKnowledgebaseStatistics200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetKnowledgebaseStatistics200Response from a JSON string
get_knowledgebase_statistics200_response_instance = GetKnowledgebaseStatistics200Response.from_json(json)
# print the JSON string representation of the object
print GetKnowledgebaseStatistics200Response.to_json()

# convert the object into a dict
get_knowledgebase_statistics200_response_dict = get_knowledgebase_statistics200_response_instance.to_dict()
# create an instance of GetKnowledgebaseStatistics200Response from a dict
get_knowledgebase_statistics200_response_form_dict = get_knowledgebase_statistics200_response.from_dict(get_knowledgebase_statistics200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


