# GetDedicatedServersPresets200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**dedicated_servers_presets** | **object** |  | 

## Example

```python
from openapi_client.models.get_dedicated_servers_presets200_response import GetDedicatedServersPresets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDedicatedServersPresets200Response from a JSON string
get_dedicated_servers_presets200_response_instance = GetDedicatedServersPresets200Response.from_json(json)
# print the JSON string representation of the object
print GetDedicatedServersPresets200Response.to_json()

# convert the object into a dict
get_dedicated_servers_presets200_response_dict = get_dedicated_servers_presets200_response_instance.to_dict()
# create an instance of GetDedicatedServersPresets200Response from a dict
get_dedicated_servers_presets200_response_form_dict = get_dedicated_servers_presets200_response.from_dict(get_dedicated_servers_presets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


