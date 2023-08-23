# DeleteDatabase200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**database_delete** | [**DeleteServiceResponse**](DeleteServiceResponse.md) |  | 

## Example

```python
from timeweb_cloud_api.models.delete_database200_response import DeleteDatabase200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteDatabase200Response from a JSON string
delete_database200_response_instance = DeleteDatabase200Response.from_json(json)
# print the JSON string representation of the object
print DeleteDatabase200Response.to_json()

# convert the object into a dict
delete_database200_response_dict = delete_database200_response_instance.to_dict()
# create an instance of DeleteDatabase200Response from a dict
delete_database200_response_form_dict = delete_database200_response.from_dict(delete_database200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


