# S3Subdomain

Поддомен.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | Уникальный идентификатор поддомена. | 
**subdomain** | **object** | Поддомен. | 
**cert_released** | **object** | Значение времени, указанное в комбинированном формате даты и времени ISO8601, которое представляет, когда был выдан SSL сертификат. | 
**tries** | **object** | Количество попыток перевыпустить SSL сертификат. | 
**status** | **object** | Поддомен. | 

## Example

```python
from timeweb_cloud_api.models.s3_subdomain import S3Subdomain

# TODO update the JSON string below
json = "{}"
# create an instance of S3Subdomain from a JSON string
s3_subdomain_instance = S3Subdomain.from_json(json)
# print the JSON string representation of the object
print S3Subdomain.to_json()

# convert the object into a dict
s3_subdomain_dict = s3_subdomain_instance.to_dict()
# create an instance of S3Subdomain from a dict
s3_subdomain_form_dict = s3_subdomain.from_dict(s3_subdomain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


