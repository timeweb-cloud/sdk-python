# AddServerToProjectRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **object** | ID добавляемого сервера. | 

## Example

```python
from timeweb_cloud_api.models.add_server_to_project_request import AddServerToProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddServerToProjectRequest from a JSON string
add_server_to_project_request_instance = AddServerToProjectRequest.from_json(json)
# print the JSON string representation of the object
print AddServerToProjectRequest.to_json()

# convert the object into a dict
add_server_to_project_request_dict = add_server_to_project_request_instance.to_dict()
# create an instance of AddServerToProjectRequest from a dict
add_server_to_project_request_form_dict = add_server_to_project_request.from_dict(add_server_to_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


