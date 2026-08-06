# PreloadCache

Параметры предварительной загрузки кэша

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paths** | **object** | Список путей к файлам, которые нужно заранее загрузить в кэш узлов CDN. | 

## Example

```python
from timeweb_cloud_api.models.preload_cache import PreloadCache

# TODO update the JSON string below
json = "{}"
# create an instance of PreloadCache from a JSON string
preload_cache_instance = PreloadCache.from_json(json)
# print the JSON string representation of the object
print PreloadCache.to_json()

# convert the object into a dict
preload_cache_dict = preload_cache_instance.to_dict()
# create an instance of PreloadCache from a dict
preload_cache_form_dict = preload_cache.from_dict(preload_cache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


