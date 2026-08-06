# ConfigCacheQueryArgs

Правила учета query-параметров в ключе кэша. `null` — не учитывать query-параметры.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **object** | Режим учета query-параметров. - &#x60;all&#x60; — учитывать все параметры; - &#x60;whitelist&#x60; — учитывать только параметры из &#x60;list&#x60;; - &#x60;blacklist&#x60; — учитывать все параметры, кроме перечисленных в &#x60;list&#x60;. | 
**list** | **object** | Список query-параметров для режимов &#x60;whitelist&#x60; и &#x60;blacklist&#x60;. | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_cache_query_args import ConfigCacheQueryArgs

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigCacheQueryArgs from a JSON string
config_cache_query_args_instance = ConfigCacheQueryArgs.from_json(json)
# print the JSON string representation of the object
print ConfigCacheQueryArgs.to_json()

# convert the object into a dict
config_cache_query_args_dict = config_cache_query_args_instance.to_dict()
# create an instance of ConfigCacheQueryArgs from a dict
config_cache_query_args_form_dict = config_cache_query_args.from_dict(config_cache_query_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


