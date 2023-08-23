# CreateClusterInstance

База данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название базы данных | [optional] 
**description** | **object** | Описание базы данных | [optional] 

## Example

```python
from openapi_client.models.create_cluster_instance import CreateClusterInstance

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterInstance from a JSON string
create_cluster_instance_instance = CreateClusterInstance.from_json(json)
# print the JSON string representation of the object
print CreateClusterInstance.to_json()

# convert the object into a dict
create_cluster_instance_dict = create_cluster_instance_instance.to_dict()
# create an instance of CreateClusterInstance from a dict
create_cluster_instance_form_dict = create_cluster_instance.from_dict(create_cluster_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


