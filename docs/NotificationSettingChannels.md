# NotificationSettingChannels

Каналы отправки уведомления.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | [**NotificationSettingChannel**](NotificationSettingChannel.md) |  | 
**sms** | [**NotificationSettingChannel**](NotificationSettingChannel.md) |  | 
**telegram** | [**NotificationSettingChannel**](NotificationSettingChannel.md) |  | 

## Example

```python
from openapi_client.models.notification_setting_channels import NotificationSettingChannels

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSettingChannels from a JSON string
notification_setting_channels_instance = NotificationSettingChannels.from_json(json)
# print the JSON string representation of the object
print NotificationSettingChannels.to_json()

# convert the object into a dict
notification_setting_channels_dict = notification_setting_channels_instance.to_dict()
# create an instance of NotificationSettingChannels from a dict
notification_setting_channels_form_dict = notification_setting_channels.from_dict(notification_setting_channels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


