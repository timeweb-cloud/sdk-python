# ForwardingIncomingIsDisabled


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включена ли пересылка входящик писем | 
**is_delete_messages** | **object** | Удалять ли входящие письма | [optional] 
**incoming_list** | **object** | Список адресов для пересылки. Не должен быть пустым при передачи параметра &#x60;is_enabled&#x60;: &#x60;true&#x60; | [optional] 

## Example

```python
from openapi_client.models.forwarding_incoming_is_disabled import ForwardingIncomingIsDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingIncomingIsDisabled from a JSON string
forwarding_incoming_is_disabled_instance = ForwardingIncomingIsDisabled.from_json(json)
# print the JSON string representation of the object
print ForwardingIncomingIsDisabled.to_json()

# convert the object into a dict
forwarding_incoming_is_disabled_dict = forwarding_incoming_is_disabled_instance.to_dict()
# create an instance of ForwardingIncomingIsDisabled from a dict
forwarding_incoming_is_disabled_form_dict = forwarding_incoming_is_disabled.from_dict(forwarding_incoming_is_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


