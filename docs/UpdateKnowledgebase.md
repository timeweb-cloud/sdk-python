# UpdateKnowledgebase

Данные для обновления базы знаний

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название базы знаний | [optional] 
**description** | **object** | Описание базы знаний | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_knowledgebase import UpdateKnowledgebase

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKnowledgebase from a JSON string
update_knowledgebase_instance = UpdateKnowledgebase.from_json(json)
# print the JSON string representation of the object
print UpdateKnowledgebase.to_json()

# convert the object into a dict
update_knowledgebase_dict = update_knowledgebase_instance.to_dict()
# create an instance of UpdateKnowledgebase from a dict
update_knowledgebase_form_dict = update_knowledgebase.from_dict(update_knowledgebase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


