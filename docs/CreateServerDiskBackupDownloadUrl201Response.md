# CreateServerDiskBackupDownloadUrl201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_url** | [**ServerBackupDownloadUrl**](ServerBackupDownloadUrl.md) |  | 

## Example

```python
from timeweb_cloud_api.models.create_server_disk_backup_download_url201_response import CreateServerDiskBackupDownloadUrl201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServerDiskBackupDownloadUrl201Response from a JSON string
create_server_disk_backup_download_url201_response_instance = CreateServerDiskBackupDownloadUrl201Response.from_json(json)
# print the JSON string representation of the object
print CreateServerDiskBackupDownloadUrl201Response.to_json()

# convert the object into a dict
create_server_disk_backup_download_url201_response_dict = create_server_disk_backup_download_url201_response_instance.to_dict()
# create an instance of CreateServerDiskBackupDownloadUrl201Response from a dict
create_server_disk_backup_download_url201_response_form_dict = create_server_disk_backup_download_url201_response.from_dict(create_server_disk_backup_download_url201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


