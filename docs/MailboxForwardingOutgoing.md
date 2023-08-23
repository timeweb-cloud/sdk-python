# MailboxForwardingOutgoing

Пересылка исходящих писем

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включена ли пересылка исходящих писем | 
**outgoing_to** | **object** | Адрес для пересылки исходящих писем | 

## Example

```python
from openapi_client.models.mailbox_forwarding_outgoing import MailboxForwardingOutgoing

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxForwardingOutgoing from a JSON string
mailbox_forwarding_outgoing_instance = MailboxForwardingOutgoing.from_json(json)
# print the JSON string representation of the object
print MailboxForwardingOutgoing.to_json()

# convert the object into a dict
mailbox_forwarding_outgoing_dict = mailbox_forwarding_outgoing_instance.to_dict()
# create an instance of MailboxForwardingOutgoing from a dict
mailbox_forwarding_outgoing_form_dict = mailbox_forwarding_outgoing.from_dict(mailbox_forwarding_outgoing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


