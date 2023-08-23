# UpdateNotificationSettingsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | **object** | Настройки каналов уведомлений. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_notification_settings_request import UpdateNotificationSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateNotificationSettingsRequest from a JSON string
update_notification_settings_request_instance = UpdateNotificationSettingsRequest.from_json(json)
# print the JSON string representation of the object
print UpdateNotificationSettingsRequest.to_json()

# convert the object into a dict
update_notification_settings_request_dict = update_notification_settings_request_instance.to_dict()
# create an instance of UpdateNotificationSettingsRequest from a dict
update_notification_settings_request_form_dict = update_notification_settings_request.from_dict(update_notification_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


