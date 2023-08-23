# UpdateRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balancer_proto** | **object** | Протокол балансировщика. | 
**balancer_port** | **object** | Порт балансировщика. | 
**server_proto** | **object** | Протокол сервера. | 
**server_port** | **object** | Порт сервера. | 

## Example

```python
from openapi_client.models.update_rule import UpdateRule

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRule from a JSON string
update_rule_instance = UpdateRule.from_json(json)
# print the JSON string representation of the object
print UpdateRule.to_json()

# convert the object into a dict
update_rule_dict = update_rule_instance.to_dict()
# create an instance of UpdateRule from a dict
update_rule_form_dict = update_rule.from_dict(update_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


