# ConfigHttpHeaders

Настройки HTTP-заголовков

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request** | **Dict[str, object]** | Статические заголовки, которые CDN добавляет к запросам на источник контента. Имена заголовков могут содержать символы &#x60;A-Za-z0-9-_.*()&#x3D;/;&#x60;, значения — печатные ASCII-символы. &#x60;null&#x60; — удалить все заголовки. | [optional] 
**cors** | [**ConfigHttpHeadersCors**](ConfigHttpHeadersCors.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_http_headers import ConfigHttpHeaders

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigHttpHeaders from a JSON string
config_http_headers_instance = ConfigHttpHeaders.from_json(json)
# print the JSON string representation of the object
print ConfigHttpHeaders.to_json()

# convert the object into a dict
config_http_headers_dict = config_http_headers_instance.to_dict()
# create an instance of ConfigHttpHeaders from a dict
config_http_headers_form_dict = config_http_headers.from_dict(config_http_headers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


