# DatabaseClusterDiskStats

Статистика использования диска кластера базы данных.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **object** | Размер (в Кб) диска кластера базы данных. | 
**used** | **object** | Размер (в Кб) использованного пространства диска кластера базы данных. | 

## Example

```python
from openapi_client.models.database_cluster_disk_stats import DatabaseClusterDiskStats

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseClusterDiskStats from a JSON string
database_cluster_disk_stats_instance = DatabaseClusterDiskStats.from_json(json)
# print the JSON string representation of the object
print DatabaseClusterDiskStats.to_json()

# convert the object into a dict
database_cluster_disk_stats_dict = database_cluster_disk_stats_instance.to_dict()
# create an instance of DatabaseClusterDiskStats from a dict
database_cluster_disk_stats_form_dict = database_cluster_disk_stats.from_dict(database_cluster_disk_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


