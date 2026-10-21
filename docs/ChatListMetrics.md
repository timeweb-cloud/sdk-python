# ChatListMetrics

Сводка по чатам агента с учётом фильтра по периоду (`from`/`to`)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_reactions** | **object** | Количество чатов с учётом фильтра &#x60;response_time_ranges&#x60; (без учёта &#x60;reaction_type&#x60;) | 
**total_time** | **object** | Количество чатов с учётом фильтра &#x60;reaction_type&#x60; (без учёта &#x60;response_time_ranges&#x60;) | 
**with_likes** | **object** | Чатов хотя бы с одной положительной оценкой | 
**with_dislikes** | **object** | Чатов хотя бы с одной отрицательной оценкой | 
**with_any** | **object** | Чатов хотя бы с одной оценкой | 
**response_time_groups_reactions** | **Dict[str, object]** | Количество чатов по среднему времени ответа (в секундах) с учётом фильтра &#x60;response_time_ranges&#x60; | 
**response_time_groups_time** | **Dict[str, object]** | Количество чатов по среднему времени ответа (в секундах) с учётом фильтра &#x60;reaction_type&#x60; | 

## Example

```python
from timeweb_cloud_api.models.chat_list_metrics import ChatListMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of ChatListMetrics from a JSON string
chat_list_metrics_instance = ChatListMetrics.from_json(json)
# print the JSON string representation of the object
print ChatListMetrics.to_json()

# convert the object into a dict
chat_list_metrics_dict = chat_list_metrics_instance.to_dict()
# create an instance of ChatListMetrics from a dict
chat_list_metrics_form_dict = chat_list_metrics.from_dict(chat_list_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


