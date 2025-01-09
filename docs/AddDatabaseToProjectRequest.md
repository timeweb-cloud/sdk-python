# AddDatabaseToProjectRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **object** | ID добавляемой базы данных. | 

## Example

```python
from timeweb_cloud_api.models.add_database_to_project_request import AddDatabaseToProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDatabaseToProjectRequest from a JSON string
add_database_to_project_request_instance = AddDatabaseToProjectRequest.from_json(json)
# print the JSON string representation of the object
print AddDatabaseToProjectRequest.to_json()

# convert the object into a dict
add_database_to_project_request_dict = add_database_to_project_request_instance.to_dict()
# create an instance of AddDatabaseToProjectRequest from a dict
add_database_to_project_request_form_dict = add_database_to_project_request.from_dict(add_database_to_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


