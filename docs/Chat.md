# Chat

Чат (диалог) агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID чата | 
**agent_id** | **object** | ID агента | 
**created_at** | **object** | Дата первого сообщения чата | 
**first_message** | [**ChatFirstMessage**](ChatFirstMessage.md) |  | 
**likes_count** | **object** | Количество положительных оценок в чате | 
**dislikes_count** | **object** | Количество отрицательных оценок в чате | 
**uptime_avg** | **object** | Среднее время до начала ответа агента в чате, в миллисекундах | 

## Example

```python
from timeweb_cloud_api.models.chat import Chat

# TODO update the JSON string below
json = "{}"
# create an instance of Chat from a JSON string
chat_instance = Chat.from_json(json)
# print the JSON string representation of the object
print Chat.to_json()

# convert the object into a dict
chat_dict = chat_instance.to_dict()
# create an instance of Chat from a dict
chat_form_dict = chat.from_dict(chat_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


