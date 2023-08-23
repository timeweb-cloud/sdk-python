# NodeGroupResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**node_group** | [**NodeGroupOut**](NodeGroupOut.md) |  | 

## Example

```python
from openapi_client.models.node_group_response import NodeGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeGroupResponse from a JSON string
node_group_response_instance = NodeGroupResponse.from_json(json)
# print the JSON string representation of the object
print NodeGroupResponse.to_json()

# convert the object into a dict
node_group_response_dict = node_group_response_instance.to_dict()
# create an instance of NodeGroupResponse from a dict
node_group_response_form_dict = node_group_response.from_dict(node_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


