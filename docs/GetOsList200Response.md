# GetOsList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**servers_os** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.get_os_list200_response import GetOsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetOsList200Response from a JSON string
get_os_list200_response_instance = GetOsList200Response.from_json(json)
# print the JSON string representation of the object
print GetOsList200Response.to_json()

# convert the object into a dict
get_os_list200_response_dict = get_os_list200_response_instance.to_dict()
# create an instance of GetOsList200Response from a dict
get_os_list200_response_form_dict = get_os_list200_response.from_dict(get_os_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


