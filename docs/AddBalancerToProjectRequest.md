# AddBalancerToProjectRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **object** | ID добавляемого балансировщика. | 

## Example

```python
from timeweb_cloud_api.models.add_balancer_to_project_request import AddBalancerToProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddBalancerToProjectRequest from a JSON string
add_balancer_to_project_request_instance = AddBalancerToProjectRequest.from_json(json)
# print the JSON string representation of the object
print AddBalancerToProjectRequest.to_json()

# convert the object into a dict
add_balancer_to_project_request_dict = add_balancer_to_project_request_instance.to_dict()
# create an instance of AddBalancerToProjectRequest from a dict
add_balancer_to_project_request_form_dict = add_balancer_to_project_request.from_dict(add_balancer_to_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


