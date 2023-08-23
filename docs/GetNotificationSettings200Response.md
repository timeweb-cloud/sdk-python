# GetNotificationSettings200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_settings** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openapi_client.models.get_notification_settings200_response import GetNotificationSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotificationSettings200Response from a JSON string
get_notification_settings200_response_instance = GetNotificationSettings200Response.from_json(json)
# print the JSON string representation of the object
print GetNotificationSettings200Response.to_json()

# convert the object into a dict
get_notification_settings200_response_dict = get_notification_settings200_response_instance.to_dict()
# create an instance of GetNotificationSettings200Response from a dict
get_notification_settings200_response_form_dict = get_notification_settings200_response.from_dict(get_notification_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


