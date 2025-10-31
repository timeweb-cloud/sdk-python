# UpdateMailboxV2

Обновление почтового ящика

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **object** | Пароль почтового ящика | [optional] 
**comment** | **object** | Комментарий к почтовому ящику | [optional] 
**owner_full_name** | **object** | ФИО владельца почтового ящика | [optional] 
**spam_protection_settings** | [**SpamProtectionIsEnabled**](SpamProtectionIsEnabled.md) |  | [optional] 
**forward_settings** | [**ForwardIsEnabled**](ForwardIsEnabled.md) |  | [optional] 
**autoreply_settings** | [**AutoreplyIsEnabled**](AutoreplyIsEnabled.md) |  | [optional] 
**outgoing_settings** | [**OutgoingIsEnabled**](OutgoingIsEnabled.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_mailbox_v2 import UpdateMailboxV2

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMailboxV2 from a JSON string
update_mailbox_v2_instance = UpdateMailboxV2.from_json(json)
# print the JSON string representation of the object
print UpdateMailboxV2.to_json()

# convert the object into a dict
update_mailbox_v2_dict = update_mailbox_v2_instance.to_dict()
# create an instance of UpdateMailboxV2 from a dict
update_mailbox_v2_form_dict = update_mailbox_v2.from_dict(update_mailbox_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


