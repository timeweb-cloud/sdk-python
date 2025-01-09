# FirewallGroupsOutResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса. | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**groups** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.firewall_groups_out_response import FirewallGroupsOutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallGroupsOutResponse from a JSON string
firewall_groups_out_response_instance = FirewallGroupsOutResponse.from_json(json)
# print the JSON string representation of the object
print FirewallGroupsOutResponse.to_json()

# convert the object into a dict
firewall_groups_out_response_dict = firewall_groups_out_response_instance.to_dict()
# create an instance of FirewallGroupsOutResponse from a dict
firewall_groups_out_response_form_dict = firewall_groups_out_response.from_dict(firewall_groups_out_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


