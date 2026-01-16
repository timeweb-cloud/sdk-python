# MailboxesBatchV2

Результат массового создания почтовых ящиков (API v2)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mailboxes** | **object** | Массив успешно созданных почтовых ящиков | 
**errors** | **object** | Массив ошибок при создании почтовых ящиков | 

## Example

```python
from timeweb_cloud_api.models.mailboxes_batch_v2 import MailboxesBatchV2

# TODO update the JSON string below
json = "{}"
# create an instance of MailboxesBatchV2 from a JSON string
mailboxes_batch_v2_instance = MailboxesBatchV2.from_json(json)
# print the JSON string representation of the object
print MailboxesBatchV2.to_json()

# convert the object into a dict
mailboxes_batch_v2_dict = mailboxes_batch_v2_instance.to_dict()
# create an instance of MailboxesBatchV2 from a dict
mailboxes_batch_v2_form_dict = mailboxes_batch_v2.from_dict(mailboxes_batch_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


