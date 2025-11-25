# ForwardIsEnabled


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включена ли пересылка входящих писем | 
**forward_list** | **object** | Список адресов для пересылки. \\  Если передан параметр &#x60;is_enabled&#x60;: &#x60;false&#x60;, то значение передавать нельзя | 
**is_leave_messages** | **object** | Оставлять ли копии входящих писем в почтовом ящике (не удалять). \\  При &#x60;is_leave_messages&#x60;: &#x60;true&#x60;— копии входящих писем не сохраняются и будут удаляться. \\  При &#x60;is_leave_messages&#x60;: &#x60;false&#x60; — копии входящих писем сохраняются. \\ \\  Если передан параметр &#x60;is_enabled&#x60;: &#x60;false&#x60;, то значение передавать нельзя | [optional] 

## Example

```python
from timeweb_cloud_api.models.forward_is_enabled import ForwardIsEnabled

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardIsEnabled from a JSON string
forward_is_enabled_instance = ForwardIsEnabled.from_json(json)
# print the JSON string representation of the object
print ForwardIsEnabled.to_json()

# convert the object into a dict
forward_is_enabled_dict = forward_is_enabled_instance.to_dict()
# create an instance of ForwardIsEnabled from a dict
forward_is_enabled_form_dict = forward_is_enabled.from_dict(forward_is_enabled_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


