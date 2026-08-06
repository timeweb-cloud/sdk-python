# DbsUpdateBackup

Новые данные бэкапа базы данных.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **object** | Новый комментарий к бэкапу. | 

## Example

```python
from timeweb_cloud_api.models.dbs_update_backup import DbsUpdateBackup

# TODO update the JSON string below
json = "{}"
# create an instance of DbsUpdateBackup from a JSON string
dbs_update_backup_instance = DbsUpdateBackup.from_json(json)
# print the JSON string representation of the object
print DbsUpdateBackup.to_json()

# convert the object into a dict
dbs_update_backup_dict = dbs_update_backup_instance.to_dict()
# create an instance of DbsUpdateBackup from a dict
dbs_update_backup_form_dict = dbs_update_backup.from_dict(dbs_update_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


