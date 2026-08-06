# ConfigCacheAlwaysOnline

Отдавать устаревший контент из кэша, если источник недоступен. `null` — отключить.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stale_conditions** | **object** | Условия, при которых из кэша отдается устаревший контент. | 

## Example

```python
from timeweb_cloud_api.models.config_cache_always_online import ConfigCacheAlwaysOnline

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigCacheAlwaysOnline from a JSON string
config_cache_always_online_instance = ConfigCacheAlwaysOnline.from_json(json)
# print the JSON string representation of the object
print ConfigCacheAlwaysOnline.to_json()

# convert the object into a dict
config_cache_always_online_dict = config_cache_always_online_instance.to_dict()
# create an instance of ConfigCacheAlwaysOnline from a dict
config_cache_always_online_form_dict = config_cache_always_online.from_dict(config_cache_always_online_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


