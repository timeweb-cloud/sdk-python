# DbsCreateBackup

Параметры создаваемого бэкапа базы данных.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **object** | Комментарий к бэкапу. | [optional] 

## Example

```python
from timeweb_cloud_api.models.dbs_create_backup import DbsCreateBackup

# TODO update the JSON string below
json = "{}"
# create an instance of DbsCreateBackup from a JSON string
dbs_create_backup_instance = DbsCreateBackup.from_json(json)
# print the JSON string representation of the object
print DbsCreateBackup.to_json()

# convert the object into a dict
dbs_create_backup_dict = dbs_create_backup_instance.to_dict()
# create an instance of DbsCreateBackup from a dict
dbs_create_backup_form_dict = dbs_create_backup.from_dict(dbs_create_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


