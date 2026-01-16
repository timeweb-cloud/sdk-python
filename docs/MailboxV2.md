# MailboxV2

Почтовый ящик (API v2)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idn_name** | **object** | IDN домен почтового ящика | 
**autoreply_message** | **object** | Сообщение автоответчика на входящие письма | 
**autoreply_status** | **object** | Включен ли автоответчик на входящие письма | 
**autoreply_subject** | **object** | Тема сообщения автоответчика на входящие письма | 
**comment** | **object** | Комментарий к почтовому ящику | 
**filter_action** | **object** | Что делать с письмами, которые попадают в спам | 
**filter_status** | **object** | Включен ли спам-фильтр | 
**forward_list** | **object** | Список адресов для пересылки входящих писем | 
**forward_status** | **object** | Включена ли пересылка входящих писем | 
**outgoing_control** | **object** | Включена ли пересылка исходящих писем | 
**outgoing_email** | **object** | Адрес для пересылки исходящих писем | 
**password** | **object** | Пароль почтового ящика (всегда возвращается пустой строкой) | 
**spambox** | **object** | Адрес для пересылки спама при выбранном действии forward | 
**white_list** | **object** | Белый список адресов от которых письма не будут попадать в спам | 
**webmail** | **object** | Доступен ли Webmail | 
**dovecot** | **object** | Есть ли доступ через dovecot | 
**fqdn** | **object** | Домен почты | 
**leave_messages** | **object** | Оставлять ли сообщения на сервере при пересылке | 
**mailbox** | **object** | Название почтового ящика | 
**owner_full_name** | **object** | ФИО владельца почтового ящика | 

## Example

```python
from timeweb_cloud_api.models.mailbox_v2 import MailboxV2

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxV2 from a JSON string
mailbox_v2_instance = MailboxV2.from_json(json)
# print the JSON string representation of the object
print MailboxV2.to_json()

# convert the object into a dict
mailbox_v2_dict = mailbox_v2_instance.to_dict()
# create an instance of MailboxV2 from a dict
mailbox_v2_form_dict = mailbox_v2.from_dict(mailbox_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


