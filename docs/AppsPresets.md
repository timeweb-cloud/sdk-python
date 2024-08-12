# AppsPresets


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend_presets** | **object** |  | [optional] 
**frontend_presets** | **object** |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.apps_presets import AppsPresets

# TODO update the JSON string below
json = "{}"
# create an instance of AppsPresets from a JSON string
apps_presets_instance = AppsPresets.from_json(json)
# print the JSON string representation of the object
print AppsPresets.to_json()

# convert the object into a dict
apps_presets_dict = apps_presets_instance.to_dict()
# create an instance of AppsPresets from a dict
apps_presets_form_dict = apps_presets.from_dict(apps_presets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


