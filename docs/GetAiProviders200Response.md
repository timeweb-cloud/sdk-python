# GetAiProviders200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**providers** | **object** |  | 
**meta** | [**GetAiProviders200ResponseMeta**](GetAiProviders200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_ai_providers200_response import GetAiProviders200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAiProviders200Response from a JSON string
get_ai_providers200_response_instance = GetAiProviders200Response.from_json(json)
# print the JSON string representation of the object
print GetAiProviders200Response.to_json()

# convert the object into a dict
get_ai_providers200_response_dict = get_ai_providers200_response_instance.to_dict()
# create an instance of GetAiProviders200Response from a dict
get_ai_providers200_response_form_dict = get_ai_providers200_response.from_dict(get_ai_providers200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


