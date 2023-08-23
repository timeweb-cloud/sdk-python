# MailboxAutoReply

Автоответчик на входящие письма

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включен ли автоответчик на входящие письма | 
**message** | **object** | Сообщение автоответчика на входящие письма | 
**subject** | **object** | Тема сообщения автоответчика на входящие письма | 

## Example

```python
from timeweb_cloud_api.models.mailbox_auto_reply import MailboxAutoReply

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxAutoReply from a JSON string
mailbox_auto_reply_instance = MailboxAutoReply.from_json(json)
# print the JSON string representation of the object
print MailboxAutoReply.to_json()

# convert the object into a dict
mailbox_auto_reply_dict = mailbox_auto_reply_instance.to_dict()
# create an instance of MailboxAutoReply from a dict
mailbox_auto_reply_form_dict = mailbox_auto_reply.from_dict(mailbox_auto_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


