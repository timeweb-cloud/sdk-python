# ServicePrice

Информация о стоимости сервиса

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cost** | **object** | Стоимость сервиса | 
**total_cost** | **object** | Общая стоимость сервиса с учетом всех дополнительных услуг | 
**type** | [**ServicePriceType**](ServicePriceType.md) |  | 
**service_id** | **object** | Идентификатор сервиса | [optional] 
**project_id** | **object** | Идентификатор проекта | [optional] 
**services** | **object** | Список вложенных сервисов | [optional] 
**info** | [**InfoServicePrice**](InfoServicePrice.md) |  | [optional] 
**configuration** | [**ServicePriceConfiguration**](ServicePriceConfiguration.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.service_price import ServicePrice

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePrice from a JSON string
service_price_instance = ServicePrice.from_json(json)
# print the JSON string representation of the object
print ServicePrice.to_json()

# convert the object into a dict
service_price_dict = service_price_instance.to_dict()
# create an instance of ServicePrice from a dict
service_price_form_dict = service_price.from_dict(service_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


