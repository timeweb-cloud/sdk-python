# MailboxSpamFilter

Спам-фильтр

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включен ли спам-фильтр | 
**action** | **object** | Что делать с письмами, которые попадают в спам. \\  Параметры: \\  &#x60;move_to_directory&#x60; - переместить в паку спам; \\  &#x60;forward&#x60; - переслать письмо на другой адрес; \\  &#x60;delete&#x60; - удалить письмо; \\  &#x60;tag&#x60; - пометить письмо; | 
**forward_to** | **object** | Адрес для пересылки при выбранном действии &#x60;forward&#x60; из параметра &#x60;action&#x60; | 
**white_list** | **object** | Белый список адресов от которых письма не будут попадать в спам | 

## Example

```python
from timeweb_cloud_api.models.mailbox_spam_filter import MailboxSpamFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxSpamFilter from a JSON string
mailbox_spam_filter_instance = MailboxSpamFilter.from_json(json)
# print the JSON string representation of the object
print MailboxSpamFilter.to_json()

# convert the object into a dict
mailbox_spam_filter_dict = mailbox_spam_filter_instance.to_dict()
# create an instance of MailboxSpamFilter from a dict
mailbox_spam_filter_form_dict = mailbox_spam_filter.from_dict(mailbox_spam_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


