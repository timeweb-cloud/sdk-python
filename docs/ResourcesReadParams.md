# ResourcesReadParams

`params` метода `resources/read`

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uri** | **object** | URI ресурса | 

## Example

```python
from timeweb_cloud_api.models.resources_read_params import ResourcesReadParams

# TODO update the JSON string below
json = "{}"
# create an instance of ResourcesReadParams from a JSON string
resources_read_params_instance = ResourcesReadParams.from_json(json)
# print the JSON string representation of the object
print ResourcesReadParams.to_json()

# convert the object into a dict
resources_read_params_dict = resources_read_params_instance.to_dict()
# create an instance of ResourcesReadParams from a dict
resources_read_params_form_dict = resources_read_params.from_dict(resources_read_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


