# DnatInLocal

Локальный (приватный) адрес назначения

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **object** | IP-адрес | 
**port** | **object** | Порт или диапазон портов | [optional] 

## Example

```python
from timeweb_cloud_api.models.dnat_in_local import DnatInLocal

# TODO update the JSON string below
json = "{}"
# create an instance of DnatInLocal from a JSON string
dnat_in_local_instance = DnatInLocal.from_json(json)
# print the JSON string representation of the object
print DnatInLocal.to_json()

# convert the object into a dict
dnat_in_local_dict = dnat_in_local_instance.to_dict()
# create an instance of DnatInLocal from a dict
dnat_in_local_form_dict = dnat_in_local.from_dict(dnat_in_local_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


