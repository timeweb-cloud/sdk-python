# Mailbox

Почтовый ящик

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_reply** | [**MailboxAutoReply**](MailboxAutoReply.md) |  | 
**spam_filter** | [**MailboxSpamFilter**](MailboxSpamFilter.md) |  | 
**forwarding_incoming** | [**MailboxForwardingIncoming**](MailboxForwardingIncoming.md) |  | 
**forwarding_outgoing** | [**MailboxForwardingOutgoing**](MailboxForwardingOutgoing.md) |  | 
**comment** | **object** | Комментарий к почтовому ящику | 
**fqdn** | **object** | Домен почты | 
**mailbox** | **object** | Название почтового ящика | 
**password** | **object** | Пароль почтового ящика | 
**usage_space** | **object** | Использованное место на почтовом ящике (в Мб) | 
**is_webmail** | **object** | Доступен ли Webmail | 
**idn_name** | **object** | IDN домен почтового ящика | 
**is_dovecot** | **object** | Есть ли доступ через dovecot | 

## Example

```python
from openapi_client.models.mailbox import Mailbox

# TODO update the JSON string below
json = "{}"
# create an instance of Mailbox from a JSON string
mailbox_instance = Mailbox.from_json(json)
# print the JSON string representation of the object
print Mailbox.to_json()

# convert the object into a dict
mailbox_dict = mailbox_instance.to_dict()
# create an instance of Mailbox from a dict
mailbox_form_dict = mailbox.from_dict(mailbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


