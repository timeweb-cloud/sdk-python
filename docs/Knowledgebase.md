# Knowledgebase

База знаний

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор базы знаний | 
**name** | **object** | Название базы знаний | 
**description** | **object** | Описание базы знаний | [optional] 
**dbaas_id** | **object** | ID базы данных (opensearch или qdrant) | 
**status** | **object** | Статус базы знаний | 
**last_sync** | **object** | Дата последней синхронизации | [optional] 
**total_tokens** | **object** | Всего токенов выделено | 
**used_tokens** | **object** | Использовано токенов | 
**remaining_tokens** | **object** | Осталось токенов | 
**token_package_id** | **object** | ID пакета токенов | 
**subscription_renewal_date** | **object** | Дата обновления подписки | 
**documents** | **object** | Документы в базе знаний | 
**agents_ids** | **object** | ID агентов, связанных с базой знаний | 
**created_at** | **object** | Дата создания базы знаний | 

## Example

```python
from timeweb_cloud_api.models.knowledgebase import Knowledgebase

# TODO update the JSON string below
json = "{}"
# create an instance of Knowledgebase from a JSON string
knowledgebase_instance = Knowledgebase.from_json(json)
# print the JSON string representation of the object
print Knowledgebase.to_json()

# convert the object into a dict
knowledgebase_dict = knowledgebase_instance.to_dict()
# create an instance of Knowledgebase from a dict
knowledgebase_form_dict = knowledgebase.from_dict(knowledgebase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


