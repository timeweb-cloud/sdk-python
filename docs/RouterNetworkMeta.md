# RouterNetworkMeta


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID сети | 
**name** | **object** | Имя сети | 
**nat_ip** | **object** | IP-адрес NAT | 
**gateway** | **object** | Шлюз | 
**dhcp** | [**RouterNetworkMetaDhcp**](RouterNetworkMetaDhcp.md) |  | 

## Example

```python
from timeweb_cloud_api.models.router_network_meta import RouterNetworkMeta

# TODO update the JSON string below
json = "{}"
# create an instance of RouterNetworkMeta from a JSON string
router_network_meta_instance = RouterNetworkMeta.from_json(json)
# print the JSON string representation of the object
print RouterNetworkMeta.to_json()

# convert the object into a dict
router_network_meta_dict = router_network_meta_instance.to_dict()
# create an instance of RouterNetworkMeta from a dict
router_network_meta_form_dict = router_network_meta.from_dict(router_network_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


