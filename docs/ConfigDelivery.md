# ConfigDelivery

Настройки раздачи контента

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**http3** | **object** | Раздавать контент по HTTP/3 (QUIC). | [optional] 
**gzip** | **object** | Сжимать ответы алгоритмом gzip. | [optional] 
**large_files** | **object** | Режим раздачи больших файлов. | [optional] 
**slice_size** | **object** | Размер слайса в мегабайтах — файл забирается с источника и кэшируется частями такого размера. &#x60;null&#x60; — не использовать слайсинг. | [optional] 
**image_optimization** | **object** | Оптимизировать изображения на лету. | [optional] 
**packaging** | [**ConfigDeliveryPackaging**](ConfigDeliveryPackaging.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_delivery import ConfigDelivery

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigDelivery from a JSON string
config_delivery_instance = ConfigDelivery.from_json(json)
# print the JSON string representation of the object
print ConfigDelivery.to_json()

# convert the object into a dict
config_delivery_dict = config_delivery_instance.to_dict()
# create an instance of ConfigDelivery from a dict
config_delivery_form_dict = config_delivery.from_dict(config_delivery_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


