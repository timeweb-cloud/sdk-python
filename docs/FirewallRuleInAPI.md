# FirewallRuleInAPI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **object** | Описание правила. | [optional] 
**direction** | [**FirewallRuleDirection**](FirewallRuleDirection.md) |  | 
**port** | **object** | Порт или диапазон портов, в случае tcp или udp. | [optional] 
**protocol** | [**FirewallRuleProtocol**](FirewallRuleProtocol.md) |  | 
**cidr** | **object** | Сетевой адрес или подсеть. Поддерживаются протоколы IPv4  и IPv.6 | [optional] 

## Example

```python
from timeweb_cloud_api.models.firewall_rule_in_api import FirewallRuleInAPI

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRuleInAPI from a JSON string
firewall_rule_in_api_instance = FirewallRuleInAPI.from_json(json)
# print the JSON string representation of the object
print FirewallRuleInAPI.to_json()

# convert the object into a dict
firewall_rule_in_api_dict = firewall_rule_in_api_instance.to_dict()
# create an instance of FirewallRuleInAPI from a dict
firewall_rule_in_api_form_dict = firewall_rule_in_api.from_dict(firewall_rule_in_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


