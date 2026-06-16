# RouterOut


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID роутера | 
**account_id** | **object** | ID аккаунта | 
**avatar_link** | **object** | Ссылка на аватар роутера | 
**name** | **object** | Имя роутера | 
**comment** | **object** | Описание роутера | 
**status** | **object** | Статус роутера | 
**zone** | **object** | Зона доступности | 
**ips** | **object** | IP-адреса | 
**preset_id** | **object** | ID тарифа | 
**preset** | [**RouterPreset**](RouterPreset.md) |  | 
**nodes** | **object** | Ноды | 
**networks** | **object** | Сети | 
**created_at** | **object** | Дата и время создания роутера в формате ISO8601 | 
**project_id** | **object** | ID проекта | [optional] 
**parent_services** | **object** | Родительские сервисы | 

## Example

```python
from timeweb_cloud_api.models.router_out import RouterOut

# TODO update the JSON string below
json = "{}"
# create an instance of RouterOut from a JSON string
router_out_instance = RouterOut.from_json(json)
# print the JSON string representation of the object
print RouterOut.to_json()

# convert the object into a dict
router_out_dict = router_out_instance.to_dict()
# create an instance of RouterOut from a dict
router_out_form_dict = router_out.from_dict(router_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


