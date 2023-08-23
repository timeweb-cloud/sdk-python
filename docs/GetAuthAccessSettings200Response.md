# GetAuthAccessSettings200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_ip_restrictions_enabled** | **object** | Это логическое значение, которое показывает, включено ли ограничение доступа по IP-адресу. | 
**is_country_restrictions_enabled** | **object** | Это логическое значение, которое показывает, включено ли ограничение доступа по стране. | 
**white_list** | [**GetAuthAccessSettings200ResponseWhiteList**](GetAuthAccessSettings200ResponseWhiteList.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_auth_access_settings200_response import GetAuthAccessSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthAccessSettings200Response from a JSON string
get_auth_access_settings200_response_instance = GetAuthAccessSettings200Response.from_json(json)
# print the JSON string representation of the object
print GetAuthAccessSettings200Response.to_json()

# convert the object into a dict
get_auth_access_settings200_response_dict = get_auth_access_settings200_response_instance.to_dict()
# create an instance of GetAuthAccessSettings200Response from a dict
get_auth_access_settings200_response_form_dict = get_auth_access_settings200_response.from_dict(get_auth_access_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


