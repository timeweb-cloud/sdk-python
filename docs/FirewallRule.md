# FirewallRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID правила. | 
**description** | **object** | Описание правила. | 
**direction** | [**FirewallRuleDirection**](FirewallRuleDirection.md) |  | 
**protocol** | [**FirewallRuleProtocol**](FirewallRuleProtocol.md) |  | 
**port** | **object** | Порт или диапазон портов, в случае tcp или udp. | [optional] 
**cidr** | **object** | Сетевой адрес или подсеть. Поддерживаются протоколы IPv4  и IPv6. | [optional] 
**group_id** | **object** | ID группы правил. | 

## Example

```python
from timeweb_cloud_api.models.firewall_rule import FirewallRule

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRule from a JSON string
firewall_rule_instance = FirewallRule.from_json(json)
# print the JSON string representation of the object
print FirewallRule.to_json()

# convert the object into a dict
firewall_rule_dict = firewall_rule_instance.to_dict()
# create an instance of FirewallRule from a dict
firewall_rule_form_dict = firewall_rule.from_dict(firewall_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


