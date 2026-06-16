# DnatRuleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**dnat_rule** | [**DnatRuleOut**](DnatRuleOut.md) |  | 

## Example

```python
from timeweb_cloud_api.models.dnat_rule_response import DnatRuleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DnatRuleResponse from a JSON string
dnat_rule_response_instance = DnatRuleResponse.from_json(json)
# print the JSON string representation of the object
print DnatRuleResponse.to_json()

# convert the object into a dict
dnat_rule_response_dict = dnat_rule_response_instance.to_dict()
# create an instance of DnatRuleResponse from a dict
dnat_rule_response_form_dict = dnat_rule_response.from_dict(dnat_rule_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


