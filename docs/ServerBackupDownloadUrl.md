# ServerBackupDownloadUrl

Ссылка для скачивания бэкапа диска сервера.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_id** | **object** | ID бэкапа. | 
**download_url** | **object** | Ссылка для скачивания бэкапа. Действует 7 дней. | 

## Example

```python
from timeweb_cloud_api.models.server_backup_download_url import ServerBackupDownloadUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ServerBackupDownloadUrl from a JSON string
server_backup_download_url_instance = ServerBackupDownloadUrl.from_json(json)
# print the JSON string representation of the object
print ServerBackupDownloadUrl.to_json()

# convert the object into a dict
server_backup_download_url_dict = server_backup_download_url_instance.to_dict()
# create an instance of ServerBackupDownloadUrl from a dict
server_backup_download_url_form_dict = server_backup_download_url.from_dict(server_backup_download_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


