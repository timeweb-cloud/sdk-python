# MailboxForwardingIncoming

Пересылка входящик писем

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включена ли пересылка входящик писем | 
**is_delete_messages** | **object** | Удалять ли входящие письма | 
**incoming_list** | **object** | Список адресов для пересылки | 

## Example

```python
from openapi_client.models.mailbox_forwarding_incoming import MailboxForwardingIncoming

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxForwardingIncoming from a JSON string
mailbox_forwarding_incoming_instance = MailboxForwardingIncoming.from_json(json)
# print the JSON string representation of the object
print MailboxForwardingIncoming.to_json()

# convert the object into a dict
mailbox_forwarding_incoming_dict = mailbox_forwarding_incoming_instance.to_dict()
# create an instance of MailboxForwardingIncoming from a dict
mailbox_forwarding_incoming_form_dict = mailbox_forwarding_incoming.from_dict(mailbox_forwarding_incoming_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


