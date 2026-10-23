# ServerBackupDownloadUrlRequest

Параметры для получения ссылки на скачивание бэкапа диска сервера.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **object** | Имя файла бэкапа. Допустимы буквы латиницы и кириллицы, цифры, символ подчеркивания, а также &#x60;-&#x60;, &#x60;.&#x60;, &#x60;,&#x60;, &#x60;:&#x60; и пробел. | 

## Example

```python
from timeweb_cloud_api.models.server_backup_download_url_request import ServerBackupDownloadUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ServerBackupDownloadUrlRequest from a JSON string
server_backup_download_url_request_instance = ServerBackupDownloadUrlRequest.from_json(json)
# print the JSON string representation of the object
print ServerBackupDownloadUrlRequest.to_json()

# convert the object into a dict
server_backup_download_url_request_dict = server_backup_download_url_request_instance.to_dict()
# create an instance of ServerBackupDownloadUrlRequest from a dict
server_backup_download_url_request_form_dict = server_backup_download_url_request.from_dict(server_backup_download_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


