# UpdateAdmin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **object** | Пароль пользователя базы данных | [optional] 
**privileges** | **object** | Список привилегий пользователя базы данных | [optional] 
**description** | **object** | Описание пользователя базы данных | [optional] 
**instance_id** | **object** | ID инстанса базы данных для применения привилегий. В данных момент поле доступно только для кластеров MySQL. Если поле не передано, то привилегии будут применены ко всем инстансам | [optional] 

## Example

```python
from timeweb_cloud_api.models.update_admin import UpdateAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAdmin from a JSON string
update_admin_instance = UpdateAdmin.from_json(json)
# print the JSON string representation of the object
print UpdateAdmin.to_json()

# convert the object into a dict
update_admin_dict = update_admin_instance.to_dict()
# create an instance of UpdateAdmin from a dict
update_admin_form_dict = update_admin.from_dict(update_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


