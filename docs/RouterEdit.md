# RouterEdit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **object** | Новое имя роутера | [optional] 
**comment** | **object** | Новое описание роутера | [optional] 

## Example

```python
from timeweb_cloud_api.models.router_edit import RouterEdit

# TODO update the JSON string below
json = "{}"
# create an instance of RouterEdit from a JSON string
router_edit_instance = RouterEdit.from_json(json)
# print the JSON string representation of the object
print RouterEdit.to_json()

# convert the object into a dict
router_edit_dict = router_edit_instance.to_dict()
# create an instance of RouterEdit from a dict
router_edit_form_dict = router_edit.from_dict(router_edit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


