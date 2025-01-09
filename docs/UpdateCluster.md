# UpdateCluster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название кластера базы данных. | [optional] 
**preset_id** | **object** | ID тарифа. | [optional] 
**description** | **object** | Описание кластера базы данных | [optional] 
**is_enabled_public_network** | **object** | Доступность публичного IP-адреса | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_cluster import UpdateCluster

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCluster from a JSON string
update_cluster_instance = UpdateCluster.from_json(json)
# print the JSON string representation of the object
print UpdateCluster.to_json()

# convert the object into a dict
update_cluster_dict = update_cluster_instance.to_dict()
# create an instance of UpdateCluster from a dict
update_cluster_form_dict = update_cluster.from_dict(update_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


