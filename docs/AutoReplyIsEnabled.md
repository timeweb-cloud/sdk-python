# AutoReplyIsEnabled


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включен ли автоответчик на входящие письма | [optional] 
**message** | **object** | Сообщение автоответчика на входящие письма. \\  Если передан параметр &#x60;is_enabled&#x60;: &#x60;false&#x60;, то значение передавать нельзя | [optional] 
**subject** | **object** | Тема сообщения автоответчика на входящие письма. \\  Если передан параметр &#x60;is_enabled&#x60;: &#x60;false&#x60;, то значение передавать нельзя | [optional] 

## Example

```python
from timeweb_cloud_api.models.auto_reply_is_enabled import AutoReplyIsEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of AutoReplyIsEnabled from a JSON string
auto_reply_is_enabled_instance = AutoReplyIsEnabled.from_json(json)
# print the JSON string representation of the object
print AutoReplyIsEnabled.to_json()

# convert the object into a dict
auto_reply_is_enabled_dict = auto_reply_is_enabled_instance.to_dict()
# create an instance of AutoReplyIsEnabled from a dict
auto_reply_is_enabled_form_dict = auto_reply_is_enabled.from_dict(auto_reply_is_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


