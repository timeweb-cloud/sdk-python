# ReplicaDisk

Статистика использования диска реплики. Возвращается `null`, если данные о диске недоступны.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **object** | Размер (в Кб) диска реплики. | 
**used** | **object** | Размер (в Кб) использованного пространства диска реплики. | 

## Example

```python
from timeweb_cloud_api.models.replica_disk import ReplicaDisk

# TODO update the JSON string below
json = "{}"
# create an instance of ReplicaDisk from a JSON string
replica_disk_instance = ReplicaDisk.from_json(json)
# print the JSON string representation of the object
print ReplicaDisk.to_json()

# convert the object into a dict
replica_disk_dict = replica_disk_instance.to_dict()
# create an instance of ReplicaDisk from a dict
replica_disk_form_dict = replica_disk.from_dict(replica_disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


