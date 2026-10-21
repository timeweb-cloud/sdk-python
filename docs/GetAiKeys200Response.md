# GetAiKeys200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ai_keys** | **object** |  | 
**meta** | [**GetAiKeys200ResponseMeta**](GetAiKeys200ResponseMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_ai_keys200_response import GetAiKeys200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAiKeys200Response from a JSON string
get_ai_keys200_response_instance = GetAiKeys200Response.from_json(json)
# print the JSON string representation of the object
print GetAiKeys200Response.to_json()

# convert the object into a dict
get_ai_keys200_response_dict = get_ai_keys200_response_instance.to_dict()
# create an instance of GetAiKeys200Response from a dict
get_ai_keys200_response_form_dict = get_ai_keys200_response.from_dict(get_ai_keys200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


