# UpdateAutoBackup

Новые настройки автобэкапов базы данных. При значении `is_enabled`: `true` поля `copy_count`, `creation_start_at`, `interval` и `day_of_week` являются обязательными.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **object** | Включено ли автобэкапирование | 
**copy_count** | **object** | Количество копий для хранения. Минимальное количество &#x60;1&#x60;, максимальное &#x60;99&#x60;. Обязательно при &#x60;is_enabled&#x60;: &#x60;true&#x60;. | [optional] 
**creation_start_at** | **object** | Дата начала создания первого автобэкапа. Значение в формате &#x60;ISO8601&#x60;. Время не учитывается. Обязательно при &#x60;is_enabled&#x60;: &#x60;true&#x60;. | [optional] 
**interval** | **object** | Периодичность создания автобэкапов. Обязательно при &#x60;is_enabled&#x60;: &#x60;true&#x60;. | [optional] 
**day_of_week** | **object** | День недели, в который будут создаваться автобэкапы. Доступные значения от &#x60;1&#x60; до &#x60;7&#x60;. Обязательно при &#x60;is_enabled&#x60;: &#x60;true&#x60; при любой периодичности, но на расписание влияет только при значении &#x60;interval&#x60;: &#x60;week&#x60;. | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_auto_backup import UpdateAutoBackup

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAutoBackup from a JSON string
update_auto_backup_instance = UpdateAutoBackup.from_json(json)
# print the JSON string representation of the object
print UpdateAutoBackup.to_json()

# convert the object into a dict
update_auto_backup_dict = update_auto_backup_instance.to_dict()
# create an instance of UpdateAutoBackup from a dict
update_auto_backup_form_dict = update_auto_backup.from_dict(update_auto_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


