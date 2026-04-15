# ClusterIn1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип дополнения | 
**config_type** | **object** | Тип конфигурации дополнения | 
**yaml_config** | **object** | YAML-конфигурация дополнения | 
**version** | **object** | Версия дополнения | 

## Example

```python
from timeweb_cloud_api.models.cluster_in1 import ClusterIn1

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterIn1 from a JSON string
cluster_in1_instance = ClusterIn1.from_json(json)
# print the JSON string representation of the object
print ClusterIn1.to_json()

# convert the object into a dict
cluster_in1_dict = cluster_in1_instance.to_dict()
# create an instance of ClusterIn1 from a dict
cluster_in1_form_dict = cluster_in1.from_dict(cluster_in1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


