# ForwardingOutgoingIsDisabled


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включена ли пересылка исходящих писем | 
**outgoing_to** | **object** | Адрес для пересылки исходящих писем | [optional] 

## Example

```python
from openapi_client.models.forwarding_outgoing_is_disabled import ForwardingOutgoingIsDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingOutgoingIsDisabled from a JSON string
forwarding_outgoing_is_disabled_instance = ForwardingOutgoingIsDisabled.from_json(json)
# print the JSON string representation of the object
print ForwardingOutgoingIsDisabled.to_json()

# convert the object into a dict
forwarding_outgoing_is_disabled_dict = forwarding_outgoing_is_disabled_instance.to_dict()
# create an instance of ForwardingOutgoingIsDisabled from a dict
forwarding_outgoing_is_disabled_form_dict = forwarding_outgoing_is_disabled.from_dict(forwarding_outgoing_is_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


