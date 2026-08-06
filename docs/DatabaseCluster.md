# DatabaseCluster

Кластер базы данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID для каждого экземпляра базы данных. Автоматически генерируется при создании. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была создана база данных. | 
**location** | **object** | Локация сервера. | 
**name** | **object** | Название кластера базы данных. | 
**description** | **object** | Описание кластера базы данных. | 
**networks** | **object** | Список сетей кластера базы данных. | 
**is_enabled_public_ipv6** | **object** | Использование публичного IPv6-адреса. | 
**type** | **object** | Тип базы данных. Список возможных значений шире, чем список типов, доступных при создании нового кластера. | 
**hash_type** | **object** | Тип хеширования кластера базы данных (mysql5 | mysql | postgres). | 
**avatar_link** | **object** | Ссылка на аватар для базы данных. | 
**port** | **object** | Порт | 
**status** | **object** | Текущий статус кластера базы данных. Значение &#x60;read_only&#x60; означает, что запись в кластер заблокирована из-за переполнения диска — чтобы снять блокировку, освободите место или увеличьте размер диска. | 
**preset_id** | **object** | ID тарифа. Равен &#x60;null&#x60; у кластеров, созданных через конфигуратор — в этом случае заполнен &#x60;configurator_id&#x60;. | 
**configurator_id** | **object** | ID конфигуратора. Равен &#x60;null&#x60; у кластеров, созданных по тарифу. | 
**cpu** | **object** | Количество ядер процессора. | 
**cpu_frequency** | **object** | Частота процессора. | 
**is_dedicated_cpu** | **object** | Используются ли выделенные ядра процессора. | 
**ram** | **object** | Объем оперативной памяти (в Мб). | 
**disk** | [**DatabaseClusterDisk**](DatabaseClusterDisk.md) |  | 
**has_additional_disk** | **object** | Подключен ли к кластеру дополнительный диск. | 
**disk_autoscaling** | [**DatabaseClusterDiskAutoscaling**](DatabaseClusterDiskAutoscaling.md) |  | 
**config_parameters** | [**Mysql**](Mysql.md) |  | 
**is_enabled_public_network** | **object** | Доступность публичного IP-адреса | 
**is_secure_connection_enabled** | **object** | Включено ли защищенное подключение к кластеру базы данных. | 
**is_autobackups_enabled** | **object** | Включены ли автоматические резервные копии кластера базы данных. | 
**is_backup_schedule_enabled** | **object** | Включено ли расписание резервного копирования кластера базы данных. | 
**availability_zone** | [**AvailabilityZone**](AvailabilityZone.md) |  | 
**project_id** | **object** | ID проекта, в котором находится кластер базы данных. | [optional] 
**replica_list** | **object** | Список реплик кластера базы данных. | 
**domains** | **object** | Список доменов кластера базы данных. Если публичная сеть отключена (&#x60;is_enabled_public_network: false&#x60;), список всегда пустой. | 
**child_services** | **object** | Список дочерних сервисов кластера базы данных. | 
**parent_services** | **object** | Список родительских сервисов кластера базы данных. | 
**maintenance_slot** | [**DatabaseClusterMaintenanceSlot**](DatabaseClusterMaintenanceSlot.md) |  | 

## Example

```python
from timeweb_cloud_api.models.database_cluster import DatabaseCluster

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseCluster from a JSON string
database_cluster_instance = DatabaseCluster.from_json(json)
# print the JSON string representation of the object
print DatabaseCluster.to_json()

# convert the object into a dict
database_cluster_dict = database_cluster_instance.to_dict()
# create an instance of DatabaseCluster from a dict
database_cluster_form_dict = database_cluster.from_dict(database_cluster_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


