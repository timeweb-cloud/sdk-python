# CreateServerDiskBackupRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **object** | Комментарий к бэкапу. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_server_disk_backup_request import CreateServerDiskBackupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServerDiskBackupRequest from a JSON string
create_server_disk_backup_request_instance = CreateServerDiskBackupRequest.from_json(json)
# print the JSON string representation of the object
print CreateServerDiskBackupRequest.to_json()

# convert the object into a dict
create_server_disk_backup_request_dict = create_server_disk_backup_request_instance.to_dict()
# create an instance of CreateServerDiskBackupRequest from a dict
create_server_disk_backup_request_form_dict = create_server_disk_backup_request.from_dict(create_server_disk_backup_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


