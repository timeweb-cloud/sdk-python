# SpamFilterIsDisabled


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включен ли спам-фильтр | 
**action** | **object** | Что делать с письмами, которые попадают в спам. \\  Параметры: \\  &#x60;move_to_directory&#x60; - переместить в паку спам; \\  &#x60;forward&#x60; - переслать письмо на другой адрес; \\  &#x60;delete&#x60; - удалить письмо; \\  &#x60;tag&#x60; - пометить письмо; | [optional] 
**forward_to** | **object** | Адрес для пересылки при выбранном действии &#x60;forward&#x60; из параметра &#x60;action&#x60;. Не может быть пустым, если &#x60;action&#x60; выбран &#x60;forward&#x60; | [optional] 
**white_list** | **object** | Белый список адресов от которых письма не будут попадать в спам | [optional] 

## Example

```python
from openapi_client.models.spam_filter_is_disabled import SpamFilterIsDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of SpamFilterIsDisabled from a JSON string
spam_filter_is_disabled_instance = SpamFilterIsDisabled.from_json(json)
# print the JSON string representation of the object
print SpamFilterIsDisabled.to_json()

# convert the object into a dict
spam_filter_is_disabled_dict = spam_filter_is_disabled_instance.to_dict()
# create an instance of SpamFilterIsDisabled from a dict
spam_filter_is_disabled_form_dict = spam_filter_is_disabled.from_dict(spam_filter_is_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


