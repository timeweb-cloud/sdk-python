# RouterIn


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Имя роутера | 
**comment** | **object** | Описание роутера | [optional] 
**preset_id** | **object** | ID тарифа | 
**project_id** | **object** | ID проекта | [optional] 
**networks** | **object** | Подключаемые сети | 
**ips** | **object** | IP-адреса | [optional] 
**parent_service** | [**RouterInParentService**](RouterInParentService.md) |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.router_in import RouterIn

# TODO update the JSON string below
json = "{}"
# create an instance of RouterIn from a JSON string
router_in_instance = RouterIn.from_json(json)
# print the JSON string representation of the object
print RouterIn.to_json()

# convert the object into a dict
router_in_dict = router_in_instance.to_dict()
# create an instance of RouterIn from a dict
router_in_form_dict = router_in.from_dict(router_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


