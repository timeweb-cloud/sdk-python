# AddDedicatedServerToProjectRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **object** | Идентификатор добавляемого выделенного сервера. | 

## Example

```python
from openapi_client.models.add_dedicated_server_to_project_request import AddDedicatedServerToProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddDedicatedServerToProjectRequest from a JSON string
add_dedicated_server_to_project_request_instance = AddDedicatedServerToProjectRequest.from_json(json)
# print the JSON string representation of the object
print AddDedicatedServerToProjectRequest.to_json()

# convert the object into a dict
add_dedicated_server_to_project_request_dict = add_dedicated_server_to_project_request_instance.to_dict()
# create an instance of AddDedicatedServerToProjectRequest from a dict
add_dedicated_server_to_project_request_form_dict = add_dedicated_server_to_project_request.from_dict(add_dedicated_server_to_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


