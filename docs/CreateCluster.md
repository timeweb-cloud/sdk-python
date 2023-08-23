# CreateCluster


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название кластера базы данных. | 
**type** | **object** | Тип базы данных. | 
**admin** | [**CreateClusterAdmin**](CreateClusterAdmin.md) |  | [optional] 
**instance** | [**CreateClusterInstance**](CreateClusterInstance.md) |  | [optional] 
**hash_type** | **object** | Тип хеширования базы данных (mysql5 | mysql | postgres). | [optional] 
**preset_id** | **object** | Идентификатор тарифа. | 
**config_parameters** | [**ConfigParameters**](ConfigParameters.md) |  | [optional] 
**network** | [**Network**](Network.md) |  | [optional] 
**description** | **object** | Описание кластера базы данных | [optional] 

## Example

```python
from openapi_client.models.create_cluster import CreateCluster

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCluster from a JSON string
create_cluster_instance = CreateCluster.from_json(json)
# print the JSON string representation of the object
print CreateCluster.to_json()

# convert the object into a dict
create_cluster_dict = create_cluster_instance.to_dict()
# create an instance of CreateCluster from a dict
create_cluster_form_dict = create_cluster.from_dict(create_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


