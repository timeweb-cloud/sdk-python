# ConfigCacheBrowser

Кэш в браузере пользователя. `null` — отключить браузерное кэширование.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ttl** | **object** | Время жизни кэша в браузере, в секундах. | 

## Example

```python
from timeweb_cloud_api.models.config_cache_browser import ConfigCacheBrowser

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigCacheBrowser from a JSON string
config_cache_browser_instance = ConfigCacheBrowser.from_json(json)
# print the JSON string representation of the object
print ConfigCacheBrowser.to_json()

# convert the object into a dict
config_cache_browser_dict = config_cache_browser_instance.to_dict()
# create an instance of ConfigCacheBrowser from a dict
config_cache_browser_form_dict = config_cache_browser.from_dict(config_cache_browser_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


