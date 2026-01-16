# CreateDomainDNSRecordV2201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dns_record** | [**DnsRecordV2**](DnsRecordV2.md) |  | 

## Example

```python
from timeweb_cloud_api.models.create_domain_dns_record_v2201_response import CreateDomainDNSRecordV2201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomainDNSRecordV2201Response from a JSON string
create_domain_dns_record_v2201_response_instance = CreateDomainDNSRecordV2201Response.from_json(json)
# print the JSON string representation of the object
print CreateDomainDNSRecordV2201Response.to_json()

# convert the object into a dict
create_domain_dns_record_v2201_response_dict = create_domain_dns_record_v2201_response_instance.to_dict()
# create an instance of CreateDomainDNSRecordV2201Response from a dict
create_domain_dns_record_v2201_response_form_dict = create_domain_dns_record_v2201_response.from_dict(create_domain_dns_record_v2201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


