# RouterPresetsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**router_presets** | **object** | Тарифы роутеров | 
**meta** | [**ComponentsSchemasMeta**](ComponentsSchemasMeta.md) |  | 

## Example

```python
from timeweb_cloud_api.models.router_presets_response import RouterPresetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouterPresetsResponse from a JSON string
router_presets_response_instance = RouterPresetsResponse.from_json(json)
# print the JSON string representation of the object
print RouterPresetsResponse.to_json()

# convert the object into a dict
router_presets_response_dict = router_presets_response_instance.to_dict()
# create an instance of RouterPresetsResponse from a dict
router_presets_response_form_dict = router_presets_response.from_dict(router_presets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


