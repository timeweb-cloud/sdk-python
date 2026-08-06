# CreateDatabaseBackupDownloadUrl201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_url** | [**BackupDownloadUrl**](BackupDownloadUrl.md) |  | 

## Example

```python
from timeweb_cloud_api.models.create_database_backup_download_url201_response import CreateDatabaseBackupDownloadUrl201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDatabaseBackupDownloadUrl201Response from a JSON string
create_database_backup_download_url201_response_instance = CreateDatabaseBackupDownloadUrl201Response.from_json(json)
# print the JSON string representation of the object
print CreateDatabaseBackupDownloadUrl201Response.to_json()

# convert the object into a dict
create_database_backup_download_url201_response_dict = create_database_backup_download_url201_response_instance.to_dict()
# create an instance of CreateDatabaseBackupDownloadUrl201Response from a dict
create_database_backup_download_url201_response_form_dict = create_database_backup_download_url201_response.from_dict(create_database_backup_download_url201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


