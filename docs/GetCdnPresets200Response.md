# GetCdnPresets200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_resource_presets** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_cdn_presets200_response import GetCdnPresets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCdnPresets200Response from a JSON string
get_cdn_presets200_response_instance = GetCdnPresets200Response.from_json(json)
# print the JSON string representation of the object
print GetCdnPresets200Response.to_json()

# convert the object into a dict
get_cdn_presets200_response_dict = get_cdn_presets200_response_instance.to_dict()
# create an instance of GetCdnPresets200Response from a dict
get_cdn_presets200_response_form_dict = get_cdn_presets200_response.from_dict(get_cdn_presets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


