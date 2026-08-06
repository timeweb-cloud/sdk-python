# UpdateHttpResource

Параметры изменения CDN-ресурса. Передавайте только те поля, которые нужно изменить.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название CDN-ресурса. | [optional] 
**description** | **object** | Описание CDN-ресурса. | [optional] 
**preset_id** | **object** | ID тарифа CDN. Список доступных тарифов можно получить в &#x60;/api/v1/cdn/presets&#x60;. | [optional] 
**storage_id** | **object** | ID S3-хранилища, которое будет источником контента. Нельзя передавать вместе с &#x60;config.origin.servers&#x60;. | [optional] 
**traffic_limit_bytes** | **object** | Лимит исходящего трафика на расчетный месяц, в байтах. &#x60;null&#x60; — снять лимит. Если ресурс был остановлен по лимиту, при снятии или увеличении лимита раздача возобновится. | [optional] 
**config** | [**HttpResourceConfig**](HttpResourceConfig.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_http_resource import UpdateHttpResource

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateHttpResource from a JSON string
update_http_resource_instance = UpdateHttpResource.from_json(json)
# print the JSON string representation of the object
print UpdateHttpResource.to_json()

# convert the object into a dict
update_http_resource_dict = update_http_resource_instance.to_dict()
# create an instance of UpdateHttpResource from a dict
update_http_resource_form_dict = update_http_resource.from_dict(update_http_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


