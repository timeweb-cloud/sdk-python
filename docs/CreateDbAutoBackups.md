# CreateDbAutoBackups

База данных

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_count** | **object** | Количество копий для хранения. Минимальное количество &#x60;1&#x60;, максимальное &#x60;99&#x60; | 
**creation_start_at** | **object** | Дата начала создания первого автобэкапа. Значение в формате &#x60;ISO8601&#x60;. Время не учитывается. | 
**interval** | **object** | Периодичность создания автобэкапов | 
**day_of_week** | **object** | День недели, в который будут создаваться автобэкапы. Работает только со значением &#x60;interval&#x60;: &#x60;week&#x60;. Доступные значение от &#x60;1 &#x60;до &#x60;7&#x60;. | 

## Example

```python
from timeweb_cloud_api.models.create_db_auto_backups import CreateDbAutoBackups

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDbAutoBackups from a JSON string
create_db_auto_backups_instance = CreateDbAutoBackups.from_json(json)
# print the JSON string representation of the object
print CreateDbAutoBackups.to_json()

# convert the object into a dict
create_db_auto_backups_dict = create_db_auto_backups_instance.to_dict()
# create an instance of CreateDbAutoBackups from a dict
create_db_auto_backups_form_dict = create_db_auto_backups.from_dict(create_db_auto_backups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


