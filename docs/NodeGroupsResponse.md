# NodeGroupsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**node_groups** | **object** | Массив объектов Группа нод | 

## Example

```python
from timeweb_cloud_api.models.node_groups_response import NodeGroupsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodeGroupsResponse from a JSON string
node_groups_response_instance = NodeGroupsResponse.from_json(json)
# print the JSON string representation of the object
print NodeGroupsResponse.to_json()

# convert the object into a dict
node_groups_response_dict = node_groups_response_instance.to_dict()
# create an instance of NodeGroupsResponse from a dict
node_groups_response_form_dict = node_groups_response.from_dict(node_groups_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


