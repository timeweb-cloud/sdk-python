# GetServerDiskAutoBackupSettings200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_backups_settings** | [**AutoBackup**](AutoBackup.md) |  | 

## Example

```python
from openapi_client.models.get_server_disk_auto_backup_settings200_response import GetServerDiskAutoBackupSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServerDiskAutoBackupSettings200Response from a JSON string
get_server_disk_auto_backup_settings200_response_instance = GetServerDiskAutoBackupSettings200Response.from_json(json)
# print the JSON string representation of the object
print GetServerDiskAutoBackupSettings200Response.to_json()

# convert the object into a dict
get_server_disk_auto_backup_settings200_response_dict = get_server_disk_auto_backup_settings200_response_instance.to_dict()
# create an instance of GetServerDiskAutoBackupSettings200Response from a dict
get_server_disk_auto_backup_settings200_response_form_dict = get_server_disk_auto_backup_settings200_response.from_dict(get_server_disk_auto_backup_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


