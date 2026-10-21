# ChatMessageFile

Файл, приложенный к сообщению; `null` — файла нет

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **object** | Имя файла | 

## Example

```python
from timeweb_cloud_api.models.chat_message_file import ChatMessageFile

# TODO update the JSON string below
json = "{}"
# create an instance of ChatMessageFile from a JSON string
chat_message_file_instance = ChatMessageFile.from_json(json)
# print the JSON string representation of the object
print ChatMessageFile.to_json()

# convert the object into a dict
chat_message_file_dict = chat_message_file_instance.to_dict()
# create an instance of ChatMessageFile from a dict
chat_message_file_form_dict = chat_message_file.from_dict(chat_message_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


