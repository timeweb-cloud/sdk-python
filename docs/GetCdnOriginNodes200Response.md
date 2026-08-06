# GetCdnOriginNodes200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**origin_nodes** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_cdn_origin_nodes200_response import GetCdnOriginNodes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCdnOriginNodes200Response from a JSON string
get_cdn_origin_nodes200_response_instance = GetCdnOriginNodes200Response.from_json(json)
# print the JSON string representation of the object
print GetCdnOriginNodes200Response.to_json()

# convert the object into a dict
get_cdn_origin_nodes200_response_dict = get_cdn_origin_nodes200_response_instance.to_dict()
# create an instance of GetCdnOriginNodes200Response from a dict
get_cdn_origin_nodes200_response_form_dict = get_cdn_origin_nodes200_response.from_dict(get_cdn_origin_nodes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


