# ConfigCacheCdnTtl

Время жизни кэша по классам HTTP-статуса ответа источника, в секундах.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_2xx** | **object** | Время жизни кэша для ответов со статусом 2xx, в секундах. | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_cache_cdn_ttl import ConfigCacheCdnTtl

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigCacheCdnTtl from a JSON string
config_cache_cdn_ttl_instance = ConfigCacheCdnTtl.from_json(json)
# print the JSON string representation of the object
print ConfigCacheCdnTtl.to_json()

# convert the object into a dict
config_cache_cdn_ttl_dict = config_cache_cdn_ttl_instance.to_dict()
# create an instance of ConfigCacheCdnTtl from a dict
config_cache_cdn_ttl_form_dict = config_cache_cdn_ttl.from_dict(config_cache_cdn_ttl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


