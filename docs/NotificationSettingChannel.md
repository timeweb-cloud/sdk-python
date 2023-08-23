# NotificationSettingChannel

Строка состояния, указывающая состояние уведомления. Может быть «on», «off», «disabled_on» или «disabled_off».

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from timeweb_cloud_api.models.notification_setting_channel import NotificationSettingChannel

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSettingChannel from a JSON string
notification_setting_channel_instance = NotificationSettingChannel.from_json(json)
# print the JSON string representation of the object
print NotificationSettingChannel.to_json()

# convert the object into a dict
notification_setting_channel_dict = notification_setting_channel_instance.to_dict()
# create an instance of NotificationSettingChannel from a dict
notification_setting_channel_form_dict = notification_setting_channel.from_dict(notification_setting_channel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


