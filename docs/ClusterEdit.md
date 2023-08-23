# ClusterEdit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **object** | Новое описание кластера | [optional] 

## Example

```python
from timeweb_cloud_api.models.cluster_edit import ClusterEdit

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterEdit from a JSON string
cluster_edit_instance = ClusterEdit.from_json(json)
# print the JSON string representation of the object
print ClusterEdit.to_json()

# convert the object into a dict
cluster_edit_dict = cluster_edit_instance.to_dict()
# create an instance of ClusterEdit from a dict
cluster_edit_form_dict = cluster_edit.from_dict(cluster_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


