# NetworkOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID сети | 
**name** | **object** | Имя сети | 
**subnet** | **object** | Подсеть | 
**nat_ip** | **object** | IP-адрес NAT | 
**gateway** | **object** | Шлюз | 
**reserved_ips** | **object** | Зарезервированные IP-адреса | 
**dhcp** | [**RouterNetworkMetaDhcp**](RouterNetworkMetaDhcp.md) |  | 
**busy_addresses** | **object** | Занятые IP-адреса | 

## Example

```python
from timeweb_cloud_api.models.network_out import NetworkOut

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkOut from a JSON string
network_out_instance = NetworkOut.from_json(json)
# print the JSON string representation of the object
print NetworkOut.to_json()

# convert the object into a dict
network_out_dict = network_out_instance.to_dict()
# create an instance of NetworkOut from a dict
network_out_form_dict = network_out.from_dict(network_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


