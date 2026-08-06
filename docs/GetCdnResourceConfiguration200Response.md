# GetCdnResourceConfiguration200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_resource_configuration** | [**HttpResourceConfig**](HttpResourceConfig.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_cdn_resource_configuration200_response import GetCdnResourceConfiguration200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCdnResourceConfiguration200Response from a JSON string
get_cdn_resource_configuration200_response_instance = GetCdnResourceConfiguration200Response.from_json(json)
# print the JSON string representation of the object
print GetCdnResourceConfiguration200Response.to_json()

# convert the object into a dict
get_cdn_resource_configuration200_response_dict = get_cdn_resource_configuration200_response_instance.to_dict()
# create an instance of GetCdnResourceConfiguration200Response from a dict
get_cdn_resource_configuration200_response_form_dict = get_cdn_resource_configuration200_response.from_dict(get_cdn_resource_configuration200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


