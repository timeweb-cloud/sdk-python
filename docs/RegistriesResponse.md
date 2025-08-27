# RegistriesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**container_registry_list** | **object** | Реестр контейнеров | [optional] 

## Example

```python
from timeweb_cloud_api.models.registries_response import RegistriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegistriesResponse from a JSON string
registries_response_instance = RegistriesResponse.from_json(json)
# print the JSON string representation of the object
print RegistriesResponse.to_json()

# convert the object into a dict
registries_response_dict = registries_response_instance.to_dict()
# create an instance of RegistriesResponse from a dict
registries_response_form_dict = registries_response.from_dict(registries_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


