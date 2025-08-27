# SchemasPresetsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**container_registry_presets** | **object** | Массив тарифов container registry | 

## Example

```python
from timeweb_cloud_api.models.schemas_presets_response import SchemasPresetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchemasPresetsResponse from a JSON string
schemas_presets_response_instance = SchemasPresetsResponse.from_json(json)
# print the JSON string representation of the object
print SchemasPresetsResponse.to_json()

# convert the object into a dict
schemas_presets_response_dict = schemas_presets_response_instance.to_dict()
# create an instance of SchemasPresetsResponse from a dict
schemas_presets_response_form_dict = schemas_presets_response.from_dict(schemas_presets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


