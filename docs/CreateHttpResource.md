# CreateHttpResource

Параметры создания CDN-ресурса. Источник контента задается ровно одним из полей: `storage_id` или `server`.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название CDN-ресурса. | 
**preset_id** | **object** | ID тарифа CDN. Список доступных тарифов можно получить в &#x60;/api/v1/cdn/presets&#x60;. | 
**description** | **object** | Описание CDN-ресурса. | [optional] 
**storage_id** | **object** | ID S3-хранилища, которое будет источником контента. Нельзя передавать вместе с &#x60;server&#x60;. | [optional] 
**server** | [**OriginServer**](OriginServer.md) |  | [optional] 
**use_https** | **object** | Обращаться к источнику контента по HTTPS. | [optional] 
**delivery_domain** | **object** | Собственный домен, с которого будет раздаваться контент. Домен добавляется к техническому домену ресурса, для его работы нужно направить CNAME-запись на &#x60;cdn_domain&#x60;. | [optional] 
**project_id** | **object** | ID проекта, в который нужно поместить ресурс. Если не указан, ресурс попадет в проект по умолчанию. | [optional] 
**traffic_limit_bytes** | **object** | Лимит исходящего трафика на расчетный месяц, в байтах. При достижении лимита раздача останавливается автоматически. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_http_resource import CreateHttpResource

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHttpResource from a JSON string
create_http_resource_instance = CreateHttpResource.from_json(json)
# print the JSON string representation of the object
print CreateHttpResource.to_json()

# convert the object into a dict
create_http_resource_dict = create_http_resource_instance.to_dict()
# create an instance of CreateHttpResource from a dict
create_http_resource_form_dict = create_http_resource.from_dict(create_http_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


