# ForwardingOutgoingIsEnabled


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включена ли пересылка исходящих писем. \\  Если передан параметр &#x60;is_enabled&#x60;: &#x60;false&#x60;, то значение передавать нельзя | [optional] 
**outgoing_to** | **object** | Адрес для пересылки исходящих писем. \\  Если передан параметр &#x60;is_enabled&#x60;: &#x60;false&#x60;, то значение передавать нельзя | [optional] 

## Example

```python
from timeweb_cloud_api.models.forwarding_outgoing_is_enabled import ForwardingOutgoingIsEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingOutgoingIsEnabled from a JSON string
forwarding_outgoing_is_enabled_instance = ForwardingOutgoingIsEnabled.from_json(json)
# print the JSON string representation of the object
print ForwardingOutgoingIsEnabled.to_json()

# convert the object into a dict
forwarding_outgoing_is_enabled_dict = forwarding_outgoing_is_enabled_instance.to_dict()
# create an instance of ForwardingOutgoingIsEnabled from a dict
forwarding_outgoing_is_enabled_form_dict = forwarding_outgoing_is_enabled.from_dict(forwarding_outgoing_is_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


