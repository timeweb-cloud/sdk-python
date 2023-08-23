# ServerIp

IP-адрес сервера

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип IP-адреса сети | 
**ip** | **object** | IP-адрес сети | 
**ptr** | **object** | Запись имени узла | 
**is_main** | **object** | Является ли сеть основной. | 

## Example

```python
from timeweb_cloud_api.models.server_ip import ServerIp

# TODO update the JSON string below
json = "{}"
# create an instance of ServerIp from a JSON string
server_ip_instance = ServerIp.from_json(json)
# print the JSON string representation of the object
print ServerIp.to_json()

# convert the object into a dict
server_ip_dict = server_ip_instance.to_dict()
# create an instance of ServerIp from a dict
server_ip_form_dict = server_ip.from_dict(server_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


