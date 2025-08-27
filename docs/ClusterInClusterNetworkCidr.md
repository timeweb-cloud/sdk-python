# ClusterInClusterNetworkCidr

Определяет сетевые диапазоны (CIDR) для подов (pods_network) и сервисов (services_network) в Kubernetes-кластере.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pods_network** | **object** | Диапазон адресов подов. Подсеть должна принадлежать диапазонам 10.0.0.0/x, 192.168.0.0/x, 172.16.0.0/x. Максимальный размер для подов CIDR 10.0.0.0/x - /8, 192.168.0.0/x - /16, 172.16.0.0/x - /12, минимальный CIDR в этих диапазонах - /28. | [optional] 
**services_network** | **object** | Диапазон адресов сервисов. Подсеть должна принадлежать диапазонам 10.0.0.0/x, 192.168.0.0/x, 172.16.0.0/x. Максимальный размер CIDR для сервисов 10.0.0.0/x - /12, 192.168.0.0/x - /16, 172.16.0.0/x - /12, минимальный CIDR в этих диапазонах - /28. | [optional] 

## Example

```python
from timeweb_cloud_api.models.cluster_in_cluster_network_cidr import ClusterInClusterNetworkCidr

# TODO update the JSON string below
json = "{}"
# create an instance of ClusterInClusterNetworkCidr from a JSON string
cluster_in_cluster_network_cidr_instance = ClusterInClusterNetworkCidr.from_json(json)
# print the JSON string representation of the object
print ClusterInClusterNetworkCidr.to_json()

# convert the object into a dict
cluster_in_cluster_network_cidr_dict = cluster_in_cluster_network_cidr_instance.to_dict()
# create an instance of ClusterInClusterNetworkCidr from a dict
cluster_in_cluster_network_cidr_form_dict = cluster_in_cluster_network_cidr.from_dict(cluster_in_cluster_network_cidr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


