# CreateKey201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssh_key** | [**SshKey**](SshKey.md) |  | 

## Example

```python
from openapi_client.models.create_key201_response import CreateKey201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKey201Response from a JSON string
create_key201_response_instance = CreateKey201Response.from_json(json)
# print the JSON string representation of the object
print CreateKey201Response.to_json()

# convert the object into a dict
create_key201_response_dict = create_key201_response_instance.to_dict()
# create an instance of CreateKey201Response from a dict
create_key201_response_form_dict = create_key201_response.from_dict(create_key201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


