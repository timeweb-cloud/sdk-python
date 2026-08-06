# ConfigCacheCdn

Кэш на узлах CDN. `null` — отключить кэширование на узлах CDN.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | [**ConfigCacheCdnTtl**](ConfigCacheCdnTtl.md) |  | 

## Example

```python
from timeweb_cloud_api.models.config_cache_cdn import ConfigCacheCdn

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigCacheCdn from a JSON string
config_cache_cdn_instance = ConfigCacheCdn.from_json(json)
# print the JSON string representation of the object
print ConfigCacheCdn.to_json()

# convert the object into a dict
config_cache_cdn_dict = config_cache_cdn_instance.to_dict()
# create an instance of ConfigCacheCdn from a dict
config_cache_cdn_form_dict = config_cache_cdn.from_dict(config_cache_cdn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


