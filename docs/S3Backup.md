# S3Backup

Резервная копия базы данных, выгруженная в объектное хранилище S3.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID резервной копии в формате UUID. | 
**name** | **object** | Название резервной копии. В текущей реализации всегда совпадает со значением &#x60;id&#x60;. | 
**status** | **object** | Статус резервной копии: &#x60;running&#x60; — копия создаётся, &#x60;success&#x60; — копия создана, &#x60;failed&#x60; — создать копию не удалось. Восстановить кластер можно только из копии со статусом &#x60;success&#x60;. | 
**size** | **object** | Размер резервной копии в байтах. | 
**progress** | **object** | Прогресс создания резервной копии, от 0 до 100. | 
**type** | **object** | Тип резервной копии: &#x60;manual&#x60; — копия создана вручную, &#x60;auto&#x60; — копия создана по расписанию. | 
**comment** | **object** | Комментарий к резервной копии. Если комментарий не задавался, возвращается &#x60;null&#x60;. | [optional] 
**created_at** | **object** | Дата и время создания резервной копии. | 

## Example

```python
from timeweb_cloud_api.models.s3_backup import S3Backup

# TODO update the JSON string below
json = "{}"
# create an instance of S3Backup from a JSON string
s3_backup_instance = S3Backup.from_json(json)
# print the JSON string representation of the object
print S3Backup.to_json()

# convert the object into a dict
s3_backup_dict = s3_backup_instance.to_dict()
# create an instance of S3Backup from a dict
s3_backup_form_dict = s3_backup.from_dict(s3_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


