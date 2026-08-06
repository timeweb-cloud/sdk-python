# AddCertificate

Параметры загрузки собственного сертификата

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private_key** | **object** | Приватный ключ сертификата в формате PEM. | 
**certificate** | **object** | Сертификат вместе с цепочкой в формате PEM. | 
**comment** | **object** | Комментарий к сертификату. | [optional] 

## Example

```python
from timeweb_cloud_api.models.add_certificate import AddCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of AddCertificate from a JSON string
add_certificate_instance = AddCertificate.from_json(json)
# print the JSON string representation of the object
print AddCertificate.to_json()

# convert the object into a dict
add_certificate_dict = add_certificate_instance.to_dict()
# create an instance of AddCertificate from a dict
add_certificate_form_dict = add_certificate.from_dict(add_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


