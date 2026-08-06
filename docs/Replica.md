# Replica

Реплика кластера базы данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID реплики. Автоматически генерируется при создании. | 
**db_id** | **object** | ID кластера базы данных, которому принадлежит реплика. | 
**status** | **object** | Текущий статус реплики. | 
**local_ip** | **object** | IP-адрес реплики в локальной сети. Возвращается пустая строка, если адрес ещё не назначен. | 
**disk** | [**ReplicaDisk**](ReplicaDisk.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.replica import Replica

# TODO update the JSON string below
json = "{}"
# create an instance of Replica from a JSON string
replica_instance = Replica.from_json(json)
# print the JSON string representation of the object
print Replica.to_json()

# convert the object into a dict
replica_dict = replica_instance.to_dict()
# create an instance of Replica from a dict
replica_form_dict = replica.from_dict(replica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


