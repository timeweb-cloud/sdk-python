# DbReplication

Репликация

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **object** | Количество реплик. | [optional] 

## Example

```python
from timeweb_cloud_api.models.db_replication import DbReplication

# TODO update the JSON string below
json = "{}"
# create an instance of DbReplication from a JSON string
db_replication_instance = DbReplication.from_json(json)
# print the JSON string representation of the object
print DbReplication.to_json()

# convert the object into a dict
db_replication_dict = db_replication_instance.to_dict()
# create an instance of DbReplication from a dict
db_replication_form_dict = db_replication.from_dict(db_replication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


