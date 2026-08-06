# ClusterAction

Действие над кластером базы данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **object** | Действие над кластером базы данных: &#x60;reboot&#x60; — перезагрузить, &#x60;shutdown&#x60; — выключить, &#x60;start&#x60; — включить. | 

## Example

```python
from timeweb_cloud_api.models.cluster_action import ClusterAction

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterAction from a JSON string
cluster_action_instance = ClusterAction.from_json(json)
# print the JSON string representation of the object
print ClusterAction.to_json()

# convert the object into a dict
cluster_action_dict = cluster_action_instance.to_dict()
# create an instance of ClusterAction from a dict
cluster_action_form_dict = cluster_action.from_dict(cluster_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


