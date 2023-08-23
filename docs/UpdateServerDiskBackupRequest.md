# UpdateServerDiskBackupRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **object** | Комментарий к бэкапу. | 

## Example

```python
from openapi_client.models.update_server_disk_backup_request import UpdateServerDiskBackupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServerDiskBackupRequest from a JSON string
update_server_disk_backup_request_instance = UpdateServerDiskBackupRequest.from_json(json)
# print the JSON string representation of the object
print UpdateServerDiskBackupRequest.to_json()

# convert the object into a dict
update_server_disk_backup_request_dict = update_server_disk_backup_request_instance.to_dict()
# create an instance of UpdateServerDiskBackupRequest from a dict
update_server_disk_backup_request_form_dict = update_server_disk_backup_request.from_dict(update_server_disk_backup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


