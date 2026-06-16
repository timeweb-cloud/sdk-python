# AvailableNetwork


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID сети | 
**description** | **object** | Описание сети | 
**name** | **object** | Имя сети | 
**subnet_v4** | **object** | Подсеть IPv4 | 
**location** | **object** | Локация | 
**created_at** | **object** | Дата и время создания | 
**availability_zone** | **object** | Зона доступности | 
**public_ip** | **object** | Публичный IP-адрес | 
**type** | **object** | Тип сети | 
**busy_address** | **object** | Занятые IP-адреса | 

## Example

```python
from timeweb_cloud_api.models.available_network import AvailableNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableNetwork from a JSON string
available_network_instance = AvailableNetwork.from_json(json)
# print the JSON string representation of the object
print AvailableNetwork.to_json()

# convert the object into a dict
available_network_dict = available_network_instance.to_dict()
# create an instance of AvailableNetwork from a dict
available_network_form_dict = available_network.from_dict(available_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


