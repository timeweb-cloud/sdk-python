# CreateClusterAdmin


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login** | **object** | Имя пользователя базы данных | [optional] 
**password** | **object** | Пароль пользователя базы данных | [optional] 
**host** | **object** | Хост пользователя | [optional] 
**privileges** | **object** | Список привилегий пользователя базы данных | [optional] 
**description** | **object** | Описание пользователя базы данных | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_cluster_admin import CreateClusterAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of CreateClusterAdmin from a JSON string
create_cluster_admin_instance = CreateClusterAdmin.from_json(json)
# print the JSON string representation of the object
print CreateClusterAdmin.to_json()

# convert the object into a dict
create_cluster_admin_dict = create_cluster_admin_instance.to_dict()
# create an instance of CreateClusterAdmin from a dict
create_cluster_admin_form_dict = create_cluster_admin.from_dict(create_cluster_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


