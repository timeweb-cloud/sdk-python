# RouterInParentService

Родительский сервис

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID сервиса | 
**type** | **object** | Тип сервиса | 

## Example

```python
from timeweb_cloud_api.models.router_in_parent_service import RouterInParentService

# TODO update the JSON string below
json = "{}"
# create an instance of RouterInParentService from a JSON string
router_in_parent_service_instance = RouterInParentService.from_json(json)
# print the JSON string representation of the object
print RouterInParentService.to_json()

# convert the object into a dict
router_in_parent_service_dict = router_in_parent_service_instance.to_dict()
# create an instance of RouterInParentService from a dict
router_in_parent_service_form_dict = router_in_parent_service.from_dict(router_in_parent_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


