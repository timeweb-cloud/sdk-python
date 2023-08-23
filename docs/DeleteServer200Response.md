# DeleteServer200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_delete** | [**DeleteServiceResponse**](DeleteServiceResponse.md) |  | 

## Example

```python
from openapi_client.models.delete_server200_response import DeleteServer200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteServer200Response from a JSON string
delete_server200_response_instance = DeleteServer200Response.from_json(json)
# print the JSON string representation of the object
print DeleteServer200Response.to_json()

# convert the object into a dict
delete_server200_response_dict = delete_server200_response_instance.to_dict()
# create an instance of DeleteServer200Response from a dict
delete_server200_response_form_dict = delete_server200_response.from_dict(delete_server200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


