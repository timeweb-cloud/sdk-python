# DomainTransfer

Заявка на перенос домена

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **object** | Тип создаваемой заявки. | 
**auth_code** | **object** | Код авторизации для переноса домена. | 
**fqdn** | **object** | Полное имя домена. | 

## Example

```python
from timeweb_cloud_api.models.domain_transfer import DomainTransfer

# TODO update the JSON string below
json = "{}"
# create an instance of DomainTransfer from a JSON string
domain_transfer_instance = DomainTransfer.from_json(json)
# print the JSON string representation of the object
print DomainTransfer.to_json()

# convert the object into a dict
domain_transfer_dict = domain_transfer_instance.to_dict()
# create an instance of DomainTransfer from a dict
domain_transfer_form_dict = domain_transfer.from_dict(domain_transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


