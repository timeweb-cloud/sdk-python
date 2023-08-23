# GetDatabasesPresets200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**Meta**](Meta.md) |  | 
**databases_presets** | **object** |  | 

## Example

```python
from timeweb_cloud_api.models.get_databases_presets200_response import GetDatabasesPresets200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasesPresets200Response from a JSON string
get_databases_presets200_response_instance = GetDatabasesPresets200Response.from_json(json)
# print the JSON string representation of the object
print GetDatabasesPresets200Response.to_json()

# convert the object into a dict
get_databases_presets200_response_dict = get_databases_presets200_response_instance.to_dict()
# create an instance of GetDatabasesPresets200Response from a dict
get_databases_presets200_response_form_dict = get_databases_presets200_response.from_dict(get_databases_presets200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


