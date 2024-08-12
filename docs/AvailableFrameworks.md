# AvailableFrameworks


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**frontend_frameworks** | **object** |  | [optional] 
**backend_frameworks** | **object** |  | [optional] 

## Example

```python
from timeweb_cloud_api.models.available_frameworks import AvailableFrameworks

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableFrameworks from a JSON string
available_frameworks_instance = AvailableFrameworks.from_json(json)
# print the JSON string representation of the object
print AvailableFrameworks.to_json()

# convert the object into a dict
available_frameworks_dict = available_frameworks_instance.to_dict()
# create an instance of AvailableFrameworks from a dict
available_frameworks_form_dict = available_frameworks.from_dict(available_frameworks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


