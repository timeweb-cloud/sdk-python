# DbDiskStats

Статистика использования диска базы данных.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **object** | Размер (в Кб) диска базы данных. | 
**used** | **object** | Размер (в Кб) использованного пространства диска базы данных. | 

## Example

```python
from openapi_client.models.db_disk_stats import DbDiskStats

# TODO update the JSON string below
json = "{}"
# create an instance of DbDiskStats from a JSON string
db_disk_stats_instance = DbDiskStats.from_json(json)
# print the JSON string representation of the object
print DbDiskStats.to_json()

# convert the object into a dict
db_disk_stats_dict = db_disk_stats_instance.to_dict()
# create an instance of DbDiskStats from a dict
db_disk_stats_form_dict = db_disk_stats.from_dict(db_disk_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


