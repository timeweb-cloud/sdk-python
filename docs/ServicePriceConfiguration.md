# ServicePriceConfiguration

Конфигурация сервиса

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | **object** | Количество ядер процессора | [optional] 
**ram** | **object** | Объем оперативной памяти в МБ | [optional] 
**disk** | **object** | Объем дискового пространства в ГБ | [optional] 

## Example

```python
from timeweb_cloud_api.models.service_price_configuration import ServicePriceConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of ServicePriceConfiguration from a JSON string
service_price_configuration_instance = ServicePriceConfiguration.from_json(json)
# print the JSON string representation of the object
print ServicePriceConfiguration.to_json()

# convert the object into a dict
service_price_configuration_dict = service_price_configuration_instance.to_dict()
# create an instance of ServicePriceConfiguration from a dict
service_price_configuration_form_dict = service_price_configuration.from_dict(service_price_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


