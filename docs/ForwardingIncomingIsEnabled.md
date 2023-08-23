# ForwardingIncomingIsEnabled


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включена ли пересылка входящик писем | [optional] 
**is_delete_messages** | **object** | Удалять ли входящие письма. \\  Если передан параметр &#x60;is_enabled&#x60;: &#x60;false&#x60;, то значение передавать нельзя | [optional] 
**incoming_list** | **object** | Список адресов для пересылки. \\  Если передан параметр &#x60;is_enabled&#x60;: &#x60;false&#x60;, то значение передавать нельзя | [optional] 

## Example

```python
from timeweb_cloud_api.models.forwarding_incoming_is_enabled import ForwardingIncomingIsEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingIncomingIsEnabled from a JSON string
forwarding_incoming_is_enabled_instance = ForwardingIncomingIsEnabled.from_json(json)
# print the JSON string representation of the object
print ForwardingIncomingIsEnabled.to_json()

# convert the object into a dict
forwarding_incoming_is_enabled_dict = forwarding_incoming_is_enabled_instance.to_dict()
# create an instance of ForwardingIncomingIsEnabled from a dict
forwarding_incoming_is_enabled_form_dict = forwarding_incoming_is_enabled.from_dict(forwarding_incoming_is_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


