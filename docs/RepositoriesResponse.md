# RepositoriesResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_id** | **object** | ID запроса | [optional] 
**meta** | [**Meta1**](Meta1.md) |  | 
**container_registries_repositories** | **object** | Массив тарифов container registry | 

## Example

```python
from timeweb_cloud_api.models.repositories_response import RepositoriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RepositoriesResponse from a JSON string
repositories_response_instance = RepositoriesResponse.from_json(json)
# print the JSON string representation of the object
print RepositoriesResponse.to_json()

# convert the object into a dict
repositories_response_dict = repositories_response_instance.to_dict()
# create an instance of RepositoriesResponse from a dict
repositories_response_form_dict = repositories_response.from_dict(repositories_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


