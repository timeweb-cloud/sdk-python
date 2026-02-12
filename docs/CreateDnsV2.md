# CreateDnsV2


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **object** | Тип DNS-записи. | 
**value** | **object** | IPv4 адрес. | 
**ttl** | **object** | Время жизни DNS-записи в секундах. | [optional] 
**app_id** | **object** | Идентификатор приложения в App Platform, к которому будет привязан домен или поддомен. | [optional] 

## Example

```python
from timeweb_cloud_api.models.create_dns_v2 import CreateDnsV2

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDnsV2 from a JSON string
create_dns_v2_instance = CreateDnsV2.from_json(json)
# print the JSON string representation of the object
print CreateDnsV2.to_json()

# convert the object into a dict
create_dns_v2_dict = create_dns_v2_instance.to_dict()
# create an instance of CreateDnsV2 from a dict
create_dns_v2_form_dict = create_dns_v2.from_dict(create_dns_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


