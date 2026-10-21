# GetKnowledgebasesV3200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledge_bases** | **object** |  | 
**meta** | [**GetKnowledgebasesV3200ResponseMeta**](GetKnowledgebasesV3200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_knowledgebases_v3200_response import GetKnowledgebasesV3200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetKnowledgebasesV3200Response from a JSON string
get_knowledgebases_v3200_response_instance = GetKnowledgebasesV3200Response.from_json(json)
# print the JSON string representation of the object
print GetKnowledgebasesV3200Response.to_json()

# convert the object into a dict
get_knowledgebases_v3200_response_dict = get_knowledgebases_v3200_response_instance.to_dict()
# create an instance of GetKnowledgebasesV3200Response from a dict
get_knowledgebases_v3200_response_form_dict = get_knowledgebases_v3200_response.from_dict(get_knowledgebases_v3200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


