# CreateS3Backup

Параметры создания резервной копии базы данных в S3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **object** | Комментарий к резервной копии. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_s3_backup import CreateS3Backup

# TODO update the JSON string below
json = "{}"
# create an instance of CreateS3Backup from a JSON string
create_s3_backup_instance = CreateS3Backup.from_json(json)
# print the JSON string representation of the object
print CreateS3Backup.to_json()

# convert the object into a dict
create_s3_backup_dict = create_s3_backup_instance.to_dict()
# create an instance of CreateS3Backup from a dict
create_s3_backup_form_dict = create_s3_backup.from_dict(create_s3_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


