# ClusterVersionEdit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**k8s_version** | **object** | Новая версия кластера | [optional] 

## Example

```python
from timeweb_cloud_api.models.cluster_version_edit import ClusterVersionEdit

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterVersionEdit from a JSON string
cluster_version_edit_instance = ClusterVersionEdit.from_json(json)
# print the JSON string representation of the object
print ClusterVersionEdit.to_json()

# convert the object into a dict
cluster_version_edit_dict = cluster_version_edit_instance.to_dict()
# create an instance of ClusterVersionEdit from a dict
cluster_version_edit_form_dict = cluster_version_edit.from_dict(cluster_version_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


