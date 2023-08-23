# AutoBackup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**copy_count** | **object** | Количество копий для хранения. Минимальное количество &#x60;1&#x60;, максимальное &#x60;99&#x60; | [optional] 
**creation_start_at** | **object** | Дата начала создания первого автобэкапа. Значение в формате &#x60;ISO8601&#x60;. Время не учитывается. | [optional] 
**is_enabled** | **object** | Включено ли автобэкапирование | 
**interval** | **object** | Периодичность создания автобэкапов | [optional] 
**day_of_week** | **object** | День недели, в который будут создаваться автобэкапы. Работает только со значением &#x60;interval&#x60;: &#x60;week&#x60;. Доступные значение от &#x60;1 &#x60;до &#x60;7&#x60;. | [optional] 

## Example

```python
from timeweb_cloud_api.models.auto_backup import AutoBackup

# TODO update the JSON string below
json = "{}"
# create an instance of AutoBackup from a JSON string
auto_backup_instance = AutoBackup.from_json(json)
# print the JSON string representation of the object
print AutoBackup.to_json()

# convert the object into a dict
auto_backup_dict = auto_backup_instance.to_dict()
# create an instance of AutoBackup from a dict
auto_backup_form_dict = auto_backup.from_dict(auto_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


