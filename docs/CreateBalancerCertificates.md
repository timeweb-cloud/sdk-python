# CreateBalancerCertificates

Сертификат SSL.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип сертификата. | [optional] 
**fqdn** | **object** | Полное имя домена. | [optional] 
**cert_data** | **object** | Данные сертификата. Нужны только для типа custom. | [optional] 
**key_data** | **object** | Данные ключа. Нужны только для типа custom. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_balancer_certificates import CreateBalancerCertificates

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBalancerCertificates from a JSON string
create_balancer_certificates_instance = CreateBalancerCertificates.from_json(json)
# print the JSON string representation of the object
print CreateBalancerCertificates.to_json()

# convert the object into a dict
create_balancer_certificates_dict = create_balancer_certificates_instance.to_dict()
# create an instance of CreateBalancerCertificates from a dict
create_balancer_certificates_form_dict = create_balancer_certificates.from_dict(create_balancer_certificates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


