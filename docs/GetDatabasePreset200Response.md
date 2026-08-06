# GetDatabasePreset200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databases_preset** | [**PresetsDbs**](PresetsDbs.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_database_preset200_response import GetDatabasePreset200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDatabasePreset200Response from a JSON string
get_database_preset200_response_instance = GetDatabasePreset200Response.from_json(json)
# print the JSON string representation of the object
print GetDatabasePreset200Response.to_json()

# convert the object into a dict
get_database_preset200_response_dict = get_database_preset200_response_instance.to_dict()
# create an instance of GetDatabasePreset200Response from a dict
get_database_preset200_response_form_dict = get_database_preset200_response.from_dict(get_database_preset200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


