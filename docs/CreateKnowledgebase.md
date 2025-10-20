# CreateKnowledgebase

Данные для создания базы знаний

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название базы знаний | 
**description** | **object** | Описание базы знаний | [optional] 
**dbaas_preset_id** | **object** | ID пресета базы данных | 
**network_id** | **object** | ID сети | 
**token_package_id** | **object** | ID пакета токенов | 
**project_id** | **object** | ID проекта | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_knowledgebase import CreateKnowledgebase

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKnowledgebase from a JSON string
create_knowledgebase_instance = CreateKnowledgebase.from_json(json)
# print the JSON string representation of the object
print CreateKnowledgebase.to_json()

# convert the object into a dict
create_knowledgebase_dict = create_knowledgebase_instance.to_dict()
# create an instance of CreateKnowledgebase from a dict
create_knowledgebase_form_dict = create_knowledgebase.from_dict(create_knowledgebase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


