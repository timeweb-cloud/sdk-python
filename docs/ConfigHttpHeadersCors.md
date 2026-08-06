# ConfigHttpHeadersCors

Настройки CORS. `null` — отключить CORS.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **object** | Домены, которым разрешены кросс-доменные запросы. Укажите &#x60;*&#x60;, чтобы разрешить все домены. | 
**always** | **object** | Отдавать CORS-заголовки во всех ответах, а не только при наличии заголовка &#x60;Origin&#x60; в запросе. | 

## Example

```python
from timeweb_cloud_api.models.config_http_headers_cors import ConfigHttpHeadersCors

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigHttpHeadersCors from a JSON string
config_http_headers_cors_instance = ConfigHttpHeadersCors.from_json(json)
# print the JSON string representation of the object
print ConfigHttpHeadersCors.to_json()

# convert the object into a dict
config_http_headers_cors_dict = config_http_headers_cors_instance.to_dict()
# create an instance of ConfigHttpHeadersCors from a dict
config_http_headers_cors_form_dict = config_http_headers_cors.from_dict(config_http_headers_cors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


