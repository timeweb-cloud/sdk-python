# NodesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**nodes** | **object** | Массив объектов Нода | 

## Example

```python
from timeweb_cloud_api.models.nodes_response import NodesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of NodesResponse from a JSON string
nodes_response_instance = NodesResponse.from_json(json)
# print the JSON string representation of the object
print NodesResponse.to_json()

# convert the object into a dict
nodes_response_dict = nodes_response_instance.to_dict()
# create an instance of NodesResponse from a dict
nodes_response_form_dict = nodes_response.from_dict(nodes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


