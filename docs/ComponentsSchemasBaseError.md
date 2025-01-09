# ComponentsSchemasBaseError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **object** |  | 
**error_code** | **object** |  | 
**message** | **object** |  | 
**response_id** | **object** |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.components_schemas_base_error import ComponentsSchemasBaseError

# TODO update the JSON string below
json = "{}"
# create an instance of ComponentsSchemasBaseError from a JSON string
components_schemas_base_error_instance = ComponentsSchemasBaseError.from_json(json)
# print the JSON string representation of the object
print ComponentsSchemasBaseError.to_json()

# convert the object into a dict
components_schemas_base_error_dict = components_schemas_base_error_instance.to_dict()
# create an instance of ComponentsSchemasBaseError from a dict
components_schemas_base_error_form_dict = components_schemas_base_error.from_dict(components_schemas_base_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


