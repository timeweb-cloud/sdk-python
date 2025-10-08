# InfoServicePrice

Дополнительная информация о сервисе

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название сервиса | [optional] 
**description** | **object** | Описание сервиса | [optional] 
**is_mounted** | **object** | Флаг, указывающий, подключен ли сервис | [optional] 
**size** | **object** | Размер в ГБ | [optional] 
**type** | **object** | Тип кластера базы данных | [optional] 
**count** | **object** | Количество | [optional] 

## Example

```python
from timeweb_cloud_api.models.info_service_price import InfoServicePrice

# TODO update the JSON string below
json = "{}"
# create an instance of InfoServicePrice from a JSON string
info_service_price_instance = InfoServicePrice.from_json(json)
# print the JSON string representation of the object
print InfoServicePrice.to_json()

# convert the object into a dict
info_service_price_dict = info_service_price_instance.to_dict()
# create an instance of InfoServicePrice from a dict
info_service_price_form_dict = info_service_price.from_dict(info_service_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


