# FirewallGroupResourceOutResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**resource** | [**FirewallGroupResourceOutAPI**](FirewallGroupResourceOutAPI.md) |  | 

## Example

```python
from timeweb_cloud_api.models.firewall_group_resource_out_response import FirewallGroupResourceOutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallGroupResourceOutResponse from a JSON string
firewall_group_resource_out_response_instance = FirewallGroupResourceOutResponse.from_json(json)
# print the JSON string representation of the object
print FirewallGroupResourceOutResponse.to_json()

# convert the object into a dict
firewall_group_resource_out_response_dict = firewall_group_resource_out_response_instance.to_dict()
# create an instance of FirewallGroupResourceOutResponse from a dict
firewall_group_resource_out_response_form_dict = firewall_group_resource_out_response.from_dict(firewall_group_resource_out_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


