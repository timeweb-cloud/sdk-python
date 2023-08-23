# GetAuthAccessSettings200ResponseWhiteList


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **object** | Список разрешенных IP-адресов. | 
**countries** | **object** | Список разрешенных стран. | 

## Example

```python
from timeweb_cloud_api.models.get_auth_access_settings200_response_white_list import GetAuthAccessSettings200ResponseWhiteList

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthAccessSettings200ResponseWhiteList from a JSON string
get_auth_access_settings200_response_white_list_instance = GetAuthAccessSettings200ResponseWhiteList.from_json(json)
# print the JSON string representation of the object
print GetAuthAccessSettings200ResponseWhiteList.to_json()

# convert the object into a dict
get_auth_access_settings200_response_white_list_dict = get_auth_access_settings200_response_white_list_instance.to_dict()
# create an instance of GetAuthAccessSettings200ResponseWhiteList from a dict
get_auth_access_settings200_response_white_list_form_dict = get_auth_access_settings200_response_white_list.from_dict(get_auth_access_settings200_response_white_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


