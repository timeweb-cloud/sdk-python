# DnsRecordV2

DNS-запись.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип DNS-записи. | 
**id** | **object** | ID DNS-записи. | [optional] 
**fqdn** | **object** | Полное имя основного домена. | [optional] 
**data** | [**DnsRecordV2Data**](DnsRecordV2Data.md) |  | 
**ttl** | **object** | Время жизни DNS-записи. | [optional] 

## Example

```python
from timeweb_cloud_api.models.dns_record_v2 import DnsRecordV2

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecordV2 from a JSON string
dns_record_v2_instance = DnsRecordV2.from_json(json)
# print the JSON string representation of the object
print DnsRecordV2.to_json()

# convert the object into a dict
dns_record_v2_dict = dns_record_v2_instance.to_dict()
# create an instance of DnsRecordV2 from a dict
dns_record_v2_form_dict = dns_record_v2.from_dict(dns_record_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


