# SchemasBaseError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **object** |  | 
**error_code** | **object** |  | 
**message** | **object** |  | 
**response_id** | **object** |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.schemas_base_error import SchemasBaseError

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasBaseError from a JSON string
schemas_base_error_instance = SchemasBaseError.from_json(json)
# print the JSON string representation of the object
print SchemasBaseError.to_json()

# convert the object into a dict
schemas_base_error_dict = schemas_base_error_instance.to_dict()
# create an instance of SchemasBaseError from a dict
schemas_base_error_form_dict = schemas_base_error.from_dict(schemas_base_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


