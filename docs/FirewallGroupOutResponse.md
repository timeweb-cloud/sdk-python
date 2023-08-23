# FirewallGroupOutResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**group** | [**FirewallGroupOutAPI**](FirewallGroupOutAPI.md) |  | 

## Example

```python
from timeweb_cloud_api.models.firewall_group_out_response import FirewallGroupOutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallGroupOutResponse from a JSON string
firewall_group_out_response_instance = FirewallGroupOutResponse.from_json(json)
# print the JSON string representation of the object
print FirewallGroupOutResponse.to_json()

# convert the object into a dict
firewall_group_out_response_dict = firewall_group_out_response_instance.to_dict()
# create an instance of FirewallGroupOutResponse from a dict
firewall_group_out_response_form_dict = firewall_group_out_response.from_dict(firewall_group_out_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


