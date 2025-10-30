# GetKnowledgebaseDocumentsV2200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**knowledgebase_documents** | **object** | Список документов | 
**meta** | [**GetKnowledgebaseDocumentsV2200ResponseMeta**](GetKnowledgebaseDocumentsV2200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_knowledgebase_documents_v2200_response import GetKnowledgebaseDocumentsV2200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetKnowledgebaseDocumentsV2200Response from a JSON string
get_knowledgebase_documents_v2200_response_instance = GetKnowledgebaseDocumentsV2200Response.from_json(json)
# print the JSON string representation of the object
print GetKnowledgebaseDocumentsV2200Response.to_json()

# convert the object into a dict
get_knowledgebase_documents_v2200_response_dict = get_knowledgebase_documents_v2200_response_instance.to_dict()
# create an instance of GetKnowledgebaseDocumentsV2200Response from a dict
get_knowledgebase_documents_v2200_response_form_dict = get_knowledgebase_documents_v2200_response.from_dict(get_knowledgebase_documents_v2200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


