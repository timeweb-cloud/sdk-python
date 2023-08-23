# ClusterIn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название кластера | 
**description** | **object** | Описание кластера | [optional] 
**ha** | **object** | Описание появится позднее | 
**k8s_version** | **object** | Версия Kubernetes | 
**network_driver** | **object** | Тип используемого сетевого драйвера в кластере | 
**ingress** | **object** | Логическое значение, которое показывает, использовать ли Ingress в кластере | 
**preset_id** | **object** | Идентификатор тарифа мастер-ноды | 
**worker_groups** | **object** | Группы воркеров в кластере | [optional] 

## Example

```python
from openapi_client.models.cluster_in import ClusterIn

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterIn from a JSON string
cluster_in_instance = ClusterIn.from_json(json)
# print the JSON string representation of the object
print ClusterIn.to_json()

# convert the object into a dict
cluster_in_dict = cluster_in_instance.to_dict()
# create an instance of ClusterIn from a dict
cluster_in_form_dict = cluster_in.from_dict(cluster_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


