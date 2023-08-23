# PresetsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | Идентификатор запроса | [optional] 
**meta** | [**Meta**](Meta.md) |  | 
**k8s_presets** | **object** | Массив тарифов k8s | 

## Example

```python
from timeweb_cloud_api.models.presets_response import PresetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PresetsResponse from a JSON string
presets_response_instance = PresetsResponse.from_json(json)
# print the JSON string representation of the object
print PresetsResponse.to_json()

# convert the object into a dict
presets_response_dict = presets_response_instance.to_dict()
# create an instance of PresetsResponse from a dict
presets_response_form_dict = presets_response.from_dict(presets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


