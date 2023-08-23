# CreateDedicatedServer201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dedicated_server** | [**DedicatedServer**](DedicatedServer.md) |  | 

## Example

```python
from openapi_client.models.create_dedicated_server201_response import CreateDedicatedServer201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDedicatedServer201Response from a JSON string
create_dedicated_server201_response_instance = CreateDedicatedServer201Response.from_json(json)
# print the JSON string representation of the object
print CreateDedicatedServer201Response.to_json()

# convert the object into a dict
create_dedicated_server201_response_dict = create_dedicated_server201_response_instance.to_dict()
# create an instance of CreateDedicatedServer201Response from a dict
create_dedicated_server201_response_form_dict = create_dedicated_server201_response.from_dict(create_dedicated_server201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


