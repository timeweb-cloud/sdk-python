# ConfigOrigin

Настройки источника контента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**servers** | **object** | Origin-серверы, с которых CDN забирает контент. Передача этого поля переключает ресурс с S3-хранилища на origin-сервер. | [optional] 
**use_https** | **object** | Обращаться к источнику контента по HTTPS. | [optional] 
**aws** | [**ConfigOriginAws**](ConfigOriginAws.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_origin import ConfigOrigin

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigOrigin from a JSON string
config_origin_instance = ConfigOrigin.from_json(json)
# print the JSON string representation of the object
print ConfigOrigin.to_json()

# convert the object into a dict
config_origin_dict = config_origin_instance.to_dict()
# create an instance of ConfigOrigin from a dict
config_origin_form_dict = config_origin.from_dict(config_origin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


