# GetDeploySettings200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_deploy_settings** | **object** |  | [optional] 
**meta** | [**Meta**](Meta.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.get_deploy_settings200_response import GetDeploySettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeploySettings200Response from a JSON string
get_deploy_settings200_response_instance = GetDeploySettings200Response.from_json(json)
# print the JSON string representation of the object
print GetDeploySettings200Response.to_json()

# convert the object into a dict
get_deploy_settings200_response_dict = get_deploy_settings200_response_instance.to_dict()
# create an instance of GetDeploySettings200Response from a dict
get_deploy_settings200_response_form_dict = get_deploy_settings200_response.from_dict(get_deploy_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


