# DatabaseClusterDisk

Статистика использования диска кластера базы данных.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **object** | Размер (в Кб) диска кластера базы данных. | 
**used** | **object** | Размер (в Кб) использованного пространства диска кластера базы данных. | 

## Example

```python
from timeweb_cloud_api.models.database_cluster_disk import DatabaseClusterDisk

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseClusterDisk from a JSON string
database_cluster_disk_instance = DatabaseClusterDisk.from_json(json)
# print the JSON string representation of the object
print DatabaseClusterDisk.to_json()

# convert the object into a dict
database_cluster_disk_dict = database_cluster_disk_instance.to_dict()
# create an instance of DatabaseClusterDisk from a dict
database_cluster_disk_form_dict = database_cluster_disk.from_dict(database_cluster_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


