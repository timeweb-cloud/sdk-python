# GetCdnResources200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http_resources** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_cdn_resources200_response import GetCdnResources200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCdnResources200Response from a JSON string
get_cdn_resources200_response_instance = GetCdnResources200Response.from_json(json)
# print the JSON string representation of the object
print GetCdnResources200Response.to_json()

# convert the object into a dict
get_cdn_resources200_response_dict = get_cdn_resources200_response_instance.to_dict()
# create an instance of GetCdnResources200Response from a dict
get_cdn_resources200_response_form_dict = get_cdn_resources200_response.from_dict(get_cdn_resources200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


