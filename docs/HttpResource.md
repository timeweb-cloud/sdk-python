# HttpResource

CDN-ресурс

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID CDN-ресурса. Генерируется автоматически при создании. | 
**name** | **object** | Название CDN-ресурса. | 
**description** | **object** | Описание CDN-ресурса. | [optional] 
**source** | **object** | Источник контента: имя S3-бакета, если ресурс создан поверх хранилища, либо хост origin-сервера. | 
**traffic_usage** | [**TrafficUsage**](TrafficUsage.md) |  | 
**status** | **object** | Статус CDN-ресурса. - &#x60;created&#x60; — ресурс создан и раздает контент; - &#x60;processing&#x60; — конфигурация применяется на стороне CDN; - &#x60;stopped&#x60; — раздача приостановлена; - &#x60;failed&#x60; — настройка ресурса завершилась с ошибкой; - &#x60;no_paid&#x60; — ресурс не оплачен; - &#x60;blocked&#x60; — ресурс заблокирован; - &#x60;traffic_limit_exceeded&#x60; — раздача остановлена автоматически из-за достижения лимита трафика &#x60;traffic_limit_bytes&#x60;. | 
**cdn_domain** | **object** | Технический домен, выданный ресурсу. Доступен сразу после создания и всегда остается в списке доменов ресурса. | 
**preset_id** | **object** | ID тарифа CDN. Список доступных тарифов можно получить в &#x60;/api/v1/cdn/presets&#x60;. | 
**project_id** | **object** | ID проекта, к которому привязан ресурс. | [optional] 
**avatar_link** | **object** | Ссылка на аватар ресурса. | [optional] 
**storage_id** | **object** | ID S3-хранилища, которое используется в качестве источника контента. &#x60;null&#x60;, если источником является origin-сервер. | [optional] 
**traffic_limit_bytes** | **object** | Лимит исходящего трафика на расчетный месяц, в байтах. При достижении лимита раздача останавливается, а ресурс переходит в статус &#x60;traffic_limit_exceeded&#x60;. &#x60;null&#x60; — лимит не задан. | [optional] 

## Example

```python
from timeweb_cloud_api.models.http_resource import HttpResource

# TODO update the JSON string below
json = "{}"
# create an instance of HttpResource from a JSON string
http_resource_instance = HttpResource.from_json(json)
# print the JSON string representation of the object
print HttpResource.to_json()

# convert the object into a dict
http_resource_dict = http_resource_instance.to_dict()
# create an instance of HttpResource from a dict
http_resource_form_dict = http_resource.from_dict(http_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


