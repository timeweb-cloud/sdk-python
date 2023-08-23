# FirewallRuleOutAPI


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Идентификатор правила | 
**description** | **object** | Описание правила | 
**direction** | [**FirewallRuleDirection**](FirewallRuleDirection.md) |  | 
**protocol** | [**FirewallRuleProtocol**](FirewallRuleProtocol.md) |  | 
**port** | **object** | Порт или диапазон портов, в случае tcp или udp | [optional] 
**cidr** | **object** | Сетевой адрес или подсеть. Поддерживаются протоколы IPv4  и IPv6 | [optional] 
**group_id** | **object** | Идентификатор группы правил | 

## Example

```python
from timeweb_cloud_api.models.firewall_rule_out_api import FirewallRuleOutAPI

# TODO update the JSON string below
json = "{}"
# create an instance of FirewallRuleOutAPI from a JSON string
firewall_rule_out_api_instance = FirewallRuleOutAPI.from_json(json)
# print the JSON string representation of the object
print FirewallRuleOutAPI.to_json()

# convert the object into a dict
firewall_rule_out_api_dict = firewall_rule_out_api_instance.to_dict()
# create an instance of FirewallRuleOutAPI from a dict
firewall_rule_out_api_form_dict = firewall_rule_out_api.from_dict(firewall_rule_out_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


