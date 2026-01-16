# DnsRecordV2Data

Данные DNS-записи. Состав полей зависит от типа записи.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**priority** | **object** | Приоритет DNS-записи (для MX и SRV записей). | [optional] 
**subdomain** | **object** | Имя поддомена (только поддомен без основного домена, например &#x60;sub&#x60; для &#x60;sub.example.com&#x60;). Для записей на основном домене это поле отсутствует в ответе. | [optional] 
**value** | **object** | Значение DNS-записи (для A, AAAA, TXT, CNAME, MX записей). | [optional] 
**host** | **object** | Каноническое имя хоста, предоставляющего сервис (для SRV записей). | [optional] 
**port** | **object** | TCP или UDP порт, на котором работает сервис (для SRV записей). | [optional] 
**service** | **object** | Имя сервиса (для SRV записей). | [optional] 
**protocol** | **object** | Протокол (для SRV записей). | [optional] 

## Example

```python
from timeweb_cloud_api.models.dns_record_v2_data import DnsRecordV2Data

# TODO update the JSON string below
json = "{}"
# create an instance of DnsRecordV2Data from a JSON string
dns_record_v2_data_instance = DnsRecordV2Data.from_json(json)
# print the JSON string representation of the object
print DnsRecordV2Data.to_json()

# convert the object into a dict
dns_record_v2_data_dict = dns_record_v2_data_instance.to_dict()
# create an instance of DnsRecordV2Data from a dict
dns_record_v2_data_form_dict = dns_record_v2_data.from_dict(dns_record_v2_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


