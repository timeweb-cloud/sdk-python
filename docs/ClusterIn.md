# ClusterIn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название кластера | 
**description** | **object** | Описание кластера | [optional] 
**k8s_version** | **object** | Версия Kubernetes | 
**availability_zone** | **object** | Зона доступности | [optional] 
**network_driver** | **object** | Тип используемого сетевого драйвера в кластере | 
**is_ingress** | **object** | Логическое значение, которое показывает, использовать ли Ingress в кластере | [optional] 
**is_k8s_dashboard** | **object** | Логическое значение, которое показывает, использовать ли Kubernetes Dashboard в кластере | [optional] 
**preset_id** | **object** | ID тарифа мастер-ноды. Нельзя передавать вместе с &#x60;configuration&#x60; | [optional] 
**configuration** | [**ClusterInConfiguration**](ClusterInConfiguration.md) |  | [optional] 
**master_nodes_count** | **object** | Количество мастер нод | [optional] 
**worker_groups** | **object** | Группы воркеров в кластере | [optional] 
**network_id** | **object** | ID приватной сети | [optional] 
**project_id** | **object** | ID проекта | [optional] 
**maintenance_slot** | [**ClusterInMaintenanceSlot**](ClusterInMaintenanceSlot.md) |  | [optional] 
**oidc_provider** | [**ClusterInOidcProvider**](ClusterInOidcProvider.md) |  | [optional] 
**cluster_network_cidr** | [**ClusterInClusterNetworkCidr**](ClusterInClusterNetworkCidr.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.cluster_in import ClusterIn

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


