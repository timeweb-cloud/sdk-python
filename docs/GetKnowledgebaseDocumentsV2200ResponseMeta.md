# GetKnowledgebaseDocumentsV2200ResponseMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **object** | Общее количество документов | 
**limit** | **object** | Количество документов на странице | 
**offset** | **object** | Количество пропущенных документов | 

## Example

```python
from timeweb_cloud_api.models.get_knowledgebase_documents_v2200_response_meta import GetKnowledgebaseDocumentsV2200ResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GetKnowledgebaseDocumentsV2200ResponseMeta from a JSON string
get_knowledgebase_documents_v2200_response_meta_instance = GetKnowledgebaseDocumentsV2200ResponseMeta.from_json(json)
# print the JSON string representation of the object
print GetKnowledgebaseDocumentsV2200ResponseMeta.to_json()

# convert the object into a dict
get_knowledgebase_documents_v2200_response_meta_dict = get_knowledgebase_documents_v2200_response_meta_instance.to_dict()
# create an instance of GetKnowledgebaseDocumentsV2200ResponseMeta from a dict
get_knowledgebase_documents_v2200_response_meta_form_dict = get_knowledgebase_documents_v2200_response_meta.from_dict(get_knowledgebase_documents_v2200_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


