# DeleteServerIPRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **object** | IP-адрес (IPv4 или IPv6) | 

## Example

```python
from timeweb_cloud_api.models.delete_server_ip_request import DeleteServerIPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteServerIPRequest from a JSON string
delete_server_ip_request_instance = DeleteServerIPRequest.from_json(json)
# print the JSON string representation of the object
print DeleteServerIPRequest.to_json()

# convert the object into a dict
delete_server_ip_request_dict = delete_server_ip_request_instance.to_dict()
# create an instance of DeleteServerIPRequest from a dict
delete_server_ip_request_form_dict = delete_server_ip_request.from_dict(delete_server_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


