# BackupDownloadUrlRequest

Параметры для получения ссылки на скачивание бэкапа.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **object** | Имя файла бэкапа. Допустимы буквы латиницы и кириллицы, цифры, символ подчеркивания, а также &#x60;-&#x60;, &#x60;.&#x60;, &#x60;,&#x60;, &#x60;:&#x60; и пробел. | 

## Example

```python
from timeweb_cloud_api.models.backup_download_url_request import BackupDownloadUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BackupDownloadUrlRequest from a JSON string
backup_download_url_request_instance = BackupDownloadUrlRequest.from_json(json)
# print the JSON string representation of the object
print BackupDownloadUrlRequest.to_json()

# convert the object into a dict
backup_download_url_request_dict = backup_download_url_request_instance.to_dict()
# create an instance of BackupDownloadUrlRequest from a dict
backup_download_url_request_form_dict = backup_download_url_request.from_dict(backup_download_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


