# AddServerIP201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_ip** | [**ServerIp**](ServerIp.md) |  | 

## Example

```python
from timeweb_cloud_api.models.add_server_ip201_response import AddServerIP201Response

# TODO update the JSON string below
json = "{}"
# create an instance of AddServerIP201Response from a JSON string
add_server_ip201_response_instance = AddServerIP201Response.from_json(json)
# print the JSON string representation of the object
print AddServerIP201Response.to_json()

# convert the object into a dict
add_server_ip201_response_dict = add_server_ip201_response_instance.to_dict()
# create an instance of AddServerIP201Response from a dict
add_server_ip201_response_form_dict = add_server_ip201_response.from_dict(add_server_ip201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


