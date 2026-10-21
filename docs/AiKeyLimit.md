# AiKeyLimit

Лимит расхода ключа AI Gateway

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID лимита (UUID) | 
**ai_key_id** | **object** | ID ключа, к которому относится лимит | 
**entity_type** | **object** | Тип сущности, на которую действует лимит. Для лимита на сам ключ — тип ключа (&#x60;aikey&#x60; или &#x60;k8s&#x60;) | 
**entity_id** | **object** | ID сущности, на которую действует лимит. Для лимита на сам ключ — ID ключа | 
**limit** | **object** | Лимит в токенах за период. Не действует, если задан &#x60;money_limit&#x60;. &#x60;0&#x60; — запросы запрещены | 
**money_limit** | **object** | Лимит в деньгах за период, в валюте аккаунта. Приоритетнее &#x60;limit&#x60;. &#x60;null&#x60; — не задан, действует &#x60;limit&#x60;; &#x60;0&#x60; — запросы запрещены | 
**limit_type** | **object** | Период лимита: &#x60;hour&#x60; — час, &#x60;day&#x60; — сутки, &#x60;week&#x60; — 7 дней, &#x60;month&#x60; — 30 дней | 
**model_id** | **object** | ID модели, на которую действует лимит. &#x60;null&#x60; — лимит на все модели | 
**usage** | **object** | Израсходовано токенов за текущий период | 
**money_usage** | **object** | Израсходовано денег за текущий период — полная стоимость запросов до списания бонусов, в валюте аккаунта | 
**created_at** | **object** | Дата и время создания лимита | 
**expire_at** | **object** | Дата и время окончания текущего периода: после него расход обнуляется и начинается новый период | 

## Example

```python
from timeweb_cloud_api.models.ai_key_limit import AiKeyLimit

# TODO update the JSON string below
json = "{}"
# create an instance of AiKeyLimit from a JSON string
ai_key_limit_instance = AiKeyLimit.from_json(json)
# print the JSON string representation of the object
print AiKeyLimit.to_json()

# convert the object into a dict
ai_key_limit_dict = ai_key_limit_instance.to_dict()
# create an instance of AiKeyLimit from a dict
ai_key_limit_form_dict = ai_key_limit.from_dict(ai_key_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


