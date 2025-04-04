# CreateServerNetwork

Параметры конфигурации приватной сети сервера

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID сети | [optional] 
**floating_ip** | **object** | Публичный IP | [optional] 
**local_ip** | **object** | Приватный IP | [optional] 
**ip** | **object** | Приватный IP | [optional] 
**network_drive_ids** | **object** | Массив ID сетевых дисков | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_server_network import CreateServerNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServerNetwork from a JSON string
create_server_network_instance = CreateServerNetwork.from_json(json)
# print the JSON string representation of the object
print CreateServerNetwork.to_json()

# convert the object into a dict
create_server_network_dict = create_server_network_instance.to_dict()
# create an instance of CreateServerNetwork from a dict
create_server_network_form_dict = create_server_network.from_dict(create_server_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


