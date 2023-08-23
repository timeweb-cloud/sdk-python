# CreateBalancerRule200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule** | [**Rule**](Rule.md) |  | 

## Example

```python
from openapi_client.models.create_balancer_rule200_response import CreateBalancerRule200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBalancerRule200Response from a JSON string
create_balancer_rule200_response_instance = CreateBalancerRule200Response.from_json(json)
# print the JSON string representation of the object
print CreateBalancerRule200Response.to_json()

# convert the object into a dict
create_balancer_rule200_response_dict = create_balancer_rule200_response_instance.to_dict()
# create an instance of CreateBalancerRule200Response from a dict
create_balancer_rule200_response_form_dict = create_balancer_rule200_response.from_dict(create_balancer_rule200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


