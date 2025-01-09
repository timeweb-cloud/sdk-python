# FirewallGroupResource


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID ресурса. | 
**type** | [**ResourceType**](ResourceType.md) |  | 

## Example

```python
from timeweb_cloud_api.models.firewall_group_resource import FirewallGroupResource

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallGroupResource from a JSON string
firewall_group_resource_instance = FirewallGroupResource.from_json(json)
# print the JSON string representation of the object
print FirewallGroupResource.to_json()

# convert the object into a dict
firewall_group_resource_dict = firewall_group_resource_instance.to_dict()
# create an instance of FirewallGroupResource from a dict
firewall_group_resource_form_dict = firewall_group_resource.from_dict(firewall_group_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


