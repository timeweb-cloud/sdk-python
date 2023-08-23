# AutoReplyIsDisabled


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включен ли автоответчик на входящие письма | 
**message** | **object** | Сообщение автоответчика на входящие письма | [optional] 
**subject** | **object** | Тема сообщения автоответчика на входящие письма. | [optional] 

## Example

```python
from openapi_client.models.auto_reply_is_disabled import AutoReplyIsDisabled

# TODO update the JSON string below
json = "{}"
# create an instance of AutoReplyIsDisabled from a JSON string
auto_reply_is_disabled_instance = AutoReplyIsDisabled.from_json(json)
# print the JSON string representation of the object
print AutoReplyIsDisabled.to_json()

# convert the object into a dict
auto_reply_is_disabled_dict = auto_reply_is_disabled_instance.to_dict()
# create an instance of AutoReplyIsDisabled from a dict
auto_reply_is_disabled_form_dict = auto_reply_is_disabled.from_dict(auto_reply_is_disabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


