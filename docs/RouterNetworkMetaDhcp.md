# RouterNetworkMetaDhcp

DHCP

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включен ли DHCP | 
**is_available** | **object** | Доступен ли DHCP | 

## Example

```python
from timeweb_cloud_api.models.router_network_meta_dhcp import RouterNetworkMetaDhcp

# TODO update the JSON string below
json = "{}"
# create an instance of RouterNetworkMetaDhcp from a JSON string
router_network_meta_dhcp_instance = RouterNetworkMetaDhcp.from_json(json)
# print the JSON string representation of the object
print RouterNetworkMetaDhcp.to_json()

# convert the object into a dict
router_network_meta_dhcp_dict = router_network_meta_dhcp_instance.to_dict()
# create an instance of RouterNetworkMetaDhcp from a dict
router_network_meta_dhcp_form_dict = router_network_meta_dhcp.from_dict(router_network_meta_dhcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


