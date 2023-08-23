# GetServersPresets200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**server_presets** | **object** |  | 

## Example

```python
from openapi_client.models.get_servers_presets200_response import GetServersPresets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServersPresets200Response from a JSON string
get_servers_presets200_response_instance = GetServersPresets200Response.from_json(json)
# print the JSON string representation of the object
print GetServersPresets200Response.to_json()

# convert the object into a dict
get_servers_presets200_response_dict = get_servers_presets200_response_instance.to_dict()
# create an instance of GetServersPresets200Response from a dict
get_servers_presets200_response_form_dict = get_servers_presets200_response.from_dict(get_servers_presets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


