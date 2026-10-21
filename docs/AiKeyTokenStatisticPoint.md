# AiKeyTokenStatisticPoint

Расход токенов ключом за интервал

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **object** | Начало интервала | 
**ingoing_tokens** | **object** | Входные токены (запрос) | 
**outgoing_tokens** | **object** | Выходные токены (ответ модели) | 
**cache_read_tokens** | **object** | Входные токены, прочитанные из кэша | 
**cache_write_tokens** | **object** | Входные токены, записанные в кэш | 
**total_cost** | **object** | Стоимость запросов за интервал с учётом скидок аккаунта, до списания бонусов, в валюте аккаунта. &#x60;null&#x60; — стоимость части запросов интервала определить не удалось | 

## Example

```python
from timeweb_cloud_api.models.ai_key_token_statistic_point import AiKeyTokenStatisticPoint

# TODO update the JSON string below
json = "{}"
# create an instance of AiKeyTokenStatisticPoint from a JSON string
ai_key_token_statistic_point_instance = AiKeyTokenStatisticPoint.from_json(json)
# print the JSON string representation of the object
print AiKeyTokenStatisticPoint.to_json()

# convert the object into a dict
ai_key_token_statistic_point_dict = ai_key_token_statistic_point_instance.to_dict()
# create an instance of AiKeyTokenStatisticPoint from a dict
ai_key_token_statistic_point_form_dict = ai_key_token_statistic_point.from_dict(ai_key_token_statistic_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


