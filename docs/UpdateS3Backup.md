# UpdateS3Backup

Параметры изменения резервной копии базы данных в S3. Изменить можно только комментарий — других полей ручка не принимает.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **object** | Новый комментарий к резервной копии. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_s3_backup import UpdateS3Backup

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateS3Backup from a JSON string
update_s3_backup_instance = UpdateS3Backup.from_json(json)
# print the JSON string representation of the object
print UpdateS3Backup.to_json()

# convert the object into a dict
update_s3_backup_dict = update_s3_backup_instance.to_dict()
# create an instance of UpdateS3Backup from a dict
update_s3_backup_form_dict = update_s3_backup.from_dict(update_s3_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


