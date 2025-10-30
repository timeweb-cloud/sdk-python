# KnowledgebaseV2

База знаний (версия API v2)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор базы знаний | 
**name** | **object** | Название базы знаний | 
**description** | **object** | Описание базы знаний | [optional] 
**dbaas_id** | **object** | ID базы данных opensearch | 
**status** | **object** | Статус базы знаний | 
**last_sync** | **object** | Дата последней синхронизации | [optional] 
**total_tokens** | **object** | Всего токенов выделено | 
**used_tokens** | **object** | Использовано токенов | 
**remaining_tokens** | **object** | Осталось токенов | 
**token_package_id** | **object** | ID пакета токенов | 
**subscription_renewal_date** | **object** | Дата обновления подписки | 
**documents_count** | **object** | Общее количество документов в базе знаний | 
**agents_ids** | **object** | ID агентов, связанных с базой знаний | 
**created_at** | **object** | Дата создания базы знаний | 

## Example

```python
from timeweb_cloud_api.models.knowledgebase_v2 import KnowledgebaseV2

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgebaseV2 from a JSON string
knowledgebase_v2_instance = KnowledgebaseV2.from_json(json)
# print the JSON string representation of the object
print KnowledgebaseV2.to_json()

# convert the object into a dict
knowledgebase_v2_dict = knowledgebase_v2_instance.to_dict()
# create an instance of KnowledgebaseV2 from a dict
knowledgebase_v2_form_dict = knowledgebase_v2.from_dict(knowledgebase_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


