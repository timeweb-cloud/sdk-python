# UpdateClusterV2

Изменение кластера базы данных (v2)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Название кластера базы данных. | [optional] 
**preset_id** | **object** | ID тарифа. Нельзя передавать вместе с &#x60;configuration&#x60; | [optional] 
**configuration** | [**UpdateClusterConfiguration**](UpdateClusterConfiguration.md) |  | [optional] 
**config_parameters** | [**Mysql**](Mysql.md) |  | [optional] 
**hash_type** | **object** | Тип хеширования базы данных (mysql | postgres). | [optional] 
**description** | **object** | Описание кластера базы данных | [optional] 
**is_enabled_public_network** | **object** | Доступность публичного IP-адреса | [optional] 
**is_enabled_public_ipv6** | **object** | Использование публичного IPv6-адреса. | [optional] 
**floating_ip** | **object** | Плавающий IP-адрес, который нужно привязать к кластеру базы данных. Передается сам адрес, а не его ID; адрес должен быть свободен (не привязан к другому сервису). | [optional] 
**is_secure_connection_enable** | **object** | Включить защищенное подключение к кластеру базы данных. Обратите внимание: в ответе это же значение возвращается под ключом &#x60;is_secure_connection_enabled&#x60;. | [optional] 
**maintenance_slot** | [**UpdateClusterV2MaintenanceSlot**](UpdateClusterV2MaintenanceSlot.md) |  | [optional] 
**disk_autoscaling** | [**UpdateClusterV2DiskAutoscaling**](UpdateClusterV2DiskAutoscaling.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_cluster_v2 import UpdateClusterV2

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClusterV2 from a JSON string
update_cluster_v2_instance = UpdateClusterV2.from_json(json)
# print the JSON string representation of the object
print UpdateClusterV2.to_json()

# convert the object into a dict
update_cluster_v2_dict = update_cluster_v2_instance.to_dict()
# create an instance of UpdateClusterV2 from a dict
update_cluster_v2_form_dict = update_cluster_v2.from_dict(update_cluster_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


