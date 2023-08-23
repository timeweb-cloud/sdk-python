# AddIPsToAllowedListRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **object** | Список разрешенных IP-адресов. | 

## Example

```python
from openapi_client.models.add_ips_to_allowed_list_request import AddIPsToAllowedListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddIPsToAllowedListRequest from a JSON string
add_ips_to_allowed_list_request_instance = AddIPsToAllowedListRequest.from_json(json)
# print the JSON string representation of the object
print AddIPsToAllowedListRequest.to_json()

# convert the object into a dict
add_ips_to_allowed_list_request_dict = add_ips_to_allowed_list_request_instance.to_dict()
# create an instance of AddIPsToAllowedListRequest from a dict
add_ips_to_allowed_list_request_form_dict = add_ips_to_allowed_list_request.from_dict(add_ips_to_allowed_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


