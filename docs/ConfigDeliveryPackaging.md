# ConfigDeliveryPackaging

Упаковка видео в потоковые форматы. `null` — отключить упаковку.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mp4** | [**ConfigDeliveryPackagingMp4**](ConfigDeliveryPackagingMp4.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.config_delivery_packaging import ConfigDeliveryPackaging

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigDeliveryPackaging from a JSON string
config_delivery_packaging_instance = ConfigDeliveryPackaging.from_json(json)
# print the JSON string representation of the object
print ConfigDeliveryPackaging.to_json()

# convert the object into a dict
config_delivery_packaging_dict = config_delivery_packaging_instance.to_dict()
# create an instance of ConfigDeliveryPackaging from a dict
config_delivery_packaging_form_dict = config_delivery_packaging.from_dict(config_delivery_packaging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


