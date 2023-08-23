# CreateRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balancer_proto** | **object** | Протокол балансировщика. | 
**balancer_port** | **object** | Порт балансировщика. | 
**server_proto** | **object** | Протокол сервера. | 
**server_port** | **object** | Порт сервера. | 

## Example

```python
from timeweb_cloud_api.models.create_rule import CreateRule

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRule from a JSON string
create_rule_instance = CreateRule.from_json(json)
# print the JSON string representation of the object
print CreateRule.to_json()

# convert the object into a dict
create_rule_dict = create_rule_instance.to_dict()
# create an instance of CreateRule from a dict
create_rule_form_dict = create_rule.from_dict(create_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


