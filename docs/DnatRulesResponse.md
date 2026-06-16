# DnatRulesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**dnat_rules** | **object** | Правила проброса портов | 
**meta** | [**ComponentsSchemasMeta**](ComponentsSchemasMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.dnat_rules_response import DnatRulesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DnatRulesResponse from a JSON string
dnat_rules_response_instance = DnatRulesResponse.from_json(json)
# print the JSON string representation of the object
print DnatRulesResponse.to_json()

# convert the object into a dict
dnat_rules_response_dict = dnat_rules_response_instance.to_dict()
# create an instance of DnatRulesResponse from a dict
dnat_rules_response_form_dict = dnat_rules_response.from_dict(dnat_rules_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


