# RegistryResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**container_registry** | [**RegistryOut**](RegistryOut.md) |  | 

## Example

```python
from timeweb_cloud_api.models.registry_response import RegistryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegistryResponse from a JSON string
registry_response_instance = RegistryResponse.from_json(json)
# print the JSON string representation of the object
print RegistryResponse.to_json()

# convert the object into a dict
registry_response_dict = registry_response_instance.to_dict()
# create an instance of RegistryResponse from a dict
registry_response_form_dict = registry_response.from_dict(registry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


