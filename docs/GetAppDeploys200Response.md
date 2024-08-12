# GetAppDeploys200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**deploys** | **object** |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.get_app_deploys200_response import GetAppDeploys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAppDeploys200Response from a JSON string
get_app_deploys200_response_instance = GetAppDeploys200Response.from_json(json)
# print the JSON string representation of the object
print GetAppDeploys200Response.to_json()

# convert the object into a dict
get_app_deploys200_response_dict = get_app_deploys200_response_instance.to_dict()
# create an instance of GetAppDeploys200Response from a dict
get_app_deploys200_response_form_dict = get_app_deploys200_response.from_dict(get_app_deploys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


