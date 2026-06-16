# DnatRuleOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID правила | 
**local_ip** | **object** | Приватный IP-адрес | 
**local_port** | **object** | Внутренний порт или диапазон | 
**public_ip** | **object** | Публичный IP-адрес | 
**public_port** | **object** | Внешний порт или диапазон | 
**protocol** | **object** | Протокол | 

## Example

```python
from timeweb_cloud_api.models.dnat_rule_out import DnatRuleOut

# TODO update the JSON string below
json = "{}"
# create an instance of DnatRuleOut from a JSON string
dnat_rule_out_instance = DnatRuleOut.from_json(json)
# print the JSON string representation of the object
print DnatRuleOut.to_json()

# convert the object into a dict
dnat_rule_out_dict = dnat_rule_out_instance.to_dict()
# create an instance of DnatRuleOut from a dict
dnat_rule_out_form_dict = dnat_rule_out.from_dict(dnat_rule_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


