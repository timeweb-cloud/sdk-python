# Rule

Правило для балансировщика

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор для каждого экземпляра правила для балансировщика. Автоматически генерируется при создании. | 
**balancer_proto** | **object** | Протокол балансировщика. | 
**balancer_port** | **object** | Порт балансировщика. | 
**server_proto** | **object** | Протокол сервера. | 
**server_port** | **object** | Порт сервера. | 

## Example

```python
from openapi_client.models.rule import Rule

# TODO update the JSON string below
json = "{}"
# create an instance of Rule from a JSON string
rule_instance = Rule.from_json(json)
# print the JSON string representation of the object
print Rule.to_json()

# convert the object into a dict
rule_dict = rule_instance.to_dict()
# create an instance of Rule from a dict
rule_form_dict = rule.from_dict(rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


