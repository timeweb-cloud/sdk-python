# UpdateServerIPRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **object** | IP-адрес (IPv4 или IPv6) | 
**ptr** | **object** | PTR-запись IP-адреса | 

## Example

```python
from openapi_client.models.update_server_ip_request import UpdateServerIPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateServerIPRequest from a JSON string
update_server_ip_request_instance = UpdateServerIPRequest.from_json(json)
# print the JSON string representation of the object
print UpdateServerIPRequest.to_json()

# convert the object into a dict
update_server_ip_request_dict = update_server_ip_request_instance.to_dict()
# create an instance of UpdateServerIPRequest from a dict
update_server_ip_request_form_dict = update_server_ip_request.from_dict(update_server_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


