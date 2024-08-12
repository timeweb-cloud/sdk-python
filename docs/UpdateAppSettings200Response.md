# UpdateAppSettings200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | [**App**](App.md) |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.update_app_settings200_response import UpdateAppSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAppSettings200Response from a JSON string
update_app_settings200_response_instance = UpdateAppSettings200Response.from_json(json)
# print the JSON string representation of the object
print UpdateAppSettings200Response.to_json()

# convert the object into a dict
update_app_settings200_response_dict = update_app_settings200_response_instance.to_dict()
# create an instance of UpdateAppSettings200Response from a dict
update_app_settings200_response_form_dict = update_app_settings200_response.from_dict(update_app_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


