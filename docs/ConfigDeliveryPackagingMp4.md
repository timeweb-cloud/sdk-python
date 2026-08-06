# ConfigDeliveryPackagingMp4

Упаковка MP4-файлов. `null` — отключить упаковку MP4.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_protocols** | **object** | Протоколы, в которые упаковывается исходный MP4. | 

## Example

```python
from timeweb_cloud_api.models.config_delivery_packaging_mp4 import ConfigDeliveryPackagingMp4

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigDeliveryPackagingMp4 from a JSON string
config_delivery_packaging_mp4_instance = ConfigDeliveryPackagingMp4.from_json(json)
# print the JSON string representation of the object
print ConfigDeliveryPackagingMp4.to_json()

# convert the object into a dict
config_delivery_packaging_mp4_dict = config_delivery_packaging_mp4_instance.to_dict()
# create an instance of ConfigDeliveryPackagingMp4 from a dict
config_delivery_packaging_mp4_form_dict = config_delivery_packaging_mp4.from_dict(config_delivery_packaging_mp4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


