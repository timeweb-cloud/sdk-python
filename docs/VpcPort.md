# VpcPort


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Идентификатор порта. | 
**nat_mode** | **object** | Тип преобразования сетевых адресов. | 
**mac** | **object** | MAC адрес. | 
**ipv4** | **object** | Внутренний адрес. | 
**service** | [**VpcPortService**](VpcPortService.md) |  | 

## Example

```python
from timeweb_cloud_api.models.vpc_port import VpcPort

# TODO update the JSON string below
json = "{}"
# create an instance of VpcPort from a JSON string
vpc_port_instance = VpcPort.from_json(json)
# print the JSON string representation of the object
print VpcPort.to_json()

# convert the object into a dict
vpc_port_dict = vpc_port_instance.to_dict()
# create an instance of VpcPort from a dict
vpc_port_form_dict = vpc_port.from_dict(vpc_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


