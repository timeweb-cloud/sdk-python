# HttpResourceConfig

Конфигурация CDN-ресурса. Все секции необязательны: при изменении конфигурации переданные поля накладываются на текущие значения, а непереданные остаются без изменений.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery** | [**ConfigDelivery**](ConfigDelivery.md) |  | [optional] 
**cache** | [**ConfigCache**](ConfigCache.md) |  | [optional] 
**origin** | [**ConfigOrigin**](ConfigOrigin.md) |  | [optional] 
**security** | [**ConfigSecurity**](ConfigSecurity.md) |  | [optional] 
**http_headers** | [**ConfigHttpHeaders**](ConfigHttpHeaders.md) |  | [optional] 
**access** | [**ConfigAccess**](ConfigAccess.md) |  | [optional] 
**domains** | [**ConfigDomains**](ConfigDomains.md) |  | [optional] 
**robots** | [**ConfigRobots**](ConfigRobots.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.http_resource_config import HttpResourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HttpResourceConfig from a JSON string
http_resource_config_instance = HttpResourceConfig.from_json(json)
# print the JSON string representation of the object
print HttpResourceConfig.to_json()

# convert the object into a dict
http_resource_config_dict = http_resource_config_instance.to_dict()
# create an instance of HttpResourceConfig from a dict
http_resource_config_form_dict = http_resource_config.from_dict(http_resource_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


