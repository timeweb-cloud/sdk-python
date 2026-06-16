# DnatInPublic

Публичный адрес

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **object** | IP-адрес | 
**port** | **object** | Порт или диапазон портов | [optional] 

## Example

```python
from timeweb_cloud_api.models.dnat_in_public import DnatInPublic

# TODO update the JSON string below
json = "{}"
# create an instance of DnatInPublic from a JSON string
dnat_in_public_instance = DnatInPublic.from_json(json)
# print the JSON string representation of the object
print DnatInPublic.to_json()

# convert the object into a dict
dnat_in_public_dict = dnat_in_public_instance.to_dict()
# create an instance of DnatInPublic from a dict
dnat_in_public_form_dict = dnat_in_public.from_dict(dnat_in_public_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


