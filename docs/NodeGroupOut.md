# NodeGroupOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID группы | 
**name** | **object** | Название группы | 
**created_at** | **object** | Дата и время создания группы в формате ISO8601 | 
**preset_id** | **object** | ID тарифа мастер-ноды | 
**node_count** | **object** | Количество нод в группе | 

## Example

```python
from timeweb_cloud_api.models.node_group_out import NodeGroupOut

# TODO update the JSON string below
json = "{}"
# create an instance of NodeGroupOut from a JSON string
node_group_out_instance = NodeGroupOut.from_json(json)
# print the JSON string representation of the object
print NodeGroupOut.to_json()

# convert the object into a dict
node_group_out_dict = node_group_out_instance.to_dict()
# create an instance of NodeGroupOut from a dict
node_group_out_form_dict = node_group_out.from_dict(node_group_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


