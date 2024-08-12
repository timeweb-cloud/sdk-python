# GetApps200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**apps** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.get_apps200_response import GetApps200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetApps200Response from a JSON string
get_apps200_response_instance = GetApps200Response.from_json(json)
# print the JSON string representation of the object
print GetApps200Response.to_json()

# convert the object into a dict
get_apps200_response_dict = get_apps200_response_instance.to_dict()
# create an instance of GetApps200Response from a dict
get_apps200_response_form_dict = get_apps200_response.from_dict(get_apps200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


