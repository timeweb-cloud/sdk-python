# ChatsCsv

Выгрузка чатов агента в CSV

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csv** | **object** | Содержимое CSV-файла: по строке на чат и на каждое его сообщение (ID диалога, ID агента, ID сообщения, время, автор, текст, оценка, время ответа в секундах) | 
**file_name** | **object** | Рекомендуемое имя файла (без расширения) | 

## Example

```python
from timeweb_cloud_api.models.chats_csv import ChatsCsv

# TODO update the JSON string below
json = "{}"
# create an instance of ChatsCsv from a JSON string
chats_csv_instance = ChatsCsv.from_json(json)
# print the JSON string representation of the object
print ChatsCsv.to_json()

# convert the object into a dict
chats_csv_dict = chats_csv_instance.to_dict()
# create an instance of ChatsCsv from a dict
chats_csv_form_dict = chats_csv.from_dict(chats_csv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


