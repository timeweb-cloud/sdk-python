# FirewallRulesOutResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**rules** | **object** | Массив объектов Firewall правил | 

## Example

```python
from timeweb_cloud_api.models.firewall_rules_out_response import FirewallRulesOutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRulesOutResponse from a JSON string
firewall_rules_out_response_instance = FirewallRulesOutResponse.from_json(json)
# print the JSON string representation of the object
print FirewallRulesOutResponse.to_json()

# convert the object into a dict
firewall_rules_out_response_dict = firewall_rules_out_response_instance.to_dict()
# create an instance of FirewallRulesOutResponse from a dict
firewall_rules_out_response_form_dict = firewall_rules_out_response.from_dict(firewall_rules_out_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


