# GetDomainMailInfo200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain_info** | [**DomainInfo**](DomainInfo.md) |  | 

## Example

```python
from timeweb_cloud_api.models.get_domain_mail_info200_response import GetDomainMailInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainMailInfo200Response from a JSON string
get_domain_mail_info200_response_instance = GetDomainMailInfo200Response.from_json(json)
# print the JSON string representation of the object
print GetDomainMailInfo200Response.to_json()

# convert the object into a dict
get_domain_mail_info200_response_dict = get_domain_mail_info200_response_instance.to_dict()
# create an instance of GetDomainMailInfo200Response from a dict
get_domain_mail_info200_response_form_dict = get_domain_mail_info200_response.from_dict(get_domain_mail_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


