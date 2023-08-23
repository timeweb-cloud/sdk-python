# DnsRecord

DNS-запись.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип DNS-записи. | 
**id** | **object** | Идентификатор DNS-записи. | [optional] 
**data** | [**DnsRecordData**](DnsRecordData.md) |  | 

## Example

```python
from openapi_client.models.dns_record import DnsRecord

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecord from a JSON string
dns_record_instance = DnsRecord.from_json(json)
# print the JSON string representation of the object
print DnsRecord.to_json()

# convert the object into a dict
dns_record_dict = dns_record_instance.to_dict()
# create an instance of DnsRecord from a dict
dns_record_form_dict = dns_record.from_dict(dns_record_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


