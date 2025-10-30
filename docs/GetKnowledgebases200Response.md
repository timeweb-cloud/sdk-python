# GetKnowledgebases200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledgebases** | **object** |  | 
**meta** | [**GetKnowledgebasesV2200ResponseMeta**](GetKnowledgebasesV2200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_knowledgebases200_response import GetKnowledgebases200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetKnowledgebases200Response from a JSON string
get_knowledgebases200_response_instance = GetKnowledgebases200Response.from_json(json)
# print the JSON string representation of the object
print GetKnowledgebases200Response.to_json()

# convert the object into a dict
get_knowledgebases200_response_dict = get_knowledgebases200_response_instance.to_dict()
# create an instance of GetKnowledgebases200Response from a dict
get_knowledgebases200_response_form_dict = get_knowledgebases200_response.from_dict(get_knowledgebases200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


