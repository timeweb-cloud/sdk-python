# CreateBalancer200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balancer** | [**Balancer**](Balancer.md) |  | 

## Example

```python
from timeweb_cloud_api.models.create_balancer200_response import CreateBalancer200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBalancer200Response from a JSON string
create_balancer200_response_instance = CreateBalancer200Response.from_json(json)
# print the JSON string representation of the object
print CreateBalancer200Response.to_json()

# convert the object into a dict
create_balancer200_response_dict = create_balancer200_response_instance.to_dict()
# create an instance of CreateBalancer200Response from a dict
create_balancer200_response_form_dict = create_balancer200_response.from_dict(create_balancer200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


