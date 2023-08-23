# NotificationSetting

Статус аккаунта

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**NotificationSettingChannels**](NotificationSettingChannels.md) |  | 
**group** | **object** | Строка, указывающая название группы уведомления. Может быть «security», «monitoring» или «finances». | 
**type** | [**NotificationSettingType**](NotificationSettingType.md) |  | 

## Example

```python
from timeweb_cloud_api.models.notification_setting import NotificationSetting

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSetting from a JSON string
notification_setting_instance = NotificationSetting.from_json(json)
# print the JSON string representation of the object
print NotificationSetting.to_json()

# convert the object into a dict
notification_setting_dict = notification_setting_instance.to_dict()
# create an instance of NotificationSetting from a dict
notification_setting_form_dict = notification_setting.from_dict(notification_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


