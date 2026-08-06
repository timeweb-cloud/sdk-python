# ClearCache

Параметры очистки кэша

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purge_type** | **object** | Тип очистки. - &#x60;full&#x60; — очистить весь кэш ресурса; - &#x60;partial&#x60; — очистить кэш только по путям из &#x60;paths&#x60;. | 
**paths** | **object** | Список путей к файлам, кэш которых нужно очистить. Обязателен при &#x60;purge_type&#x60; &#x3D; &#x60;partial&#x60;. | [optional] 

## Example

```python
from timeweb_cloud_api.models.clear_cache import ClearCache

# TODO update the JSON string below
json = "{}"
# create an instance of ClearCache from a JSON string
clear_cache_instance = ClearCache.from_json(json)
# print the JSON string representation of the object
print ClearCache.to_json()

# convert the object into a dict
clear_cache_dict = clear_cache_instance.to_dict()
# create an instance of ClearCache from a dict
clear_cache_form_dict = clear_cache.from_dict(clear_cache_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


