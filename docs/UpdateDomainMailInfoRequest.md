# UpdateDomainMailInfoRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **object** | Адрес для сбора почты с ошибочных ящиков | 

## Example

```python
from timeweb_cloud_api.models.update_domain_mail_info_request import UpdateDomainMailInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomainMailInfoRequest from a JSON string
update_domain_mail_info_request_instance = UpdateDomainMailInfoRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDomainMailInfoRequest.to_json()

# convert the object into a dict
update_domain_mail_info_request_dict = update_domain_mail_info_request_instance.to_dict()
# create an instance of UpdateDomainMailInfoRequest from a dict
update_domain_mail_info_request_form_dict = update_domain_mail_info_request.from_dict(update_domain_mail_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


