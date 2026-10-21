# ResourcesReadResult

Результат `resources/read`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contents** | **object** | Содержимое ресурса | 

## Example

```python
from timeweb_cloud_api.models.resources_read_result import ResourcesReadResult

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesReadResult from a JSON string
resources_read_result_instance = ResourcesReadResult.from_json(json)
# print the JSON string representation of the object
print ResourcesReadResult.to_json()

# convert the object into a dict
resources_read_result_dict = resources_read_result_instance.to_dict()
# create an instance of ResourcesReadResult from a dict
resources_read_result_form_dict = resources_read_result.from_dict(resources_read_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


