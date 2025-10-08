# ServiceServicePrice

Информация о стоимости вложенного сервиса

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Идентификатор сервиса | [optional] 
**cost** | **object** | Стоимость сервиса | [optional] 
**description** | **object** | Описание сервиса | [optional] 
**type** | [**ServiceCostType**](ServiceCostType.md) |  | [optional] 
**node_groups** | **object** | Группы узлов для Kubernetes кластера | [optional] 

## Example

```python
from timeweb_cloud_api.models.service_service_price import ServiceServicePrice

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceServicePrice from a JSON string
service_service_price_instance = ServiceServicePrice.from_json(json)
# print the JSON string representation of the object
print ServiceServicePrice.to_json()

# convert the object into a dict
service_service_price_dict = service_service_price_instance.to_dict()
# create an instance of ServiceServicePrice from a dict
service_service_price_form_dict = service_service_price.from_dict(service_service_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


