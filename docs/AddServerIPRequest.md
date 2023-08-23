# AddServerIPRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип IP-адреса | 
**ptr** | **object** | PTR-запись IP-адреса | [optional] 

## Example

```python
from timeweb_cloud_api.models.add_server_ip_request import AddServerIPRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddServerIPRequest from a JSON string
add_server_ip_request_instance = AddServerIPRequest.from_json(json)
# print the JSON string representation of the object
print AddServerIPRequest.to_json()

# convert the object into a dict
add_server_ip_request_dict = add_server_ip_request_instance.to_dict()
# create an instance of AddServerIPRequest from a dict
add_server_ip_request_form_dict = add_server_ip_request.from_dict(add_server_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


