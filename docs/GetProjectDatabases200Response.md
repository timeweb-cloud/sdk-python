# GetProjectDatabases200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databases** | **object** |  | 
**meta** | [**Meta**](Meta.md) |  | 

## Example

```python
from openapi_client.models.get_project_databases200_response import GetProjectDatabases200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetProjectDatabases200Response from a JSON string
get_project_databases200_response_instance = GetProjectDatabases200Response.from_json(json)
# print the JSON string representation of the object
print GetProjectDatabases200Response.to_json()

# convert the object into a dict
get_project_databases200_response_dict = get_project_databases200_response_instance.to_dict()
# create an instance of GetProjectDatabases200Response from a dict
get_project_databases200_response_form_dict = get_project_databases200_response.from_dict(get_project_databases200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


