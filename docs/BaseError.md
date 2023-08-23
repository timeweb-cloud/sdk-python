# BaseError


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **object** |  | 
**error_code** | **object** |  | 
**message** | **object** |  | 
**response_id** | **object** |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.base_error import BaseError

# TODO update the JSON string below
json = "{}"
# create an instance of BaseError from a JSON string
base_error_instance = BaseError.from_json(json)
# print the JSON string representation of the object
print BaseError.to_json()

# convert the object into a dict
base_error_dict = base_error_instance.to_dict()
# create an instance of BaseError from a dict
base_error_form_dict = base_error.from_dict(base_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


