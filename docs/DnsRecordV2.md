# DnsRecordV2

DNS-запись.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **object** | ID DNS-записи. | 
**type** | **object** | Тип DNS-записи. | 
**data** | [**DnsRecordV2Data**](DnsRecordV2Data.md) |  | 
**fqdn** | **object** | Домен, относительно которого указано &#x60;data.subdomain&#x60;. Полное имя записи — &#x60;data.subdomain&#x60; + &#x60;.&#x60; + &#x60;fqdn&#x60;, а если &#x60;data.subdomain&#x60; нет — &#x60;fqdn&#x60;. | 
**ttl** | **object** | Время жизни DNS-записи в секундах. | 

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


