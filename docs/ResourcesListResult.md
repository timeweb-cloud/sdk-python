# ResourcesListResult

Результат `resources/list`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | **object** | Ресурсы сервера | 

## Example

```python
from timeweb_cloud_api.models.resources_list_result import ResourcesListResult

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesListResult from a JSON string
resources_list_result_instance = ResourcesListResult.from_json(json)
# print the JSON string representation of the object
print ResourcesListResult.to_json()

# convert the object into a dict
resources_list_result_dict = resources_list_result_instance.to_dict()
# create an instance of ResourcesListResult from a dict
resources_list_result_form_dict = resources_list_result.from_dict(resources_list_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


