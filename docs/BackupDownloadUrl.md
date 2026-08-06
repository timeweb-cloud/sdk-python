# BackupDownloadUrl

Ссылка для скачивания бэкапа базы данных.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup_id** | **object** | ID резервной копии. | 
**download_url** | **object** | Ссылка для скачивания бэкапа. | 

## Example

```python
from timeweb_cloud_api.models.backup_download_url import BackupDownloadUrl

# TODO update the JSON string below
json = "{}"
# create an instance of BackupDownloadUrl from a JSON string
backup_download_url_instance = BackupDownloadUrl.from_json(json)
# print the JSON string representation of the object
print BackupDownloadUrl.to_json()

# convert the object into a dict
backup_download_url_dict = backup_download_url_instance.to_dict()
# create an instance of BackupDownloadUrl from a dict
backup_download_url_form_dict = backup_download_url.from_dict(backup_download_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


