# Backup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Идентификатор резервной копии. | 
**name** | **object** | Название резервной копии. | 
**comment** | **object** | Комментарий. | 
**created_at** | **object** | Дата создания. | 
**status** | **object** | Статус бэкапа. | 
**size** | **object** | Размер резервной копии (Мб). | 
**type** | **object** | Тип бэкапа. | 
**progress** | **object** | Прогресс создания бэкапа. Значение будет меняться в статусе бэкапа &#x60;create&#x60; от 0 до 99, для остальных статусов всегда будет возвращаться 0. | 

## Example

```python
from timeweb_cloud_api.models.backup import Backup

# TODO update the JSON string below
json = "{}"
# create an instance of Backup from a JSON string
backup_instance = Backup.from_json(json)
# print the JSON string representation of the object
print Backup.to_json()

# convert the object into a dict
backup_dict = backup_instance.to_dict()
# create an instance of Backup from a dict
backup_form_dict = backup.from_dict(backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


