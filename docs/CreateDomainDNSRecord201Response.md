# CreateDomainDNSRecord201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_record** | [**DnsRecord**](DnsRecord.md) |  | 

## Example

```python
from openapi_client.models.create_domain_dns_record201_response import CreateDomainDNSRecord201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomainDNSRecord201Response from a JSON string
create_domain_dns_record201_response_instance = CreateDomainDNSRecord201Response.from_json(json)
# print the JSON string representation of the object
print CreateDomainDNSRecord201Response.to_json()

# convert the object into a dict
create_domain_dns_record201_response_dict = create_domain_dns_record201_response_instance.to_dict()
# create an instance of CreateDomainDNSRecord201Response from a dict
create_domain_dns_record201_response_form_dict = create_domain_dns_record201_response.from_dict(create_domain_dns_record201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


