# Subdomain


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fqdn** | **object** | Полное имя поддомена. | 
**id** | **object** | ID поддомена. | 
**linked_ip** | **object** | Привязанный к поддомену IP-адрес. | 

## Example

```python
from timeweb_cloud_api.models.subdomain import Subdomain

# TODO update the JSON string below
json = "{}"
# create an instance of Subdomain from a JSON string
subdomain_instance = Subdomain.from_json(json)
# print the JSON string representation of the object
print Subdomain.to_json()

# convert the object into a dict
subdomain_dict = subdomain_instance.to_dict()
# create an instance of Subdomain from a dict
subdomain_form_dict = subdomain.from_dict(subdomain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


