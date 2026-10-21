# KnowledgebaseV2

База знаний (v2): вместо списка документов — их количество

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID базы знаний | 
**name** | **object** | Название базы знаний | 
**description** | **object** | Описание базы знаний | 
**project_id** | **object** | ID проекта, в котором находится база знаний. Поля нет, если проект не определён | [optional] 
**dbaas_id** | **object** | ID кластера базы данных OpenSearch, который создан для базы знаний в вашем аккаунте | 
**status** | **object** | Статус базы знаний: - &#x60;creating&#x60; — создаётся кластер базы данных, документы будут проиндексированы после перехода в &#x60;active&#x60; - &#x60;active&#x60; — база знаний работает - &#x60;blocked&#x60; — заблокирована: закончились токены или не удалось продлить подписку - &#x60;deleted&#x60; — удалена | 
**last_sync** | **object** | Дата и время последней синхронизации. &#x60;null&#x60;, если синхронизации не было | 
**total_tokens** | **object** | Количество токенов, доступных в текущем периоде подписки (пакет подписки и докупленные пакеты) | 
**used_tokens** | **object** | Количество израсходованных токенов | 
**remaining_tokens** | **object** | Количество оставшихся токенов | 
**token_package_id** | **object** | ID пакета токенов подписки базы знаний | 
**subscription_renewal_date** | **object** | Дата следующего продления подписки (списания стоимости пакета токенов) | 
**documents_count** | **object** | Количество документов в базе знаний | 
**agents_ids** | **object** | ID агентов, к которым привязана база знаний | 
**created_at** | **object** | Дата и время создания базы знаний | 

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


