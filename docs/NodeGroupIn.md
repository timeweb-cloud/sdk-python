# NodeGroupIn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название группы | 
**preset_id** | **object** | Идентификатор тарифа воркер-ноды | 
**node_count** | **object** | Количество нод в группе | 

## Example

```python
from openapi_client.models.node_group_in import NodeGroupIn

# TODO update the JSON string below
json = "{}"
# create an instance of NodeGroupIn from a JSON string
node_group_in_instance = NodeGroupIn.from_json(json)
# print the JSON string representation of the object
print NodeGroupIn.to_json()

# convert the object into a dict
node_group_in_dict = node_group_in_instance.to_dict()
# create an instance of NodeGroupIn from a dict
node_group_in_form_dict = node_group_in.from_dict(node_group_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


