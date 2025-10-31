# MailboxResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idn_name** | **object** | IDN имя домена | [optional] 
**autoreply_message** | **object** | Сообщение автоответчика | [optional] 
**autoreply_status** | **object** | Статус автоответчика | [optional] 
**autoreply_subject** | **object** | Тема автоответчика | [optional] 
**comment** | **object** | Комментарий | [optional] 
**filter_action** | **object** | Действие фильтра спама | [optional] 
**filter_status** | **object** | Статус фильтра спама | [optional] 
**forward_list** | **object** | Список адресов для пересылки | [optional] 
**forward_status** | **object** | Статус пересылки | [optional] 
**outgoing_control** | **object** | Контроль исходящей почты | [optional] 
**outgoing_email** | **object** | Email для исходящих писем | [optional] 
**password** | **object** | Пароль (обычно пустая строка в ответе) | [optional] 
**white_list** | **object** | Белый список адресов | [optional] 
**webmail** | **object** | Доступ к веб-почте | [optional] 
**dovecot** | **object** | Использование Dovecot | [optional] 
**fqdn** | **object** | Полное доменное имя | [optional] 
**leave_messages** | **object** | Оставлять копии писем при пересылке | [optional] 
**mailbox** | **object** | Имя почтового ящика | [optional] 
**owner_full_name** | **object** | ФИО владельца | [optional] 

## Example

```python
from timeweb_cloud_api.models.mailbox_response import MailboxResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxResponse from a JSON string
mailbox_response_instance = MailboxResponse.from_json(json)
# print the JSON string representation of the object
print MailboxResponse.to_json()

# convert the object into a dict
mailbox_response_dict = mailbox_response_instance.to_dict()
# create an instance of MailboxResponse from a dict
mailbox_response_form_dict = mailbox_response.from_dict(mailbox_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


