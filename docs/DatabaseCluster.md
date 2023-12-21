# DatabaseCluster

Кластер базы данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор для каждого экземпляра базы данных. Автоматически генерируется при создании. | 
**created_at** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда была создана база данных. | 
**location** | **object** | Локация сервера. | 
**name** | **object** | Название кластера базы данных. | 
**networks** | **object** | Список сетей кластера базы данных. | 
**type** | [**DbType**](DbType.md) |  | 
**hash_type** | **object** | Тип хеширования кластера базы данных (mysql5 | mysql | postgres). | 
**port** | **object** | Порт | 
**status** | **object** | Текущий статус кластера базы данных. | 
**preset_id** | **object** | Идентификатор тарифа. | 
**disk_stats** | [**DatabaseClusterDiskStats**](DatabaseClusterDiskStats.md) |  | 
**config_parameters** | [**ConfigParameters**](ConfigParameters.md) |  | 
**is_enabled_public_network** | **object** | Доступность публичного IP-адреса | 

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


