# UpdateMailbox

Изменение почтового ящика

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_reply** | [**AutoReplyIsDisabled**](AutoReplyIsDisabled.md) |  | [optional] 
**spam_filter** | [**SpamFilterIsDisabled**](SpamFilterIsDisabled.md) |  | [optional] 
**forwarding_incoming** | [**ForwardingIncomingIsDisabled**](ForwardingIncomingIsDisabled.md) |  | [optional] 
**forwarding_outgoing** | [**ForwardingOutgoingIsDisabled**](ForwardingOutgoingIsDisabled.md) |  | [optional] 
**comment** | **object** | Комментарий к почтовому ящику | [optional] 
**password** | **object** | Пароль почтового ящика | [optional] 

## Example

```python
from openapi_client.models.update_mailbox import UpdateMailbox

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMailbox from a JSON string
update_mailbox_instance = UpdateMailbox.from_json(json)
# print the JSON string representation of the object
print UpdateMailbox.to_json()

# convert the object into a dict
update_mailbox_dict = update_mailbox_instance.to_dict()
# create an instance of UpdateMailbox from a dict
update_mailbox_form_dict = update_mailbox.from_dict(update_mailbox_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


