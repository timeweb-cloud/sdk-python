# GetModels200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **object** |  | 
**meta** | [**GetModels200ResponseMeta**](GetModels200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_models200_response import GetModels200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetModels200Response from a JSON string
get_models200_response_instance = GetModels200Response.from_json(json)
# print the JSON string representation of the object
print GetModels200Response.to_json()

# convert the object into a dict
get_models200_response_dict = get_models200_response_instance.to_dict()
# create an instance of GetModels200Response from a dict
get_models200_response_form_dict = get_models200_response.from_dict(get_models200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


