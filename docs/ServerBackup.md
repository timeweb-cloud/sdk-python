# ServerBackup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор бэкапа сервера. | 
**name** | **object** | Название бэкапа. | 
**comment** | **object** | Комментарий к бэкапу. | 
**created_at** | **object** | Дата создания бэкапа. | 
**status** | **object** | Статус бэкапа. | 
**size** | **object** | Размер бэкапа (в Мб). | 
**type** | **object** | Тип бэкапа. | 
**progress** | **object** | Прогресс создания бэкапа. Значение будет меняться в статусе бэкапа &#x60;create&#x60; от 0 до 99, для остальных статусов всегда будет возвращаться 0. | 

## Example

```python
from openapi_client.models.server_backup import ServerBackup

# TODO update the JSON string below
json = "{}"
# create an instance of ServerBackup from a JSON string
server_backup_instance = ServerBackup.from_json(json)
# print the JSON string representation of the object
print ServerBackup.to_json()

# convert the object into a dict
server_backup_dict = server_backup_instance.to_dict()
# create an instance of ServerBackup from a dict
server_backup_form_dict = server_backup.from_dict(server_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


