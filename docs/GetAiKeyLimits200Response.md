# GetAiKeyLimits200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_key_entity_limits** | **object** |  | 
**meta** | [**GetAiKeyLimits200ResponseMeta**](GetAiKeyLimits200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_ai_key_limits200_response import GetAiKeyLimits200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAiKeyLimits200Response from a JSON string
get_ai_key_limits200_response_instance = GetAiKeyLimits200Response.from_json(json)
# print the JSON string representation of the object
print GetAiKeyLimits200Response.to_json()

# convert the object into a dict
get_ai_key_limits200_response_dict = get_ai_key_limits200_response_instance.to_dict()
# create an instance of GetAiKeyLimits200Response from a dict
get_ai_key_limits200_response_form_dict = get_ai_key_limits200_response.from_dict(get_ai_key_limits200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


