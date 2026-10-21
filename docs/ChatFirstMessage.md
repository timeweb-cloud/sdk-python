# ChatFirstMessage

Первое сообщение пользователя в чате

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID сообщения | 
**role** | **object** | Автор сообщения | 
**created_at** | **object** | Дата создания сообщения | 
**text** | **object** | Текст сообщения | 

## Example

```python
from timeweb_cloud_api.models.chat_first_message import ChatFirstMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ChatFirstMessage from a JSON string
chat_first_message_instance = ChatFirstMessage.from_json(json)
# print the JSON string representation of the object
print ChatFirstMessage.to_json()

# convert the object into a dict
chat_first_message_dict = chat_first_message_instance.to_dict()
# create an instance of ChatFirstMessage from a dict
chat_first_message_form_dict = chat_first_message.from_dict(chat_first_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


