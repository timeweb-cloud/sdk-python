# Certificate

SSL-сертификат CDN

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID сертификата. Указывается в поле &#x60;config.security.certificate_id&#x60; при привязке сертификата к ресурсу. | 
**type** | **object** | Тип сертификата. - &#x60;lets_encrypt&#x60; — сертификат, выпущенный через Let&#39;s Encrypt; - &#x60;uploaded&#x60; — сертификат, загруженный вами. | 
**cn** | **object** | Основное доменное имя сертификата. | 
**domains** | **object** | Все доменные имена сертификата, включая указанные в SAN. | 
**issued_at** | **object** | Дата выпуска сертификата. | 
**expires_at** | **object** | Дата окончания действия сертификата. | 

## Example

```python
from timeweb_cloud_api.models.certificate import Certificate

# TODO update the JSON string below
json = "{}"
# create an instance of Certificate from a JSON string
certificate_instance = Certificate.from_json(json)
# print the JSON string representation of the object
print Certificate.to_json()

# convert the object into a dict
certificate_dict = certificate_instance.to_dict()
# create an instance of Certificate from a dict
certificate_form_dict = certificate.from_dict(certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


