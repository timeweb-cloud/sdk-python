# DeleteIPsFromAllowedListRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **object** | Список удаляемых из списка разрешенных IP-адресов. | 

## Example

```python
from timeweb_cloud_api.models.delete_ips_from_allowed_list_request import DeleteIPsFromAllowedListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteIPsFromAllowedListRequest from a JSON string
delete_ips_from_allowed_list_request_instance = DeleteIPsFromAllowedListRequest.from_json(json)
# print the JSON string representation of the object
print DeleteIPsFromAllowedListRequest.to_json()

# convert the object into a dict
delete_ips_from_allowed_list_request_dict = delete_ips_from_allowed_list_request_instance.to_dict()
# create an instance of DeleteIPsFromAllowedListRequest from a dict
delete_ips_from_allowed_list_request_form_dict = delete_ips_from_allowed_list_request.from_dict(delete_ips_from_allowed_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


