# SpamProtectionIsEnabled


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включен ли спам-фильтр | 
**filter_action** | **object** | Что делать с письмами, которые попадают в спам. \\  Параметры: \\  &#x60;directory&#x60; - переместить в папку спам; \\  &#x60;label&#x60; - пометить письмо; \\  Если передан параметр &#x60;is_enabled&#x60;: &#x60;false&#x60;, то значение передавать нельзя | [optional] 
**white_list** | **object** | Белый список адресов от которых письма не будут попадать в спам. \\  Если передан параметр &#x60;is_enabled&#x60;: &#x60;false&#x60;, то значение передавать нельзя | [optional] 

## Example

```python
from timeweb_cloud_api.models.spam_protection_is_enabled import SpamProtectionIsEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of SpamProtectionIsEnabled from a JSON string
spam_protection_is_enabled_instance = SpamProtectionIsEnabled.from_json(json)
# print the JSON string representation of the object
print SpamProtectionIsEnabled.to_json()

# convert the object into a dict
spam_protection_is_enabled_dict = spam_protection_is_enabled_instance.to_dict()
# create an instance of SpamProtectionIsEnabled from a dict
spam_protection_is_enabled_form_dict = spam_protection_is_enabled.from_dict(spam_protection_is_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


