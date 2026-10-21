# ChatMessage

Сообщение чата агента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID сообщения | 
**message_id** | **object** | Строковый идентификатор сообщения. Есть не у всех сообщений. | [optional] 
**role** | **object** | Автор сообщения | 
**created_at** | **object** | Дата создания сообщения | 
**text** | **object** | Текст сообщения | 
**is_good** | **object** | Оценка ответа: &#x60;true&#x60; — понравился, &#x60;false&#x60; — не понравился, &#x60;null&#x60; — без оценки | 
**uptime_ms** | **object** | Время до начала ответа агента в миллисекундах (для ответов агента) | 
**file** | [**ChatMessageFile**](ChatMessageFile.md) |  | 

## Example

```python
from timeweb_cloud_api.models.chat_message import ChatMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessage from a JSON string
chat_message_instance = ChatMessage.from_json(json)
# print the JSON string representation of the object
print ChatMessage.to_json()

# convert the object into a dict
chat_message_dict = chat_message_instance.to_dict()
# create an instance of ChatMessage from a dict
chat_message_form_dict = chat_message.from_dict(chat_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


