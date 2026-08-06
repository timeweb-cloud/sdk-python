# IssueCertificate

Параметры выпуска сертификата Let's Encrypt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **object** | ID CDN-ресурса, для доменов которого нужно выпустить сертификат. | 

## Example

```python
from timeweb_cloud_api.models.issue_certificate import IssueCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of IssueCertificate from a JSON string
issue_certificate_instance = IssueCertificate.from_json(json)
# print the JSON string representation of the object
print IssueCertificate.to_json()

# convert the object into a dict
issue_certificate_dict = issue_certificate_instance.to_dict()
# create an instance of IssueCertificate from a dict
issue_certificate_form_dict = issue_certificate.from_dict(issue_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


