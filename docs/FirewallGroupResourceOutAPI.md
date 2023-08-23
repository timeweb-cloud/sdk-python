# FirewallGroupResourceOutAPI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | resource id | 
**type** | [**ResourceType**](ResourceType.md) |  | 

## Example

```python
from openapi_client.models.firewall_group_resource_out_api import FirewallGroupResourceOutAPI

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallGroupResourceOutAPI from a JSON string
firewall_group_resource_out_api_instance = FirewallGroupResourceOutAPI.from_json(json)
# print the JSON string representation of the object
print FirewallGroupResourceOutAPI.to_json()

# convert the object into a dict
firewall_group_resource_out_api_dict = firewall_group_resource_out_api_instance.to_dict()
# create an instance of FirewallGroupResourceOutAPI from a dict
firewall_group_resource_out_api_form_dict = firewall_group_resource_out_api.from_dict(firewall_group_resource_out_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


