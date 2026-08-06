# ConfigCache

Настройки кэширования

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdn** | [**ConfigCacheCdn**](ConfigCacheCdn.md) |  | [optional] 
**browser** | [**ConfigCacheBrowser**](ConfigCacheBrowser.md) |  | [optional] 
**always_online** | [**ConfigCacheAlwaysOnline**](ConfigCacheAlwaysOnline.md) |  | [optional] 
**query_args** | [**ConfigCacheQueryArgs**](ConfigCacheQueryArgs.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_cache import ConfigCache

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigCache from a JSON string
config_cache_instance = ConfigCache.from_json(json)
# print the JSON string representation of the object
print ConfigCache.to_json()

# convert the object into a dict
config_cache_dict = config_cache_instance.to_dict()
# create an instance of ConfigCache from a dict
config_cache_form_dict = config_cache.from_dict(config_cache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


