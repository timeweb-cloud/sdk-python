# LinkKnowledgebase

Параметры привязки базы знаний к агенту

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retrieval_mode** | [**RetrievalMode**](RetrievalMode.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.link_knowledgebase import LinkKnowledgebase

# TODO update the JSON string below
json = "{}"
# create an instance of LinkKnowledgebase from a JSON string
link_knowledgebase_instance = LinkKnowledgebase.from_json(json)
# print the JSON string representation of the object
print LinkKnowledgebase.to_json()

# convert the object into a dict
link_knowledgebase_dict = link_knowledgebase_instance.to_dict()
# create an instance of LinkKnowledgebase from a dict
link_knowledgebase_form_dict = link_knowledgebase.from_dict(link_knowledgebase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


