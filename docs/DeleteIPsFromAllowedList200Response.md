# DeleteIPsFromAllowedList200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | [**RemoveIps**](RemoveIps.md) |  | 

## Example

```python
from openapi_client.models.delete_ips_from_allowed_list200_response import DeleteIPsFromAllowedList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteIPsFromAllowedList200Response from a JSON string
delete_ips_from_allowed_list200_response_instance = DeleteIPsFromAllowedList200Response.from_json(json)
# print the JSON string representation of the object
print DeleteIPsFromAllowedList200Response.to_json()

# convert the object into a dict
delete_ips_from_allowed_list200_response_dict = delete_ips_from_allowed_list200_response_instance.to_dict()
# create an instance of DeleteIPsFromAllowedList200Response from a dict
delete_ips_from_allowed_list200_response_form_dict = delete_ips_from_allowed_list200_response.from_dict(delete_ips_from_allowed_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


