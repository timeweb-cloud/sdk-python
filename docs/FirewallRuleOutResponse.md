# FirewallRuleOutResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**rule** | [**FirewallRuleOutAPI**](FirewallRuleOutAPI.md) |  | 

## Example

```python
from timeweb_cloud_api.models.firewall_rule_out_response import FirewallRuleOutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRuleOutResponse from a JSON string
firewall_rule_out_response_instance = FirewallRuleOutResponse.from_json(json)
# print the JSON string representation of the object
print FirewallRuleOutResponse.to_json()

# convert the object into a dict
firewall_rule_out_response_dict = firewall_rule_out_response_instance.to_dict()
# create an instance of FirewallRuleOutResponse from a dict
firewall_rule_out_response_form_dict = firewall_rule_out_response.from_dict(firewall_rule_out_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


