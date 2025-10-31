# OutgoingIsEnabled


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включена ли пересылка исходящих писем | 
**outgoing_email** | **object** | Адрес для пересылки исходящих писем. \\  Если передан параметр &#x60;is_enabled&#x60;: &#x60;false&#x60;, то значение передавать нельзя | 

## Example

```python
from timeweb_cloud_api.models.outgoing_is_enabled import OutgoingIsEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of OutgoingIsEnabled from a JSON string
outgoing_is_enabled_instance = OutgoingIsEnabled.from_json(json)
# print the JSON string representation of the object
print OutgoingIsEnabled.to_json()

# convert the object into a dict
outgoing_is_enabled_dict = outgoing_is_enabled_instance.to_dict()
# create an instance of OutgoingIsEnabled from a dict
outgoing_is_enabled_form_dict = outgoing_is_enabled.from_dict(outgoing_is_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


